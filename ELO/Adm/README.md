# LETProject.ELO.Adm

## Função

Pasta que contém o módulo de administração.
Esta parte do projeto é a responsável pelas páginas do administrador, através das quais ele poderá criar e deletar cursos, bem como matricular e desmatricular alunos ou professores e associar estes.

## Conteúdo

As entradas em negrito indicam pastas, e as normais indicam arquivos isolados.

* __init__.py
* forms.py
* AdmUnit.py

## __init__.py

Arquivo requisitado pelo python para reconhecer a pasta como um repositório de arquivos referenciável.
Em outras palavras, é um arquivo que só é útil para a linguagem e deve ser ignorado em outras instâncias.

## forms.py

Arquivo que contém a definição das classes que modelam os formulários deste módulo.
Neste caso, ele é responsável por modelar os forms de registro de dados de um Estudante ou Professor, como dados de Nome, Matrícula, Campus, Sexo, E-mail e Senha, e de Cursos que é requisitado um Código do Curso, Nome e o Professor Responsável. Forms de deleção e edição de contas também são modelados neste arquivo, sendo este primeiramente coordenado com um form de procura da identidade da conta, sendo matrícula para Estudantes e Professores e para os Cursos é requisitado o código referente. E para que ocorra qualquer ação citada acima será necessário a confirmação de senha de administrador que também é distribuído em um form à parte.

## AdmUnit.py

Arquivo principal do módulo.
Contém as diferentes camadas, bem como suas devidas interfaces e variadas implementações.
É o arquivo que é responsável pelo controle do sistema pelo Administrador, criando, editando e deletando contas de Estudantes e Professores, e realizando a criação e deleção de Cursos. Neste arquivo é implementado métodos que interagem com a Factory (ver MainUnit.py dentro de LETProject.ELO.ELO) para o controle geral, classes que importam os formulários para inserção de dados no sistema, comunicação com banco de dados para estas alterações e cookies para atualização das contas que foram alteradas.
Observação: O Administrador não é capaz de editar um curso, somente o Professor responsável poderá editá-lo.
