from django.db import models
class Giornalista(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    def __str__(self):
        return (self.nome+" "+self.cognome)

class Articolo(models.Model):
    """ modello generico di articolo"""
    titolo = models.CharField(max_length = 100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista,on_delete = models.CASCADE,related_name="articoli") 

    def __str__(self):
        return (self.titolo)
    
