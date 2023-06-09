import logging

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from util.Parser import request_data_to_user, request_data_to_addtional_data
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from .forms import RegistrationForm
from util.Logger import Logger
from util.UserValidator import MSG_USERDATA_VALID

REGISTER_PAGE = "registration/register.html"
LOGIN_PAGE = "registration/login.html"
logger = Logger("villveyfed.log")


def show_register_page(request):
    logger.log_request(request)

    if request.method == 'GET':
        return render(request, REGISTER_PAGE, {"form": request.GET})

    if request.method == 'POST':
        try:
            validation_message = RegistrationForm(request.POST).validate()
            if validation_message == MSG_USERDATA_VALID:
                request_data_to_user(request.POST).save()
                user = User.objects.filter(email=request.POST.get("email"))[0]
                additional_data = request_data_to_addtional_data(request.POST, user)
                additional_data.save()
                return redirect("/login")
        except Exception as err:
            validation_message = str(err)
            logging.log(0, err)
        return render(request, REGISTER_PAGE, {
            "form": request.POST,
            "message": validation_message,
            "color": "red"
        })
    return render(request, REGISTER_PAGE, {
        "message": "Only GET and POST methods allowed. Are you debugging?",
        "color": "orange"
    })



class MyPasswordResetView(PasswordResetView):
    template_name = 'my_password_reset.html'
    email_template_name = 'my_password_reset_email.html'
    subject_template_name = 'my_password_reset_subject.txt'

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'my_password_reset_done.html'
