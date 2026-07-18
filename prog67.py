cursos=["Matematica", "Portugues"]
item=input("Digite mais um curso: ")
cursos.append(item)
print("Listagem e cursos")
for i in cursos:
    print(i)
print("Escolha um cursos para excluir")
rem=input("Digite qual curso deseja excluir: ")
cursos.remove(rem)
for i in cursos:
    print(i)