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

Orientador:
**Professor Cláudio Correa e Castro Gonçalves**

Unidade Acadêmica / Departamento:
**Instituto de Letras/IL - Departamento de Línguas Estrangeiras e Tradução/LET**

Alunos Envolvidos:
* Yurick Hauschild Caetano da Costa 12/0024136
* André Accioly Lima 12/0059908
* Diego Santos da Silva 11/0027892

### 3. Documentação

Toda a documentação do projeto pode ser encontrada na pasta doc/.

> **ATENÇÃO**:
> A documentação acima referenciada inclui explanações das funções de
> todas as classes e métodos implementados e tem por público alvo
> principalmente desenvolvedores interessados em contribuir com o projeto.

> Para uma versão específica para usuários, ou seja, pessoas que estão interessadas no funcionamento da ferramenta e não em seus mecanismos, leia o ponto *4. Instalação e execução*

#### 3.i. Doxyfile (html)

 No intuito de simplificar a navegação dentro da documentação do projeto, utilizamos a ferramenta Doxygen, gerando, assim, um arquivo HTML que contém uma interface amigável.
 Este arquivo está contido em doc/html/ e para acessá-lo basta abrir o arquivo doc/html/index.html com o seu navegador.
 
### 4. Instalação e execução

Para executar o programa, siga as instruções abaixo.

1. Baixe o código fonte do projeto.
  Para isso, basta clicar no botão "Download ZIP" ao lado deste arquivo, como na imagem abaixo.  
![example1](http://i.imgur.com/kJtzWwf.jpg)

2. Para instalar o python no Windows:


3. Para instalar o python no Linux:
> OBS: As últimas versões do Ubuntu e Fedora já vêm com o python 2.7 e as últimas versões do RHEL e CentOS já vêm com o python 2.6.

[BAIXE O PYTHON SCRIPT AQUI, E EXECUTE](http://python-distribute.org/distribute_setup.py). Para executar, use no terminal `python distributte_setup.py`
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
  * Baixe [Download Django-1.6.2.tar.gz](https://www.djangoproject.com/download/1.6.2/tarball/). Então extraia o arquivo, inicie o DOS
 shell com permissão de administrador e execute o comando no diretório cujo nome inicie com "Django-":
	`$ python setup.py install`

5. Para instalar django no Ubuntu:
  * Pelo pip:
	`$ pip install Django==1.6.2`
  * "Manualmente":
	* Baixe [Download Django-1.6.2.tar.gz](https://www.djangoproject.com/download/1.6.2/tarball/). Então:
		`$ tar xzvf Django-1.6.2.tar.gz`
		`$ cd Django-1.6.2`
		`$ sudo python setup.py install`
