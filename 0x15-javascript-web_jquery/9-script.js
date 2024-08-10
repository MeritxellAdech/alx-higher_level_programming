/**
 * Display the respective value of the key-hello from an API
 */

$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const value = data.hello;
  $('#hello').append(value);
});
