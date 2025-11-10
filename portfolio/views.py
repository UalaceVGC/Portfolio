from django.shortcuts import render, get_object_or_404, redirect,HttpResponse

from django.core.mail import BadHeaderError
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import messages
from smtplib import SMTPException, SMTPAuthenticationError, SMTPServerDisconnected

# Create your views here.

def portfolio(request):
    return render(request, 'portfolio.html')

def enviar_email(request):
    if request.method == 'POST':

        name = request.POST.get("nome")
        message = request.POST.get("mensagem")
        from_email = request.POST.get("email")

        # 1. Checagem de campos e uso do Messages Framework para feedback ao usuário
        if name and message and from_email:
            try:
                # Detalhes do email
                subject = "Contato via portfolio - " + name
                body = f"Nome: {name}\nEmail: {from_email}\n\nMensagem:\n{message}"

                # Enviar email para adm
                email = EmailMessage(
                    subject,
                    body,
                    # Não é estritamente necessário definir o 'from' se DEFAULT_FROM_EMAIL
                    # estiver configurado no settings.py, mas aqui o Django usa ele.
                    to=["ualacegcd@gmail.com"], 
                    reply_to=[from_email],
                )
                
                email.send()
                
                # Sucesso: Adiciona uma mensagem para ser exibida no template
                messages.success(request, "A sua mensagem foi enviada com sucesso! Em breve entrarei em contacto.")
                return redirect('portfolio')
            
            # 2. Tratamento de Erros SMTP: Mais específico e útil
            except (SMTPAuthenticationError, SMTPServerDisconnected) as e:
                # Erro de credenciais, porta, ou host (como o 535 que tivemos)
                print(f"Erro de autenticação/conexão SMTP: {e}") 
                messages.error(request, "Ocorreu um erro nas credenciais de e-mail do servidor. Por favor, tente novamente mais tarde.")
                return redirect('portfolio')
                
            except SMTPException as e:
                # Captura outros erros gerais de SMTP
                print(f"Erro SMTP: {e}")
                messages.error(request, "Ocorreu um erro geral no envio. Por favor, tente novamente mais tarde.")
                return redirect('portfolio')
                
            except Exception as e:
                # Captura quaisquer outros erros inesperados
                print(f"Erro inesperado no envio de email: {e}")
                messages.error(request, "Ocorreu um erro inesperado. Por favor, tente novamente mais tarde.")
                return redirect('portfolio')

        else:
            # Falha: Informa o usuário sobre o que está faltando
            messages.error(request, "Por favor, preencha todos os campos obrigatórios (Nome, E-mail e Mensagem).")
            return redirect('portfolio')

    # Se a requisição não for POST, apenas renderiza a página
    return render(request, 'portfolio.html')