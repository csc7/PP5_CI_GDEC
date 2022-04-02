console.log("Download data loaded")

$('#digital').change(function() {
    let status = $("#digital").is(':checked');
    console.log(status);
    this.form.submit();
    //if (status) {
    //    $('#cancel_delivery_cost>label').html("Check this box to download the data and avoid shipment costs");
    //} else {
    //    $('#cancel_delivery_cost>label').html("Uncheck this box to receive the data in USB drives (delivery costs apply)");
    //}    
});
