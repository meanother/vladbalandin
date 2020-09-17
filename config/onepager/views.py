from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.core.mail import send_mail
from .serializers import ShortQuestionsSerializer, PollQuestionsSerializer, QuizQuestionsSerializer
from config.settings import EMAIL_HOST_USER, EMAIL_TO


class ShortQuestionsDetailView(generics.CreateAPIView):
    serializer_class = ShortQuestionsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        mail_name = serializer.data['name']
        mail_phone = serializer.data['phone']
        mail_message = serializer.data['message']
        create_time = serializer.data['create_time']
        mail_mail = serializer.data['email']

        mail_headers = f'Новая заявка: {mail_name}, номер телефона: {mail_phone} дата: {create_time}'
        mail_text = f'Заявка от {mail_name} \n' \
                    f'номер телефона: {mail_phone}\n' \
                    f'@Mail: {mail_mail} \n' \
                    f'Дополнительный текст сообщения: {mail_message}\n' \
                    f'\n\n ______\n @fl-bankrotstvo.ru'

        send_mail(mail_headers, mail_text, EMAIL_HOST_USER, EMAIL_TO, fail_silently=False)
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


class PollQuestionsDetailView(generics.CreateAPIView):
    serializer_class = PollQuestionsSerializer

    def create(self, request, *args, **kwargs):
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

        mail_headers = f'Новая заявка: {name}, номер телефона: {phone_number} дата: {create_time}'
        mail_text = f'Заявка от: {name} \n' \
                    f'Номер телефона: {phone_number} \n' \
                    f'Общая сумма задолженности: {summ} \n' \
                    f'Кол-во кредиторов: {amount} \n' \
                    f'Ежемесячный доход: {income} \n' \
                    f'Есть ипотека или иное имущество: {pledge} \n' \
                    f'Владение имуществом (через запятую): {property} \n' \
                    f'Город обращения: {city} \n' \
                    f'Город регистрации: {registration_city} \n' \
                    f'Имя: {name} \n' \
                    f'@Mail: {mail_mail} \n' \
                    f'\n\n\n ______\n @fl-bankrotstvo.ru'
        send_mail(mail_headers, mail_text, EMAIL_HOST_USER, EMAIL_TO, fail_silently=False)

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


class QuizQuestionsDetailView(generics.CreateAPIView):
    serializer_class = QuizQuestionsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        header = f"Квиз, новая заявка! От: {serializer.data['name']}," \
                 f" номер телефона: {serializer.data['phone_number']}," \
                 f" дата: {serializer.data['create_time']}"

        body = f"Данные:\n" \
               f"Имя: {serializer.data['name']}\n" \
               f"Номер телефона: {serializer.data['phone_number']}\n" \
               f"e-mail: {serializer.data['email']}\n" \
               f"Город: {serializer.data['city']}\n" \
               f"Общая сумма задолженности: {serializer.data['sum']}\n" \
               f"Кол-во кредиторов: {serializer.data['amount']}\n" \
               f"Просрочки по платежам: {serializer.data['has_delay']}\n" \
               f"Официальный доход: {serializer.data['income']}\n" \
               f"Дети: {serializer.data['has_child']}\n" \
               f"Брак: {serializer.data['is_marriage']}\n" \
               f"Собственность: {serializer.data['property']}\n" \
               f"Собственность, приобретенная в браке: {serializer.data['own_per_marriage']}\n" \
               f"Сделки с имуществом: {serializer.data['property_transaction']}\n" \
               f"Ипотека или залог: {serializer.data['pledge']}\n" \
               f"\n\n ______\n @fl-bankrotstvo.ru"

        send_mail(header, body, EMAIL_HOST_USER, EMAIL_TO, fail_silently=False)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}