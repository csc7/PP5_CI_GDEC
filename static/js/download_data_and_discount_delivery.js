console.log("Download data loaded")

$('#digital').change(function() {
    if ($('#digital').is(':checked')) {
        let applyDiscount = 1;
        console.log("clicking");
        $.ajax({
            type: 'POST',        
            url: '/contexts.py',
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
