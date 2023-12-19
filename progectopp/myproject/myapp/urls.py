from django.urls import path,include
from . import views 
urlpatterns = [
    # path('',include("myapp.urls")),
    path('',views.index,name='home'),
    path('loge/',views.store1,name='logo'),
    path('index1/<int:p>',views.item_view1,name='index1'),
    path('item/<int:p>',views.item_view,name='item'),
    path('william/',views.storess,name='william'),
    path('About_us/',views.About_us,name='About_us'),
    path('Contact_Us/',views.Contact_Us,name='Contact_Us'),
    path('login/', views.user_login, name="login1"),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.user_logout,name='user_logout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:p>',views.remove_item,name='remove'),
]
