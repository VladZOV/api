from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Pereval
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


class GetPerevalView(RetrieveAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
