from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from apps.coins.views import CoinsListAPIView, CoinsCreateAPIView, \
# CoinsUpdateAPIView, CoinsDeleteAPIView, CoinsRetrievAPIView
from apps.coins.views import CoinsAPI

router = DefaultRouter()
router.register("api_coins", CoinsAPI, basename='api-coins')
router.register("coins_viewsets", CoinsAPI, basename='api-coins-viewsets')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls

# urlpatterns = [
#     path("news_list", NewsListAPIView.as_view(), name='list_api'),
#     path("create/", NewsCreateAPIView.as_view(), name='create news'),
#     path("update/<int:pk>", NewsUpdateAPIView.as_view(), name='delete news'),
#     path("<int:pk>", NewsRetrievAPIView.as_view(), name='retriev_news'),
#     path("delete/<int:pk>", NewsDeleteAPIView.as_view(), name='delete_news')
# ]