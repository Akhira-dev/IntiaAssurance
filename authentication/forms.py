from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from authentication.models import Client  

class ClientForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'password']  

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Les mots de passe ne correspondent pas.")

        try:
            validate_password(password)  
        except ValidationError as e:
            raise ValidationError({"password": e.messages})

        return cleaned_data


