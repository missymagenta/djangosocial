from django.contrib import admin
from . import models

# edit models on the same page as a parent model
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)