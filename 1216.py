soma = 0
dist = 0
i = 1
while True:
   try:
       nome = str(input())
       dist = int(input())
       soma = dist + soma
       i += 1

   except EOFError:
       break

media = soma/i
print(f'{media:.1f}')