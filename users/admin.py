from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка юзера"""
    list_display = ('id', 'email', 'phone', 'city', 'last_login',)


admin.site.register(Payment)
