from django.urls import path

from users.apps import UsersConfig

from users.views import PaymentListApiView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListApiView.as_view(), name="payment_list"),
]
