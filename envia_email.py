import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import password


print('////////// Preparando o email... //////////')
		
# Iniciando o servidor SMTP legacy outlook para TCP 1.1
host = 'smtp-legacy.office365.com'
port = '587'
login = 'sistema@exemplo.com.br'
senha = password.outlook_sistema

# # Iniciando o servidor SMTP hostgator
# host = 'mail.sistema.exemplo.com.br'
# port = '587'
# login = 'naoresponder@sistema.exemplo.com.br'
# senha = password.senha_hostgator

# # Iniciando o servidor SMTP ZOHO
# host = 'smtp.zoho.com'
# port = '587'
# login = 'sistema@exemplo.com.br'
# senha = password.senha_zoho

# Entrando no servidor
print('Variáveis declaradas. Abrindo servidor com SMTP lib')
server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login, senha)
print('SERVIDOR ACESSADO', server)
print('ENTRADA FEITA')
print('START SERVER EMAIL')
print('//////// Servidor de email SMTP: OK ////////')


## Pega o e-mail do usuário
print("Pegando o e-mail do usuário...")
emailUser = 'exemplo@gmail.com'
print('ENVIANDO EMAIL PARA :', emailUser)

# Criando o e-mail
print('Criando o e-mail...')

corpo = '<h1>corpo_email__TESTE__.html</h1>'
assunto = 'TESTANDO O ENVIO DE EMAIL.'

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = emailUser
email_msg['Subject'] = assunto
email_msg.attach(MIMEText(corpo, 'html'))

# Lendo e transformando o aquivo de anexo em binário
print('Preparando anexo do email')
caminho_arquivo = r'anexo.txt'
arquivo = open(caminho_arquivo, 'rb')
anexo = MIMEBase('aplication', 'octet-stream') 
anexo.set_payload(arquivo.read())
encoders.encode_base64(anexo) 

# Adidionando o cabeçalho, anexo e fechando o arquivo
anexo.add_header('Content-Disposition', f'arquivo; filename=anexo.txt')
arquivo.close()
email_msg.attach(anexo)

# Envia o e-mail
server.sendmail(
    email_msg['From'],
    email_msg['To'],
    email_msg.as_string()
)
print('//////// E-mail enviado com sucesso ////////')

server.quit() # Fechando o servidor
print('servidor fechado')
