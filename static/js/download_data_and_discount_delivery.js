console.log("Download data loaded")

$('#digital').change(function() {
    if ($('#digital').is(':checked')) {
        let applyDiscount = 1;
        console.log("clicking");
        $.ajax({
            type: 'POST',        
            url: {% url 'adjust_bag' %},
            data: {
                'applyDiscount' : applyDiscount },                
            success: function (data) {
              if (applyDiscount){
                  alert("Database updated, new data will appear below.");
                }
            }               
        });

    }
});
