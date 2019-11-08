from django.contrib import admin
from app.models import Coffee
from app.models import Transaction

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
# Register your models here.
