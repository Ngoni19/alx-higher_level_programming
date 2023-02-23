$(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    let itm = $('ul.my_list li');
    if (itm.length > 0) {
      itm[itm.length - 1].remove();
    }
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
