from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    list_per_page = 50

    raw_id_fields = ('liked_by',)

    fieldsets = (
        (None, {
            'fields': ('created_at', 'active', 'description', 'price', 'liked_by',),
        }),
        ('Расположение', {
            'fields': ('town', 'town_district', 'address', 'floor',),
        }),
        ('Информация о доме', {
            'fields': ('construction_year', 'new_building',),
        }),
        ('Характеристики квартиры', {
            'fields': ('rooms_number', 'living_area', 'has_balcony'),
        }),
    )


@admin.register(Complaint)
class CompliantAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
