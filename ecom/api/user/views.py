from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re
import random
# Create your views here.

def generate_session_token(length=10):
    list1 = [chr(i) for i in range(97,123)]
    list2 = [str(i) for i in range(10)]
    return ''.join(random.SystemRandom().choice(list1 + list2) for _ in range(length))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'send a post request with valid parameter'})

    username = request.POST['email']
    password = request.POST['password']

    #validation part
    if not re.match('([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}', username):
        return JsonResponse({'error':'Please provide a valid email'})
    
    if len(password) < 5:
        return JsonResponse({'error':'Password Should be more than 5 characters'})

    UserModel = get_user_model() #getting the user model from django(customized) 

    try:
        #objects.get() gives the single object not queryset
        user = UserModel.objects.get(email =  username)
        if user.check_password(password):
            # objects.filter() gives the matching queryset(s)
            usr_dict = user.objects.filter(email = username).values().first()
            usr_dict.pop('password')
    
            #check if previous session is exist
            #if user trying to login
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'previous session exists'})
        
        #generating the session token
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request,user)
            return JsonResponse({'token':token, 'user' : usr_dict})
        else:
            return JsonResponse({'error':'invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid User'})


def signout(request,id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk = id)
        user.session_token = "0"
        user.save()
        logout(request)
        return JsonResponse({'message':'Logged out succesfully'})
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid User'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]




    
