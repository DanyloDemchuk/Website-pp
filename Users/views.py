from django.shortcuts import render, redirect, get_object_or_404
from . models import Member
from . forms import MemberForm, LoginForm, MemberEditForm
from django.contrib.auth import login, logout
from rest_framework import generics
from .serializers import MemberSerializer
from .decorators import check_login

@check_login
def home_page(request):
    return render(request, "home_page.html", {})

@check_login
def user_add(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users_page")
    else:
        form = MemberForm()
    return render(request, "user_registration.html",{"form":form})

@check_login
def user_edit(request, pk):
    print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)
    user = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users_page")
    else:
        form = MemberEditForm(instance=user)
    return render(request, "user_edit.html", {"form":form})

@check_login
def user_page(request):
    print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)

    users = Member.objects.all()
    context = {"users":users}
    return render(request, "users_list_page.html", context)


@check_login
def user_delete(request,pk):
    user = get_object_or_404(Member, pk=pk)
    user.delete()
    return redirect("users_page")



def user_registration(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form = MemberForm()
        return render(request, "user_registration.html", {"form": form})

# def user_registration(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get("username")
#             login(request,user)
#             return redirect("home_page")
#     else:
#         form = UserCreationForm
#         return render(request, "user_registration.html", {"form": form})



def user_login(request):
    print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)
    error_message = ""
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Member.objects.get(username=username)
            if user.check_password(password):
                # Пароль збігається, користувач вірний
                request.session.set_expiry(0)  # Завершити сесію при закритті браузера
                request.session['user_id'] = user.id
                login(request, user)
                print("Користувач авторизований. Ідентифікатор сесії:", request.session.session_key)
                return redirect('home_page')
        except Member.DoesNotExist:
            error_message = "Invalid email or password. Please try again."

    return render(request, 'user_login.html', {"form": form, "error_message":error_message})

# def user_login(request):
#     error_message = ""
#     form = LoginForm()
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home_page')
#         else:
#             error_message = "Invalid email or password. Please try again."
#
#     return render(request, 'user_login.html', {"form": form, "error_message":error_message})

def user_logout(request):
    logout(request)
    return redirect("user_login")


class UserListAPI(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


