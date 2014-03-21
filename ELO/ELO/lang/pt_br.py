# coding: utf-8

## @package Lingua Português
#Contem as macros para textos em Português
# Excessões para os tipos básicos.
#

DICT = {
	## Mensagem de erro para um password menor que o especificado.
	'EXCEPTION_INV_PW_S' : "A senha deve conter no mínimo 6 caracteres.",

	## Mensagem de erro para um nome maior do que o especificado.
	'EXCEPTION_INV_NM_B' : "O nome deve conter menos de 32 caracteres.",
	## Mensagem de erro para um nome menor que o especificado.
	'EXCEPTION_INV_NM_S' : "O nome deve conter algum caractere.",
	## Mensagem de erro para um nome que contém caracteres não alfanuméricos.
	'EXCEPTION_INV_NM_F' : "O nome deve conter apenas caracteres alfanuméricos.",

	## Mensagem de erro para uma matric maior que o especificado.
	'EXCEPTION_INV_MT_B' : "O número de matrícula ultrapassou o tamanho máximo permitido.",
	## Mensagem de erro para uma matric menor que o especificado.
	'EXCEPTION_INV_MT_S' : "O número de matrícula digitado é menor do que o mínimo permitido.",
	## Mensagem de erro para uma matric com conteúdo não numérico.
	'EXCEPTION_INT_MT_F' : "Valor inválido para matrícula.",

	## Mensagem de erro para um texto maior que o especificado.
	'EXCEPTION_INV_PT_B' : "O texto deve conter no máximo 1024 caracteres.",

	## Mensagem de erro para um número de campus menor que o especificado.
	'EXCEPTION_INV_CP_S' : "O número do campus deve ser maior do que 0.",
	## Mensagem de erro para um valor de campus não numérico.
	'EXCEPTION_INV_CP_F' : "Valor inválido para o Campus.",

	## Mensagem de erro para um valor de sexo inválido.
	'EXCEPTION_INV_SX_F' : "O caractere de sexo deve ser 'M', 'm', 'f' e 'F'.",

	## Mensagem de erro para um link que é NULL.
	'EXCEPTION_INV_LK_S' : "O link deve conter pelo menos um caractere.",
	## Mensagem de erro para um link que contém caracteres não alfanuéricos.
	'EXCEPTION_INV_LK_F' : "O link deve conter apenas caracteres alfanuméricos.",

	## Mensagem de erro para um mail vazio.
	'EXCEPTION_INV_ML_S' : "O campo e-mail nao pode ser nulo.",
	## Mensagem de erro para para um mail escrito no formato incrreto.
	'EXCEPTION_INV_ML_F' : "O campo e-mail esta escrito no formato incorreto (Mais de um '@', algum espaço ou nenhum ponto).",

	## Mensagem de erro para um tipo de exercício manor que o especificado ou igual a zero.
	'EXCEPTION_INV_ET_S' : "O id do tipo de exercício deve ser maior que zero.",
	## Mensagem de erro para um valor não numérico.
	'EXCEPTION_INV_ET_F' : "Tipo de exercício inválido.",

	## Mensagem de erro para uma nota negativa.
	'EXCEPTION_INV_GR_S' : "A nota deve ser maior ou igual a zero.",
	## Mensagem de erro para uma nota maior que 100.
	'EXCEPTION_INV_GR_B' : "A nota deve ser menor do que cem.",
	## Mensagem de erro para uma nota com valor não numérico.
	'EXCEPTION_INV_GR_F' : "A nota deve ser um valor numérico.",

	## Mensagem de erro para um número de Id muito baixo.
	'EXCEPTION_INV_ID_S' : "O campo Id deve ser maior ou igual a 1.",
	## Mensagem de erro para um valor de Id inválido.
	'EXCEPTION_INV_ID_F' : "Valor inválido para o campo ID.",

	## Mensagem de erro para um idioma inexistente.
	'EXCEPTION_INV_LG_F' : "Idioma inválido.",

	## Mensagem de erro para
	'EXCEPTION_INV_DT_D' : "Dia inválido.",
	## Mensagem de erro para
	'EXCEPTION_INV_DT_M' : "Mês inválido.",
	## Mensagem de erro para
	'EXCEPTION_INV_DT_Y' : "Ano inválido.",

	## Prefixo usado para compor mensagens de erro.
	'EXCEPTION_TEST_PREFIX' : "Ocorreu um erro:",
	## Mensagem de erro para erro no getValue.
	'EXCEPTION_TEST_INV_GET' : "Ocorreu um erro no método getValue.",

	# Excessões para os tipos de entidades.

	## Mensagem de erro para um username inválido.
	'EXCEPTION_INV_USR_NM' : "Nome de usuário inválido.",
	## Mensagem de erro para um password inválido.
	'EXCEPTION_INV_USR_PW' : "Senha de usuário inválida.",

	## Mensagem de erro para um erro com o número de registro (matric) do professor.
	'EXCEPTION_INV_PRF_MT' : "Ocorreu um erro na matrícula do professor.",
	## Mensagem de erro para um erro na biografia do professor.
	'EXCEPTION_INV_PRF_BS' : "Ocorreu um erro na biografia do professor.",
	## Mensagem de erro para um erro com o campus do professor.
	'EXCEPTION_INV_PRF_CP' : "Ocorreu um erro no campus do professor.",
	## Mensagem de erro para um erro com os cursos do professor.
	'EXCEPTION_INV_PRF_CS' : "Ocorreu um erro nos cursos do professor.",
	## Mensagem de erro para um erro com o avatar do professor.
	'EXCEPTION_INV_PRF_AV' : "Ocorreu um erro no avatar do professor.",
	## Mensagem de erro para um erro com o sexo do professor.
	'EXCEPTION_INV_PRF_SX' : "Ocorreu um erro no sexo do professor.",

	## Mensagem de erro para um número de registro de estudante (matric) inválido.
	'EXCEPTION_INV_STU_MT' : "Matricula de aluno inválida.",
	## Mensagem de erro para uma biografia de estudante inválida.
	'EXCEPTION_INV_STU_BS' : "Biografia de aluno inválida.",
	## Mensagem de erro para um vampus de estudante inválido.
	'EXCEPTION_INV_STU_CP' : "Campus de aluno inválido.",
	## Mensagem de erro para um curso de estudante inválido
	'EXCEPTION_INV_STU_CO' : "Campo curso de aluno inválido.",
	## Mensagem de erro para um avatar de estudante inválido.
	'EXCEPTION_INV_STU_AV' : "Avatar de aluno inválido.",
	## Mensagem de erro para um sexo de estudante inválido.
	'EXCEPTION_INV_STU_SX' : "Sexo de aluno inválido.",
	## Mensagem de erro para um e-mail de aluno inválido
	'EXCEPTION_INV_STU_ML' : "E-mail de aluno inválido.",
	## Mensagem de erro para notas de estudante em formato inválido.
	'EXCEPTION_INV_STU_GR' : "Formato de notas do aluno inválidas.",
	## Mensagem de erro para interesses de estudante escritos em formato inválido.
	'EXCEPTION_INV_STU_IN' : "Interesses do aluno em formato inválido.",
	## Mensagem de erro para um idioma selecionado inexistente.
	'EXCEPTION_INV_STU_LN' : "O idioma selecionado não existe.",

	## Mensagem de erro para um nome de curso inválido.
	'EXCEPTION_INV_CRS_NM' : "Nome do curso inválido.",
	## Mensagem de erro para um Id de curso inválido.
	'EXCEPTION_INV_CRS_ID' : "Id do curso inválido.",
	## Mensagem de erro para um curso de estudante inválido.
	'EXCEPTION_INV_CRS_ST' : "Aluno(s) do curso inválido(s).",
	## Mensagem de erro para um módulo de curso inválido.
	'EXCEPTION_INV_CRS_MD' : "Módulo(s) do curso inválido(s).",

	## Mensagem de erro para um nome de módulo inválido.
	'EXCEPTION_INV_MD_NM' : "Nome de módulo inválido.",
	## Mensagem de erro para um Id de módulo inválido.
	'EXCEPTION_INV_MD_ID' : "Id do módulo inválido.",
	## Mensagem de erro para um tipo de lição inválido.
	'EXCEPTION_INV_MD_LT' : "Tipo de lição inválido.",

	## Mensagem de erro para um nome de lição inválido.
	'EXCEPTION_INV_LS_NM' : "Nome da lição inválido.",
	## Mensagem de erro para um Id de lição inválido.
	'EXCEPTION_INV_LS_ID' : "Id da lição inválido.",
	## Mensagem de erro para um link de lição inválido.
	'EXCEPTION_INV_LS_LK' : "Link da lição inválido.",
	## Mensagem de erro para um tipo de exercício inválido.
	'EXCEPTION_INV_LS_ST' : "Tipo de exercício da lição inválido.",

	## Mensagem de erro para um Id de exercício inválido.
	'EXCEPTION_INV_EX_ID' : "Id do exercício inválido.",
	## Mensagem de erro para um link de exercício inválido.
	'EXCEPTION_INV_EX_LK' : "Link do exercício inválido.",
	## Mensagem de erro para um tipo de exercício inválido.
	'EXCEPTION_INV_EX_ET' : "Tipo do exercício inválido.",
	## Mensagem de erro para um formato de exercício inválido.
	'EXCEPTION_INV_EX_FT' : "Formato do exercicio inválido.",
	## Mensagem de erro para itens de exercício inválidos.
	'EXCEPTION_INV_EX_IT' : "Itens do exercício inválidos.",


	## Mensagem de erro para login inválido.
	'EXCEPTION_INV_LOG' : "Login ou senha inválidos.",

	## Mensagem de erro padrão 403
	'EXCEPTION_403_STD' : "Permissão de acesso negada.",
	## Mensagem de erro inesperado 404
	'EXCEPTION_404_ERR' : "Ocorreu um erro inesperado. Favor tentar novamente.",

	'USERNAME' : 'Usuário:',
	'PASSWORD' : 'Senha:',
}
