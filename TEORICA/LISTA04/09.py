vnt, vnm = [], []
maior = 0
menor = 100
for i in range(5):
    nt, nm = input("Nota Nome: ").split(" ")
    nt = float(nt)
    nm = str(nm)
    if nt >= maior:
        maior = nt
        i_maior = i
    if nt <= menor:
        menor = nt
        i_menor = i
    vnt.append(nt)
    vnm.append(nm)

print(f"Maior nota: {maior} - Aluno: {vnm[i_maior]}")
print(f"Menor nota: {menor} - Aluno: {vnm[i_menor]}")