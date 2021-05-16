from django.http import JsonResponse

# Create your views here.
def home(request):
    data = {
        "info" : 'ecom backend'
    }
    return JsonResponse(data)