$(document).ready(function () {
    $("#messageForm").on("submit", function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $("#messageForm").action,
            data: $(this).serialize(),
            dataType: "json",
            success: function () {

            }
        })
        $("#name").val("");
        $("#message").val("");
    })
})

