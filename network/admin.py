from django.contrib import admin

from network.models import Product, Contact, Link


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'date',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'debt', 'created_at')
    list_filter = ('contact__city',)
    list_display_links = ('id', 'name')
    filter_horizontal = ('products', )
    readonly_fields = ('level', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'link')
    readonly_fields = ('link',)
