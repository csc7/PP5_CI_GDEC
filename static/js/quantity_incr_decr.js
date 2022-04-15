// From Code Institute

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

// Update quantity on click for the bag
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click the bag
$('.remove-item').click(function(e) {
    //var csrfToken = "{{ csrf_token }}";
    var itemId;
    if ($(window).width() < 768) {
        itemId = $(this).attr('id').split('remove-from-bag-small-screen_')[1];
    } else {
        itemId = $(this).attr('id').split('remove-from-bag-large-screen_')[1];
    } 
    var resolution = $(this).data('product_resolution');
    var url = `/bag/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'product_resolution': resolution};
    $.post(url, data)
     .done(function() {
         location.reload();
     });
})

// Update quantity on click for the wish list
$('.update-link-wish-list').click(function(e) {

    if ($(window).width() < 768) {
        $('#form-wish-list-small-screen').submit();
    } else {
        $('#form-wish-list-large-screen').submit();
    } 
})

// Remove item and reload on click for the wish list in large screens
console.log($(this).attr('id'))
$('.remove-item-wish-list').click(function(e) {
    //var csrfToken = "{{ csrf_token }}";
    var itemId;
    if ($(window).width() < 768) {
        itemId = $(this).attr('id').split('remove-from-wish-list-small-screen_')[1];
    } else {
        itemId = $(this).attr('id').split('remove-from-wish-list-large-screen_')[1];
    }    
    var resolution = $(this).data('product_resolution');
    var url = `/wish_list/remove_from_wish_list/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'product_resolution': resolution};
    $.post(url, data)
     .done(function() {
         location.reload();
     });
})

console.log("Incr/Decr JS loaded");

// Change "Update Quantity" and "Remove Product" to "Update" and "Remove"
// in middle size screens
$(window).on('resize', function(){
    if ($(window).width() < 992 && $(window).width() >=768) {
        $('.remove-item').html('<small>Remove</small>');
        $('.remove-item-wish-list').html('<small>Remove</small>');
        $('.update-link').html('<small>Update</small>');
        $('.update-link-wish-list').html('<small>Update</small>');
    } else {
        $('.remove-item').html('<small>Remove Product</small>');
        $('.remove-item-wish-list').html('<small>Remove Product</small>');
        $('.update-link').html('<small>Update Quantity</small>');
        $('.update-link-wish-list').html('<small>Update Quantity</small>');
    }

});

