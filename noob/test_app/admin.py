# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Shopping, Restaurant


class ShoppingAdmin(admin.ModelAdmin):
    list_display = ("name", "address")


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "shopping", "address")


admin.site.register(Shopping, ShoppingAdmin)
admin.site.register(Restaurant, RestaurantAdmin)