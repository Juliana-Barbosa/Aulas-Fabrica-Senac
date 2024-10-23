medias = []

numalunos = 0
mediamaior = 0

while numalunos < 10:
    notas = []
    numnotas = 0
    while numnotas < 4:
        nota = float(input(f"Digite a nota {numnotas + 1} do aluno {numalunos + 1}: "))
        notas.append(nota)
        numnotas += 1
        
    media = sum(notas) / 4
    medias.append(media)
    numalunos += 1

for media in medias:
    if media >= 7:
        mediamaior += 1

print(mediamaior)


#------------------------------------------------------------------------------#

aluno1nota1 = int(input("Digite sua nota: "))
aluno1nota2 = int(input("Digite sua nota: "))
aluno1nota3 = int(input("Digite sua nota: "))
aluno1nota4 = int(input("Digite sua nota: "))

aluno1 = (aluno1nota1 + aluno1nota2 + aluno1nota3 + aluno1nota4) / 4

cont = aluno1

while aluno1 >= 7:
    print(aluno1)
    if aluno1 < 7:
        print("Média menor que sete")
    break
    
aluno2nota1 = int(input("Digite sua nota: "))
aluno2nota2 = int(input("Digite sua nota: "))
aluno2nota3 = int(input("Digite sua nota: "))
aluno2nota4 = int(input("Digite sua nota: "))

aluno2 = (aluno2nota1 + aluno2nota2 + aluno2nota3 + aluno2nota4) / 4

cont = aluno2

while aluno2 >= 7:
    print(aluno2)
    if aluno2 < 7:
        print("Média menor que sete")
        break
    break
