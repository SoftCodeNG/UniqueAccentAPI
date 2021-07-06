from django.urls import path

from accounts.views import registration_view, staff_registration_view, admin_registration_view, login_with_google, \
    forget_password, reset_password

urlpatterns = [
    path('register', registration_view, name='register'),
    path('registerStaff', staff_registration_view, name='registerStaff'),
    path('registerAdmin', admin_registration_view, name='registerAdmin'),
    path('loginWithGoogle', login_with_google, name='loginWithGoogle'),
    path('forgetPassword', forget_password, name='forgetPassword'),
    path('resetPassword', reset_password, name='resetPassword'),
]
