
const CACHE_NAME = "discover-balochistan-v3";

const FILES_TO_CACHE = [
    "/",
    "/static/manifest.json",
    "/static/css/style.css",
    "/static/js/app.js",

    // App icons
    "/static/icons/icon-192.png",
    "/static/icons/icon-512.png",
    "/static/icons/icon-512-maskable.png",

    // Offline destination database
    "/static/data/destinations.json",

    // Offline destination photographs
    "/static/images/hingol.jpg",
    "/static/images/kund-malir.jpg",
    "/static/images/ziarat.jpg",
    "/static/images/hanna-lake.jpg",
    "/static/images/gwadar.jpg",
    "/static/images/moola-chotok.jpg"
];


// Install service worker and cache essential files
self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(async (cache) => {
            await cache.addAll(FILES_TO_CACHE);
            console.log("All offline files cached successfully.");
        })
    );

    self.skipWaiting();
});


// Activate new service worker
self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((names) => {
            return Promise.all(
                names
                    .filter((name) => name !== CACHE_NAME)
                    .map((name) => caches.delete(name))
            );
        }).then(() => self.clients.claim())
    );
});


// Handle network requests
self.addEventListener("fetch", (event) => {

    if (event.request.method !== "GET") return;

    const url = new URL(event.request.url);

    // Only handle requests from this website
    if (url.origin !== self.location.origin) return;

    event.respondWith(
        caches.match(event.request).then(async (cachedResponse) => {

            // Return cached file when available
            if (cachedResponse) {
                return cachedResponse;
            }

            try {
                const response = await fetch(event.request);

                if (response && response.ok) {
                    const cache = await caches.open(CACHE_NAME);

                    cache.put(
                        event.request,
                        response.clone()
                    );
                }

                return response;

            } catch (error) {

                // Return cached homepage for offline navigation
                if (event.request.mode === "navigate") {
                    return await caches.match("/");
                }

                return new Response(
                    "Offline: resource unavailable.",
                    {
                        status: 503,
                        headers: {
                            "Content-Type": "text/plain"
                        }
                    }
                );
            }
        })
    );
});
