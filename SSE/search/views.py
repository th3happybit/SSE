# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
def index(request):
	messages.info(request,'d yah')
	search_keywords = {'keywords':request.GET['search'],'result':'in progress ^-^'}
	return render(request,'index.html' , search_keywords)

def msgsToJson(request):
	msgs = messages.get_messages(request)
	msgs_dict = {}
	ar = []
	for msg in msgs:
		ar.append(msg)
	msgs_dict = {'aaaa':ar}
	return JsonResponse(msgs_dict)