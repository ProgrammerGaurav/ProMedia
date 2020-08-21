$(".delete").click(function (e) {
    var id = this.id;
    var href = this.href;
    e.preventDefault();
    $("#" + id).fadeOut("fast");
    $.ajax({
        url: href,
        data: {},
    });

});

$(".like").click(function (e) {
    var href = this.href;
    var id = this.id;
    e.preventDefault();
    $.ajax({
        url: href,
        data: {},
        success: function (response) {
            if (response.liked) {
                $("#" + id + " > i").addClass("fas");
                $("#" + id + " > i").removeClass("far");
                $("#" + id + " > i").addClass("animate__heartBeat");
            } else {
                $("#" + id + " > i").addClass("far");
                $("#" + id + " > i").removeClass("fas");
                $("#" + id + " > i").removeClass("animate__heartBeat");
            }
        },
    });
});