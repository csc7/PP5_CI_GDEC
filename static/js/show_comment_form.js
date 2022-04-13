// Show comment form in product details
$('#comment-form-button').click(function() {
    if ($('#comment-form-button').text() =='Leave a Comment') {
        $('#comment-form').css('display', 'inline');
        $('#comment-form-button').text('Hide Comment Form');
    } else {
        if ($('#comment-form-button').text() =='Hide Comment Form') {
            $('#comment-form').css('display', 'none');
            $('#comment-form-button').text('Leave a Comment');
        }
    }
});