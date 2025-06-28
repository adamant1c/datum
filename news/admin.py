from django.contrib import admin
from .models import News, Commenti



class  NewsModelAdmin(admin.ModelAdmin):
    model = News
    list_display = ["titolo", "user_nutrizionista"]
    search_fields = ["titolo"]
    list_filter = ["titolo","data"]


class CommentiModelAdmin(admin.ModelAdmin):
    model = Commenti
    list_display = ["autore","titolo", "news"]
    search_fields = ["titolo","autore"]
    list_filter = ["titolo","data"]




admin.site.register(News, NewsModelAdmin)
admin.site.register(Commenti, CommentiModelAdmin)
