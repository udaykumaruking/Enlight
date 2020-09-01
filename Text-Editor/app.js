document.getElementById('heading').innerHTML =
  localStorage['title'] || 'Just Write';
document.getElementById('content').innerHTML =
  localStorage['text'] || 'This Text is saved automatically';

setInterval(function () {
  localStorage['title'] = document.getElementById('heading').innerHTML;
  localStorage['text'] = document.getElementById('content').innerHTML;
}, 1000);
