from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceSerializer


class NotificationsView(generics.GenericAPIView):
    http_method_names = ['post']
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ok, device_id = Device.objects.register_device(serializer.validated_data['device_token'],
                                                       serializer.validated_data['device_type'],
                                                       request.user
                                                       )

        response = {'success': ok}
        if device_id is not None:
            response['id'] = str(device_id)

        return Response(data=response)
