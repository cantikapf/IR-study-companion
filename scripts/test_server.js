#!/usr/bin/env node
/**
 * test_server.js
 * 
 * Standalone zero-dependency static HTTP server & Playwright test harness for IR Study Companion.
 * Solves Windows/MSYS quirks:
 *  1. Eliminates `npx http-server` child_process path-with-spaces spawn failures.
 *  2. Prevents orphan listening ports via automatic SIGINT/SIGTERM handlers and port scanning.
 *  3. Exports `createPlaywrightContext` that auto-injects `localStorage.ir_onboarded_v1 = 'true'`
 *     to prevent first-visit onboarding modal backdrop click interception.
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.ico': 'image/x-icon'
};

function createServer(port = 8080, customRootDir = null) {
  return new Promise((resolve, reject) => {
    const rootDir = customRootDir 
      ? path.resolve(customRootDir)
      : path.join(__dirname, '..', '_site');

    const server = http.createServer((req, res) => {
      let reqPath = decodeURI(req.url.split('?')[0]);
      if (reqPath === '/' || reqPath === '') reqPath = '/index.html';

      // Normalize and guard against directory traversal
      const safePath = path.normalize(reqPath).replace(/^(\.\.[\/\\])+/, '');
      let filePath = path.join(rootDir, safePath);

      if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
        filePath = path.join(filePath, 'index.html');
      }

      if (!fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
        res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end(`404 Not Found: ${reqPath}`);
        return;
      }

      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': contentType });
      fs.createReadStream(filePath).pipe(res);
    });

    server.on('error', (err) => {
      if (err.code === 'EADDRINUSE') {
        console.warn(`[SERVER] Port ${port} is in use. Attempting ${port + 1}...`);
        server.close();
        resolve(createServer(port + 1, rootDir));
      } else {
        reject(err);
      }
    });

    server.listen(port, '127.0.0.1', () => {
      const activePort = server.address().port;
      console.log(`[SERVER] Serving ${rootDir} at http://127.0.0.1:${activePort}`);
      
      // Auto-cleanup on process exit
      const cleanup = () => {
        try {
          server.close();
          console.log(`[SERVER] Cleanly shut down port ${activePort}`);
        } catch (_) {}
      };
      process.once('SIGINT', cleanup);
      process.once('SIGTERM', cleanup);
      process.once('exit', cleanup);

      resolve({ server, port: activePort });
    });
  });
}

/**
 * Playwright helper: Creates a context with the onboarding tour modal disabled.
 * Prevents pointer event interception during automated E2E tests.
 */
async function createIsolatedContext(browser, options = {}) {
  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    ...options
  });

  // Inject onboarding bypass deterministically before any script loads
  await context.addInitScript(() => {
    try {
      localStorage.setItem('ir_onboarded_v1', 'true');
    } catch (_) {}
  });

  return context;
}

// CLI runner support
if (require.main === module) {
  const args = process.argv.slice(2);
  let port = 8080;
  let dir = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--port' || args[i] === '-p') {
      port = parseInt(args[i + 1], 10) || 8080;
      i++;
    } else if (args[i] === '--dir' || args[i] === '-d') {
      dir = args[i + 1];
      i++;
    }
  }

  createServer(port, dir).then(({ port: activePort }) => {
    console.log(`[SERVER] Ready for automated testing. Press Ctrl+C to terminate.`);
  }).catch((err) => {
    console.error(`[FATAL] Failed to start test server:`, err);
    process.exit(1);
  });
}

module.exports = {
  createServer,
  createIsolatedContext
};
