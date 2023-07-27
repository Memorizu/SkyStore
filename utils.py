# from django.core.mail import send_mail
#
# from django.conf import settings
#
#
# def send_congratulations(article_title):
#     subject = 'Поздравление с достижением 10 просмотров статьи'
#     message = f'Статья "{article_title}" достигла 10 просмотров! Поздравляем!'
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [settings.EMAIL_HOST_USER]  # Замените на свой адрес почты
#
#     send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#
