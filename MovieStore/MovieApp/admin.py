from django.contrib import admin

# Register your models here.
import MovieApp.models

admin.site.register(MovieApp.models.Movie) 
admin.site.register(MovieApp.models.Message)

