"""URLs for the {{ app_name }} pages."""
from django.urls import path

from . import views


# URL patterns should use a resource_name/resource_id/action pattern.
# URL names could be list_models, show_model, create_model, edit_model,
# delete_model, autocomplete_model, list_models_by_user.
app_name = "{{ app_name }}"
"""Namespace for {{ app_name }} URLs."""
urlpatterns = [
    path("", views.index, name="index"),
    # path('<int:model_id>/', views.show_model, name='show_model'),
]
"""URLs for the {{ app_name }} application."""
