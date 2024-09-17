def enviar_email(destinatario:str="Sem assunto", assunto:str="", corpo:str='') -> None:
    '''Função para enviar um email'''
    print(f'Email enviado para: {destinatario}')
    print(f'Assunto: {assunto}')
    print(f'Mensagem: {corpo}')
enviar_email("Pessoa x", "algum assunto", "Olá venho por meio deste canal de texto para informar esse teste")