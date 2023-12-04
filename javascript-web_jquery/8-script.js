const $ = window.$;
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  success: (data) => {
    data.results.forEach((movie) => {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
