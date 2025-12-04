<h1>Aprendendo Python</h1> 

> O antigo repositório foi apagado, assim, o primeiro commit recupera os arquivos do antigo e adiciona a pasta API.

<p align="center">
  <img src="https://img.shields.io/static/v1?label=python&message=linguagem&color=blue&style=for-the-badge&logo=PYTHON"/>
  <img src="https://img.shields.io/static/v1?label=React&message=Frontend&color=blue&style=for-the-badge&logo=react"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>

> Status do Projeto: :warning: Em Desenvolvimento

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

:small_blue_diamond: [Linguagens, dependências e libs](#linguagens-dependências-e-libs-utilizadas-books)

:small_blue_diamond: [Desenvolvedor](#desenvolvedor-octocat)

:small_blue_diamond: [Referência de Estrutura](#referência-de-estrutura)

## Descrição do projeto 

<p align="justify">
  O projeto é um mosaico de várias funcionalidades que o Python consegue realizar, desde integrações com IA até uma API. Ele foi desenvolvido e elaborado na disciplina de Programação Web III do 3° ano do Curso Técnico em Informática para Internet do Instituto Federal de Ciência, Tecnologia e Educação do Rio Grande do Sul (IFRS) - <i>Campus</i> Bento Gonçalves.

  Assim, a proposta é obter um aprendizado geral sobre as possibilidades e potencialidades de projetos feitos em Python, o que demandou pesquisas em sites e vídeos para estabelecer uma base robusta e achar ideias de projetos a serem feitos.
</p>

## Funcionalidades

:heavy_check_mark: API

:heavy_check_mark: Bot Discord 

:heavy_check_mark: GUI Simples

:heavy_check_mark: Integração com IA

:heavy_check_mark: Jogo "Life"

## Pré-requisitos

:warning: [Python >= 3.12](https://www.python.org/downloads/)

:warning: [Node >= 22.21.1](https://nodejs.org/pt/download)

:warning: [Token - Bot Discord](https://discordapp.com/developers/applications/)

:warning: [Token - Gemini](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br&lang=python)

:warning: [Git](https://git-scm.com/downloads)

## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/Arthur-Sbeghen/Python
```

Abaixo, há uma explicação para cada funcionalidade.

Para rodar a API:
Abra o terminal da pasta ```Api/```
Execute:
```
pip install fastapi "uvicorn[standard]" pydantic google-genai
```

Coloque seu token Gemini no placeholder do ```main.py```: ```client = genai.Client(api_key="Coloque_Aqui")```

Volte ao terminal e execute:
```
uvicorn main:app --reload
cd react
npm i
npm run dev
```
Acesse a URL gerada que funcionará.

Para rodar o Bot de Discord:

Abra o ```bot.py``` da pasta ```Discord/```

Coloque seu token de Bot no placeholder do ```bot.py```: ```bot.run("Aqui")```

Abra o terminal da pasta ```Discord/```

Execute:
```
pip install discord.py
py main.py
```

Para rodar os Fundamentos:

Abra o terminal da pasta ```Fundamentos_Testes```

Execute
```
py fundamentos.py
```
Para rodar o ```fundamentos.py``` e, para o ```input.py```,
```
py input.py
```

Para rodar o GUI:

Abra o terminal da pasta ```GUI/```

Execute:
```
python app_gui.py
```

Para rodar a IA:

Abra o arquivo ```helper_functions.py``` da pasta ```IA/```

Coloque seu token Gemini no placeholder dele: ```client = genai.Client(api_key="Coloque_Aqui")```

Abra o arquivo ```teste.py``` da mesma pasta

Altere o placeholder de ```print_llm_response("Coloque aqui o que você deseja da IA")```

Abra o terminal da pasta ```IA/```

Execute:
```
pip install google-genai
py teste.py
```

Para rodar o jogo Life:

Abra o terminal da pasta ```Life/```

Execute:
```
pip install numpy matplotlib
```
Depois:
```
py main.py
```
OU
```
py main.py --tamanho-grade 128 --intervalo 500 --planador
```


## Linguagens, dependências e libs utilizadas :books:

- [Python](https://www.python.org/downloads/)
- [React](https://react.dev/)

### Dependências Python:
- Univicorn
- Fastapi
- Pydantic
- Discord
- Google-genai
- Numpy
- Matplotlib


## Desenvolvedor :octocat:

Arthur Vitório Sbeghen

2025 - Aprendendo Python

## Referência de Estrutura

Modelo de documentação baseado neste [template](https://gist.github.com/reginadiana/e044fe93ed81aa04a10361cb841c0409).
