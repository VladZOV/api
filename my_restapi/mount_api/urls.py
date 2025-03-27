from django.urls import path
from .views import SubmitDataView, GetPerevalView

urlpatterns = [
    path('submitData/', SubmitDataView.as_view(), name='submit-data'),
    path('submitData/<int:pk>/', GetPerevalView.as_view(), name='get-pereval'),
]