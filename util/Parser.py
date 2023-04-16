from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from memdcs.models import AdditionalDetails, Member


def request_data_to_user(post_data):
    user = User()
    user.username = post_data.get('username')
    user.email = post_data.get('email')
    user.password = make_password(post_data.get('password'))
    return user

def request_data_to_addtional_data(post_data, user):
    additional_details = AdditionalDetails()
    additional_details.user = user
    additional_details.user_id = user.id
    additional_details.mobilenum = post_data.get("mobilenum")
    additional_details.union = post_data.get("union")
    additional_details.designation = post_data.get("designation")
    return additional_details

def request_data_to_villager_data(post_data, user):
    member = Member()
    member.name = post_data.get("name")
    member.father_name = post_data.get("father_name")
    member.ward_num = post_data.get("ward_num")
    member.contact_num = post_data.get("contact_num")
    member.cows = post_data.get("cows")
    member.buffaloes = post_data.get("buffaloes")
    member.total_milk_produced = post_data.get("total_milk_produced")
    member.balance_milk_remaining = post_data.get("balance_milk_remaining")
    member.selling_to_sudha = post_data.get("selling_to_sudha")=="on"
    member.selling_to_other_whom = post_data.get("selling_to_other_whom")
    member.selling_to_other_rate = post_data.get("selling_to_other_rate")
    member.village_code = post_data.get("village_code")
    member.created_by = user
    return member