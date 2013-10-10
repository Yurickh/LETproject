# coding: utf-8

#Exceptions for the basic types.

EXCEPTION_INV_PW_S = "The password must be at least 6 characters long."

EXCEPTION_INV_NM_B = "The name must not have more than 32 characters."
EXCEPTION_INV_NM_S = "The name field can't be empty."
EXCEPTION_INV_NM_F = "The name must have only alphanumeric characters."

EXCEPTION_INV_MT_B = "The registration number must be smaller."
EXCEPTION_INV_MT_S = "The registration number is smaller than the minimum acceptable."
EXCEPTION_INT_MT_F = "Invalid value for the regisration number."

EXCEPTION_INV_PT_B = "The text must contain 1024 characters or less."

EXCEPTION_INV_CP_S = "The campus ID must be bigger than 0."
EXCEPTION_INV_CP_F = "Invalid value for the campus ID."

EXCEPTION_INV_SX_F = "The sex character must be 'M', 'm', 'F' or 'f'."

EXCEPTION_INV_LK_S = "The link must contain at least one character."
EXCEPTION_INV_LK_F = "The link must contain only alphanumeric characters."

EXCEPTION_INV_GR_S = "The grade must be at least zero."
EXCEPTION_INV_GR_B = "The grade must be smaller than one hundred."
EXCEPTION_INV_GR_F = "The grade must be a numerical value."

EXCEPTION_INV_ML_S = "The mail field can't be empty."
EXCEPTION_INV_ML_F = "The mail is written in the wrong format."

EXCEPTION_INV_ET_S = "The exercise type must be greater than zero"
EXCEPTION_INV_ET_F = "Invalid exercise type."

EXCEPTION_INV_ID_S = "The Id has to be greater than zero."
EXCEPTION_INV_ID_F = "Invalid value for the ID field."

EXCEPTION_INV_LG_F = "Invalid language."

EXCEPTION_TEST_PREFIX = "An Error has been ocurred."
EXCEPTION_TEST_INV_GET = "An Error has ocurred in the getValue method."

#Exceptions for the entitiy types.

EXCEPTION_INV_USR_NM = "Invalid user name."
EXCEPTION_INV_USR_PW = "Invalid user's password."

EXCEPTION_INV_PRF_MT = "An error has ocurred with the professor's registration number."
EXCEPTION_INV_PRF_BS = "An error has ocurred with the professor's bios."
EXCEPTION_INV_PRF_CP = "An error has ocurred with the professor's campus."
EXCEPTION_INV_PRF_CS = "An error has ocurred with the professor's courses. "
EXCEPTION_INV_PRF_AV = "An error has ocurred with the professor's avatar."
EXCEPTION_INV_PRF_SX = "An error has ocurred with the professor's sex."

EXCEPTION_INV_STU_MT = "Invalid student's registrantion number."
EXCEPTION_INV_STU_BS = "Invalid student's bios."
EXCEPTION_INV_STU_CP = "Invalid student's campus."
EXCEPTION_INV_STU_AV = "Invalid student's avatar."
EXCEPTION_INV_STU_SX = "Invalid student's sex."
EXCEPTION_INV_STU_ML = "Invalid student's mail."
EXCEPTION_INV_STU_GR = "Student's grades is in an invalid format."
EXCEPTION_INV_STU_IN = "Student's interests is in an invalid format."
EXCEPTION_INV_STU_LN = "The selected language does not exist."
