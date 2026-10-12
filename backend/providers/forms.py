from django import forms
from django.contrib.auth.models import User

from .models import Provider, Booking


class ProviderRegistrationForm(forms.ModelForm):

    email = forms.EmailField(required=True)

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:

        model = Provider

        fields = [
            "full_name",
            "email",
            "password",
            "confirm_password",
            "phone",
            "cnic",
            "service",
            "experience",
            "address",
            "skills",
            "profile_picture",
            "cnic_front",
            "cnic_back",
            "certificate",
        ]

        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
            "skills": forms.Textarea(attrs={"rows": 3}),
        }


    def clean_email(self):

        email = self.cleaned_data["email"].lower()

        if User.objects.filter(username=email).exists():

            raise forms.ValidationError(
                "This email is already registered."
            )

        return email


    def clean(self):

        cleaned = super().clean()

        password = cleaned.get("password")
        confirm_password = cleaned.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:

                self.add_error(
                    "confirm_password",
                    "Passwords do not match."
                )

        return cleaned


    def save(self, commit=True):

        provider = super().save(commit=False)

        email = self.cleaned_data["email"].lower()
        password = self.cleaned_data["password"]

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        provider.user = user
        provider.status = "pending"

        if commit:

            provider.save()

        return provider


# =========================
# BOOKING FORM
# =========================

class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = [
            "client_name",
            "client_email",
            "client_phone",
            "service",
            "booking_date",
            "booking_time",
            "address",
            "additional_details",
        ]

        widgets = {

            "booking_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "booking_time": forms.TimeInput(
                attrs={
                    "type": "time"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),

            "additional_details": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),
        }