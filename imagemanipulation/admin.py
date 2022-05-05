from django.contrib import admin
from .models import Imager
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomAdmin(UserAdmin): 

    list_display = ("username","first_name", "last_name", "email","is_active","is_staff")
    list_filter = ()
    # Static overriding 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class ImagerUpdated(admin.ModelAdmin):
    #actions_selection_counter = True
    #actions_on_bottom = False
    #actions_on_top = True

    fields = ('show_image', 'actual_label','predicted_label', 'image')
    list_display = [
        'show_image',
        'actual_label',
        'predicted_label',
    ]
    list_display_links=[
        'actual_label',
        'predicted_label'
    ]
    list_filter = [
        'actual_label',
        'predicted_label',
        'image'
    ]
    
    readonly_fields = ('show_image',)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomAdmin)
admin.site.register(Imager,ImagerUpdated)
