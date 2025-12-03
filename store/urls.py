from django.urls import path
from django.contrib.auth import views as auth_views
<<<<<<< HEAD

<<<<<<< HEAD
=======
=======
>>>>>>> 02c616b2ffaa34c481adc325e929f0ae3b80dfb9
>>>>>>> cafb8291092cf80568e4e4fad28f361b900fb328
from .views import contact, detail, register, logout_user, add_item

from .forms import LoginForm

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_item/', add_item, name='add_item'),
    path('detail/<int:pk>/', detail, name='detail'),
]