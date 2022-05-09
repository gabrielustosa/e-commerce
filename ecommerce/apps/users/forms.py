from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'cpf', 'password1', 'password2')
        labels = {'username': 'E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'cpf', 'phone_number')
        labels = {'username': 'E-mail'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', 'Salvar'))
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('phone_number')
            ),
            'cpf',
            'username',
        )
