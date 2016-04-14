from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from tracker.models import Site,Visit
from datetime import datetime as dt

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class SiteForm(forms.ModelForm):
    base_url = forms.URLField(label='Website URL')

    class Meta:
        model = Site
        fields = '__all__'


class VisitForm(forms.ModelForm):
    browser = forms.CharField()
    date = forms.DateTimeField()
    event = forms.CharField()
    url = forms.URLField()
    ip_address = forms.GenericIPAddressField()
    site = forms.ModelMultipleChoiceField(queryset=Site.objects.all())

    class Meta:
        model = Visit
        fields = '__all__'