from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
                'password' : {'write_only' : True},
                'email' : {'required' : True},
                }

    def create(self, validated_data):
        print('yes user serializer executed')
        user = get_user_model().objects.create_user(
                email= validated_data['email'],
                password = validated_data['password'],
                username = validated_data.get('username', ''),
                               )

        return user 
