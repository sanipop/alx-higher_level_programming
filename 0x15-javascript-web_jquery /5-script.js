// Add div#add_item tag is clicked
// <li>Item</li> and mus to UL.my_list

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
