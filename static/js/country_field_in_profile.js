// This Javascript function changes the style of the country list in the
// Django forms, showing them unselected until the selection occurs

// Copied and modified from Code Institute "Boutique Ado" project

$('#id_default_country').css('color', '#aab7c4');

$('#id_default_country').change(function() {
    if ($(this).val() == "") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black');
    }
});
