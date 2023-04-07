$(document).ready(function () {





    let button = document.querySelectorAll("#buttonMovie");
    let modalWindow = document.querySelector("#modalWindow");
    let closeButton = document.querySelector("#Cross");
    console.log(button[0]);

    function openModalWindow(event) {
        function showCover() {
            let coverDiv = document.createElement("div");
            coverDiv.classList.add("cover-div");
            document.body.append(coverDiv);


        }
        showCover();
        modalWindow.style.display = "flex";
        setTimeout(() => modalWindow.style.opacity = 1, 1)
        let windowWidth = document.body.clientWidth;
        let windowHeight = document.body.clientHeight;
        let modalWindowWidth = modalWindow.clientWidth;
        let modalWindowHeight = modalWindow.clientHeight;
        let left = windowWidth / 2 - modalWindowWidth / 2;
        let top = windowHeight / 2 - modalWindowHeight / 2;
        modalWindow.style.top = top + "px";
        modalWindow.style.left = left + "px";
    }

    function closeModalWindow() {
        let coverDiv = document.querySelector(".cover-div");
        coverDiv.remove();
        modalWindow.style.display = "none";
        modalWindow.style.opacity = 0;
    }
    for (let i = 0; i < 3; i++) {
        button[i].addEventListener("click", openModalWindow)
    }
    closeButton.addEventListener("click", closeModalWindow)



    $("#sentForm").on("submit", function (event) {
        event.preventDefault()
        $.ajax({
            type: "POST",
            url: $("#sentForm").action,
            data: $(this).serialize(),
            dataType: "json",
            success: function (response) {




            }
        })
        closeModalWindow()
    })
})

