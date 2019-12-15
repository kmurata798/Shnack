from django.urls import path, include
from accounts.views import SignUpView, LogInView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="sign-up-page"),
    path('login/', LogInView.as_view(), name="log-in-page")
    # path('accounts/', include('django.contrib.auth.urls')),
]