// This is the "Offline copy of assets" service worker
//cacheTo

const CACHE_NAME = "WebDeveloper2" , urlsToCache = [
  /*Aquí se cargan todos los archivos que utilizaré para mi PWA*/
  './',
  './index.html',
  './styles.css',

  './regist_serviceWorker.js',
  './Service_Worker.js',

  './images/01.jpg',
  './images/02.jpg',
  './images/03.jpg',
  './images/04.jpg',
  './images/icon-24x24.png',
  './images/icon-42x42.png',
  './images/icon-72x72.png',
  './images/icon-96x96.png',
  './images/icon-128x128.png',
  './images/icon-144x144.png',
  './images/icon-152x152.png',
  './images/icon-192x192.png',
  './images/icon-256x256.png',
  './images/icon-384x384.png',
  './images/icon-512x512.png',
  './main.js',
  './manifest.json',

];

//Durante la fase de instalación, generalmente se almacena en caché los activos estáticos.
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache)
          .then(() => self.skipWaiting())
      })
      .catch(err => console.log('Falló registro de cache', err))
  )
})

//Una vez que se instala el SW, se activa y busca los recursos para hacer que funcione sin conexión.
self.addEventListener('activate', e => {
  const cacheWhitelist = [CACHE_NAME]

  e.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            //Eliminamos lo que ya no se necesita en cache
            if (cacheWhitelist.indexOf(cacheName) === -1) {
              return caches.delete(cacheName)
            }
          })
        )
      })
      // Le indica al SW activar el cache actual
      .then(() => self.clients.claim())
  )
})

//Cuando el navegador recupera una url
self.addEventListener('fetch', e => {
  //Responder ya sea con el objeto en caché o continuar y buscar la url real
  e.respondWith(
    caches.match(e.request)
      .then(res => {
        if (res) {
          //Recuperar del cache
          return res
        }
        //Recuperar de la petición a la url
        return fetch(e.request)
      })
  )
})