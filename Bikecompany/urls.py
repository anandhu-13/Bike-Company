"""
URL configuration for Bikecompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Store import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.SigninView.as_view(),name="signin"),
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("productlist/",views.ProductListView.as_view(),name="product-list"),
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("bike/blog/",views.WhyUsView.as_view(),name="blog"),
    path("signout/",views.SignOutView.as_view(),name="sign-out"),
    path("bike/detail/<int:pk>",views.BikeDetailView.as_view(),name="detail"),

    path('checkout/<int:pk>/',views.CheckOutView.as_view(),name="checkout"),
    path('order/summary/',views.OrderSummaryView.as_view(),name="summary"),
    path('ordetitem/<int:pk>remove/',views.OrderItemRemoveView.as_view(),name="item-delete"),
    
    path('sucess/',views.SucessView.as_view(),name="success"),

    path('payment/verification/',views.PaymentVerificationView.as_view(),name="verification"),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
