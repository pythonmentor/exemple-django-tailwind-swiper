from django.shortcuts import render
from django import forms


class ExempleForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)


def home(request):
    return render(request, "home.html", {"form": ExempleForm()})
