from django.contrib.auth.models import User, Group
from rest_framework import viewsets ,status
from rest_framework import permissions
from rest_framework.decorators import api_view ,authentication_classes,permission_classes
from APPtest.serializers import UserSerializer, GroupSerializer , ItemSerializer \
    , CharityRegistrationSerializer , UserRegistrationSerializer,CharityLoginSerializer \
    ,UserLoginSerializer,CharityGetAllSerializer ,OrderedItemSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from APPtest.models import CharityRegistration , UserRegistration , Item
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# @api_view(['POST'])
# @authentication_classes([ TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def add_item(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return  Response({"Status":"Added"},status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_new_charity(request):
    serializer = CharityRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return  Response({"Status":"Added"},status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_new_charity(request):
    serializer = CharityLoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.data['Email']
        try:
            Password = list(CharityRegistration.objects.filter(Email=email).values())[0]['Password']
            print(Password)
            if Password == serializer.data['Password']:
                return Response({"Status": "Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status": "Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.data['Email']
        try:
            Password = list(UserRegistration.objects.filter(Email=email).values())[0]['Password']
            print(Password)
            if Password == serializer.data['Password']:
                return Response({"Status": "Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status": "Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_all_charities(request):
    charities = CharityRegistration.objects.all().order_by('-CharityName')
    serializer = CharityGetAllSerializer(charities,many=True)
    return  Response(serializer.data)





@api_view(['GET'])
def get_all_items_by_charity(request):
    email = dict(request.data)['email'][0]
    charities = Item.objects.filter(Charity=email)
    serializer = ItemSerializer(charities,many=True)
    return  Response(serializer.data)


@api_view(['POST'])
def order_new_item(request):
    serializer = OrderedItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return  Response({"Status":"Ordered"},status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def modify_charity_details(request):
    serializer = CharityRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['Email']
        CharityName = serializer.data['CharityName']
        Password = serializer.data['Password']
        City = serializer.data['City']
        CharityRegistration.objects.filter(Email=email).update(CharityName=CharityName,
                                                               Password=Password,
                                                               City=City)

        #serializer.save()
        return  Response({"Status":"Modified"},status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_charity_participants(request):
    CharityName = dict(request.data)['CharityName'][0]
    participants = UserRegistration.objects.filter(CharityName=CharityName)
    serializer = UserRegistrationSerializer(participants, many=True)
    return Response(serializer.data)



@api_view(['DELETE'])
def delete_item(request):
    ItemID = dict(request.data)['ItemID'][0]
    Item.objects.get(ItemID=ItemID).delete()

    return Response({"Status": "Delted"}, status=status.HTTP_200_OK)


