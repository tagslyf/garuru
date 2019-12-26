from django.contrib import admin

from .models import (Host,
                     NetSelect,
                     Resource,)


class HostAdmin(admin.ModelAdmin):
    list_display = ('host', 'active', 'created_at',)


class NetSelectAdmin(admin.ModelAdmin):
    list_display = ('host', 'speed', 'created_at')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.register(Host, HostAdmin)
admin.site.register(NetSelect, NetSelectAdmin)
admin.site.register(Resource, ResourceAdmin)
