from django.contrib import admin
from signup.models import Expense, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email','password')  # Add 'id' to make it visible

admin.site.register(User)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('username', 'day', 'month', 'year', 'item', 'price')

admin.site.register(Expense)