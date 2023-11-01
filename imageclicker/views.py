from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Gif

def index(request) :
    print(request)
    gifs = serializers.serialize("json", Gif.objects.all());
    return JsonResponse({'data': gifs});

def vote_gif(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            gif = Gif.objects.get(id=id)
        except Gif.DoesNotExist:
            return JsonResponse({'error': 'Gif not found'}, status=404)
            
        gif.votes = gif.votes+1
        gif.save()
        gif = serializers.serialize("json", [gif]);

        return JsonResponse({'message': 'Votes updated successfully', 'data': gif})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
