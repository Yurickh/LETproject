# LETProject.ELO.Course

## Função

Pasta que contém o módulo de curso.
Responsável pela página de exibição de curso, bem como da reconstrução, organização, navegação e execução de páginas de curso e exercícios.

## Conteúdo

As entradas em negrito indicam pastas, e as normais indicam arquivos isolados.

* _init_.py
* forms.py
* CourseUnit.py
* macros.py

## _init_.py

Arquivo requisitado pelo python para reconhecer a pasta como um repositório de arquivos referenciável.
Em outras palavras, é um arquivo que só é útil para a linguagem e deve ser ignorado em outras instâncias.

## forms.py

Arquivo que contém a definição das classes que modelam os formulários deste módulo.
Neste caso, ele é responsável por modelar as forms de lição e dos diferentes tipos de exercícios.

## CourseUnit.py

Arquivo principal do módulo.
Contém as diferentes camadas, bem como suas devidas interfaces e variadas implementações.
É o arquivo que recebe o controle do programa após a chamada da Factory (ver MainUnit.py dentro de LETProject.ELO.ELO). 
É responsável por se utilizar das classes formulário (ver forms.py) bem como dos outros recursos do programa - como o banco de dados e os cookies - para criar a página que será mostrada para o usuário.
No caso da CourseUnit, ela deve ser responsável por administrar o acesso aos cursos, lições e exercícios somente para os usuários autorizados, organizar o histórico e notas dos alunos, bem como manter um log de registro das atividades destes.

## macros.py

Arquivo de macros e wrappers.
Este arquivo contém pequenas constantes e funções anônimas que deverão ser utilizados no decorrer da execução do CourseUnit.