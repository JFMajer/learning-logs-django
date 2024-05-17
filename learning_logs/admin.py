from django.contrib import admin
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 1

class TopicAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
