$(document).ready(function () {
    $('.service-info').each(function (f) {

        var newstr = $(this).text().substring(0, 350);
        $(this).text(newstr + '.....');

    });
});