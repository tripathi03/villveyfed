from django.urls import path, include
from .views import show_member_details

urlpatterns = [
    path("MemberDCS", show_member_details),
   # path('MemberDCS/edit/*', edit_member_details),
]