from django.contrib import admin
from .models import Machine
from .models import Occurrence

# Register your models here.
admin.site.register(Machine)
admin.site.register(Occurrence)
