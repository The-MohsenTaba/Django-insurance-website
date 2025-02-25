from django.contrib import admin
from .models import Insurance,UserInfo
# Register your models here.
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('user','plan', 'status', 'request_date', 'accepted_date', 'expired_date', 'time_left_display')

    def time_left_display(self, obj):
        return obj.time_left

    time_left_display.short_description = 'Time Left (days)'  # Column header in admin panel

admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(UserInfo)
