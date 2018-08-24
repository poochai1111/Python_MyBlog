$(document).ready(function () {
    $("#submit").click(function () {
        alert("IN")
        var vals = [];
        $('input:checkbox:checked').each(function () {
            vals.push($(this).val());
        });
        var str_blog_id = ""
        alert(vals)
        for (var i = 0; i < vals.length; i++) {
            if (str_blog_id.length == 0) {
                str_blog_id = vals[i]
            } else {
                str_blog_id = str_blog_id + "," + vals[i]
            }
        }
        alert(str_blog_id)
        $.ajax({
            type: "POST",
            url: "/delete/",
            data: {blog_id: str_blog_id},
            success: function () {
                alert("OK")
            }
        })
    })

    $("#reset").click(function () {
       $('.blog_id input').prop('checked', false);
    })
})