import math
class UtilitariosMatematicos:
    def __init__(self,teste):
        self.teste=teste

    def menu_principal(self):
        while True:
            print("|============================|")
            print("|            Menu            |")
            print("|1. Calculadora              |")
            print("|2. Tabuada                  |")
            print("|3. Verificar Número         |")
            print("|4. Tamanho do texto         |")
            print("|5. Conversores              |")
            print("|0. Sair                     |")
            print("|============================|")
            esc=input("Escolha uma opção: ")
            match esc:
                case "0":
                    print("Fim do Programa.")
                    break
                
                case "1":
                    self.calculadora()

                case "2":
                    self.tabuada()

                case "3":
                    self.verificar_numero()

                case "4":
                    self.tamanho_do_texto()

                case "5":
                    self.conversores()

                case _:
                    print("Opção inválida. Por favor, escolha novamente.")
        

    def calculadora(self):
        print("|============================|")
        print("|        Calculadora         |")
        print("|1. Adição                   |")
        print("|2. Subtração                |")
        print("|3. Multiplicação            |")
        print("|4. Divisão                  |")
        print("|5. Potência                 |")
        print("|6. Raiz quadrada            |")
        print("|7. Múltiplos                |")
        print("|8. Média                    |")
        print("|9. Soma de números          |")
        print("|10. Fatorial                |")
        print("|0. Sair                     |")
        print("|============================|")
        esc=input("Escolha uma opção:")
        match esc:
            case "0":
                self.menu_principal()

            case "1":
                print("A operação escolhida foi Adição")
                a=int(input("Entre com um número: "))
                b=int(input("Entre com um número: "))
                print(f"A soma é: {a+b}")

            case "2":
                print("A operação escolhida foi Subtração")
                a=int(input("Entre com um número: "))
                b=int(input("Entre com um número: "))
                print(f"O resto é: {a-b}")
                
            case "3":
                print("A operação escolhida foi Multiplicação")
                a=int(input("Entre com um número: "))
                b=int(input("Entre com um número: "))
                print(f"O produto é: {a*b}")
                
            case "4":
                print("A operação escolhida foi Divisão")
                a=int(input("Entre com um número: "))
                b=int(input("Entre com um número: "))
                print(f"O quociente é: {a/b}")

            case "5":
                b=int(input("Entre com o número de vezes com o qual se deseja calcular a potência: "))
                while d!=b:
                    r=a*a
                    d+1
                print(f"A potência de {a} multiplicado {b} vezes é: {r}")
                
            case "6":
                b=int(input("Entre com o número de vezes com o qual se deseja calcular a raiz: "))
                while d!=b:
                    r=a/a
                    d+1
                print(f"A raiz de {a} dividido {b} vezes é: {r}")

            case "7":
                a=int(input("Digite um número: "))
                mu=int(input("Digite o multiplo: "))
                if a%mu==0:
                    print(f"O número {a} é multiplo de {mu}")
                else:
                    print(f"O número {a} não é multiplo de {mu}")

            case "8":
                v=int(input("Digite até quantos números deverá ser calculada a média:"))
                while c<=v:
                    n=int(input(f"Digite o {c}º número: "))
                    s=s+n
                    c=c+1
                md=s/v
                print(f"A média dos números é: {md}")

            case "9":
                nu=int(input("Digite o número até o qual deseja somar: "))
                d=0
                for c in range(nu+1):
                    d=d+c
                print(f"A soma de 1 até {nu} é: {d}")

            case "10":
                nu=int(input("Digite até que número se deseja obter o fatorial: "))
                f=0
                while f<=nu:
                    mu=mu*f
                    f=f+1
                print(f"O fatorial de {nu} é: {mu}")

            case _:
                print("Opção invalida, tente novamente.")
                self.calculadora()

    def tabuada(self):
        print("|============================|")
        print("|           Tabuada          |")
        print("|============================|")
        num=int(input("Insira um número para ver sua tabuada: "))
        for i in range(1,11):
            print(f"{num} x {i} = {num*i}")

    def verificar_numero(self):
        print("|============================|")
        print("|     Verificar Número       |")
        print("|1. Positivo, negativo, zero |")
        print("|2. Primo                    |")
        print("|3. Par, ímpar               |")
        print("|4. Quadrado perfeito        |")
        print("|5. Número triangular        |")
        print("|0. Sair                     |")
        print("|============================|")
        esc=input("Escolha uma opção:")
        match esc:
            case "0":
                self.menu_principal()

            case "1":
                b=int(input("Insira um número para identificar se ele é positivo, negativo ou igual a zero: "))
                if b>0:
                    print(f"O número {b} é positivo.")
                            
                elif b<0:
                    print(f"O número {b} é negativo.")
                
                else:
                    print(f"O número {b} é igual a zero.")
                            
            case "2":
                b=int(input("Insira um número para identificar se ele é primo: "))
                if b>1:
                    div = 0
                    for va in range(1,b+1):
                        if b%va==0:
                            div+=1
                    if div==2:
                        print(f"O número {b} é primo!")
                    else:
                        print(f"O número {b} não é primo!")
                else:
                    print(f"{b} é um valor negativo ou igual a zero!")
                                
            case "3":
                b=int(input("Insira um número para identificar se ele é par o impar: "))
                if b%2==0:
                    print(f"O número {b} é par.")
                else:
                    print(f"O número {b} é impar.")

            case "4":
                b=int(input("\nInsira um número para identificar se ele é um quadrado perfeito: "))
                r=math.sqrt(b)
                if r.is_integer() and r/2 == b:
                    print(f"O número {b} é um quadrado perfeito.")
                else:
                    print(f"O número {b} não é um quadrado perfeito.")

            case "5":
                a=int(input("\nInsira um número para identificar se ele é um número triangular: "))
                nu=a
                aux=0
                for i in range(1,a+1):
                    if (i*(i+1))//2==a:
                        aux=1
                if aux==1:
                    print(f"O número {nu} é um número triangular.")
                else:
                    print(f"O número {nu} não é um número triangular.")

            case _:
                print("Opção invalida, tente novamente.")
                self.verificar_numero()

    def tamanho_do_texto(self,texto):
        texto=input("Digite o texto: ")
        resultado=len(texto)
        print(f"O tamanho do texto é: {resultado}")

    def conversores(self):
        print("|============================|")
        print("|         Conversores        |")
        print("|1. Comprimento              |")
        print("|0. Sair                     |")
        print("|============================|")
        con=input("Sua escolha: ")
        match con:
            case "0":
                self.menu_principal()

            case "1":
                self.u_comp()

            case _:
                print("Opção invalida, tente novamente.")
                self.conversores()

    def u_comp(self):
        print("|============================|")
        print("|     Unidades de Medida     |")
        print("|1. Quilômetros              |")
        print("|2. Metros                   |")
        print("|3. Centímetros              |")
        print("|4. Milímetros               |")
        print("|5. Pés                      |")
        print("|6. Polegadas                |")
        print("|7. Jardas                   |")
        print("|8. Milhas                   |")
        print("|0. Sair                     |")
        print("|============================|")
        med=input("Sua escolha: ")
        match med:
            case "0":
                self.conversores()

            case "1":
                valor = float(input("Insira o valor em Quilômetros para ser convertido para:\nMetros, Centímetros, Milímetros, Pés, Polegadas, Jardas e Milhas: "))
                km = valor
                met = km * 1000
                cm = km * 100000
                mm = km * 1000000
                ft = km * 3280.84
                inch = km * 39370.1
                yd = km * 1094.61
                mile = km / 1.60934
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "2":
                valor = float(input("Insira o valor em Metros para ser convertido para:\n Quilômetros, Centímetros, Milímetros, Pés, Polegadas, Jardas e Milhas: "))
                km = met / 1000
                met = valor
                cm = met * 100
                mm = met * 1000
                ft = met * 3.28084
                inch = met * 39.3701
                yd = met * 1.09361
                mile = met / 1609.34
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "3":
                valor = float(input("Insira o valor em Centímetros para ser convertido para:\n Quilômetros, Metros, Milímetros, Pés, Polegadas, Jardas e Milhas: "))
                km = cm / 100000
                met = cm / 100
                cm = valor
                mm = cm * 10
                ft = cm / 30.48
                inch = cm / 2.54
                yd = cm / 91.44
                mile = cm / 160934
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "4":
                valor = float(input("Insira o valor em Milímetros para ser convertido para:\n Quilômetros, Metros, Centímetros, Pés, Polegadas, Jardas e Milhas: "))
                km = mm / 1000000
                met = mm / 1000
                cm = mm /10
                mm = mm
                ft = mm / 304.8
                inch = mm / 25.4
                yd = mm / 914.4
                mile = mm / 1609344
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "5":
                valor = float(input("Insira o valor em Pés para ser convertido para:\n Quilômetros, Metros, Centímetros, Milímetros, Polegadas, Jardas e Milhas: "))
                km = ft / 3280.84
                met = ft / 3.28084
                cm = ft * 30.48
                mm = ft * 304.8
                ft = valor
                inch = ft * 12
                yd = ft / 3
                mile = ft / 5280
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "6":
                valor = float(input("Insira o valor em Polegadas para ser convertido para:\n Quilômetros, Metros, Centímetros, Milímetros, Pés, Jardas e Milhas: "))
                km = inch / 39370.1
                met = inch / 39.3701
                cm = inch * 2.54
                mm = inch * 25.4
                ft = inch / 12
                inch = valor
                yd = inch / 36
                mile = inch / 63360
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "7":
                valor = float(input("Insira o valor em Jardas para ser convertido para:\n Quilômetros, Metros, Centímetros, Milímetros, Pés, Polegadas e Milhas: "))
                km = yd / 1093.61
                met = yd / 1.09361
                cm = yd * 91.44
                mm = yd * 9.144
                ft = yd * 3
                inch = yd * 36
                yd = valor
                mile = yd / 1760
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case "8":
                valor = float(input("Insira o valor em Milhas para ser convertido para:\n Quilômetros, Metros, Centímetros, Milímetros, Pés, Polegadas e Jardas: "))
                km = mile * 1.60934
                met = mile * 1609.34
                cm = mile * 160934
                mm = mile * 1609344
                ft = mile * 5280
                inch = mile * 63360
                yd = mile * 1760
                mile = valor
                print("\nO valor em Quilômetros é:", km, "Km")
                print("\nO valor em Metros é:", met, "M")
                print("\nO valor em Centímetros é:", cm, "Cm")
                print("\nO valor em Milímetros é:", mm, "mm")
                print("\nO valor em Pés é:", ft, "ft")
                print("\nO valor em Polegadas é:", inch, "in")
                print("\nO valor em Jardas é:", yd, "yd")
                print("\nO valor em Milhas é:", mile, "mile")
        
            case _:
                print("Opção invalida, tente novamente.")
                self.u_comp()
