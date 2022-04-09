$("#mc-embedded-subscribe-form").submit(function(e) {
e.preventDefault();
$("#mce-EMAIL").hide();
$("#mc-embedded-subscribe-form > div > div.input-group-append > button").hide();
$("#mce-success-response").css("color", "rgb(75, 241, 131)");
$("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("color", "white");
$("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("text-align", "left");
$("#div-for-newsletter-in-footer > div > div > div:nth-child(4) > p").css("padding-left", "10px");
});