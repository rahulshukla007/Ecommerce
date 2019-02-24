from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='shophome'),
    path('about/',views.about, name='Aboutus'),
    path('contact/',views.contact, name='Contactus'),
    path('tracker/',views.tracker, name='TrackingStatus'),
    path('search/',views.search, name='Search'),
    path('product/',views.productlist, name='ProductItems'),
    path('checkout/',views.checkout, name='Checkout'),

]
