from django.shortcuts import render
from django.http import HttpResponse

from .models import Articolo, Giornalista




def home(request):

    giornalisti = Giornalista.objects.all();
    articoli = Articolo.objects.all();
    context = {"articoli":articoli,"giornalisti":giornalisti}

    return render(request,"home.html/",context)

def contacts(request):    

    context = {"nome":"Manuel","cognome":"della Gala","telephone":"34712345",}    
    
    return render(request,"contacts.html",context)


