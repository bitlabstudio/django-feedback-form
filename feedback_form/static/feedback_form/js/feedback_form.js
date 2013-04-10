function hideForm() {
    $('#feedbackForm').fadeOut('fast', function() {
        $('#feedbackSnippet').animate({left: '-5'});
    });
}

function initiateForm() {
    $('#feedbackForm').unbind('submit');
    $('#feedbackForm input, #feedbackForm textarea').each(function() {
        $(this).attr('placeholder', $('[for=' + $(this).attr('id') + ']').text());
    });

    $('#feedbackForm #feedbackClose').click(function() {
        hideForm();
        return false;
    });

    $('#feedbackForm').submit(function() {
        var form = $(this);
        $.post(form.attr('action'), form.serializeArray(), function(data) {
            if (data.toLowerCase().indexOf('errorlist') == -1) {
                hideForm();
                $('#feedbackSuccess').fadeIn().delay(2000).animate({left: '-500'}).fadeOut().animate({left: '10'});
            }
            form.html(data);
            initiateForm();
        });
        return false;
    });
}

$(document).ready(function() {
    initiateForm();

    $('#feedbackSnippet').attr('href', '#');
    $('#feedbackSnippet').click(function() {
        $(this).animate({left: '-100'});
        $('#feedbackForm').fadeIn();
        $('html').click(function() {
            hideForm();
         });

         $('#feedbackForm').click(function(event){
            event.stopPropagation();
         });
        return false;
    });
});