$(document).ready(function () {
    $('.service-info').each(function (f) {
        var newstr = $(this).text().substring(0, 350);
        $(this).text(newstr + '.....');
    });

    $('.btn-close').click(function (e) {
        $(".navbar-collapse").removeClass("show");
        $("body").removeClass("offcanvas-active");
    })

    const dateTimePickerInit = () => {
        $('#datetime, div[id^=cart_datetime-], div[id^=cart_datetime_sm-]').datetimepicker({
            format: 'DD/MM/YYYY HH:mm',
            minDate: new Date(),
            enabledHours: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            stepping: 30,
        });
        $('div[id^=cart_datetime-], div[id^=cart_datetime_sm-]').each(function () {
            $(this).children('input.datetimepicker-input').val($(this).data('value'));
        });
    };
    dateTimePickerInit();

    $('.btt-link').click(function (e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, '100');
    })

    bttbutton = document.getElementById("back-top-btn");
    window.onscroll = function () {
        scrollFunction()
    };

    function scrollFunction() {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 100) {
            bttbutton.style.display = "block";
        } else {
            bttbutton.style.display = "none";
        }
    }
});