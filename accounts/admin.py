from django.contrib import admin
from accounts.models import UserProfile, FriendShip


class FriendShipInline(admin.StackedInline):
    model = FriendShip
    extra = 0
    fk_name = 'from_user'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [FriendShipInline]
