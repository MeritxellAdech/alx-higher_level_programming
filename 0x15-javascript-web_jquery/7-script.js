/**
 * Fetch the name of a character from an API
 */

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const name = data.name;
  $('#character').text(name);
});
