# Create your views here.

from django.http import HttpResponse
from django.template.response import TemplateResponse

import models


def general_view(request):
	items = models.Item.objects.all()
	return TemplateResponse(request, 'items_block.html', {'items': items})