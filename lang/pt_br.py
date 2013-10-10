# coding: utf-8

#Exceptions for the basic types.

EXCEPTION_INV_PW_S = "A senha deve conter no mínimo 6 caracteres."
""" Error message for a password that is too small."""

EXCEPTION_INV_NM_B = "O nome deve conter menos de 32 caracteres."
""" Error message for a name that is too big."""
EXCEPTION_INV_NM_S = "O nome deve conter algum caractere."
""" Error message for a name that is too small."""
EXCEPTION_INV_NM_F = "O nome deve conter apenas caracteres alfanuméricos."
""" Error message for a name that contains non-alphanumeric characters."""

EXCEPTION_INV_MT_B = "O número de matrícula ultrapassou o tamanho máximo permitido."
""" Error message for a matric that is too big."""
EXCEPTION_INV_MT_S = "O número de matrícula digitado é menor do que o mínimo permitido."
""" Error message for a matric that is too small."""
EXCEPTION_INT_MT_F = "Valor inválido para matrícula."
""" Error message for a NaN value. """

EXCEPTION_INV_PT_B = "O texto deve conter no máximo 1024 caracteres."
""" Error message for a Plain Text that is too big."""

EXCEPTION_INV_CP_S = "O número do campus deve ser maior do que 0."
""" Error message for a Campus number that is too small."""
EXCEPTION_INV_CP_F = "Valor inválido para o Campus."
""" Error message for a NaN value. """

EXCEPTION_INV_SX_F = "O caractere de sexo deve ser 'M', 'm', 'f' e 'F'."
""" Error message for a sex that is invalid."""

EXCEPTION_INV_LK_S = "O link deve conter pelo menos um caractere."
""" Error message for a link that is NULL."""
EXCEPTION_INV_LK_F = "O link deve conter apenas caracteres alfanúmericos."
""" Error message for a link that contains non-alphanumeric chars."""

EXCEPTION_INV_ML_S = "O campo e-mail nao pode ser nulo."
""" Error message for a mail that is empty."""
EXCEPTION_INV_ML_F = "O campo e-mail esta escrito no formato incorreto (Mais de um '@', algum espaço ou nenhum ponto)."
""" Error message for a mail that is written in the wrong format."""

EXCEPTION_INV_ET_S = "O id do tipo de exercício deve ser maior que zero."
""" Error message for a exercise type that is smaller or equals than zero."""
EXCEPTION_INV_ET_F = "Tipo de exercício inválido."
""" Error message for a NaN value."""

EXCEPTION_INV_GR_S = "A nota deve ser maior ou igual a zero."
""" Error message for grade that is smaller than zero."""
EXCEPTION_INV_GR_B = "A nota deve ser menor do que cem."
""" Error message for a grade that is bigger than one hundred."""
EXCEPTION_INV_GR_F = "A nota deve ser um valor numérico."
""" Error message for a NaN value."""

EXCEPTION_INV_ID_S = "O campo Id deve ser maior ou igual a 1."
""" Error message for an Id too small."""

EXCEPTION_INV_LG_F = "Idioma invalido."
""" Error message for an inexistent language."""

EXCEPTION_TEST_PREFIX = "Ocorreu um erro:"
""" Prefix used to compose the error message."""
EXCEPTION_TEST_INV_GET = "Ocorreu um erro no metodo getValue."
""" Error message for the getValue error."""

#Exceptions for the entity types.

EXCEPTION_INV_USR_NM = "Nome de usuário inválido."
""" Error message for an invalid username."""
EXCEPTION_INV_USR_PW = "Senha de usuário inválida."
""" Error message for an invalid user's password."""

EXCEPTION_INV_PRF_MT = "Ocorreu um erro na matrícula do professor."
""" Error message for an error with the professor registration number."""
EXCEPTION_INV_PRF_BS = "Ocorreu um erro na biografia do professor."
""" Error message for an error with the professor bios."""
EXCEPTION_INV_PRF_CP = "Ocorreu um erro no campus do professor."
""" Error message for an error with the professor campus."""
EXCEPTION_INV_PRF_CS = "Ocorreu um erro nos cursos do professor. "
""" Error message for an error with the professor courses."""
EXCEPTION_INV_PRF_AV = "Ocorreu um erro no avatar do professor."
""" Error message for an error with the professor avatar."""
EXCEPTION_INV_PRF_SX = "Ocorreu um erro no sexo do professor."
""" Error message for an error with the professor sex."""

EXCEPTION_INV_STU_MT = "Matricula de aluno inválida."
""" Error message for an invalid student's registration number"""
EXCEPTION_INV_STU_BS = "Biografia de aluno inválida."
""" Error message for an invalid students's bios."""
EXCEPTION_INV_STU_CP = "Campus de aluno inválido."
""" Error message for an invalid student's campus"""
EXCEPTION_INV_STU_AV = "Avatar de aluno inválido."
""" Error message for an invalid student's avatar."""
EXCEPTION_INV_STU_SX = "Sexo de aluno inválido."
""" Error message for an invalid student's sex."""
EXCEPTION_INV_STU_ML = "E-mail de aluno inválido."
""" Error message for an invalid email."""
EXCEPTION_INV_STU_GR = "Formato de notas do aluno inválidas."
""" Error message for an invalid student's grades format."""
EXCEPTION_INV_STU_IN = "Interesses do aluno em formato inválido."
""" Error message for the student's interests written in an invalid format."""
EXCEPTION_INV_STU_LN = "O idioma selecionado não existe."
""" Error message for an innexistent selected language."""
