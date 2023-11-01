from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import Gif

def index(request) :
    print(request)
    gifs = serializers.serialize("json", Gif.objects.all());
    return JsonResponse({'data': gifs});

@require_http_methods(["POST"])
def vote_gif(request):
        try:
            id = request.POST.get('id')
            gif = Gif.objects.get(id=id)
        except Gif.DoesNotExist:
            return JsonResponse({'error': 'Gif not found'}, status=404)
            
        gif.votes = gif.votes+1
        gif.save()
        gif = serializers.serialize("json", [gif]);

        return JsonResponse({'message': 'Votes updated successfully', 'data': gif})
