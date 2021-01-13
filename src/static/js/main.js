$(document).ready(function () {
    $('.service-info').each(function (f) {
        var newstr = $(this).text().substring(0, 350);
        $(this).text(newstr + '.....');
    });

    $('.btn-close').click(function(e){
        $(".navbar-collapse").removeClass("show");
        $("body").removeClass("offcanvas-active");
    })

    const dateTimePickerInit = () => {
        $('#datetime, div[id^=cart_datetime-]').datetimepicker({
            format: 'DD/MM/YYYY HH:mm',
            minDate: new Date(),
            enabledHours: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            stepping: 30,
        });
        $('div[id^=cart_datetime-]').each(function () {
            $(this).children('input.datetimepicker-input').val($(this).data('value'));
          });
    };
    dateTimePickerInit();
});