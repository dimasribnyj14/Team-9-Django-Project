$(document).ready(function () {

    $(".deleteCookie").on("submit", function (event) {
        event.preventDefault()
        $.ajax({
            type: "POST",
            url: $(".deleteCookie").action,
            data: $(this).serialize(),
            dataType: "json",
            success: function (response) { }
        })
        console.log('mopdekaizer')
    })
})