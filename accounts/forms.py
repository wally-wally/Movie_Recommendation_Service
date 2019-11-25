from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    CHOICES = [('M', '남'), ('W', '여')]
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
    age = forms.IntegerField(min_value=0, max_value=100, required=True)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'sex', 'age',)
