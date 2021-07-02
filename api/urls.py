from django.conf.urls import url
from django.urls import include, path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter


from api import views

router = DefaultRouter()
router.register(
    r'polls',
    views.PollsViewSet
)
router.register(
    r'questions',
    views.QuestionViewSet
)
router.register(
    r'votes',
    views.VoteViewSet,
    'votes-detail'
)
router.register(
    r'answer',
    views.AnswerViewSet
)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),

]