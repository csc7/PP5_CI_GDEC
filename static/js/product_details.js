// Show comment form in product details
$('#comment-form-button').click(function() {
    if ($('#comment-form-button').text() =='Leave a Comment') {
        $('#comment-form').css('display', 'inline');
        $('#comment-form-button').text('Hide Comment Form');
    } else {
        if ($('#comment-form-button').text() =='Hide Comment Form') {
            $('#comment-form').css('display', 'none');
            $('#comment-form-button').text('Leave a Comment');
        }
    }
});


// Change form action to have it sent to the bag or wish list, based
// on the clicked button

$('#send-to-wish-list-button').click(function() {
    $('#add-product-form').attr('action', '{% url "add_to_wish_list" product.id %}');
    $("form").submit();
    //var page_id = document.getElementById("add-product-form").options.selectedIndex;

});
