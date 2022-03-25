from django.contrib import admin

# Register your models here.
from user.models import (
    User,
    Blood_info,
)

admin.site.register(User)
admin.site.register(Blood_info)