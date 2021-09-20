from django.contrib import admin
from .models import Example, Programmer, Language

# Register your models here.


admin.site.register(Example)
admin.site.register(Programmer)
admin.site.register(Language)
