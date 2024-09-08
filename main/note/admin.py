from django.contrib import admin
from.models import *

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'content', 'created_by', 'created_at')
    search_fields = ('id', 'title', 'created_by')
    readonly_fields = ['created_at', 'created_by']
    
admin.site.register(Note, NoteAdmin)