from django.shortcuts import render
from travello.models import Destination
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def home(request):

    dest1 = Destination()
    dest1.name='MUMBAI'
    dest1.img='destination_4.jpg'

    return render(request,'index.html',{'dest1':dest1})