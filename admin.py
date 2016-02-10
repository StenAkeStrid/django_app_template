"""Registers {{ app_name }} models to the admin site."""
from django.contrib import admin

# from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# from .models import Model


# class ModelAdmin(admin.ModelAdmin):
#    """ModelAdmin class for Model class."""
#    # actions = []
#    list_display = ['web_link',]
#    list_filter = []
#    search_fields = []
#
#    def web_link(self, obj):
#        """Canonical link to the object on the web page."""
#        html_template = '<a href="{link}">{link_text}</a>'
#        link = obj.get_absolute_url()
#        return format_html(html_template, link=link, link_text=_('link'))
#    web_link.short_description = _('link')


# admin.site.register(Model, ModelAdmin)
