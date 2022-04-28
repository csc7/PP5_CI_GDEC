// This Javascript function disables the minus and plus buttons when quantities
// are below 1 and above 98 respectively

// Copied and modified from Code Institute "Boutique Ado" project, except functions for
// classes ".update-link-wish-list", ".increment-qty-prod-det", ".decrement-qty-prod-det" and
// ".remove-item-wish-list"


// Check if input values in product details and wish list are between accepted
// limits when loading the page and disable control buttons if they are not.
// No need to do this in the bag, as the bag is built from the previous pages when
// adding products.
if (parseInt($('.decrement-qty-prod-det').closest('div').siblings('input').val()) <=1) {
    $('.decrement-qty-prod-det').prop('disabled', true);
}
if (parseInt($('.decrement-qty-prod-det').closest('div').siblings('input').val()) >=98) {
    $('.increment-qty-prod-det').prop('disabled', true);
}
if (parseInt($('.qty_input').val()) <=1) {
    $('.decrement-qty').prop('disabled', true);
}
    

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    var currentValue;
    var minusDisabled = currentValue <= 2;
    var plusDisabled = currentValue >= 98;
    if ($(window).width() < 768) {
        currentValue = parseInt($(`#ss_id_qty_${itemId}`).val());
        $(`#ss_decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#ss_increment-qty_${itemId}`).prop('disabled', plusDisabled);
    } else {
        currentValue = parseInt($(`#ls_id_qty_${itemId}`).val());
        $(`#ls_decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#ls_increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }
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

    var itemId2;

    // For bag
    handleEnableDisable(itemId);

    // For wish list
    if (currentValue <= 2) {
        itemId2 = $(this).closest('td').find('button')[0];
        $(`#${itemId2.id}`).prop('disabled',false);
    }
    if (currentValue >=98) {
        itemId2 = $(this).closest('td').find('button')[1];
        $(`#${itemId2.id}`).prop('disabled',true);
    }
});


// Decrement quantity in product details only
$('.decrement-qty-prod-det').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('div').siblings();
    
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);

    var itemIdMinus;

    if (currentValue <=2) {
        itemIdMinus = $(this).closest('button');
        $(itemIdMinus).prop('disabled',true);
    }
    if (currentValue >= 98) {
        itemIdMinus = $(this).parents().siblings('div').children('button');
        $(itemIdMinus).prop('disabled',false);
    } 
});


// Increment quantity in product details only
$('.increment-qty-prod-det').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('div').prev().prev();
    
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);

    var itemIdPlus;

    if (currentValue >= 98) {
        itemIdPlus = $(this).closest('button');
        $(itemIdPlus).prop('disabled',true);
    }
    if (currentValue <=2) {
        itemIdPlus = $(this).parents().siblings('div').children('button');
        $(itemIdPlus).prop('disabled',false);
    }
});


// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');

    // For bag
    handleEnableDisable(itemId);

    var itemId2;
   
    // For wish list
    if (currentValue >= 98) {
        itemId2 = $(this).closest('td').find('button')[1];
        $(`#${itemId2.id}`).prop('disabled',false);
    }
    if (currentValue <=2) {
        itemId2 = $(this).closest('td').find('button')[0];
        $(`#${itemId2.id}`).prop('disabled',true);
    }
});


// Update quantity on click for the bag
$('.update-link').click(function(e) {

    var full_itemId = $(this).attr('id');
    var resolutionText;
    var resolution;
    var url;
    var quantity = $(this).closest('td').find('.qty_input').val();
    
    if ($(window).width() < 768) {        
        itemId = full_itemId.split('update-bag-small-screen_')[1];
        itemId = itemId.split('_')[0];

        // Split text in different statges until resolution is achieved
        // This way in order to guarantee we are accessing it regardless
        // the amount of rows in the table for small screens, which does not
        // contain all elements in the same row
  
        resolutionText = $(this).closest('tr').prevAll('tr').first().text();
        resolutionText = resolutionText.split('Resolution: ')[1];
        resolution = resolutionText.split(' ')[0];
        url=`adjust/${itemId}/`;

    } else {
        itemId = full_itemId.split('update-bag-large-screen_')[1];
        itemId = itemId.split('_')[0];

        // Read resolution, if available, of item in wish list, by accessing
        // the resolution in the same row (product) of the table
        resolutionText = $(this).closest('tr').children("td:nth-child(2)").children("p:nth-child(2)").text();
        resolution = resolutionText.split(' ')[1];
        url=`adjust/${itemId}/`;
    }

    //var csrfToken;

    $.ajax({
    type: 'POST',        
    url: url,
    data: {
        'csrfmiddlewaretoken': csrfToken,
        'itemId': itemId,
        'resolution' : resolution,
        'quantity': quantity},
    success: function () {
        window.location = '/bag/';
    }
    });
});


