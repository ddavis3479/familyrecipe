from django.shortcuts import render_to_response
from django.template.context import RequestContext

from accounts.models import Account


def homepage(request):
    accounts = Account.objects.all()
    return render_to_response('homepage/homepage.html',
                              {'accounts': accounts},
                              context_instance=RequestContext(request))
