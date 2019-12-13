from django.urls import path, include
from accounts.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="sign-up-page"),
    # path('accounts/', include('django.contrib.auth.urls')),
]