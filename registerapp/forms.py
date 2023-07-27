from django import forms
from registerapp.models import RegisterModel

class RegisterForm(forms.ModelForm):
    password_again=forms.CharField(widget=forms.PasswordInput(),label='Re-enter Password')
    class Meta:
        model=RegisterModel
        fields=['username','first_name','last_name','gender','email','contact','password']
        widgets={
        'password':forms.PasswordInput(),
        'gender':forms.RadioSelect()
        }
    def clean(self):
        password=self.cleaned_data['password']
        password_again=self.cleaned_data['password_again']
        if password!=password_again:
            raise forms.ValidationError('password and re-enter password are not same')
    