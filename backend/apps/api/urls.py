from rest_framework.routers import SimpleRouter

from apps.api.views import QuestionsViewSet

router = SimpleRouter()
router.register('questions', QuestionsViewSet, basename='question')

urlpatterns = router.urls
