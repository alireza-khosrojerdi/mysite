from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # login
    path('logout/', views.logout_view, name='logout'),
    # logout
    path('signup/', views.signup_view, name='signup'),
    # resigtration / signup
    #path('password_change/', views.password_change, name='password_change'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirm,
         name='password_reset_confirm'),
]
