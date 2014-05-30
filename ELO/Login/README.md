# LETProject.ELO.Login

## Função

Pasta que contém o módulo de login.
Responsável pelo controle de login e logout dos usuários do sistema. É capaz de validar nomes e senhas.

## Conteúdo

As entradas em negrito indicam pastas, e as normais indicam arquivos isolados.

* __init__.py
* forms.py
* LoginUnit.py

## __init__.py

Arquivo requisitado pelo python para reconhecer a pasta como um repositório de arquivos referenciável.
Em outras palavras, é um arquivo que só é útil para a linguagem e deve ser ignorado em outras instâncias.

## forms.py

Arquivo que contém a definição das classes que modelam os formulários deste módulo.
Neste caso, ele é responsável por modelar a form de login, ou seja, definir as caixas de entrada de nome e senha, sem as quais seria impossível realizar o login.

## LoginUnit.py

Arquivo principal do módulo.
Contém as diferentes camadas, bem como suas devidas interfaces e variadas implementações.
É o arquivo que recebe o controle do programa após a chamada da Factory (ver MainUnit.py dentro de LETProject.ELO.ELO). 
É responsável por se utilizar das classes formulário (ver forms.py) bem como dos outros recursos do programa - como o banco de dados e os cookies - para criar a página que será mostrada para o usuário.
No caso da LoginUnit, ela deve ser responsável por barrar o acesso de usuários não registrados, ou que não consigam inserir a senha.