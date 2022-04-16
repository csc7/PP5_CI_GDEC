// Disable Mailchimp submit button to avoid sending a blank e-mail address
$( "#mce-EMAIL" ).click(function() {
    $("#mce-EMAIL").val('');
    $("#Mailchimp-newsletter-button").prop("disabled",true);
    $("#Mailchimp-newsletter-button>span>p").removeClass("text-light");
    $("#Mailchimp-newsletter-button>span>p").addClass("text-info");
    $("#Mailchimp-newsletter-button").css("display","inline");
});


// Detect changes in input (user writing e-mail) and activate/deactivate
// submit button when e-mail address is validated.

$("#mce-EMAIL").on("input", function() {
    if ($("#mce-EMAIL").val()==''){
        $("#Mailchimp-newsletter-button>span>p").removeClass("text-light");
        $("#Mailchimp-newsletter-button>span>p").addClass("text-info");
    }
    if (validateEMail($("#mce-EMAIL").val())) {
        $("#Mailchimp-newsletter-button").prop("disabled",false);
        $("#Mailchimp-newsletter-button").attr('type', 'submit');
        $("#Mailchimp-newsletter-button>span>p").removeClass("text-info");
        $("#Mailchimp-newsletter-button>span>p").addClass("text-light");
    } else {
        $("#Mailchimp-newsletter-button").prop("disabled",true);
        $("#Mailchimp-newsletter-button>span>p").removeClass("text-light");
        $("#Mailchimp-newsletter-button>span>p").addClass("text-info");
        $("#Mailchimp-newsletter-button").attr('type', 'button');
    }
});


// Check if a form is submitted with jQuery
// https://stackoverflow.com/questions/14969467/how-to-check-with-jquery-if-any-form-is-submitted,
// accessed on April 9th, 2022, at 15:30, except validateEMail() function

$("#mc-embedded-subscribe-form").submit(function(e) {
    e.preventDefault();

    // Do not show form again after submitting it
    $("#mce-EMAIL").hide();
    $("#mc-embedded-subscribe-form > div > div.input-group-append > button").hide();

    // Assign success and red colours for returning messages of Mailchimp form
    $("#mce-success-response").css("color", "rgb(75, 241, 131)");
    $("#mce-success-response").css("font-size", "80%");
    $("#mce-success-response").css("padding-top", "3px");
    $("#mce-error-response").css("color", "rgb(255, 0, 0)");
    $("#mce-error-response").css("font-size", "80%");
    $("#mce-error-response").css("padding-top", "3px");

    console.log($("#mce-error-response"));

    // Do not display "Sing up for newsletter" message withing this widths as the height of the footer is not enough
    if ($(window).width() > 992 && $(window).width() < 1080) {
        $("#div-for-newsletter-form-message").css("display", "none");
    }

    // Change style of Mailchimp form messages (after submission)
    if ($(window).width() < 992) {
        $("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("text-align", "center");
        $("#mce-responses").css("margin", "auto");
        $("#mce-success-response").css("text-align", "center");
        $("#mce-error-response").css("text-align", "center");
    } else {
        $("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("text-align", "left");
        $("#mce-success-response").css("text-align", "left");
        $("#mce-error-response").css("text-align", "left");
    };
    $("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("padding-left", "10px");

});


// Validate e-mail address, very basic function, not all non-permitted characters included
function validateEMail(eMailAddress) {

    var numberOfAtSign = 0;
    var numberOfDots = 0;
    var numberOfOtherCharacters = 0;
    var allCharacters = '@.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    //Basic validation of e-mail address before hiding it
    var eMailString = eMailAddress;
    for (var i=0; i < eMailString.length; i++) {
        if (eMailString[i] == '@') {
            numberOfAtSign++;
        }
        if (eMailString[i] == '.') {
            numberOfDots++;
        }
        // Some wrong characters for e-mail addresses
        if (eMailString[i] == '|' || eMailString[i] == '#' || eMailString[i] == '$' || eMailString[i] == '%' ||
            eMailString[i] == '&' || eMailString[i] == '/' || eMailString[i] == '(' || eMailString[i] == ')' || 
            eMailString[i] == '=' || eMailString[i] == '?' || eMailString[i] == '¡' || eMailString[i] == '+' ||  
            eMailString[i] == '*' || eMailString[i] == '°' || eMailString[i] == '{' || eMailString[i] == '}') {
            numberOfOtherCharacters++;
        }
        
    }
    console.log(numberOfAtSign + ' ' + numberOfDots + ' ' + numberOfOtherCharacters + '' + eMailString[eMailString.length-1]);
    // There must be only one at sign, at least one dot, and no other characters
    // to validate the e-mail address
    if (numberOfAtSign == 1 && numberOfDots > 0 && numberOfOtherCharacters == 0 && eMailString[eMailString.length-1] !='.') {
        return true;
    } else {
        return false;
    }
}