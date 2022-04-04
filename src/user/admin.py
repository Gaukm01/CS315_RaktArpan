from django.contrib import admin

# Register your models here.
from user.models import (
    User,
    City,
    RBC,
    Platelets,
    Plasma,
    CryoAHF,
    Granulocytes
)

admin.site.register(User)
admin.site.register(RBC)
admin.site.register(City)
admin.site.register(Platelets)
admin.site.register(Plasma)
admin.site.register(CryoAHF)
admin.site.register(Granulocytes)