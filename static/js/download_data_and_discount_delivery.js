console.log("Download data loaded")



$('#digital').change(function() {
    let status = $("#digital").is(':checked');
    console.log(status);
    this.form.submit();
    //if (status) {
    //    $('#digital').prop('checked', true);
    //} else {
    //    $('#digital').prop('checked', false);
    //}
    
    
});
