var countDownDate = new Date("Aug 30, 2024 18:00:00 UTC").getTime();

var x = setInterval(function () {
    var countdownElement = document.getElementById("countdown");

    if (countdownElement !== null) {
        var now = new Date().getTime();
        var distance = countDownDate - now;

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownElement.innerHTML = days + "d - " + hours + "h - " + minutes + "m - " + seconds + "s  ";

        if (distance < 0) {
            clearInterval(x);
            countdownElement.innerHTML = "¡Comienza nuestra boda!";
        }
    }
}, 1000);

