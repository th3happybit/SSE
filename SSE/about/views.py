# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
	values = {'username':request.user}
	return render(request,'about/index.html',values)


def contact(request):
	return render(request,'about/contact.html')
