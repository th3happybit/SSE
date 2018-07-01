# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from xml.dom import minidom
from .models import Post, Seller, Group
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

def toDb(request):
		#next step is to get all groups from db and perform this operation on them
		md = minidom.parse('posts/150322621832912.xml')
		fbgroup = Group(gid='150322621832912',url='https://www.facebook.com/groups/150322621832912')
		#from xml to db
		posts = md.getElementsByTagName('post')
		fbgroup.save()
		for i in posts:
			post = Post()
			print(i.attributes['title'].value)
			#chlidnodes we have time -> 0, person -> 1, imagesUrls -> 2 
			print(i.childNodes[0].attributes['timeT'].value)
			fbseller = Seller(name=i.childNodes[1].attributes['name'].value,profile=i.childNodes[1].attributes['url'].value)
			fbseller.save()
			post = Post(title=i.attributes['title'].value,url=i.attributes['url'].value,price=i.attributes['price'].value,desc=i.attributes['desc'].value,location=i.attributes['location'].value,timeT=i.childNodes[0].attributes['timeT'].value,timeU=i.childNodes[0].attributes['timeU'].value,group=fbgroup,seller=fbseller)
			post.save()
		return HttpResponse("Operation succed !")