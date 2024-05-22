from django.shortcuts import redirect

def check_login(func):
    def wrapper(request, *args, **kwargs):
        if request.session.session_key is not None:
            return func(request, *args, **kwargs)
        else:
            return redirect("user_login")
    return wrapper