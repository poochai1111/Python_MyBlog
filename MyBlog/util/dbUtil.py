from MyBlog.models import User


def insert(context):
    try:
        User(context).save()
    except OSError as orr:
        print("OS error: {0}", format(orr))
    finally:
        return "Insert success"


def delete(context):
    try:
        User.objects.filter(context).delete()
    except OSError as orr:
        print("OS error: {0}", format(orr))
    finally:
        return "Delete success"


def update(context):
    try:
        User.objects.get(context).updatedate(context)
    except OSError as orr:
        print("OS error: {0}", format(orr))
    finally:
        return "update success"
