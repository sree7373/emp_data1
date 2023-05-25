#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import requests


def employee_prof(request):
    try:
        if request.method == 'GET':
            a = request.body
            b=json.loads(a)
            b=b['id']
            Emp_Prof = Employee_Profiles.objects.get(pk=b)
            
            Name=(Emp_Prof.First_Name)
            First_Name = (Emp_Prof.First_Name)
            Last_Name = (Emp_Prof.Last_Name)
            Email = (Emp_Prof.Email)
            Phone = (Emp_Prof.Phone)
            Dob = (Emp_Prof.Dob)
            Blood_Group = (Emp_Prof.Blood_Group)
            
            Emp_Prof.First_Name = First_Name
            Emp_Prof.Last_Name = Last_Name
            Emp_Prof.Email = Email
            Emp_Prof.Phone = Phone
            Emp_Prof.Dob = Dob
            Emp_Prof.Blood_Group = Blood_Group
            Name = Emp_Prof.add_name()
            
            Emp_Prof.save()
            resposne = {First_Name : True}
            resposne = {Last_Name : True}
            resposne = {Email : True}
            resposne = {Phone : True}
            resposne = {Dob : True}
            resposne = {Blood_Group : True}
            return JsonResponse(resposne)
        
    except Exception as ex:
        return(ex)