import os
from time import sleep
import speech_recognition as sr
# https://amadorprograma.com/2021/08/24/sintese-de-voz-com-python-e-pyttsx3/
# Inicializando o pyttsx3
import pyttsx3
import aspose.words as aw
from googlesearch import search
import pyautogui as pyg


def anunciar_acao(acao):
    # instanciar a engine do sintetizador, através da factory function init()
    engine = pyttsx3.init()
    # O id da voz desejada, por exemplo “brazil”
    engine.setProperty("voice", "brazil")
    # A velocidade da fala, em palavras por minuto
    engine.setProperty("rate", 150)
    # Volume do áudio, de 0. a 1.
    engine.setProperty("volume", 1.)
    engine.say(acao)
    engine.runAndWait()

def solicitar_funcao():
    anunciar_acao("Escolha uma ação")
    anunciar_acao("Gerar documento")
    anunciar_acao("ou")
    anunciar_acao("Navegar")
    anunciar_acao("ou")
    anunciar_acao("Leitura")
    anunciar_acao("ou")
    anunciar_acao("Fechar")

    # HABILITA MICROFONE
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        # CHAMA UM ALGORITIMO DE REDUÇÃO DE RUIDOS NO SOM
        microfone.adjust_for_ambient_noise(source)

        # ARMAZENA O QUE FOI DITO EM UMA VARIÁVEL
        audio = microfone.listen(source)

        try:
            # PASSA VARIÁVEL PARA ALGORITIMO RECONHECER PADRÕES
            ff = microfone.recognize_google(audio, language='pt-BR')
            
            if "gerar documento" in ff:
                anunciar_acao(
                    "A parti de agora sera gerado o documento com o áudio capturado")
                ouvir_microfone_gerando_arquivo()
                return
            elif "leitura" in ff:
                # print("lendo")
                ler_arquivo()
                return
            elif "navegar" in ff:
                # print("navegar")
                pesquisa_google()
                return
            elif "fechar" in ff:
                anunciar_acao("Aplicação será encerrada.")
                sr.Microphone.__exit__

        except sr.UnknownValueError:
            # ouvir_microfone()
            sr.Microphone.__exit__
            anunciar_acao("Não entendi")
            solicitar_funcao()






# REPRESENTA UM DOCUMENTO
doc = aw.Document()
# CRIA UM DOCUMENTO
builder = aw.DocumentBuilder(doc)


def ouvir_microfone_gerando_arquivo():

    # HABILITA MICROFONE
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        # CHAMA UM ALGORITIMO DE REDUÇÃO DE RUIDOS NO SOM
        microfone.adjust_for_ambient_noise(source)

        # ARMAZENA O QUE FOI DITO EM UMA VARIÁVEL
        audio = microfone.listen(source)

        try:

            # PASSA VARIÁVEL PARA ALGORITIMO RECONHECER PADRÕES
            frase = microfone.recognize_google(audio, language='pt-BR')

            print(frase)
            # ESCREVENDO NO ARQUIVO
            builder.writeln(frase)

            if "concluir" in frase:
                sr.Microphone.__exit__
                anunciar_acao("salvando documento")
                doc.save(caminho_salvar_arquivo)
                solicitar_funcao()
                return

            ouvir_microfone_gerando_arquivo()

        except sr.UnknownValueError:
            anunciar_acao("Não entendi")
            solicitar_funcao()

        return frase



def ler_arquivo():

    with open(caminho_ler_arquivo, "r") as arquivo:
        email = arquivo.readlines()
        anunciar_acao(str(email).replace("\\n", ""))
    solicitar_funcao()


def pesquisa_google():
   
    anunciar_acao("Sobre o que você deseja pesquisar?")

    # HABILITA MICROFONE
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        # CHAMA UM ALGORITIMO DE REDUÇÃO DE RUIDOS NO SOM
        microfone.adjust_for_ambient_noise(source)

        # ARMAZENA O QUE FOI DITO EM UMA VARIÁVEL
        audio = microfone.listen(source)

        try:
            # PASSA VARIÁVEL PARA ALGORITIMO RECONHECER PADRÕES
            query = str(microfone.recognize_google(audio, language='pt-BR'))

            # query = string de consulta que desejamos pesquisar.
            # tld: tld significa domínio de nível superior, o que significa que queremos pesquisar nosso resultado em google.com ou google.in ou algum outro domínio
            # num: número de resultados que queremos.
            # stop: último resultado a recuperar. Use Nenhum para continuar pesquisando para sempre.
            # pause: lapso de espera entre as solicitações HTTP. Um lapso muito curto pode fazer com que o Google bloqueie seu IP. Manter um lapso significativo tornará seu programa lento, mas é uma opção segura e melhor
            print("=============================================================================")
            print("=============================================================================")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            print("=============================================================================")
            print("=============================================================================")
        except sr.UnknownValueError:
            anunciar_acao("Não entendi")
            solicitar_funcao()

        solicitar_funcao()


caminho_ler_arquivo = ''
while (caminho_ler_arquivo == ''):
    caminho_ler_arquivo = pyg.prompt('Caminho do Arquivo para ler. \n Deve ser um arquivo .txt')

caminho_salvar_arquivo = ''
while (caminho_salvar_arquivo == ''):
    caminho_salvar_arquivo = pyg.prompt('Caminho do Arquivo para salvar')

print("Assistente ativo.")

solicitar_funcao()
