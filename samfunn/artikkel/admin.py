# Lager et admingrensesnitt og legger til objekt/modell som
# skal kunne redigeres i databasen

from django.contrib import admin
from .models import Innlegg

# Registrerer objektet/modellen Innlegg
admin.site.register(Innlegg)
