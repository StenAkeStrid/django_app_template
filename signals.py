# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver, Signal

# from {{app_name}}.models import Model


# @receiver(post_save, sender=Model, dispatch_uid="example")
# def example(sender, instance, created, **kwargs):
#     if created:
#         pass
