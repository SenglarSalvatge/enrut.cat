# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    #foto //encara en fase de desenvolupament
    descripcio = models.CharField(max_length=800, help_text="Descripció", blank=True)
    puntuacio = models.IntegerField(help_text="Puntuació", default = 0)
    #nick = 
    usuari = models.OneToOneField(User, help_text="Usuari")
    
    def __unicode__(self):  
        return self.usuari.username


from django.db.models.signals import post_save

# definition of UserProfile from above
# ...

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #generar nick
        Perfil.objects.create(usuari=instance, descripcio="" )

#connectem event: després de que es crea l'usuari s'invoca la funció 'create_user_profile'
post_save.connect(create_user_profile, sender=User)