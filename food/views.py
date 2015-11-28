from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import Food, FoodUser
from food.serializers import FoodSerializer, FoodUserSerializer


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        return Food.objects.filter(giver__company=self.request.user.company)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = super().get_serializer_context()
        context['company_id'] = self.request.user.company_id
        return context

    def perform_create(self, serializer):
        place = self.request.user.company.place_set.first()
        # for test purposes set some data
        serializer.save(giver=self.request.user, place=place, taker=None)

    @detail_route(methods=['get'], url_path='claim')
    def claim(self, request, pk):
        food = get_object_or_404(Food, id=pk)
        if not food.taker:
            food.taker = request.user
            food.save()
            content = {'food': 'Food claimed successfully'}
        else:
            content = {'food': 'Food already taken'}
        return Response(content)


class FoodUserViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):

    queryset = FoodUser.objects.all()
    serializer_class = FoodUserSerializer

    def get_queryset(self):
        return FoodUser.objects.filter(company=self.request.user.company)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = super().get_serializer_context()
        context['company_id'] = self.request.user.company_id
        return context


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': user.id})


obtain_auth_token = ObtainAuthToken.as_view()
