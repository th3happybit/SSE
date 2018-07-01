# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Seller(models.Model):
	name = models.CharField(max_length=50)
	profile = models.URLField()

class Group(models.Model):
	gid = models.CharField(max_length=50,unique=True)
	url = models.URLField(unique=True)

class Post(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(unique=True)
	price = models.CharField(max_length=50)
	desc = models.TextField()
	location  = models.CharField(max_length=50)
	timeT = models.CharField(max_length=50)
	timeU = models.CharField(max_length=50)
	group = models.ForeignKey(Group)
	seller = models.ForeignKey(Seller)
	created_on = models.DateTimeField(auto_now_add=True)