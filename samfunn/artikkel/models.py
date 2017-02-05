# App kalt ARTIKKEL
# Publiserer saker som inneholder tekst, bilder, video, lenker
# Tar imot opplasting av tekst og mediefiler
# Loggin - sikkerhet

# Importerer biter fra andre filer
from django.db import models
from django.utils import timezone

# Lager objekt/modell som kalles Innlegg
# Modeller navngis med stor bokstav, benevnes models.Model i Django
# Django lagerer alle modeller i databasen
# Elementene etter class: beskriver objektet Innlegg

class Innlegg(models.Model):
# ForeignKey kobler til en annen modell som kalles User:
    author = models.ForeignKey('auth.User')
    title  = models.CharField(max_length=200)
# Tekstfeltet er ubetrenset:
    text   = models.TextField()
    created_date = models.DateTimeField(
            default = timezone.now)
    published_date = models.DateTimeField(
            blank = True, null = True)

# Funksjon/metode som publiserer
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
