# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class {{camel_case_app_name}}Config(AppConfig):

    name = '{{app_name}}'

    def ready(self):
        import {{app_name}}.signals
