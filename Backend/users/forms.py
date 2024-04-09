from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ValidationError
from .models import NewUser

class UserForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = UserCreationForm.Meta.fields + ("username","Bearer_Token","Refresh_Token","Blacklisted",)
    
    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    

class updateUserForm (ModelForm):
    class Meta:
        model = NewUser
        fields = ['username', 'email' , 'first_name' , 'last_name']
    
    

class LoginForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ("username","password")
        
        
