from django.urls import include, path
from rest_framework import routers

from .views import (CategoriesViewSet, GenresViewSet, TitlesViewSet,
                    UserCreateViewSet, UserReceiveTokenViewSet, UserViewSet,
                    ReviewViewSet, CommentViewSet)

app_name = 'api'

router_v1 = routers.DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'titles', TitlesViewSet, basename='titles')
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

auth_urls = [
    path(
        'signup/',
        UserCreateViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        'token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    )
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', include(router_v1.urls)),
]
