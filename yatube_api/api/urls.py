from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts_v1')
router_v1.register('groups', GroupViewSet, basename='groups_v1')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments-list_v1'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
    CommentViewSet,
    basename='comments-detail_v1'
)


urlpatterns = (
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
)
