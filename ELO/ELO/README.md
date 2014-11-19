# LETProject.ELO.ELO

## Função

Pasta que contém os arquivos que são comuns a todos os módulos, assim como as pastas de template, static e media.
São arquivos responsáveis, em geral, pelo controle do fluxo e a organização intermodular.

## Conteúdo

Entradas em negrito indicam pastas, entradas normais indicam arquivos isolados.

* __init__.py
* BaseUnit.py
* **database**
* EntityUnit.py
* **lang**
* MainUnit.py
* **media**
* models.py
* settings.py
* **static**
* **templates**
* **Trash**
* urls.py
* wsgi.py

### __init__.py

Arquivo requisitado pelo python para reconhecer a pasta como um repositório de arquivos referenciável.
Em outras palavras, é um arquivo que só é útil para a linguagem e deve ser ignorado em outras instâncias.

### BaseUnit.py

Arquivo que contém os tipos básicos do sistema.
Um tipo básico é a unidade mínima de dado do programa (e.g. Nome, Senha, Matrícula e afins). 
É o tipo básico quem executa a validação dos dados recebidos e/ou enviados; isso quer dizer que só é possível criar um Nome, se ele atender aos requisitos dados para tal, ou seja, ser uma sequência de caracteres alfanuméricos de até 32 caracteres. Caso tais requisitos não sejam atendidos, o tipo básico não será criado e uma exceção do tipo ValueError será lançada.

### database

Pasta responsável pelo armazenamento do banco de dados.
Contém o arquivo binário correspondente ao banco de dados e um arquivo SQL que corresponde ao DUMP da última versão daquele. Vale salientar que o GIT somente irá armazenar e atualizar este último.

### EntityUnit.py

Arquivo que contém as entidades do sistema.
Uma entidade é uma classe que só possui tipos básicos por atributos. Ela é responsável por armazenar a validar os dados de todas as entidades do sistema (e.g. Aluno, Professor, Administrador, Curso etc).
Analogamente a um Tipo Básico, só é possível criar uma entidade no caso de todos os seus atributos serem válidos. Esse tipo de assertiva garante que somente sobreviverão dentro do sistema entidades com todos os tipos básicos válidos.

### lang

Pasta que contém os arquivos-dicionário e o arquivo de configuração de linguagem.
Esta pasta é a responsável por converter todo o texto do programa para diferentes línguas.

### MainUnit.py

Arquivo de montagem dos módulos do programa.
Contém procedimentos de inicialização do programa e a classe Factory.
Esta classe tem a responsabilidade de administrar o fluxo intermodular, ou seja, é ela quem monta e desmonta as camadas de um mesmo módulo de forma a viabilizar o tráfego entre eles.

### media

Pasta que contém os arquivos de media do sistema.
É ela quem contém os dados de upload dos usuários, como os avatares dos alunos ou os vídeos dos professores.

### models.py

Arquivo que contém as definições dos modelos do programa.
Este arquivo é o responsável por modelar as tabelas do banco de dados de forma a viabilizar as consultas das camadas de persistência.
Note que aqui utilizamos a filosofia de triplestore em detrimento da organização relacional.

### settings.py

Arquivo de configuração do Django.
Será a primeira coisa a desaparecer após a publicação do sistema, por conter alguns dados de segurança.

### static

Pasta que contém os arquivos estáticos do sistema.
Arquivos CSS e Javascript são armazenados aqui para simplificar a busca por eles. Diferentemente dos templates, os arquivos estáticos nem sempre são carregados, sendo guardados preferencialmente no cache do navegador.

### templates

Pasta que contém os templates do sistema.
Os templates são os arquivos HTML que serão manipulados pelos módulos e corresponderão as páginas vistas pelo usuário do sistema.

### urls.py

Arquivo conhecido como URLConf. Ele é o guia da Factory (ver MainUnit.py), apontando-a para a direção correta, baseando-se na URL que lhe foi passada.
É o primeiro arquivo a ser chamado, sendo o primeiro divisor de águas no fluxo do programa.

### wsgi.py

Arquivo do Django que configura o Web-Server. Não deve ser modificado por hora.