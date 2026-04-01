from django.http import JsonResponse

def home(request):
    return JsonResponse("This is the backend homepage.", safe = False)