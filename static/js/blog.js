$(document).ready(function () {
    $("#reset").click(function () {
        $("#blogTitle").attr("value","");
        $("#blogBody").attr("value","");
    });
    $("#submit").click(function () {
        if ($("#blogTitle").val() == null || $("#blogTitle").val() == ""){
            $("#blogTitleWarning").css("visibility","visible");
            $("#blogTitleWarning").css("margin-bottom","5px");
            return false;
        }
        if ($("#blogBody").val() == null || $("#blogBody").val() == ""){
            $("#blogBodyWarning").css("visibility","visible");
            $("#blogBodyWarning").attr("margin-bottom","3px");
            return false;
        }
    })
})