$('.remove-item').click(function(e) {
    var full_itemId = $(this).attr('id');
    var resolutionText;
    var resolution;
    var url;

    if ($(window).width() < 768) {
        itemId = full_itemId.split('remove-from-bag-small-screen_')[1];
        itemId = itemId.split('_')[0];
        // Split text in different statges until resolution is achieved
        // This way in order to guarantee we are accessing it regardless
        // the amount of rows in the table for small screens, which does not
        // contain all elements in the same row
        resolutionText = $(this).closest('tr').prevAll('tr').first().text();
        resolutionText = resolutionText.split('Resolution: ')[1];
        resolution = resolutionText.split(' ')[0];
        url=`remove/${itemId}/`;

    } else {
        itemId = full_itemId.split('remove-from-bag-large-screen_')[1];
        itemId = itemId.split('_')[0];

        // Read resolution, if available, of item in wish list, by accessing
        // the resolution in the same row (product) of the table
        resolutionText = $(this).closest('tr').children("td:nth-child(2)").children("p:nth-child(2)").text();
        resolution = resolutionText.split(' ')[1];
        url=`remove/${itemId}/`;
    }

    //var csrfToken;
    
    // Send AJAX post to remove_from_wish_list in views.py of wish app
    $.ajax({
        type: 'POST',        
        url: url,
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'itemId': itemId,
            'resolution' : resolution},
        success: function () {
             location.reload();
        }
    });
});


// Update quantity on click for the wish list
$('.update-link-wish-list').click(function(e) {

    var full_itemId = $(this).attr('id');
    var resolutionText;
    var resolution;
    //var quantity = parseInt($(`#id_qty_${itemId}`).val());
    //var quantity = $(this).closest('td').children().children().children("input").val();
    var quantity = $(this).closest('td').find('.qty_input').val();

    if ($(window).width() < 768) {

        itemId = full_itemId.split('update-from-wish-list-small-screen_')[1];

        // Split text in different statges until resolution is achieved
        // This way in order to guarantee we are accessing it regardless
        // the amount of rows in the table for small screens, which does not
        // contain all elements in the same row
  
        resolutionText = $(this).closest('tr').prevAll('tr').first().text();
        resolutionText = resolutionText.split('Resolution: ')[1];
        resolution = resolutionText.split(' ')[0];

    } else {

        itemId = full_itemId.split('update-from-wish-list-large-screen_')[1];

        // Read resolution, if available, of item in wish list, by accessing
        // the resolution in the same row (product) of the table
        resolutionText = $(this).closest('tr').children("td:nth-child(2)").children("p:nth-child(2)").text();
        resolution = resolutionText.split(' ')[1];
    }

    //var csrfToken;
    
    // Send AJAX post to adjust_wish_list in views.py of wish app, with ID and resolution
    $.ajax({
    type: 'POST',        
    url: '/wish_list/adjust_wish_list/',
    data: {
        'csrfmiddlewaretoken': csrfToken,
        'itemId': itemId,
        'resolution' : resolution,
        'quantity': quantity},
    success: function () {
        window.location = '/wish_list/';
    }
    });
});


// Send data to database using AJAX
$(document).on("click", ".remove-item-wish-list", function() {
    
    var full_itemId = $(this).attr('id');
    var resolutionText;
    var resolution;
    
    if ($(window).width() < 768) {
        itemId = full_itemId.split('remove-from-wish-list-small-screen_')[1];

        // Split text in different statges until resolution is achieved
        // This way in order to guarantee we are accessing it regardless
        // the amount of rows in the table for small screens, which does not
        // contain all elements in the same row
        resolutionText = $(this).closest('tr').prevAll('tr').first().text();
        resolutionText = resolutionText.split('Resolution: ')[1];
        resolution = resolutionText.split(' ')[0];

    } else {
        itemId = full_itemId.split('remove-from-wish-list-large-screen_')[1];

        // Read resolution, if available, of item in wish list, by accessing
        // the resolution in the same row (product) of the table
        resolutionText = $(this).closest('tr').children("td:nth-child(2)").children("p:nth-child(2)").text();
        resolution = resolutionText.split(' ')[1];
    }

    //var csrfToken;

    // Send AJAX post to remove_from_wish_list in views.py of wish app
    $.ajax({
        type: 'POST',        
        url: '/wish_list/remove_from_wish_list/',
        //dataType: 'json',
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'itemId': itemId,
            'resolution' : resolution},
        success: function () {
             location.reload();
        }
    });
});


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
