# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
def index(request):
	values = {'username':request.user}
	return render(request,'about/index.html',values)


class ContactPage(View):
	contact = 'about/contact.html'
	"""@ this for contact page """
	def get(self,request):
		wel = {'welcome':request.user}
		return render(request,self.contact,wel)
	def post(self,request):
		email = {'welcome':request.POST['email']}
		return render(request,self.contact,email)