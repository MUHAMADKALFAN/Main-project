from django.contrib import admin
from .models import plants
from .models import store
from .models import storess
from .models import CartItem


# Register your models here.
admin.site.register(plants)
admin.site.register(store)
admin.site.register(storess)
admin.site.register(CartItem)
 