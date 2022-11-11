function AddZero(num) {
    return (num >= 0 && num < 10) ? "0" + num : num + "";
}

window.addEventListener("load", function(){
    var now = new Date();
    var strDateTime = [[AddZero(now.getDate()), AddZero(now.getMonth() + 1),  now.getFullYear()].join("/")]
    document.getElementById("time").innerHTML = strDateTime
})