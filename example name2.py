#two.py

# Nota 1 para o meu eu do futuro: Não deixar espaços em módulos e pacotes
# Nota 2 para o meu futuro eu: Caso tenha espaços repetir o método abaixo
example_name = __import__("example name")
example_name

print('TOP LEVEL IN TWO.PY')

example_name.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly!')
else:
    print('TWO.PY has been imported!')