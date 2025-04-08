from django.urls import path
from .views import SubmitDataView, SubmitDataUpdateView, UserPerevalsListView

urlpatterns = [
    path('submitData/', SubmitDataView.as_view(), name='submit-data'),
    path('submitData/<int:pk>/', SubmitDataUpdateView.as_view(), name='update-data'),
    path('submitData/list_mail/', UserPerevalsListView.as_view(), name='user-pereval-list-mail'),
]
