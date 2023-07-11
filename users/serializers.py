from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # referral = ReferralSerializer(source="user_referral", required=False)

    class Meta:
        model = User
        fields = [
            "url",
            "slug",
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "percentage",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
        ]
        read_only_fields = [
            "is_staff",
            "percentage",
            "is_active",
            "last_login",
            "date_joined",
        ]    
        extra_kwargs = {"url": {"view_name": "user-detail", "lookup_field": "slug"}}
