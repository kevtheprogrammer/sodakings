from django.urls import path,include
from .views import *

app_name = 'account'

urlpatterns = [
    path('edit/', UserEditCreateView.as_view(), name='edit'),
    path("signup/", SignUpView.as_view(),name="signup"),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]


 