// This Javascript function informs Django admin of an image change

// Copied and modified from Code Institute "Boutique Ado" project

$('#id_image_name').change(function() {
    var file = $('#id_image_name')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
    $('body > div.container.mb-2.dark-blue-font > div:nth-child(2) > div > form > span').css('color', 'blue');    
    $(this).css('color', 'blue');
});
