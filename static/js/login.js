/*Check input*/
$(#submit).click(function () {
    if ($(#name).value == null || $(#name).value == "")
        alert("Please input your name!!!")
    else if ($(#password).value == null || $(#password).value == "")
        alert("Please input your password!!!")
})


