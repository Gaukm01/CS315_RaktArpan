from django.contrib import admin

# Register your models here.
from user.models import (
    User,
    City,
    Bloodtype_info,
    Blood_details
)

admin.site.register(City)
admin.site.register(User)
admin.site.register(Bloodtype_info)
admin.site.register(Blood_details)
