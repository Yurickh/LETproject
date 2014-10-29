# LETProject.ELO

## Conteúdo

As entradas em negrito indicam pastas, as normais indicam arquivos.

* **Adm**
* **Building**
* **Course**
* **ELO**
* **Login**
* manage.py
* **Profile**

### Adm

Pasta que contém o módulo de administração.
Esta parte do projeto é a responsável pelas páginas do administrador, através das quais ele poderá criar e deletar cursos, bem como matricular e desmatricular alunos ou professores e associar estes.

### Building

Pasta que contém o módulo de contrução de curso.
Esta parte do projeto é a responsável pelas páginas de contrução de curso, visível somente aos professores. Com elas será possível desenvolver conteúdo visualmente interessante e personalizado sem conhecimentos avançados de HTML, CSS ou Javascript.


### Course

Pasta que contém o módulo de visualização de curso.
Cria e organiza as páginas que possibilitam ao aluno acompanhar os cursos, bem como interagir com o professor através de exercícios e talvez comentários.

### ELO

Pasta que contém os arquivos que são comuns a todos os módulos, assim como as pastas de template, static e media.
São arquivos responsáveis, em geral, pelo controle do fluxo e a organização intermodular.

### Login

Pasta que contém o módulo de login.
Responsável pelo controle de login e logout dos usuários do sistema. É capaz de validar nomes e senhas.

### manage.py

Arquivo de controle do Django.
Utilizado para simular um servidor local, bem como rodar versões de debug do python e outros utilitários para desenvolvimento.

### Profile

Pasta que contém o módulo de perfil.
Responsável pelas páginas onde se encontram os dados do usuário, seja ela a Home ou a página de dados detalhados (referenciada internamente como 'perfil completo'). Também permite ao usuário editar seus próprios dados. A uma primeira versão, é inacessível para administradores.
