from django.contrib import admin
from .models import User_Coffee, Admin_Coffee


class ApprovalAdmin(admin.ModelAdmin):
    change_list_template = 'admin/User_Coffee/admin_approval.html'

admin.site.register(User_Coffee, ApprovalAdmin)
