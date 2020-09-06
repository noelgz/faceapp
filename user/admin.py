from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'phoneNumber', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'phoneNumber', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phoneNumber', 'user__username')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phoneNumber'),
                ('biography')
            )
        }), 
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )


    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delkete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
