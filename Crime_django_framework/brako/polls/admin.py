from django.contrib import admin
from .models import Braquage, Lieu, Securite, Ville, Blesse, Braqueur, Article, Source, Arme, Utilisation_arme, Fuite, Arrestation_calme, Arrestation_musclee

# Register your models here.
admin.site.register(Braquage)
admin.site.register(Lieu)
admin.site.register(Securite)
admin.site.register(Ville)
admin.site.register(Blesse)
admin.site.register(Braqueur)
admin.site.register(Article)
admin.site.register(Source)
admin.site.register(Arme)
admin.site.register(Utilisation_arme)
admin.site.register(Fuite)
admin.site.register(Arrestation_calme)
admin.site.register(Arrestation_musclee)
