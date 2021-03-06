# LETproject

## Index

1. Definição
2. Dados do projeto
3. Documentação
  3.1. Doxygen (html)
4. Instalação e execução
5. Metas de desenvolvimento
6. Log de Atividades

## Conteúdo

### 1. Definição

O LETproject é uma iniciativa do laboratório do LET para o desenvolvimento de uma plataforma de ensino de línguas online.
Seu principal objetivo é criar uma interface amigável entre alunos e professores de forma a incluir o estudo doméstico de línguas no mundo informatizado.

### 2. Dados do projeto

Título do projeto:
* **LETproject (nome temporário)**
* **ELO (Ensino de Línguas Online) (nome temporário)**
* **SALiE (nome final)**

Orientador:
**Professor Cláudio Correa e Castro Gonçalves**

Unidade Acadêmica / Departamento:
**Instituto de Letras/IL - Departamento de Línguas Estrangeiras e Tradução/LET**

Alunos Envolvidos:
* Yurick Hauschild Caetano da Costa 12/0024136
* Dayanne Fernandes 13/0107191

### 3. Documentação

Toda a documentação do projeto pode ser encontrada na pasta doc/.

> **ATENÇÃO**:
> A documentação acima referenciada inclui explanações das funções de
> todas as classes e métodos implementados e tem por público alvo
> principalmente desenvolvedores interessados em contribuir com o projeto.

> Para uma versão específica para usuários, ou seja, pessoas que estão interessadas no funcionamento da ferramenta e não em seus mecanismos, leia o ponto *4. Instalação e execução*

#### 3.i. Doxyfile (html)

 No intuito de simplificar a navegação dentro da documentação do projeto, utilizamos a ferramenta Doxygen, gerando, assim, um arquivo HTML que contém uma interface amigável, bem como um arquivo .tex capaz de gerar um pdf.
 Tanto o pdf quanto o html possuem as mesmas informações.
 Estes arquivos estão contidos em vendor e para acessá-los basta abrir o arquivo doc/html/index.html ou doc/latex/refman.pdf com o seu navegador ou visualizador de pdf, respectivamente.
 
### 4. Instalação e execução

Para executar o programa, siga as instruções abaixo.

1. Baixe o código fonte do projeto.
  Para isso, basta clicar no botão "Download ZIP" ao lado deste arquivo, como na imagem abaixo.  
![example1](http://i.imgur.com/kJtzWwf.jpg)

2. Para instalar o python no Windows:

 Obs: Não desenvolvemos a plataforma em Windows, e não temos o hábito de testar neste ambiente. Então, caro usuário da microsoft, na ocasião de encontrar algum bug ocasionado por incompatibilidade, sintá-se convidado a abrir uma issue e nos avisar, para que o corrijamos o mais rápido possível.
 [Siga este tutorial](http://docs.python-guide.org/en/latest/starting/install/win/).

3. Para instalar o python no Linux:
> OBS: As últimas versões do Ubuntu e Fedora já vêm com o python 2.7 e as últimas versões do RHEL e CentOS já vêm com o python 2.6.

  * Instale o pip:
    `$ easy_install pip`
  * Instale o virtualenv:
	`$ pip install virtualenv`
  * Selecione o diretório para a instalação do python e execute o virtualenv.
	`$ virtualenv --distributte venv`
  * Para executar o ambiente, rode:
	`$ source venv/bin/activate`
  * Para sair do ambiente:
	`$ deactivate`

4. Para instalar django no Windows:
  * Baixe [Download Django-1.7.1.tar.gz](https://www.djangoproject.com/download/1.7.1/tarball/). Então extraia o arquivo, inicie o DOS
 shell (ctrl+E, cmd) com permissão de administrador e execute o comando no diretório cujo nome inicie com "Django-":
	`$ python setup.py install`

5. Para instalar django no Ubuntu:
  * Pelo pip:
	`$ pip install Django==1.7`
  * "Manualmente":
	* Baixe [Download Django-1.7.1.tar.gz](https://www.djangoproject.com/download/1.7.1/tarball/). Então:
		`$ tar xzvf Django-1.6.2.tar.gz`
		`$ cd Django-1.6.2`
		`$ sudo python setup.py install`
