from django.urls import path
from .views import SportList, SportDetail

urlpatterns = [
    path('', SportList.as_view(), name='sport_list'),
    path('<int:pk>/', SportDetail.as_view(), name='sport_detail')
]



