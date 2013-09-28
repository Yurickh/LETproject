from base_unit import *

""" TESTE DO PASSWORD"""
pw = raw_input("password: ")
try:
	pw = Password(pw)
except ValueError as exc:
	print exc
else:
	print pw.getValue()
	try:
		pw.setValue(raw_input("again, please: "))
	except ValueError as exc2:
		print exc2
	else:
		print pw.getValue()

""" TESTE DA MATRICULA
matricula = int(raw_input("Matricula: "))
try:
	matricula = Matric(matricula)
except ValueError as exc:
	print exc
else:
	print matricula.getValue()
	try:
		matricula.setValue(int(raw_input("again, please: ")))
	except ValueError as exc2:
		print exc2
	else:
		print matricula.getValue()
"""
