$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (resp, status) {
    if (status === 'success') {
      $('#hello').text(data.hello);
    }
  });
});
