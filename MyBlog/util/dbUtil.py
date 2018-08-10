from MyBlog.models import User


def insert(context):
    try:
        User(init(context)).save()
    except OSError as orr:
        print("OS error: {0}", format(orr))
    finally:
        return "Insert success"


def delete(context):
    try:
        User.objects.filter(init(context)).delete()
    except OSError as orr:
        print("OS error: {0}", format(orr))
        return False
    finally:
        return True


def update(context):
    try:
        User.objects.get(init(context)).updatedate(init(context))
    except OSError as orr:
        print("OS error: {0}", format(orr))
        return False
    finally:
        return True


def select(context):
    try:
        count = User.objects.filter(init(context)).count()
        if count > 0:
            return True
        else:
            return False
    except OSError as orr:
        print("OS error: {0}", format(orr))
        return False


def init(dic):
    param = ""
    for key in dic.keys():
        if len(param) > 0:
            param = param + "," + key + "=" + dic[key]
        else:
            param = param + "=" + dic[key]

    return param
