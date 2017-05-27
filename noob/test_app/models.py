# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Shopping(models.Model):

    name = models.CharField(max_length=200)
    address = models.TextField()
    logo = models.ImageField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "Shopping %s" % self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    shopping = models.ForeignKey(Shopping)
