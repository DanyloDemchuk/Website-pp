from django import forms
from . models import Member
#форма
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }


class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ['username', 'password']
#         widgets = {
#             "password": forms.PasswordInput(),
#         }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)