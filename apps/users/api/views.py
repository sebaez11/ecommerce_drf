# Local imports
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

# Django imports
from django.http import Http404

# Third imports
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.filter(is_active=True)
        data = UserSerializer(users, many=True)

        return Response(data.data)

    def post(self, request):
        post_data = request.data
        user_serializer = UserSerializer(data=post_data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data=user_serializer.data)
        else:
            return Response(user_serializer.errors)


class UserDetailAPIView(APIView):

    def get_user(self, id):
        try:
            return User.objects.get(pk=id, is_active=True)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_user(id=id)
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data)

    def put(self, request, id):
        user = self.get_user(id=id)
        user_serializer = UserSerializer(user, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self.get_user(id=id)
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)