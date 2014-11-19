# LETProject.ELO.Profile

## Função

Pasta que contém o módulo de perfil.
Responsável pelas páginas onde se encontram os dados do usuário, seja ela a Home ou a página de dados detalhados (referenciada internamente como 'perfil completo'). Também permite ao usuário editar seus próprios dados. A uma primeira versão, é inacessível para administradores.

## Conteúdo

As entradas em negrito indicam pastas, e as normais indicam arquivos isolados.

* __init__.py
* forms.py
* ProfileUnit.py

## __init__.py

Arquivo requisitado pelo python para reconhecer a pasta como um repositório de arquivos referenciável.
Em outras palavras, é um arquivo que só é útil para a linguagem e deve ser ignorado em outras instâncias.

## forms.py

Arquivo que contém a definição das classes que modelam os formulários deste módulo.
Neste caso, ele é responsável por modelar as forms de edição de dados de usuário, possbilitando ao usuário comum (estudante ou professor) editar seus dados pessoais, como nome e sexo.

## LoginUnit.py

Arquivo principal do módulo.
Contém as diferentes camadas, bem como suas devidas interfaces e variadas implementações.
É o arquivo que recebe o controle do programa após a chamada da Factory (ver MainUnit.py dentro de LETProject.ELO.ELO). 
É responsável por se utilizar das classes formulário (ver forms.py) bem como dos outros recursos do programa - como o banco de dados e os cookies - para criar a página que será mostrada para o usuário.
No caso da ProfileUnit, ele será responsável por possibilitar a visualização e edição dos dados pessoais - sensíveis ou não - ao usuário comum.