from django.urls import path
from . import views

urlpatterns = [

    path(
        "register/",
        views.register,
        name="provider_register"
    ),

    path(
        "booking/",
        views.booking,
        name="booking"
    ),

    path(
        "list/",
        views.providers,
        name="providers"
    ),

    path(
        "<int:pk>/",
        views.detail,
        name="provider_detail"
    ),
]