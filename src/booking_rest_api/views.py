from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from booking_app.models import HotelOwner, Hobby
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import Http404
from .serializers import UserSerializer, HotelOwnerSerializer, HobbiesModelSerializer


class UserApiView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class HotelOwnerListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        hotel_owners = HotelOwner.objects.all()
        serializer = HotelOwnerSerializer(hotel_owners, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelOwnerDetailView(APIView):

    def get_object(self, pk):
        try:
            return HotelOwner.objects.get(pk=pk)
        except HotelOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        owner = self.get_object(pk)
        serializer = HotelOwnerSerializer(owner)
        return Response(serializer.data)

    def put(self, request, pk):
        owner = self.get_object(pk)
        serializer = HotelOwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        owner = self.get_object(pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HobbyListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = HobbiesModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Hobby.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)