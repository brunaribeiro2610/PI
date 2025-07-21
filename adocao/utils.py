from django.core.mail import send_mail
from django.conf import settings

def enviar_email_confirmacao_adocao(nome_usuario, email_usuario, nome_animal):
    assunto = f"Adoção solicitada para {nome_animal}"
    mensagem = (
        f"Olá, {nome_usuario}!\n\n"
        f"Recebemos sua solicitação de adoção para o animal {nome_animal}.\n"
        f"Nossa equipe irá analisar seu pedido e entraremos em contato em breve.\n\n"
        f"Obrigado por escolher adotar!\n\n"
        f"Equipe - Projeto de Adoção"
    )
    send_mail(
        assunto,
        mensagem,
        settings.DEFAULT_FROM_EMAIL,
        [email_usuario],
        fail_silently=False,
    )
