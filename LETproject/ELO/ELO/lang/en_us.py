# coding: utf-8

## @package Lingua inglês
#Contem as macros para textos em inglês
# Os comentários de cada tipo de excessão está no arquivo pt_br.py
#
## Excessões para tipos básicos.

DICT = {
	'EXCEPTION_INV_PW_S' : "The password must be at least 6 characters long.",

	'EXCEPTION_INV_NM_B' : "The name must not have more than 32 characters.",
	'EXCEPTION_INV_NM_S' : "The name field can't be empty.",
	'EXCEPTION_INV_NM_F' : "The name must have only alphanumeric characters.",

	'EXCEPTION_INV_MT_B' : "The registration number must be smaller.",
	'EXCEPTION_INV_MT_S' : "The registration number is smaller than the minimum acceptable.",
	'EXCEPTION_INT_MT_F' : "Invalid value for the regisration number.",

	'EXCEPTION_INV_PT_B' : "The text must contain 1024 characters or less.",

	'EXCEPTION_INV_CP_S' : "The campus ID must be bigger than 0.",
	'EXCEPTION_INV_CP_F' : "Invalid value for the campus ID.",

	'EXCEPTION_INV_SX_F' : "The sex character must be 'M', 'm', 'F' or 'f'.",

	'EXCEPTION_INV_LK_S' : "The link must contain at least one character.",
	'EXCEPTION_INV_LK_F' : "The link must contain only alphanumeric characters.",

	'EXCEPTION_INV_GR_S' : "The grade must be at least zero.",
	'EXCEPTION_INV_GR_B' : "The grade must be smaller than one hundred.",
	'EXCEPTION_INV_GR_F' : "The grade must be a numerical value.",

	'EXCEPTION_INV_ML_S' : "The mail field can't be empty.",
	'EXCEPTION_INV_ML_F' : "The mail is written in the wrong format.",

	'EXCEPTION_INV_ET_S' : "The exercise type must be greater than zero.",
	'EXCEPTION_INV_ET_F' : "Invalid exercise type.",

	'EXCEPTION_INV_ID_S' : "The Id has to be greater than zero.",
	'EXCEPTION_INV_ID_F' : "Invalid value for the ID field.",

	'EXCEPTION_INV_DT_D' : "Invalid day.",
	'EXCEPTION_INV_DT_M' : "Invalid month.",
	'EXCEPTION_INV_DT_Y' : "Invalid year.",

	'EXCEPTION_INV_LG_F' : "Invalid language.",

	'EXCEPTION_TEST_PREFIX' : "An Error has been ocurred.",
	'EXCEPTION_TEST_INV_GET' : "An Error has ocurred in the getValue method.",

	#Excessões para os tipos de entidades.

	'EXCEPTION_INV_USR_NM' : "Invalid user name.",
	'EXCEPTION_INV_USR_PW' : "Invalid user's password.",

	'EXCEPTION_INV_PRF_MT' : "An error has ocurred with the professor registration number.",
	'EXCEPTION_INV_PRF_BS' : "An error has ocurred with the professor bios.",
	'EXCEPTION_INV_PRF_CP' : "An error has ocurred with the professor campus.",
	'EXCEPTION_INV_PRF_CS' : "An error has ocurred with the professor courses.",
	'EXCEPTION_INV_PRF_AV' : "An error has ocurred with the professor avatar.",
	'EXCEPTION_INV_PRF_SX' : "An error has ocurred with the professor sex.",

	'EXCEPTION_INV_STU_MT' : "Invalid student registrantion number.",
	'EXCEPTION_INV_STU_BS' : "Invalid student bios.",
	'EXCEPTION_INV_STU_CP' : "Invalid student campus.",
	'EXCEPTION_INV_STU_CO' : "Invalid student courses.",
	'EXCEPTION_INV_STU_AV' : "Invalid student avatar.",
	'EXCEPTION_INV_STU_SX' : "Invalid student sex.",
	'EXCEPTION_INV_STU_ML' : "Invalid student mail.",
	'EXCEPTION_INV_STU_GR' : "Student grades is in an invalid format.",
	'EXCEPTION_INV_STU_IN' : "Student interests is in an invalid format.",
	'EXCEPTION_INV_STU_LN' : "The selected language does not exist.",

	'EXCEPTION_INV_CRS_NM' : "Invalid course name.",
	'EXCEPTION_INV_CRS_ID' : "Invalid couse Id.",
	'EXCEPTION_INV_CRS_ST' : "Invalid course students.",
	'EXCEPTION_INV_CRS_MD' : "Invalid course modules.",

	'EXCEPTION_INV_MD_NM' : "Invalid module name.",
	'EXCEPTION_INV_MD_ID' : "invalid module Id.",
	'EXCEPTION_INV_MD_LT' : "Invalid module lesson type.",

	'EXCEPTION_INV_LS_NM' : "Invalid lesson name.",
	'EXCEPTION_INV_LS_ID' : "Invalid lesson Id.",
	'EXCEPTION_INV_LS_LK' : "Invalid lesson link.",
	'EXCEPTION_INV_LS_ST' : "Invalid lesson exercises.",

	'EXCEPTION_INV_EX_ID' : "Invalid exercise Id.",
	'EXCEPTION_INV_EX_LK' : "Invalid exercise link.",
	'EXCEPTION_INV_EX_ET' : "Invalid exercise type.",
	'EXCEPTION_INV_EX_FT' : "Invalid exercise format.",
	'EXCEPTION_INV_EX_IT' : "Invalid exercise items.",

	'EXCEPTION_INV_LOG' : "Incorrect username or password.",

	'EXCEPTION_403_STD' : "Permission denied.",
	'EXCEPTION_404_ERR' : "Unexpected error.",

	'USERNAME': 'Username:',
	'PASSWORD': 'Password:',
}