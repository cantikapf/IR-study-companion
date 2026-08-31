---
layout: null
---
const CACHE_NAME = 'ir-companion-lms-v3';
const urlsToCache = [
  '{{ site.baseurl }}/',
  '{{ site.baseurl }}/assets/css/course-player.css',
  '{{ site.baseurl }}/assets/js/course-player.js',
  '{{ site.baseurl }}/{{ site.favicon_path }}'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Network-first for navigation (HTML pages), Stale-while-revalidate for static assets
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  
  // For page navigation (HTML), always fetch fresh from network first
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request)
        .then(networkResponse => {
          if (networkResponse.ok) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, responseClone);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          return caches.match(event.request).then(cachedResponse => {
            return cachedResponse || caches.match('{{ site.baseurl }}/');
          });
        })
    );
    return;
  }

  // Stale-while-revalidate for static assets (CSS, JS, fonts, images)
  event.respondWith(
    caches.match(event.request)
      .then(cachedResponse => {
        const fetchPromise = fetch(event.request).then(networkResponse => {
          if (networkResponse.ok) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, responseClone);
            });
          }
          return networkResponse;
        }).catch(() => {
          return cachedResponse;
        });
        
        return cachedResponse || fetchPromise;
      })
  );
});
