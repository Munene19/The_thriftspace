from thrift.views import PostViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', PostViewSet)

router.register('users', UserViewSet)

