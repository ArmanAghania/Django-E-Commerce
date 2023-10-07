from django.contrib import admin
from .models import Product

# Register your models here.
class ProducAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','category','created_at', 'modified_at','is_available')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Product, ProducAdmin)