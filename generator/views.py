from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator\home.html')

def info(request):
    return render(request, 'generator\info.html')

def password(request):
#    thepassword = 'testing'
    characters = list('abcdefghighlmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special characters'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
#    length = 10
    length = int(request.GET.get('length',8))
    thepassword = ''
    for x in range(length):
#    x =x+1
        thepassword += random.choice(characters)
    return render(request, 'generator\password.html', {'password':thepassword})
