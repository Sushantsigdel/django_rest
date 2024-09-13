from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.apps.product.views import CategoryViewSet, BrandViewSet, ProductViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('category', CategoryViewSet),
router.register('brand', BrandViewSet),
router.register('product', ProductViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
