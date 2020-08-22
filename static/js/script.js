$(".delete").click(function (e) {
    var id = this.id;
    var href = this.href;
    e.preventDefault();

    $.ajax({
        url: href,
        data: {},
        success: function () {
            $("#" + id).addClass("animate__fadeOutLeft");
            $("#" + id).fadeOut("slow");
        }
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

$(".follow").click(function (e) {
    var id = this.id;
    var href = this.href;
    e.preventDefault();
    $.ajax({
        url: href,
        data: {},
        success: function (response) {
            if (response.followed) {
                $("#" + id).html("unfollow");
                $("#" + id).removeClass("btn-outline-primary");
                $("#" + id).addClass("btn-primary");
                $("#" + id).addClass("animate__pulse");

            } else {
                $("#" + id).html("follow");
                $("#" + id).addClass("btn-outline-primary");
                $("#" + id).removeClass("btn-primary");
                $("#" + id).removeClass("animate__pulse");
            }
        },
    });

});

function workinpro() {
    alert("Ye banane nahi aata, abhi kaam chalu hai");
}