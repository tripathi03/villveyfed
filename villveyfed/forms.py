import re

from django import forms
from django.core import validators
from util.UserValidator import *


class RegistrationForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=28)
    mobilenum = forms.IntegerField()
    union = forms.CharField(max_length=50)
    designation = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=28)
    email = forms.EmailField()

    def __init__(self, post_data=None):
        super().__init__()
        if post_data:
            self.username = post_data.get('username')
            self.email = post_data.get('email')
            self.password = post_data.get('password')
            self.confirm_password = post_data.get('confirmPassword')
            self.union = post_data.get("union")
            self.designation = post_data.get("designation")
            self.mobilenum = post_data.get("mobilenum")

    def validate(self):
        if self.password != self.confirm_password:
            return MSG_PASSWORD_NO_MATCH
        if not re.match(RE_PASSWORD, self.password):
            return MSG_PASSWORD_INVALID
        if not re.match(RE_USERNAME, self.username):
            return MSG_USERNAME_INVALID
        validators.validate_email(self.email)
        return MSG_USERDATA_VALID