from django import forms
# returns user model currently active
from django.contrib.auth import get_user_model
# good doc-> contrib.auth.forms
from django.contrib.auth.forms import UserCreationForm

# overriding the default fields (CSS) created by create view and update view
from django.forms import ModelForm,Textarea
from django.forms.widgets import TextInput
from basic_app.models import MyGroup,MyPost

# SIGNUP PAGE -> TO CREATE USER
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    class meta:
        # fields from django.contrib.auth -> fields a user can access when signing up when connecting to a model
        fields = ('email','username','password1','password2')
        model = get_user_model
    
    # labels on a form
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 'display name' will be shown on the form
        self.fields['username'].label = 'Display Name'

    def save(self,commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    


class MyPostForm(ModelForm):

    class Meta:
        model = MyPost
        fields = ('mssg','group')
        widgets = {
            'mssg': Textarea(attrs={'cols': 150, 'rows': 13}),
        }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 'display name' will be shown on the form
        self.fields['mssg'].label = 'Message'

class MyGroupForm(ModelForm):

    class Meta:
        model = MyGroup
        fields = ('name','description')
        widgets = {
            'name': Textarea(attrs={'cols': 150,'rows':1}),
            'description': Textarea(attrs={'cols': 150, 'rows': 14}),
        }