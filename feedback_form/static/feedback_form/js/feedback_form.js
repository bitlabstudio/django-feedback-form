$(document).ready(function() {
    $('#feedbackForm input, #feedbackForm textarea').each(function() {
        $(this).attr('placeholder', $('[for=' + $(this).attr('id') + ']').text());
    });

    $('#feedbackSnippet').attr('href', '#');
    $('#feedbackSnippet').click(function() {
        $(this).animate({left: '-100'});
        $('#feedbackForm').fadeIn();
        return false;
    });

    $('#feedbackForm #feedbackClose').click(function() {
        $('#feedbackForm').fadeOut('fast', function() {
            $('#feedbackSnippet').animate({left: '-5'});
        });
        return false;
    });
});