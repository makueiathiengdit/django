from django.contrib import admin
from .models import Question

# Register your models here.
#give admin access to the models
admin.site.register(Question)