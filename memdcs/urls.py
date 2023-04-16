from django.urls import path, include
from .views import *

urlpatterns = [
    path("MemberDCS", show_member_details),
]