// Check if a form is submitted with jQuery
// https://stackoverflow.com/questions/14969467/how-to-check-with-jquery-if-any-form-is-submitted,
// accessed on April 9th, 2022, at 15:30.

$("#mc-embedded-subscribe-form").submit(function(e) {
    e.preventDefault();

    // Do not show form again after submitting it
    $("#mce-EMAIL").hide();
    $("#mc-embedded-subscribe-form > div > div.input-group-append > button").hide();

    // Assign success and red colours for returning messages of Mailchimp form
    $("#mce-success-response").css("color", "rgb(75, 241, 131)");
    $("#mce-error-response").css("color", "rgb(255, 0, 0)");
    console.log($("#mce-error-response"));

    // Do not display "Sing up for newsletter" message withing this widths as the height of the footer is not enough
    if ($(window).width() > 992 && $(window).width() < 1080) {
        $("#div-for-newsletter-form-message").css("display", "none");
    }

    // Change style of Mailchimp form messages (after submission)
    if ($(window).width() < 992) {
        $("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("text-align", "center");
    } else {
        $("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("text-align", "left");
        $("#mce-success-response").css("text-align", "left");
        $("#mce-error-response").css("text-align", "left");
    };
    $("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("padding-left", "10px");
});
