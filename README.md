<h1>Assistente Virtual</h1> 

<p align="center">
  <img src="http://img.shields.io/static/v1?label=Python&message=3.8&color=red&style=for-the-badge&logo=python"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/
</p>

> Status do Projeto: :heavy_check_mark: :warning: (em desenvolvimento)

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

... 

Insira os tópicos do README em links para facilitar a navegação do leitor

## Descrição do projeto 

<p align="justify">
  Projeto realizado como trabalho final do curso EY Fast Track Specialist - Machine Learning.
  Com o propósito de desenvolver um assistente virtual.
</p>

## Funcionalidades

:heavy_check_mark: Reconhecer comandos de voz  

:heavy_check_mark: Gerar um documento com o aúdio capturado durante a execução do sistema  

:heavy_check_mark: Fazer uma busca no Google através de comado de voz  

:heavy_check_mark: Gerar áudio a partir da leitura de um arquivo TXT

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
:heavy_check_mark: [Python](https://docs.python.org/3.8/)

:heavy_check_mark: [SpeechRecognition 3.8.1](https://pypi.org/project/SpeechRecognition/)

:heavy_check_mark: [pyttsx3 2.90](https://pypi.org/project/pyttsx3/)

:heavy_check_mark: [aspose-words 22.10.0](https://pypi.org/project/aspose-words/)

:heavy_check_mark: [googlesearch-python 1.1.0](https://pypi.org/project/googlesearch-python/)

:heavy_check_mark: [PyAutoGUI 0.9.53](https://pypi.org/project/PyAutoGUI/). 

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)


## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/ariaguiarfilho/Assistente-Virtual.git
```
Execute: python3 assistente.py



## Casos de Uso

Ao iniciar a aplicação será solicitao ao usuário que preencha onde está o arquivo TXT para ser lido e onde será salvo o documento gerado, após esse procedimento o sistema solicita que o usuário escolha uma ação via comando de voz. 

Ao escolher **Gerar Documento** o sistema deve capturar o áudio do usuário e ao falar a palavra **CONCLUIR** será gerado um documento com o áudio capturado.

Ao escolher **Navegar** o sistema deve solicitar ao usuário via comando de voz qual o termo que deseja pesquisar, o sistema deverá listar uma relação de sistes relacionados ao tema escolhido.

Ao escolher **Leitura** o sistema deverá ler um arquivo **TXT** e gerar o áudio do texto.

Ao escolher **Fechar** o sistema apresenta uma mensagem que a aplicação será encerrada o sistema é fechado.

## Linguagens, dependencias e libs utilizadas :books:

- [Python](https://docs.python.org/3.8/)

- [SpeechRecognition 3.8.1](https://pypi.org/project/SpeechRecognition/)

- [pyttsx3 2.90](https://pypi.org/project/pyttsx3/)

- [aspose-words 22.10.0](https://pypi.org/project/aspose-words/)

- [googlesearch-python 1.1.0](https://pypi.org/project/googlesearch-python/)

- [PyAutoGUI 0.9.53](https://pypi.org/project/PyAutoGUI/). 



## Desenvolvedores/Contribuintes :octocat:

Liste o time responsável pelo desenvolvimento do projeto



| [<img src="https://avatars.githubusercontent.com/u/79552007?s=400&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Ari Aguiar</sub>](https://github.com/ariaguiarfilho) |  [<img src="https://media-exp1.licdn.com/dms/image/C4E03AQHOGY2PGnMmng/profile-displayphoto-shrink_200_200/0/1516944394021?e=1671667200&v=beta&t=S4Ib3WhlW-QiXdmh9AB2-E0mu5Vmgdm2IqgECXmamyk" width=115><br><sub>Diego Renan</sub>](https://www.linkedin.com/in/diego-renan-bruno-48194484/) |
| :---: | :---: 

Copyright :copyright: 2022 - Assistente Virtual
