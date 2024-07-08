from django import forms
from .models import User, Feedback


class BookingRoom(forms.Form):
    hotel_name = forms.CharField(max_length=255, initial='Hill Inc')
    number_of_room = forms.CharField(max_length=10, initial='2')
    user = forms.CharField(max_length=50, initial='Jose Smith')
    start_date = forms.DateField(initial='2024-06-01')
    end_date = forms.DateField(initial='2024-06-02')


class UserModelAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "age", "city", "sex", "email", "photo"]


class FeedbackModelAddForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["text", "user"]
        widgets = {
            "text": forms.Textarea(attrs={"size": 5, 'class': 'special', 'required': False})
        }