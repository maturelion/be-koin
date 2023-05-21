from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import BasePermission
class IsOwnerOrAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object or admin to view/edit it,
    but deny non-admin users from seeing the list of objects.
    """

    # def has_permission(self, request, view):
    #     if view.action == 'list':
    #         return request.user.is_staff
    #     return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff



class UserViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    # filterset_fields = ("", )

    def get_object(self):
        obj = User.objects.get(slug=self.request.user.slug)
        return obj

    def update(self, request, *arg, **kwargs):
        user_object = self.get_object()
        data = request.data

        user_object.slug = slugify(data["username"])

        fields = user_object._meta.fields
        for field in fields:
            field = field.name.split(".")[-1]  # to get column name
            exec("user_object.%s = data.get(field, user_object.%s)" % (field, field))

        serializer_context = {
            "request": request,
        }

        user_object.save()

        serializer = UserSerializer(user_object, context=serializer_context)
        return Response(serializer.data)
