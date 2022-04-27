// This JavaScript function shows and hide the button to make comments
// in the product details


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

    var itemId = $(this).closest('form').attr('action');
    itemId = itemId.split('add/')[1].slice(0, -1);
    var resolution = $(this).closest('form').find('select').val();
   
    var url=`/wish_list/add_to_wish_list/${itemId}/`;

    var redirect_url = `/products/${itemId}`;

    var quantity = $(this).closest('form').find('.qty_input').val();

    var csrfToken;

    $.ajax({
        type: 'POST',        
        url: url,
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'itemId': itemId,
            'resolution' : resolution,
            'redirect_url':redirect_url,
            'quantity': quantity},
        success: function () {
             location.reload();
        }
    });

});
