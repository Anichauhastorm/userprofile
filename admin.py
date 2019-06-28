from django.contrib import admin
from uform.models import Userform
# Register your models here.


class UserFormAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


admin.site.register(Userform)
