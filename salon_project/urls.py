"""
URL configuration for salon_project project.
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from salon import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    # ==============================
    # CUSTOMER PAGES
    # ==============================

    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('academy/', views.academy, name='academy'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),


    # ==============================
    # OWNER DASHBOARD
    # ==============================

    path(
        'owner/login/',
        auth_views.LoginView.as_view(
            template_name='owner_login.html'
        ),
        name='owner_login'
    ),

    path(
        'owner/logout/',
        auth_views.LogoutView.as_view(),
        name='owner_logout'
    ),

    path(
        'owner/dashboard/',
        views.owner_dashboard,
        name='owner_dashboard'
    ),

    path(
        'owner/appointment/<int:appointment_id>/<str:status>/',
        views.update_appointment_status,
        name='update_appointment_status'
    ),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)