// This JavaScript function shows and hide the button to make comments in the product details


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
    //$('#add-product-form').attr('action', '{% url "add_to_wish_list" product.id %}');
    //$("form").submit();
    //var page_id = document.getElementById("add-product-form").options.selectedIndex;

    itemId = $(this).closest('form').attr('action');
    itemId = itemId.split('add/')[1].slice(0, -1);
    resolution = $(this).closest('form').find('select').val();

    console.log(itemId);
    console.log(resolution);
    
    var url=`/wish_list/add_to_wish_list/${itemId}/`;
    console.log(url);

    var redirect_url = `/products/${itemId}`;
    console.log(redirect_url);

    quantity = $(this).closest('form').find('.qty_input').val();
    console.log(quantity);

    $.ajax({
        type: 'POST',        
        url: url,
        //dataType: 'json',
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
