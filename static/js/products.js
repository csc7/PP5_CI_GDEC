// This Javascript function returns to top of page when clicking
// on the arrow bottom right

// Copied and modified from Code Institute "Boutique Ado" project


$('.go-to-top-button-link').click(function(e) {
    window.scrollTo(0,0);
});

$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});


// Alert superuser before deleting a product
$('.delete-product-from-database').click(function(){
    return confirm('\nThis will delete the product or comment' +
        ' from the database.\n\nClick "Ok" to confirm and delete;' +
        ' or click "Cancel" to avoid any change.');
});