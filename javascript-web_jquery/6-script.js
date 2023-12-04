const $ = window.$;
$('DIV#update_header').click(() => {
  const update = 'New Header!!!';
  $('header').text(update);
});
