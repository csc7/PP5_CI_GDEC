// This JavaScript function checks if the user has selected the option
// to have the data downloaded and therefore avoid shipping costs

$('#digital').change(function() {
    var status = $("#digital").is(':checked');
    this.form.submit();   
});
