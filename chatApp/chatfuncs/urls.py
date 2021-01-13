from rest_framework import routers
from chatfuncs.views import ChatViewSet, LikesViewSet

router = routers.DefaultRouter()
router.register('xan', ChatViewSet, 'chats')
router.register('likes', LikesViewSet, 'likes')
# router.register('update', ChatUpdateSet, 'update')

urlpatterns = router.urls
