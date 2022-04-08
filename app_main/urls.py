from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'algorithms', views.AlgorithmViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.sort_profile, name='sort_profile'),
    path('ajax/algos/<int:item_count>/<int:sort_percentage>',
         views.ajax_algos, name='ajax_algos'),
    path('ajax/algos_code/<str:algo_name>',
         views.ajax_algos_code, name='ajax_algos_code'),


]
