import math

while True:
    print('''
          [1] Fazer calculo
          [2] Sair
          ''')

    try:
        opção = int(input('Você quer fazer cálculo ou sair? '))

        if opção == 2:
            print('Calculadora encerrada.')
        elif opção== 1:


            print('''
        [+] Soma
        [-] Subtração
        [*] Multiplicação
        [%] Porcentagem
        [/] Divisão
        [R] Raiz quadrada
        [P] Potência          
        ''')


        sinais= input('Escolha uma opcão: ')

        if sinais in ['+', '-', '*', '/', 'P']:
            n1=input('Digite um número: ')
            n2=input('Digite outro nùmero: ')

            match sinais:
                case '+':
                    res= n1+n2
                    print(res)
                case '-':
                    res= n1 - n2
                    print(res)
                case '*':
                    res= n1*n2
                    print(res)
                case '/':
                    res= n1/n2
                    print(res)
                case '%':
                    res= n/100
                case 'R':
                    res=math.sqrt(n3)
                case 'P':
                    res= n1**n2

    except ValueError:
        print("você digitou um valor inválido ")
    except ZeroDivisionError:
        print('Divisão por 0 não é permitida :p ')

    # resposta= ""
    # while resposta.lower() != "sair":
    #     resposta= input ('Digite sair para terminar: ')
    #     if resposta.lower()!="sair":
    #         print("Você digitou:",resposta)
    # print("Obrigado por ter usado")