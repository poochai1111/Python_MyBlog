/*Clear input value*/
$(document).ready(function () {
    $("#loginForm")[0].reset();
    $("#name").attr("value","");
    $("#password").attr("value","");
    /*Check input*/
    $("#submit").click(function () {
        if ($("#name").val() == null || $("#name").val() == ""){
            alert("Please input your name!!!");
            window.location.reload();
            return false;
        }
        if ($("#password").val() == null || $("#password").val() == ""){
            alert("Please input your password!!!")
            window.location.reload();
            return false;
        }
});
});




