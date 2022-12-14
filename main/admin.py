from django.contrib import admin
from . import models

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    model = models.Account
    list_display = ('id','username', 'email', 'mobile','interests','is_staff','is_verified','is_active','last_login','joined_date') 
    
    readonly_fields = ('last_login','joined_date','password')
    ordering = ('joined_date', )
    filter_horizontal =()
    list_filter = ()
    fieldsets =()

# Register your models here.

admin.site.register(models.Account,AccountAdmin)
admin.site.register(models.CourseRating)
admin.site.register(models.FavoriteCourse)
admin.site.register(models.StudentAssignment)
admin.site.register(models.AssignmentAnswer)
