from django.shortcuts import render
from ed.models import Disclosure

def index(request):
    disclosure = Disclosure.objects.order_by('+id')[:5]
    context = {
         'disclosure': disclosure
     }
    return render(request, 'ed/index.html', context)
