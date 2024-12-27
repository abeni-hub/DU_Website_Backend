from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from django.core import serializers
from django.db.models import Sum
from rest_framework import permissions
from rest_framework.permissions import AllowAny

from django.utils.timezone import now
from datetime import timedelta
from rest_framework import status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
import json

from .models import UserAccount, Role , UserAccountManager, UserAccount, UserAccountManager
from .serializers import UserAccountSerializer, UserCreateSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    from rest_framework import permissions


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [AllowAny]  # Temporarily allow any user to delete

    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.AllowAny()]  # Allow any user to delete
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned users to a given email,
    #     by filtering against a 'email' query parameter in the URL.
    #     """
    #     queryset = super().get_queryset()
    #     email = self.request.query_params.get('email', None)
    #     if email is not None:
    #         queryset = queryset.filter(email=email)
    #     return queryset
    #
    # def retrieve(self, request, *args, **kwargs):
    #     # Get the user instance
    #     instance = self.get_object()
    #
    #     # Clear user groups and permissions
    #     instance.remove_groups()
    #     instance.remove_permissions()
    #
    #     # Serialize the user instance
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer

@api_view(('GET',))
# @renderer_classes( JSONRenderer)
def UserDetail(request):
    if request.method == "GET":

        user = UserAccount.objects.filter(email=request.GET.get('email'))
        # & UserAccount.objects.filter(password = request.GET.get('password'))
        if user:
            js = serializers.serialize('json', user)
            return JsonResponse(js, safe=False)
        else:
            return Response({"error": "user not found"}, status=404)    