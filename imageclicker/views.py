from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import Gif

def index(request) :
    return JsonResponse({'data': list(Gif.objects.all().values())}, safe=False)

@require_http_methods(["POST"])
def vote_gif(request):
    try:
        id = request.POST.get('id')
        gif = Gif.objects.get(id=id)
    except Gif.DoesNotExist:
        return JsonResponse({'error': 'Gif not found'}, status=404)
        
    gif.votes = gif.votes+1
    gif.save()                
    return JsonResponse({'message': 'Votes updated successfully', 'success': True })
