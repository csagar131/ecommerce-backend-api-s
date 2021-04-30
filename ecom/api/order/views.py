from .models import Order
from .serializers import OrderSerializers
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk = id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add_order(request,id,token):
    if not validate_user_session(id, token):
        return JsonResponse({"error":"Invalid User"}, status=HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        total_product = len(products.split(','))

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk = id)
            
        except UserModel.DoesNotExist:
            return JsonResponse({"error": "User does not exist"})

        order =  Order(user=user,product_names=products,total_product=total_product,amount=amount,transaction_id=transaction_id)
        order.save()
        return JsonResponse({'message': "order placed successfully"}, status=HTTP_201_CREATED)





class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializers
    queryset = Order.objects.all().order_by('id')
