# crm_app/views.py
from rest_framework import viewsets
from .models import Lead, Contact, Opportunity
from .serializers import LeadSerializer, ContactSerializer, OpportunitySerializer
from django.urls import resolve

def debug_urls(request):
    url_info = resolve(request.path)
    print("URL namespace:", url_info.namespace)
    print("URL name:", url_info.url_name)
    print("View function:", url_info.func.__name__)
    return HttpResponse("URL debugging")
    
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

# crm_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'leads', views.LeadViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'opportunities', views.OpportunityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

# crm_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm_app.urls')),
]

from django.urls import get_resolver

def debug_urls(request):
    resolver = get_resolver()
    print(resolver.url_patterns)
    return HttpResponse("URL debugging")