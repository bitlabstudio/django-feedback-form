function hideForm(mobile) {
    $('#feedbackForm').fadeOut('fast', function() {
        if (mobile) {
            $('#feedbackSnippet').animate({bottom: '-4'});
        } else {
            $('#feedbackSnippet').animate({left: '-4'});
        }
    });
}

function initiateForm(mobile) {
    $('#feedbackForm').unbind('submit');
    $('#feedbackForm input, #feedbackForm textarea').each(function() {
        $(this).attr('placeholder', $('[for=' + $(this).attr('id') + ']').text());
    });

    $('#feedbackForm #feedbackClose').click(function() {
        hideForm(mobile);
        return false;
    });

    $('#feedbackForm').submit(function() {
        var form = $(this);
        $.post(form.attr('action'), form.serializeArray(), function(data) {
            if (data.toLowerCase().indexOf('errorlist') == -1) {
                hideForm(mobile);
                if (mobile) {
                    $('#feedbackSuccess').fadeIn().delay(2000).animate({bottom: '-500'}).fadeOut().animate({bottom: '40'});
                } else {
                    $('#feedbackSuccess').fadeIn().delay(2000).animate({left: '-500'}).fadeOut().animate({left: '40'});
                }
            }
            form.html(data);
            initiateForm(mobile);
        });
        return false;
    });

    $('#feedbackSnippet').attr('href', '#');
    $('#feedbackSnippet').click(function() {
        if (mobile) {
            $(this).animate({bottom: '-100'});
        } else {
            $(this).animate({left: '-100'});
        }
        $('#feedbackForm').fadeIn();
        $('html').click(function() {
            hideForm(mobile);
         });

         $('#feedbackForm').click(function(event){
            event.stopPropagation();
         });
        return false;
    });
}

$(document).ready(function() {
    if ($('body').innerWidth() < 768) {
        initiateForm(true);
    } else {
        initiateForm(false);
    }
});