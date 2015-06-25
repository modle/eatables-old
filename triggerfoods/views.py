from django.shortcuts import render

from .models import TriggerFood

# Create your views here.
def index(request):
    triggerfood_query = TriggerFood.objects.all()  #[:5]
    context = {'triggerfood_query': triggerfood_query}
    return render(request, 'triggerfoods/index.html', context)
