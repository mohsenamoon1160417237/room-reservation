from rest_framework.generics import GenericAPIView
from user_register.model_serializers.register import RegisterSerializer
from user_register.views.utils.register import register


class NormalUserRegister(GenericAPIView):

    def post(self, request):

        return register(request.data, RegisterSerializer, 'normal')
