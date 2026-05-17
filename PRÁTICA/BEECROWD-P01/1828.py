n = int(input('Digite qtos casos: '))

for i in range(1,n+1):
    s, r = input().split(' ')
    if s == r:
        print(f'Caso #{i}: De novo!')
    elif s == 'tesoura' and r == 'papel':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'papel' and r == 'pedra':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'pedra' and r == 'lagarto':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'lagarto' and r == 'Spock':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'Spock' and r == 'tesoura':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'tesoura' and r == 'lagarto':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'lagarto' and r == 'papel':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'papel' and r == 'Spock':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'Spock' and r == 'pedra':
        print(f'Caso #{i}: Bazinga!')
    elif s == 'pedra' and r == 'tesoura':
        print(f'Caso #{i}: Bazinga!')

    elif r == 'tesoura' and s == 'papel':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'papel' and s == 'pedra':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'pedra' and s == 'lagarto':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'lagarto' and s == 'Spock':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'Spock' and s == 'tesoura':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'tesoura' and s == 'lagarto':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'lagarto' and s == 'papel':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'papel' and s == 'Spock':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'Spock' and s == 'pedra':
        print(f'Caso #{i}: Raj trapaceou!')
    elif r == 'pedra' and s == 'tesoura':
        print(f'Caso #{i}: Raj trapaceou!')