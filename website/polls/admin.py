from django.contrib import admin
from polls import models

class ProductDataInline(admin.TabularInline):
    model = models.ProductData
    extra = 3

class StoreDataInLine(admin.TabularInline):
    model = models.StoreData
    extra = 3

class UserAdmin(admin.ModelAdmin):
    inlines = [ProductDataInline, StoreDataInLine]
admin.site.register(models.Users, UserAdmin)

class ClientProductDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.ClientProductData, ClientProductDataAdmin)

class StoreSalesAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.StoreSales, StoreSalesAdmin)