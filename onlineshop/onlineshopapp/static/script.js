$(document).ready(function () {
    let Storage = window.localStorage;
    $("#name").val(Storage.getItem("username"));
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
        Storage.setItem("username", $("#name").val());
        $("#name").val("");
        $("#message").val("");
        $("#successText").css("display", 'block');
    })
    $("#choice").on("submit", function (event) {
        console.log("kameni")
    })
})


