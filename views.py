# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.decorators.http import require_POST, require_safe

from {{app_name}}.models import Model

# Use the decorators such as @require_POST as appropiate.

