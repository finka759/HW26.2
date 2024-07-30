from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


class PaymentListApiView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('course', 'payment_method',)
    ordering_fields = ('payment_date',)


class UserListApiView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentCreateApiView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        stripe_product_id = create_stripe_product(payment)
        # payment.amount = payment.summ
        price = create_stripe_price(summ=payment.summ, stripe_product_id=stripe_product_id)
        payment_id, payment_link = create_stripe_session(summ=price)
        payment.payment_id = payment_id
        payment.payment_link = payment_link
        payment.save()
