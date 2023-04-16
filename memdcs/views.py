# Views file to handle all extra data

from django.shortcuts import render, redirect
from .models import Member, VillageData
from util.Parser import request_data_to_villager_data
from datetime import datetime 

def show_member_details(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    print(request.POST, request.method)
    if request.method=="GET":
        return render(request, "memberdetails.html")

    if request.method=="POST":
        if request.POST.get("contact_num"):
            user = request.user
            request_data_to_villager_data(request.POST, user).save()
            return render(request, "memberdetails.html", {
                "villager_data": Member.objects.filter(contact_num=request.POST.get("contact_num"))[0],
                "village_data": VillageData.objects.filter(village_code=request.POST.get("village_code"))[0],
                "user_data": user,
                "current_time": datetime.now()
            })

        village_details = VillageData.objects.filter(
                village_code=request.POST.get("village_code") if request.POST.get("village_code")
                else 0
            )
        return render(request, "memberdetails.html",{
            "village_details" : village_details[0] if len(village_details)>0 else None
        })
