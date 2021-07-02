from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(
    r'polls',
    views.PollsViewSet
)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]