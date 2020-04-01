from django.contrib import admin

from .models import Ccont
from .models import Rubric
from .models import VidRubric

class CcontAdmin(admin.ModelAdmin):
    list_display = ('title','textContent' , 'photo', 'video', 'rubric', 'vrubric', 'published')
    list_display_links = ('title', 'rubric', 'vrubric')
    search_fields = ('title', 'rubric', 'vruvric')

admin.site.register(Ccont, CcontAdmin)
admin.site.register(Rubric)
admin.site.register(VidRubric)
# Register your models here.
