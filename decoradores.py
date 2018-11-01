

PASSWORD = '12345'

def password_requierd(func):
	def wrapper():
		passdord = input('Cual es tu clave? ')

		if passdord == PASSWORD:
			return func()
		print('La clave es incorrecta')

	return wrapper

@password_requierd
def needs_password():
	print("Ingreso al sistema exitoso")
	return True


def decorator_name(func):
	def wrapper(*args, **kargs):
		restult = func(*args, **kargs)

		return restult.upper()
	return wrapper


@decorator_name
def say_hello(name):
	return 'Hola, {}'.format(name)

if __name__ == '__main__':
	if needs_password():	
		print(say_hello('vic'))