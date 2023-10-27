from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile


class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def __int__(self, *args, **kwargs):
        super(UserRegistration, self).__int__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        exclude = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
                   'groups', 'last_login', 'user_permissions', 'date_joined')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'first_name', 'last_name', 'username', 'email', 'telphone', 'whatsapp', 'quartier', 'bio']

    def __int__(self, *args, **kwargs):
        super(ProfileForm, self).__int__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
