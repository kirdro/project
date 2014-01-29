# Create your views here.
from datetime import datetime

from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response

import models


def general_view(request):

	if request.method=='POST':
		data = request.POST

		formtype 	= data.get('formtype', '')
		email 	= data.get('email', '')
		phone 	= data.get('phone', '')
		itemid 	= data.get('itemid', '')

		print '==> form type =', formtype
		if (formtype=='callme'):
			if (email!='')&(phone!=''):
				item 	= None
				if (itemid!=''):
					idd 	= int(itemid)
					print '==> item id =', idd
					item 	= models.Item.objects.get(id=idd)
				newcallme 	= models.CallMe.objects.create(email=email,
														   phone=phone,
														   item=item,
														   date=datetime.now())
				newcallme.save()

		elif (formtype=='action'):
			if (email!='')&(phone!=''):
				newobject 	= models.GetAction.objects.create(email=email,
															  phone=phone,
															  date=datetime.now())
				newobject.save()			

	items = models.Item.objects.all()

	c 	= {'items': items}
	c.update(csrf(request))
	return render_to_response('items_block.html', c)
