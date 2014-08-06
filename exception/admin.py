from django.contrib import admin
from .models import Exemption, Note, Port, Subnet, Sensor

class ExemptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Exemption, ExemptionAdmin)

class NoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Note, NoteAdmin)

class PortAdmin(admin.ModelAdmin):
    pass
admin.site.register(Port, PortAdmin)

class SubnetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subnet, SubnetAdmin)

class SensorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sensor, SensorAdmin)