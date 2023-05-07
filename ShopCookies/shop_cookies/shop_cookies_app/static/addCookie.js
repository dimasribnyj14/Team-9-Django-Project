$(document).ready(function () {
    // let madeBeforeFunctions = $(".count").val()
    function changeTimesPlus() {
        console.log("plus")
        let a = $(".count").val()
        $(".count").val(++a)
    }
    function changeTimesMinus() {
        console.log("minus")
        if ($(".count").val() > 1) {
            let a = $(".count").val()
            $(".count").val(--a)
        }
    }
    $(".plus").on("click", changeTimesPlus)
    $(".minus").on("click", changeTimesMinus)
    $(".addCookie").on("submit", function (event) {
        // for (let i = 0; i < madeBeforeFunctions; i++) {
        // setTimeout(function (event) { 
        event.preventDefault()
        $.ajax({
            type: "POST",
            url: $(".addCookie").action,
            data: $(this).serialize(),
            dataType: "json",
            success: function (response) { }
        })
        $(".count").val(1)
        // }, 500)
        // }
    })
})