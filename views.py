"""
For more information on Django views, see
https://docs.djangoproject.com/en/4.0/topics/http/views/.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.decorators.http import require_POST, require_safe

# from .models import Model

User = get_user_model()


@require_safe
@login_required
def index(request):
    """Start page."""
    return render(request=request, template_name="{{ app_name }}/index.html")
