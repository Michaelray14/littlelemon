from django.contrib import admin
from django.urls import include, path
from .views import sayHello
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    ##path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
]
