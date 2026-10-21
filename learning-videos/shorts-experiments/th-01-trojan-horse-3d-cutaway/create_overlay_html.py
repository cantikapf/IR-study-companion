const fs = require("fs");

const srcPath = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html";
let html = fs.readFileSync(srcPath, "utf-8");

// Make body transparent and remove video-bg and canvas background
html = html.replace(
  `body {`,
  `body { background: transparent !important;`
);

html = html.replace(
  `#canvas-root {`,
  `#canvas-root { background: transparent !important;`
);

html = html.replace(
  `<img id="video-bg"`,
  `<img id="video-bg" style="display: none !important;"`
);

// Disable updateVideoPlate calls in GSAP
html = html.replace(
  /tl\.call\(\(\) => updateVideoPlate\(timeSec\), null, timeSec\);/g,
  `// updateVideoPlate disabled for native FFmpeg MP4 stream compositing`
);

fs.writeFileSync(
  "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition_overlay.html",
  html
);

console.log("Created composition_overlay.html with transparent background!");
