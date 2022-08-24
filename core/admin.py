from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'phone', 'full_name', 'is_admin')
    list_filter = ('full_name',)
    fieldsets = (
        ('User Credentials', {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('full_name', 'address')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'full_name', 'address', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone', 'id')
    filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
