from django.urls import path,include
from . import views



urlpatterns = [
    path('api-urls/',views.apiOverview,name = 'api-overview'),
    path('detail-list/',views.detailList,name = 'detail-list'),
    path('person-detail/<str:pk>/',views.personDetail,name = 'person-detail'),
    path('person-create/',views.createPerson,name = 'create-person'),
    path('person-update/<str:pk>/',views.updatePerson,name = 'update-person'),
    path('person-delete/<str:pk>/',views.deletePerson,name = 'delete-person'),
]