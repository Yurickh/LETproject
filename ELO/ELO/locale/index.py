# coding: utf-8

from django.utils.translation import ugettext_noop as _

from django.conf import settings

## @file Arquivo que carrega as strings que devem ser traduzidas.

available_langs = dict(settings.LANGUAGES).keys()

DICT = {
	## Mensagem de erro para um password menor que o especificado.
	'EXCEPTION_INV_PW_S' : _("A senha deve conter no mínimo 6 caracteres."),

	## Mensagem de erro para um nome maior do que o especificado.
	'EXCEPTION_INV_NM_B' : _("O nome deve conter menos de 32 caracteres."),
	## Mensagem de erro para um nome menor que o especificado.
	'EXCEPTION_INV_NM_S' : _("O nome deve conter algum caractere."),
	## Mensagem de erro para um nome que contém caracteres não alfanuméricos.
	'EXCEPTION_INV_NM_F' : _("O nome deve conter apenas caracteres alfanuméricos."),

	## Mensagem de erro para uma matric maior que o especificado.
	'EXCEPTION_INV_MT_B' : _("O número de matrícula ultrapassou o tamanho máximo permitido."),
	## Mensagem de erro para uma matric menor que o especificado.
	'EXCEPTION_INV_MT_S' : _("O número de matrícula digitado é menor do que o mínimo permitido."),
	## Mensagem de erro para uma matric com conteúdo não numérico.
	'EXCEPTION_INT_MT_F' : _("Valor inválido para matrícula."),

	## Mensagem de erro para um texto maior que o especificado.
	'EXCEPTION_INV_PT_B' : _("O texto deve conter no máximo 1024 caracteres."),

	## Mensagem de erro para um número de campus menor que o especificado.
	'EXCEPTION_INV_CP_S' : _("O número do campus deve ser maior do que 0."),
	## Mensagem de erro para um valor de campus não numérico.
	'EXCEPTION_INV_CP_F' : _("Valor inválido para o Campus."),

	## Mensagem de erro para um valor de sexo inválido.
	'EXCEPTION_INV_SX_F' : _("O caractere de sexo deve ser 'M', 'm', 'f' e 'F'."),

	## Mensagem de erro para um link que é NULL.
	'EXCEPTION_INV_LK_S' : _("O link deve conter pelo menos um caractere."),
	## Mensagem de erro para um link que contém caracteres não alfanuéricos.
	'EXCEPTION_INV_LK_F' : _("O link deve conter apenas caracteres alfanuméricos."),

	## Mensagem de erro para um mail vazio.
	'EXCEPTION_INV_ML_S' : _("O campo e-mail nao pode ser nulo."),
	## Mensagem de erro para para um mail escrito no formato incrreto.
	'EXCEPTION_INV_ML_F' : _("O campo e-mail esta escrito no formato incorreto (Mais de um '@', algum espaço ou nenhum ponto)."),

	## Mensagem de erro para um tipo de exercício manor que o especificado ou igual a zero.
	'EXCEPTION_INV_ET_S' : _("O id do tipo de exercício deve ser maior que zero."),
	## Mensagem de erro para um valor não numérico.
	'EXCEPTION_INV_ET_F' : _("Tipo de exercício inválido."),

	## Mensagem de erro para uma nota negativa.
	'EXCEPTION_INV_GR_S' : _("A nota deve ser maior ou igual a zero."),
	## Mensagem de erro para uma nota maior que 100.
	'EXCEPTION_INV_GR_B' : _("A nota deve ser menor do que cem."),
	## Mensagem de erro para uma nota com valor não numérico.
	'EXCEPTION_INV_GR_F' : _("A nota deve ser um valor numérico."),

	## Mensagem de erro para um número de Id muito baixo.
	'EXCEPTION_INV_ID_S' : _("O campo Id deve ser maior ou igual a 1."),
	## Mensagem de erro para um valor de Id inválido.
	'EXCEPTION_INV_ID_F' : _("Valor inválido para o campo ID."),

	## Mensagem de erro para um idioma inexistente.
	'EXCEPTION_INV_LG_F' : _("Idioma inválido."),

	## Mensagem de erro para
	'EXCEPTION_INV_DT_D' : _("Dia inválido."),
	## Mensagem de erro para
	'EXCEPTION_INV_DT_M' : _("Mês inválido."),
	## Mensagem de erro para
	'EXCEPTION_INV_DT_Y' : _("Ano inválido."),

	## Prefixo usado para compor mensagens de erro.
	'EXCEPTION_TEST_PREFIX' : _("Ocorreu um erro:"),
	## Mensagem de erro para erro no getValue.
	'EXCEPTION_TEST_INV_GET' : _("Ocorreu um erro no método getValue."),

	# Excessões para os tipos de entidades.

	## Mensagem de erro para um username inválido.
	'EXCEPTION_INV_USR_NM' : _("Nome de usuário inválido."),
	## Mensagem de erro para um password inválido.
	'EXCEPTION_INV_USR_PW' : _("Senha de usuário inválida."),

	## Mensagem de erro para um erro com o número de registro (matric) do professor.
	'EXCEPTION_INV_PRF_MT' : _("Ocorreu um erro na matrícula do professor."),
	## Mensagem de erro para um erro na biografia do professor.
	'EXCEPTION_INV_PRF_BS' : _("Ocorreu um erro na biografia do professor."),
	## Mensagem de erro para um erro com o campus do professor.
	'EXCEPTION_INV_PRF_CP' : _("Ocorreu um erro no campus do professor."),
	## Mensagem de erro para um erro com os cursos do professor.
	'EXCEPTION_INV_PRF_CS' : _("Ocorreu um erro nos cursos do professor."),
	## Mensagem de erro para um erro com o avatar do professor.
	'EXCEPTION_INV_PRF_AV' : _("Ocorreu um erro no avatar do professor."),
	## Mensagem de erro para um erro com o sexo do professor.
	'EXCEPTION_INV_PRF_SX' : _("Ocorreu um erro no sexo do professor."),
	## Mensagem de erro para um e-mail de professor inválido
	'EXCEPTION_INV_PRF_ML' : _("E-mail de professor inválido."),

	## Mensagem de erro para um número de registro de estudante (matric) inválido.
	'EXCEPTION_INV_STU_MT' : _("Matricula de aluno inválida."),
	## Mensagem de erro para uma biografia de estudante inválida.
	'EXCEPTION_INV_STU_BS' : _("Biografia de aluno inválida."),
	## Mensagem de erro para um vampus de estudante inválido.
	'EXCEPTION_INV_STU_CP' : _("Campus de aluno inválido."),
	## Mensagem de erro para um curso de estudante inválido
	'EXCEPTION_INV_STU_CO' : _("Campo curso de aluno inválido."),
	## Mensagem de erro para um avatar de estudante inválido.
	'EXCEPTION_INV_STU_AV' : _("Avatar de aluno inválido."),
	## Mensagem de erro para um sexo de estudante inválido.
	'EXCEPTION_INV_STU_SX' : _("Sexo de aluno inválido."),
	## Mensagem de erro para um e-mail de aluno inválido
	'EXCEPTION_INV_STU_ML' : _("E-mail de aluno inválido."),
	## Mensagem de erro para notas de estudante em formato inválido.
	'EXCEPTION_INV_STU_GR' : _("Formato de notas do aluno inválidas."),
	## Mensagem de erro para interesses de estudante escritos em formato inválido.
	'EXCEPTION_INV_STU_IN' : _("Interesses do aluno em formato inválido."),
	## Mensagem de erro para um idioma selecionado inexistente.
	'EXCEPTION_INV_STU_LN' : _("O idioma selecionado não existe."),

	## Mensagem de erro para um nome de curso inválido.
	'EXCEPTION_INV_CRS_NM' : _("Nome do curso inválido."),
	## Mensagem de erro para um Id de curso inválido.
	'EXCEPTION_INV_CRS_ID' : _("Id do curso inválido."),
	## Mensagem de erro para um curso de estudante inválido.
	'EXCEPTION_INV_CRS_ST' : _("Aluno(s) do curso inválido(s)."),
	## Mensagem de erro para um módulo de curso inválido.
	'EXCEPTION_INV_CRS_MD' : _("Módulo(s) do curso inválido(s)."),

	## Mensagem de erro para um nome de módulo inválido.
	'EXCEPTION_INV_MD_NM' : _("Nome de módulo inválido."),
	## Mensagem de erro para um Id de módulo inválido.
	'EXCEPTION_INV_MD_ID' : _("Id do módulo inválido."),
	## Mensagem de erro para um tipo de lição inválido.
	'EXCEPTION_INV_MD_LT' : _("Tipo de lição inválido."),

	## Mensagem de erro para um nome de lição inválido.
	'EXCEPTION_INV_LS_NM' : _("Nome da lição inválido."),
	## Mensagem de erro para um Id de lição inválido.
	'EXCEPTION_INV_LS_ID' : _("Id da lição inválido."),
	## Mensagem de erro para um link de lição inválido.
	'EXCEPTION_INV_LS_LK' : _("Link da lição inválido."),
	## Mensagem de erro para um tipo de exercício inválido.
	'EXCEPTION_INV_LS_ST' : _("Tipo de exercício da lição inválido."),

	## Mensagem de erro para um Id de exercício inválido.
	'EXCEPTION_INV_EX_ID' : _("Id do exercício inválido."),
	## Mensagem de erro para um link de exercício inválido.
	'EXCEPTION_INV_EX_LK' : _("Link do exercício inválido."),
	## Mensagem de erro para um tipo de exercício inválido.
	'EXCEPTION_INV_EX_ET' : _("Tipo do exercício inválido."),
	## Mensagem de erro para um formato de exercício inválido.
	'EXCEPTION_INV_EX_FT' : _("Formato do exercicio inválido."),
	## Mensagem de erro para itens de exercício inválidos.
	'EXCEPTION_INV_EX_IT' : _("Itens do exercício inválidos."),


	## Mensagem de erro para login inválido.
	'EXCEPTION_INV_LOG' : _("Login ou senha inválidos."),

	## Mensagem de erro para dados de form incorretos.
	'EXCEPTION_INV_FRM' : _("Dados incorretos"),

	## Mensagem de erro padrão 403
	'EXCEPTION_403_STD' : _("Permissão de acesso negada."),
	## Mensagem de erro inesperado 404
	'EXCEPTION_404_ERR' : _("Ocorreu um erro inesperado. Favor tentar novamente."),

	## Mensagem de erro de update em banco de dados
	'EXCEPTION_ERR_DB_U': _("Ocorreu um erro ao salvar seu dado. Favor tentar novamente."),

	## Mensagem de erro de formulário
	'ERROR_FORM'  : _("Ocorreu um problema ao carregar o formulário. Favor tentar novamente mais tarde."),

	'SUBMIT' : _('Atualizar'), 
	'USERNAME' : _('Usuário:'),
	'PASSWORD' : _('Senha:'),
	'ELO_HOME' : _('ELO - Página Inicial'),
	'ELO_PROFILE' : _('ELO - Perfil'),
	'ELO_ADM': _('ELO - Administração'),

	'LANGUAGE': _('Linguagem'),
	'ENGLISH': _('Inglês'),
	'PORTUGUESE': _('Português'),

	'SEX': _('Sexo'),
	'SEX_MALE': _('Masculino'),
	'SEX_FEMALE': _('Feminino'),

	'MATRIC': _('Matrícula'),
	'BIOS' : _('Biografia'),

	'HOME' : _('Principal'),
	'LOGIN' : _('Entrar'),
	'LOGOUT' : _('Sair'),
	'PROFILE' : _('Perfil'),
	'ELO' : _('ELO'),
}
