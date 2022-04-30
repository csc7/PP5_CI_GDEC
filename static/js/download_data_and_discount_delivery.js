// This JavaScript function checks if the user has selected the option
// to have the data downloaded and therefore avoid shipping costs

$('#digital').change(function() {
    var status = $("#digital").is(':checked');
    console.log(status);
    this.form.submit();

    //$.ajax({
    //type: 'POST',        
    //url: '/bag/',
    //data: {
    //    'csrfmiddlewaretoken': csrfToken,
    //    'status': status},
    //success: function () {
    //    //window.location = '/view_bag/';
    //    $("#digital").load(location.href+" #digital>*","");
    //}
    //});


});
