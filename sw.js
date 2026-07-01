self.addEventListener('push', function(event) {
  if (!event.data) return;
  const data = event.data.json();
  const options = {
    body: data.body || '새 신호가 발생했습니다.',
    icon: '/favicon-192v2.png',
    badge: '/favicon-192v2.png',
    vibrate: [200, 100, 200],
    data: { url: data.url || '/' },
    actions: [
      { action: 'open', title: '확인하기' }
    ]
  };
  event.waitUntil(
    self.registration.showNotification(data.title || '차티스트 인사이트', options)
  );
});

self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  const url = event.notification.data.url || '/';
  event.waitUntil(clients.openWindow(url));
});
