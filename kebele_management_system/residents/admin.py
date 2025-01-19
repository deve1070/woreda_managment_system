from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ResidentialID,Profile,CustomUser


@admin.register(ResidentialID)
class ResidentialIDAdmin(admin.ModelAdmin):
    list_display=['id_number','used']
    list_filter=['used']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','residential_id']


class CustomUserAdmin(UserAdmin):
    model=CustomUser
    fieldsets=UserAdmin.fieldsets + ((None,{'fields':('role',)}),
        )
    list_display=('username','email','role')
    list_filter=('role',)
    actions=['make_staff']

    def make_staff(self,request,queryset):
        queryset.update(role='staff')
    make_staff.short_description='Change selected useres to staff'
admin.site.register(CustomUser,CustomUserAdmin)
    