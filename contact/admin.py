from django.contrib import admin

from contact.models import ContactMessage, Category

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Category)