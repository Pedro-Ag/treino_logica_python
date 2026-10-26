aprovado = 0   
reprovado = 0 
media = 0 
soma = 0
print ("Digite 0 para encerrar o programa")
for i in range (1, 6 + 1):
    nota = float(input ("Digite a nota do aluno: "))
    if nota >= 6:
        aprovado += 1
        soma += nota
    else:
        reprovado += 1
        soma += nota

    if aprovado + reprovado > 0:
        media = soma / (aprovado + reprovado)
    elif nota == 0:
        break
    
    

print(f"Quantidade de alunos aprovados: {aprovado}")
print(f"Quantidade de alunos reprovados: {reprovado}")
print(f"Soma das notas: {soma}")
print(f"Média das notas: {media:.2f}")