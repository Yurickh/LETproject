# coding: utf-8

from django.utils.translation import ugettext_lazy as _

from django.conf import settings

## @file Arquivo que carrega as strings que devem ser traduzidas.
#	Aqui ficam todas as macros do sistema. Evite utilizar hard-coded text.

available_langs = dict(settings.LANGUAGES).keys()

DICT = {
	## Mensagem de erro para um password menor que o especificado.
	'EXCEPTION_INV_PW_S' : _(u"A senha deve conter no mínimo 6 caracteres."),
	## Mensagem de erro para um password inválido.
	'EXCEPTION_INV_PW_F' : _(u"Senha inválida."),
	## Mensagem de erro para validação de senha repetida.
	'EXCEPTION_INV_PW_R' : _(u"As senhas inseridas não batem."),

	## Mensagem de erro para um nome maior do que o especificado.
	'EXCEPTION_INV_NM_B' : _(u"O nome deve conter menos de 32 caracteres."),
	## Mensagem de erro para um nome menor que o especificado.
	'EXCEPTION_INV_NM_S' : _(u"O nome deve conter algum caractere."),
	## Mensagem de erro para um nome que contém caracteres não alfanuméricos.
	'EXCEPTION_INV_NM_F' : _(u"O nome deve conter apenas caracteres alfanuméricos."),

	## Mensagem de erro para uma matric maior que o especificado.
	'EXCEPTION_INV_MT_B' : _(u"O número de matrícula ultrapassou o tamanho máximo permitido."),
	## Mensagem de erro para uma matric menor que o especificado.
	'EXCEPTION_INV_MT_S' : _(u"O número de matrícula digitado é menor do que o mínimo permitido."),
	## Mensagem de erro para uma matric com conteúdo não numérico.
	'EXCEPTION_INT_MT_F' : _(u"Valor inválido para matrícula."),

	## Mensagem de erro para um texto maior que o especificado.
	'EXCEPTION_INV_PT_B' : _(u"O texto deve conter no máximo 1024 caracteres."),

	## Mensagem de erro para um número de campus menor que o especificado.
	'EXCEPTION_INV_CP_S' : _(u"O número do campus deve ser maior do que 0."),
	## Mensagem de erro para um valor de campus não numérico.
	'EXCEPTION_INV_CP_F' : _(u"Valor inválido para o Campus."),

	## Mensagem de erro para um valor de sexo inválido.
	'EXCEPTION_INV_SX_F' : _(u"O caractere de sexo deve ser 'M', 'm', 'f' e 'F'."),

	## Mensagem de erro para um link que é NULL.
	'EXCEPTION_INV_LK_S' : _(u"O link deve conter pelo menos um caractere."),
	## Mensagem de erro para um link que contém caracteres não alfanuéricos.
	'EXCEPTION_INV_LK_F' : _(u"O link deve conter apenas caracteres alfanuméricos."),

	## Mensagem de erro para um mail vazio.
	'EXCEPTION_INV_ML_S' : _(u"O campo e-mail nao pode ser nulo."),
	## Mensagem de erro para para um mail escrito no formato incrreto.
	'EXCEPTION_INV_ML_F' : _(u"O campo e-mail esta escrito no formato incorreto (Mais de um '@', algum espaço ou nenhum ponto)."),

	## Mensagem de erro para um tipo de exercício manor que o especificado ou igual a zero.
	'EXCEPTION_INV_ET_S' : _(u"O id do tipo de exercício deve ser maior que zero."),
	## Mensagem de erro para um valor não numérico.
	'EXCEPTION_INV_ET_F' : _(u"Tipo de exercício inválido."),

	## Mensagem de erro para uma nota negativa.
	'EXCEPTION_INV_GR_S' : _(u"A nota deve ser maior ou igual a zero."),
	## Mensagem de erro para uma nota maior que 100.
	'EXCEPTION_INV_GR_B' : _(u"A nota deve ser menor do que cem."),
	## Mensagem de erro para uma nota com valor não numérico.
	'EXCEPTION_INV_GR_F' : _(u"A nota deve ser um valor numérico."),

	## Mensagem de erro para um número de Id muito baixo.
	'EXCEPTION_INV_ID_S' : _(u"O campo Id deve ser maior ou igual a 1."),
	## Mensagem de erro para um valor de Id inválido.
	'EXCEPTION_INV_ID_F' : _(u"Valor inválido para o campo ID."),

	## Mensagem de erro para um idioma inexistente.
	'EXCEPTION_INV_LG_F' : _(u"Idioma inválido."),

	## Mensagem de erro para
	'EXCEPTION_INV_DT_D' : _(u"Dia inválido."),
	## Mensagem de erro para
	'EXCEPTION_INV_DT_M' : _(u"Mês inválido."),
	## Mensagem de erro para
	'EXCEPTION_INV_DT_Y' : _(u"Ano inválido."),

	## Prefixo usado para compor mensagens de erro.
	'EXCEPTION_TEST_PREFIX' : _(u"Ocorreu um erro:"),
	## Mensagem de erro para erro no getValue.
	'EXCEPTION_TEST_INV_GET' : _(u"Ocorreu um erro no método getValue."),

	# Excessões para os tipos de entidades.

	## Mensagem de erro para um username inválido.
	'EXCEPTION_INV_USR_NM' : _(u"Nome de usuário inválido."),
	## Mensagem de erro para um password inválido.
	'EXCEPTION_INV_USR_PW' : _(u"Senha de usuário inválida."),

	## Mensagem de erro para um erro com o número de registro (matric) do professor.
	'EXCEPTION_INV_PRF_MT' : _(u"Ocorreu um erro na matrícula do professor."),
	## Mensagem de erro para um erro na biografia do professor.
	'EXCEPTION_INV_PRF_BS' : _(u"Ocorreu um erro na biografia do professor."),
	## Mensagem de erro para um erro com o campus do professor.
	'EXCEPTION_INV_PRF_CP' : _(u"Ocorreu um erro no campus do professor."),
	## Mensagem de erro para um erro com os cursos do professor.
	'EXCEPTION_INV_PRF_CS' : _(u"Ocorreu um erro nos cursos do professor."),
	## Mensagem de erro para um erro com o avatar do professor.
	'EXCEPTION_INV_PRF_AV' : _(u"Ocorreu um erro no avatar do professor."),
	## Mensagem de erro para um erro com o sexo do professor.
	'EXCEPTION_INV_PRF_SX' : _(u"Ocorreu um erro no sexo do professor."),
	## Mensagem de erro para um e-mail de professor inválido
	'EXCEPTION_INV_PRF_ML' : _(u"E-mail de professor inválido."),

	## Mensagem de erro para um número de registro de estudante (matric) inválido.
	'EXCEPTION_INV_STU_MT' : _(u"Matricula de aluno inválida."),
	## Mensagem de erro para uma biografia de estudante inválida.
	'EXCEPTION_INV_STU_BS' : _(u"Biografia de aluno inválida."),
	## Mensagem de erro para um vampus de estudante inválido.
	'EXCEPTION_INV_STU_CP' : _(u"Campus de aluno inválido."),
	## Mensagem de erro para um curso de estudante inválido
	'EXCEPTION_INV_STU_CO' : _(u"Campo curso de aluno inválido."),
	## Mensagem de erro para um avatar de estudante inválido.
	'EXCEPTION_INV_STU_AV' : _(u"Avatar de aluno inválido."),
	## Mensagem de erro para um sexo de estudante inválido.
	'EXCEPTION_INV_STU_SX' : _(u"Sexo de aluno inválido."),
	## Mensagem de erro para um e-mail de aluno inválido
	'EXCEPTION_INV_STU_ML' : _(u"E-mail de aluno inválido."),
	## Mensagem de erro para notas de estudante em formato inválido.
	'EXCEPTION_INV_STU_GR' : _(u"Formato de notas do aluno inválidas."),
	## Mensagem de erro para interesses de estudante escritos em formato inválido.
	'EXCEPTION_INV_STU_IN' : _(u"Interesses do aluno em formato inválido."),
	## Mensagem de erro para um idioma selecionado inexistente.
	'EXCEPTION_INV_STU_LN' : _(u"O idioma selecionado não existe."),

	## Mensagem de erro para um nome de curso inválido.
	'EXCEPTION_INV_CRS_NM' : _(u"Nome do curso inválido."),
	## Mensagem de erro para um Id de curso inválido.
	'EXCEPTION_INV_CRS_ID' : _(u"Id do curso inválido."),
	## Mensagem de erro para um curso de estudante inválido.
	'EXCEPTION_INV_CRS_ST' : _(u"Aluno(s) do curso inválido(s)."),
	## Mensagem de erro para um módulo de curso inválido.
	'EXCEPTION_INV_CRS_MD' : _(u"Módulo(s) do curso inválido(s)."),

	## Mensagem de erro para um nome de módulo inválido.
	'EXCEPTION_INV_MD_NM' : _(u"Nome de módulo inválido."),
	## Mensagem de erro para um Id de módulo inválido.
	'EXCEPTION_INV_MD_ID' : _(u"Id do módulo inválido."),
	## Mensagem de erro para um tipo de lição inválido.
	'EXCEPTION_INV_MD_LT' : _(u"Tipo de lição inválido."),

	## Mensagem de erro para um nome de lição inválido.
	'EXCEPTION_INV_LS_NM' : _(u"Nome da lição inválido."),
	## Mensagem de erro para um Id de lição inválido.
	'EXCEPTION_INV_LS_ID' : _(u"Id da lição inválido."),
	## Mensagem de erro para um link de lição inválido.
	'EXCEPTION_INV_LS_LK' : _(u"Link da lição inválido."),
	## Mensagem de erro para um tipo de exercício inválido.
	'EXCEPTION_INV_LS_ST' : _(u"Tipo de exercício da lição inválido."),

	## Mensagem de erro para um Id de exercício inválido.
	'EXCEPTION_INV_EX_ID' : _(u"Id do exercício inválido."),
	## Mensagem de erro para um link de exercício inválido.
	'EXCEPTION_INV_EX_LK' : _(u"Link do exercício inválido."),
	## Mensagem de erro para um tipo de exercício inválido.
	'EXCEPTION_INV_EX_ET' : _(u"Tipo do exercício inválido."),
	## Mensagem de erro para um formato de exercício inválido.
	'EXCEPTION_INV_EX_FT' : _(u"Formato do exercicio inválido."),
	## Mensagem de erro para itens de exercício inválidos.
	'EXCEPTION_INV_EX_IT' : _(u"Itens do exercício inválidos."),


	## Mensagem de erro para login inválido.
	'EXCEPTION_INV_LOG' : _(u"Login ou senha inválidos."),

	## Mensagem de erro para dados de form incorretos.
	'EXCEPTION_INV_FRM' : _(u"Dados incorretos"),

	## Mensagem de erro para requisição de lição forjada.
	'EXCEPTION_INV_LES' : _(u"Id de lição inválido"),

	## Mensagem de erro padrão 403
	'EXCEPTION_403_STD' : _(u"Permissão de acesso negada."),
	## Mensagem de erro inesperado 404
	'EXCEPTION_404_ERR' : _(u"Ocorreu um erro inesperado. Favor tentar novamente."),

	## Mensagem de erro de update em banco de dados
	'EXCEPTION_ERR_DB_U': _(u"Ocorreu um erro ao salvar seu dado. Favor tentar novamente."),

	## Mensagem de erro para Lição não disponível
	'EXCEPTION_INV_LS_W': _(u"A lição requisitada não está disponível."),

	## Mensagem de erro de formulário
	'ERROR_FORM'  : _(u"Ocorreu um problema ao carregar o formulário. Favor tentar novamente mais tarde."),
	
	'ELO_HOME' : _(u'SALiE - Página Inicial'),
	'ELO_PROFILE' : _(u'SALiE - Perfil'),
	'ELO_ADM': _(u'SALiE - Administração'),
	'ELO_COURSE': _(u'SALiE - Cursos'),

	'LANGUAGE': _(u'Linguagem'),
	'ENGLISH': _(u'Inglês'),
	'PORTUGUESE': _(u'Português'),

	'SEX': _(u'Sexo'),
	'SEX_MALE': _(u'Masculino'),
	'SEX_FEMALE': _(u'Feminino'),

	'USERNAME' : _(u'Usuário:'),
	'PASSWORD' : _(u'Senha:'),
	'MATRIC': _(u'Matrícula'),
	'BIOS' : _(u'Biografia'),
	'INTERESTS': _(u'Interesses'),
	'NAME': _(u'Nome'),
	'EMAIL': _(u'Email'),
	'AVATAR': _(u'Avatar'),
	'CAMPUS': _(u'Campus'),

	'HOME' : _(u'Principal'),
	'MENU' : _(u'Menu'),
	'LOGIN' : _(u'Entrar'),
	'LOGOUT' : _(u'Sair'),
	'PROFILE' : _(u'Perfil'),
	'ELO' : _(u'SALiE'),

	'STUDENT' : _(u'Aluno'),
	'COURSE' : _(u'Curso'),
	'PROFESSOR' : _(u'Professor'),

	'SUBMIT' : _(u'Atualizar'), 
	'REGISTER' : _(u'Cadastrar'),
	'SEARCH' : _(u'Procurar'),
	'DEL' : _(u'Deletar'),

	'REGISTER_STUDENT' : _(u'Registrar Novo Aluno'),
	'SUBMIT_STUDENT' : _(u'Atualizar dados de Aluno'),
	'DEL_STUDENT' : _(u'Apagar Registro de Aluno'),
	
	'REGISTER_COURSE' : _(u'Registrar Novo Curso'),
	'SUBMIT_COURSE' : _(u'Atualizar dados de Curso'),
	'DEL_COURSE' : _(u'Apagar Registro de Curso'),
	
	'REGISTER_PROFESSOR' : _(u'Registrar Novo Professor'),
	'SUBMIT_PROFESSOR' : _(u'Atualizar dados de Professor'),
	'DEL_PROFESSOR' : _(u'Apagar Registro de Professor'),
}
