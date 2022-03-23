console.log("Country field js loaded");

$('#id_default_country').css('color', '#aab7c4');

$('#id_default_country').change(function() {
    if ($(this).val() == "") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black');
    }
});



