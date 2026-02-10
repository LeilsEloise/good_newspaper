from django.contrib import admin

from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_on")


# Code Institute Codestar Blog code
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "read",
    )
