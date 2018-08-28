$(document).ready(function () {
    $("#submit").click(function (event) {
        var blog_id = ""
        if ($('input:checkbox:checked').length > 0) {
            $('input:checkbox:checked').each(function () {
                if (blog_id.length == 0) {
                    blog_id = $(this).val()
                } else {
                    blog_id = blog_id + "," + $(this).val()
                }
            });
            $('#myModal').find('.modal-title').text('Confirm Dialog');
            $('#myModal').find('.modal-body').text('Are you sure you want to delete blog id [' + blog_id + ']?');
            $('#myModal').modal('show')
            $('#ok').click(function () {
                $.ajax({
                    type: "POST",
                    url: "/delete/",
                    data: {"blog_id": blog_id},
                    success: function () {
                        window.reload()
                    }
                });
            })
            event.preventDefault();
        }
        else {
            alert("No record to be chosen")
        }
    })
    $("#reset").click(function () {
       $('.blog_id input').prop('checked', false);
    })
})