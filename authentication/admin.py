from django.contrib import admin
from django.contrib.auth.hashers import make_password

from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # custom logic
        obj.password = make_password(obj.password)
        obj.save()
