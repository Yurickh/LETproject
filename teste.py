from base_unit import *

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
