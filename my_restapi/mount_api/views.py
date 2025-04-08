from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Pereval, User
from .serializers import PerevalSerializer


class SubmitDataView(APIView):
    def post(self, request):
        serializer = PerevalSerializer(data=request.data)

        if serializer.is_valid():
            try:
                pereval = serializer.save()
                response_data = {
                    'status': status.HTTP_200_OK,
                    'message': 'Отправлено успешно',
                    'id': pereval.id
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except Exception as e:
                response_data = {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': str(e),
                    'id': None
                }
                return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            response_data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': serializer.errors,
                'id': None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class SubmitDataUpdateView(RetrieveUpdateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['patch']  # только редактирование

    def patch(self, request, *args, **kwargs):
        pereval = self.get_object()

        # проверка что статус именно "new"
        if pereval.status != 'new':
            return Response({
                'state': 0,
                'message': 'Редактирование запрещено: запись не в статусе "new"'
            }, status=400)

        # запрет изменений данных пользователя
        user_data = request.data.get('user', {})
        if user_data:
            original_user = pereval.user
            if (user_data.get('email') != original_user.email or
                    user_data.get('fam') != original_user.fam or
                    user_data.get('name') != original_user.name or
                    user_data.get('otc') != original_user.otc or
                    user_data.get('phone') != original_user.phone):
                return Response({
                    'state': 0,
                    'message': 'Редактирование данных пользователя запрещено'
                }, status=400)

        try:
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            return Response({
                'state': 0,
                'message': str(e)
            }, status=400)


class UserPerevalsListView(ListAPIView):
    serializer_class = PerevalSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        if not email:
            raise ValidationError("Не указан email пользователя")

        user = get_object_or_404(User, email=email)
        return Pereval.objects.filter(user=user)
