# Crie uma função valida_email(email) que verifique se um e-mail é válido.

def valida_email(email):
    if email.count('@') != 1 or email.count('.') == 0:
        return False
    
    local, dominio = email.split('@')
    
    if len(local) == 0 or len(dominio) < 3:
        return False
    
    if '.' not in dominio:
        return False
    
    extensao = dominio.split('.')[-1]
    if len(extensao) < 2:
        return False
    
    return True

emails = [
    "teste@dominio.com", 
    "teste@dominio", 
    "teste@.com", 
    "@dominio.com", 
    "teste@dominio@com", 
    "teste@dominio.c"
]

for email in emails:
    print(f"{email}: {valida_email(email)}")
