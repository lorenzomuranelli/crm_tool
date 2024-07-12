# crm_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import debug_urls


router = DefaultRouter()
router.register(r'leads', views.LeadViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'opportunities', views.OpportunityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('debug/', debug_urls, name='debug'),
]