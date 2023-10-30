from django.urls import path
from home.views import product_list,login_user,logout_user,register_user,cart
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login_user, name='login'),    
    path('logout/', logout_user, name='logout'),    
    path('home/', product_list, name='product_list'),
    path('register/', register_user, name='register'),
    path('cart/', cart, name='cart'),
    path('', product_list, name='product_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)