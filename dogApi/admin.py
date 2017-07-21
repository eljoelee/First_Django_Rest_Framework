from django.contrib import admin
from .models import Dog

class DogAdmin(admin.ModelAdmin):
    list_display=('dogName', 'dogInfo', 'dogPob', 'dogPersonality',)

admin.site.register(Dog, DogAdmin)