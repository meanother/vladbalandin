from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.core.mail import send_mail
from .serializers import ShortQuestionsSerializer, PollQuestionsSerializer
from config.settings import EMAIL_HOST_USER

# from rest_framework import pagination
# from django_filters import rest_framework as rest_filter
# from rest_framework import filters

# Create your views here.


class ShortQuestionsDetailView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShortQuestionsSerializer

    # queryset = MailSend.objects.all()

    def create(self, request, *args, **kwargs):
        # print('===================')
        # print(request.data)
        # print(dir(request.data))
        # print(type(request.data))
        # print(request.data['name'])
        # print(request['context'])
        # print('>>>>>>>>')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print(serializer.data)
        # print('----------')
        # print(serializer.data['name'])
        # print(serializer.data['phone'])
        # print(serializer.data['message'])
        mail_name = serializer.data['name']
        mail_phone = serializer.data['phone']
        mail_message = serializer.data['message']
        create_time = serializer.data['create_time']
        mail_mail = serializer.data['email']

        mail_headers = f'Заявка от {mail_name}, номер телефона: {mail_phone}, {mail_mail} от {create_time}'
        mail_text = f'Заявка от {mail_name} \nномер телефона: {mail_phone} \nТут должен быть текст сообщения: {mail_message}\n\n\n ______\n Semenov Artur'
        #

        # send_mail(mail_headers, mail_text, 'juicehqperfect@gmail.com', ['juicehq@yandex.ru'], fail_silently=False)
        send_mail(mail_headers, mail_text, EMAIL_HOST_USER, ['juicehq@yandex.ru'], fail_silently=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # serializer.save(name='NEW NAME X')
        print('qweqweqwe')
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class PollQuestionsDetailView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PollQuestionsSerializer

    # queryset = MailSend.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        summ = serializer.data['summ']
        amount = serializer.data['amount']
        income = serializer.data['income']
        pledge = serializer.data['pledge']
        property = serializer.data['property']
        city = serializer.data['city']
        registration_city = serializer.data['registration_city']
        name = serializer.data['name']
        phone_number = serializer.data['phone_number']
        create_time = serializer.data['create_time']
        mail_mail = serializer.data['email']


        mail_headers = f'Заявка от {name}, номер телефона: {phone_number} от {create_time}'
        mail_text = f'Заявка от: {name} \n' \
                    f'номер телефона: {phone_number} \n' \
                    f'Общая сумма задолженности: {summ} \n' \
                    f'Кол-во кредиторов: {amount} \n' \
                    f'Ежемесячных доход: {income} \n' \
                    f'Есть ипотека или иное имущество: {pledge} \n' \
                    f'Владение имуществом (через запятую): {property} \n' \
                    f'Город обращения: {city} \n' \
                    f'Город регистрации: {registration_city} \n' \
                    f'Имя: {name} \n' \
                    f'Mail: {mail_mail} \n' \
                    f'Номер телефона: {phone_number}' \
                    f'\n\n\n ______\n Semenov Artur'
        send_mail(mail_headers, mail_text, EMAIL_HOST_USER, ['juicehq@yandex.ru'], fail_silently=False)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # serializer.save(name='NEW NAME X')
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
