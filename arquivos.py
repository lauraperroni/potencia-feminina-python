
file = 'arquivo.txt'
arquivo_leitura = open(file, "r")
arquivo_escrita = open(file, "w")
#   arquivo_binario = open(file, "wb")
arquivo_escrita.write("Texto a ser escrito")
arquivo_escrita.close()

arquivo_leitura = open(file, "r")
leitura = arquivo_leitura.read()
print(leitura)