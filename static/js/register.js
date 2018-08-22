$(document).ready(function(){
    $("#form").validate({
        rules: {
            password: "required",
            password_again: {
                equalTo: "#password"
            }
        }
    });
    $("#submit").click(function () {
        if($("#name").val()== null || $("#name").val()== ""){
            alert("Please input your name.")
            return false
        }
        if($("#secondPwd").val()==null || $("#secondPwd").val()==""){
            alert("Please input your password.")
            return false
        }

    })
})