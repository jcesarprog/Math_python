""" 
Esta conjectura aplica-se a qualquer número natural não nulo, e diz-nos para, se este número for par, o dividir por 2 (/2), e se for impar, para multiplicar por 3 e adicionar 1 (*3+1). Desta forma, por exemplo, se a sequência iniciar com o número 5 ter-se-á: 5; 16; 8; 4; 2; 1. A conjectura apresenta uma regra dizendo que, qualquer número natural não nulo, quando aplicado a esta regra, eventualmente sempre chegará a 4, que se converte em 2 e termina em 1. Essa sequência em questão também pode ser chamada de Números de Granizo ou Números Maravilhosos. A explicação destes últimos nomes está em "como o granizo nas nuvens antes de cair, os números saltam de um lugar ao outro antes de chegar ao 4, 2, 1".[1]
 """

def collatz(num):   # With recursion 
    num = int(num)
    print(num, end=', ')    
    if num == 1:
        print("\nCollatz sequence is over!")
    elif num % 2 == 0:
        num = num //2
        collatz(num)
    else:
        num = 3 * num +1
        collatz(num)

try:
    num = input("Type a number to start the Collatz sequence: ")
    print("\nCollatz sequence started!!")
    collatz(num)    
except (TypeError, ValueError) as e:
    print("was typed and this is not a valid integer or cant be converted to integer!!")
    print("The number typed needs to be an Integer")
    print(f"Error generated: {e}")
