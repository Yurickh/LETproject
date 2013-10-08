#coding: utf-8

from baseUnit import *

class TestUnit:
	
	def test(self, info, classtype):
		print "------------------------------------------"
		print "Testing " + str(info) + " into an " + str(classtype)
		print "------------------------------------------"

		classType = globals()[classtype]

		try:
			testing = classType(info);
			print "No errors ocurred in the object's creation process."
			testing.setValue(info);
			print "No errors ocurred in the object's setValue() execution."
		except ValueError as exc:
			print exc
			return False
		else:
			if classtype == "Password":
				if hashlib.md5(hashlib.sha256(info).hexdigest()).hexdigest() != testing.getValue():
					print "Error: Invalid getValue() return expression."
					return False
				else:
					print "No error ocurred in the object's getValue() execution."
					return True
			else:
				if info != testing.getValue():
					print "Error: Invalid getValue() return expression."
					return False
				else:
					print "No errors ocurred in the object's getValue() execution."
					return True


def main():
	index = {
		'Password'	:['abcde','Yurick Hauschild_@'], 
		'Name'		:['Joao Calmon Anisio Teixeira', 'Joao Calmon Anisio Teixeira Icc Sul Icc Norte', 'Andre123', 'Renato(){}`'], 
		'Matric'	:[2, 999999, 999999999999999, 0, -12345, 'wat'],
		'PlainText'	:['The quick brown fox jumps over the lazy dog', 'Frase aleatória', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec blandit pretium lorem eu posuere. Duis egestas laoreet orci, at vestibulum mi sodales facilisis. Duis tempor non dui at ornare. In volutpat sed leo in pellentesque. Quisque non malesuada lacus. Ut posuere tristique orci, at sodales erat pretium ut. Pellentesque et ante vitae eros pellentesque iaculis nec sit amet tortor. Phasellus molestie, ipsum varius mollis blandit, ipsum turpis porta augue, ac hendrerit quam sem sit amet leo.In id fermentum felis, sed eleifend tellus. Nunc blandit lacinia mauris vitae porta. Ut vitae egestas nisl, sit amet ultrices risus. Fusce venenatis malesuada ipsum. Cras aliquam ut eros sit amet scelerisque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eleifend venenatis sapien. Curabitur vitae lacinia augue. Vivamus a velit vel tellus tristique dapibus. Sed nisl urna, commodo non eros non, iaculis mollis eros. Maecenas vel risus tellus. Cras ac ligula eu risus bibendum facilisis.Mauris eu dolor lacinia, sodales odio a, vulputate erat. Nam sit amet porta enim. Phasellus rutrum massa eu nisl egestas elementum. Suspendisse vitae pellentesque purus. Sed eu orci augue. Nulla bibendum ipsum in turpis porttitor elementum vel non augue. Nullam sed ligula augue. Sed dictum erat arcu, ut pulvinar dui fermentum gravida. Maecenas in massa et arcu dignissim eleifend. Nam tincidunt lobortis dignissim. Etiam feugiat urna sed orci tristique, a molestie metus pellentesque. Aliquam quis eros a risus blandit tincidunt ut non leo. Fusce viverra erat sed quam fermentum feugiat.Sed tincidunt ut tellus vel laoreet. Proin luctus vel odio id posuere. Pellentesque ut bibendum leo. Aliquam erat volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed condimentum nec risus id lobortis. Vestibulum in quam dictum, tempus nisi quis, consectetur neque. Suspendisse dignissim hendrerit scelerisque. Aenean ultrices, tortor eget varius fermentum, est quam tincidunt urna, nec congue purus ipsum in ipsum. Aenean vitae porta magna. Sed pulvinar ac augue quis commodo. Quisque consequat scelerisque diam, porttitor aliquam purus adipiscing ut. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas congue ipsum sit amet odio ultricies ornare.Aenean quis leo vitae leo blandit accumsan. Nam laoreet nibh eget mauris rhoncus aliquam. Vivamus blandit orci vitae urna malesuada viverra. Aenean ultrices aliquet faucibus. Phasellus eleifend nulla tellus, nec ultricies urna fermentum eu. Suspendisse massa diam, dignissim vel aliquet facilisis, rutrum vitae eros. Nulla nec semper ante, vel commodo sapien. Aenean mattis rhoncus nulla. Quisque sed eleifend libero. Curabitur libero tellus, dignissim at cursus non, eleifend vitae lectus. Nunc placerat tellus egestas scelerisque vestibulum. Cras aliquet diam massa, id pellentesque ipsum elementum in. Ut id iaculis dui. Cras elementum est ante, sit amet dignissim nulla eleifend non. Morbi consectetur ultrices tortor, quis bibendum diam dictum eu.Morbi venenatis porta purus, nec gravida elit lacinia et. Sed id tortor placerat mi venenatis aliquam. Fusce id mollis turpis. Donec sagittis justo sed ligula mollis iaculis. Donec ultricies felis nec justo convallis posuere. Phasellus sed est sed purus fringilla iaculis porttitor vitae nisi. Aliquam dui neque, consequat et arcu sit amet, tincidunt consectetur magna. Integer non lorem at mi commodo ultricies. Nam porta dapibus sapien, congue facilisis massa dictum a. Nunc vulputate accumsan tincidunt. Ut mauris dui, commodo quis elementum nec, accumsan vitae diam. Nam et dictum leo.'],
		'Campus'	:[3, 0, -1, 99999999999999999, 1024],
		'Sex'		:['q','w','e','r','t','y','u','i','o','p','[',']','\\','a','s','d','f','g','h','j','k','l',';','\'','z','x','c','v','b','n','m',',','.','/','1','2','3','4','5','6','7','8','9','0','-','=','¡','™','£','¢','∞','§','¶','•','ª','º','–','≠','å','ß','∂','ƒ','©','˙','∆','˚','¬','…','æ','Ω','≈','ç','√','∫','˜','µ','≤','≥','÷','“','‘','«','!','@','$','%','^','&','*','(',')','_','+','Q','E','R','T','Y','U','I','O','P','{','}','|','A','S','D','F','G','H','J','K','L',':','\"','Z','X','C','V','B','N','M','<','>','?'],
		'Link'		:['exercicios/lol', '', 'adress.br', 'André Lima'],
		'Mail'		:['noreply@elo.org', 'testy @adress.co.uk', '', 'at@@@at.at', 'someone@spotcom'],
		'Grades'	:[88, -45, 105, 0, 'foo'],
		'Id'		:[15, 0, -1, 'wabba'],
		'Language'	:[60, 0, -1, 999, 'pt_br'],
		'ExType'	:[5, 0, -2, "multipla escolha"]
		}

	valid = invalid = 0

	for cls in index:
		for ans in index[cls]:
			if TestUnit().test(ans, cls):
				valid += 1
			else:
				invalid += 1

	print "\nFinished testing."
	print str(valid) + " valid assertives found."
	print str(invalid) + " invalid assertives found."

main()