from django.urls import path, include
from backend import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('backend', views.SubscriberListView)
router.register('backend', views.ServiceListView)
router.register('backend', views.OrganizationListView)

urlpatterns = [
    path('', include(router.urls))
]