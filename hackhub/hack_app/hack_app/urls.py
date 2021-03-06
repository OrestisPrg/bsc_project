"""hack_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from exercises import views as exercises_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hackme/welcome.html'), name='logout'),
    path('chapter1/exercise1', exercises_views.ch1ex1, name='ch1ex1'),
    path('chapter1/exercise1/quiz', exercises_views.ch1qz1, name='ch1qz1'),
    path('chapter1/exercise2', exercises_views.ch1ex2, name='ch1ex2'),
    path('chapter1/exercise2/quiz', exercises_views.ch1qz2, name='ch1qz2'),
    path('chapter1/exercise3', exercises_views.ch1ex3, name='ch1ex3'),
    path('chapter1/exercise3/quiz', exercises_views.ch1qz3, name='ch1qz3'),
    path('chapter2/exercise1', exercises_views.ch2ex1, name='ch2ex1'),
    path('chapter2/exercise2', exercises_views.ch2ex2, name='ch2ex2'),
    path('chapter2/exercise2/quiz', exercises_views.ch2qz2, name='ch2qz2'),
    path('chapter2/exercise3', exercises_views.ch2ex3, name='ch2ex3'),
    path('chapter2/exercise3/quiz', exercises_views.ch2qz3, name='ch2qz3'),
    path('chapter2/exercise4', exercises_views.ch2ex4, name='ch2ex4'),
    path('chapter2/exercise4/quiz', exercises_views.ch2qz4, name='ch2qz4'),
    path('chapter3/exercise1', exercises_views.ch3ex1, name='ch3ex1'),
    path('chapter3/exercise1/quiz', exercises_views.ch3qz1, name='ch3qz1'),
    path('chapter3/exercise2', exercises_views.ch3ex2, name='ch3ex2'),
    path('chapter3/exercise2/quiz', exercises_views.ch3qz2, name='ch3qz2'),
    path('chapter3/exercise3', exercises_views.ch3ex3, name='ch3ex3'),
    path('chapter3/exercise3/quiz', exercises_views.ch3qz3, name='ch3qz3'),
    path('chapter3/exercise4', exercises_views.ch3ex4, name='ch3ex4'),
    path('chapter3/exercise4/quiz', exercises_views.ch3qz4, name='ch3qz4'),
    path('completed', exercises_views.ex_completed, name='ex_completed'),

    path('password-reset/',
     auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
     name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
     name='password_reset_done'),
    path('', include('hackme.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
