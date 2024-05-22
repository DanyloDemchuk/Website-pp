from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views



urlpatterns = [
    path("", views.home_page, name = "home_page"),
    path("registration/", views.user_registration, name = "user_registration"),
    path("login/", views.user_login, name = "user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("users/", views.user_page, name="users_page"),
    path("users/add/", views.user_add, name="user_add"),
    path("users/<int:pk>/", views.user_edit, name="user_edit"),
    path("users/delete/<int:pk>/", views.user_delete, name="user_delete"),
    path("users/list/api/", views.UserListAPI.as_view(), name="user_list_api"),
    path("users/detail/api/<int:pk>/", views.UserDetailAPI.as_view(), name="user_detail_api"),
]
