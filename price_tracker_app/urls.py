from django.urls import path
from rest_framework import routers
from .views import AlertViews

router = routers.DefaultRouter()
router.register(r'alerts', AlertViews,basename="price-tracker")

urlpatterns = router.urls


urlpatterns+=[
    path('api/alerts/check', AlertViews.as_view({'get': 'check'}), name='alert-check')
]