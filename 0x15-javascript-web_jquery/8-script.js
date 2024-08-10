/**
 * List all the movie title from an API
 */

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const res = data.results;
  let i = 0;
  $.each(res, function () {
    $('#list_movies').append(`<li>${res[i++].title}</li>`);
  });
});
