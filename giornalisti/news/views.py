from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Articolo, Giornalista


def home(request):

    giornalisti = Giornalista.objects.all()
    articoli = Articolo.objects.all()
    
    context = {"articoli":articoli,"giornalisti":giornalisti}

    return render(request,"home.html",context)

def contacts(request,number):    
    #number = get_object_or_404(int,number)
    context = {"nome":"Manuel","cognome":"della Gala","telephone":"34712345","number":number}    
    
    return render(request,"contacts.html",context)

def detail(request,pk):

    giornalisti = get_object_or_404(Giornalista,pk=pk)
    articolo = Articolo.objects.all()

    print("pk: "+str(pk))

    context = {"articolo":articolo[pk],"giornalisti":giornalisti,"pk":pk}
    
    return render(request,"ArticoloDetailView.html",context)



