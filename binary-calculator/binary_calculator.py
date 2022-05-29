'''
    Autor: Leonardo dos Anjos Boslooper

    Implementações: Soma e Subtração de binários;

    Possiveis Futuras Implementações: Divisão e Multiplicação
'''
def clear_screen() -> None:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def binary_input(posicao) -> str:
    while True:
        binary = input(f"Digite o {posicao}° número binário: ")
        if(verify_valid_binary(str(binary))):
            return binary

        clear_screen()
        print("Binário invalido, digite novamente")


def binary_sum_tests(num_tests, mostrar_testes) -> None:

    import random

    num_tests *= 2

    binary_list = [random.randint(1, 4096) for x in range(num_tests)]
    binary_list2 = [random.randint(1, 4096) for x in range(num_tests)]
    erros = 0
    for i in range(len(binary_list)):
        num1 = convert_decimal_to_binary(binary_list[i])
        num2 = convert_decimal_to_binary(binary_list2[i])
        result = binary_sum(num1, num2)
        if(result[1]):
            result[0] = '1' + result[0]
        true_result = binary_list[i] + binary_list2[i]
        negative = True if "-" in result else False
        correct = True if (true_result == convert_binary_to_decimal(
            result[0].strip('-'), negative)) else False

        if (mostrar_testes == "s"):
            print(f"{num1} ({binary_list[i]}) + {num2} ({binary_list2[i]}) = {int(result[0])} ({convert_binary_to_decimal(result[0].strip('-'), negative)} | {true_result})")
        else:
            if(not correct):
                erros += 1
                print(
                    f"{num1} ({binary_list[i]}) + {num2} ({binary_list2[i]}) = {int(result[0])} ({convert_binary_to_decimal(result[0].strip('-'), negative)} | {true_result})")

    print(
        f"Quantidade de erros em uma amostra de {num_tests//2} somas: {erros}")


def binary_subtract_tests(num_tests, mostrar_testes) -> None:

    import random

    num_tests *= 2

    binary_list = [random.randint(1, 4096) for x in range(num_tests)]
    binary_list2 = [random.randint(1, 4096) for x in range(num_tests)]
    erros = 0
    for i in range(len(binary_list)):
        num1 = convert_decimal_to_binary(binary_list[i])
        num2 = convert_decimal_to_binary(binary_list2[i])
        result = binary_subtract(num1, num2)[0]
        true_result = binary_list[i] - binary_list2[i]
        negative = True if "-" in result else False
        correct = (binary_list[i] - binary_list2[i] ==
                   convert_binary_to_decimal(result.strip('-'), negative))

        
        if (mostrar_testes == "s"):
             print(
                f"{num1} ({binary_list[i]}) - {num2} ({binary_list2[i]}) = {int(result)} ({convert_binary_to_decimal(result.strip('-'), negative)} | {true_result})")
        else:
            if(not correct):
                erros += 1
                print(
                    f"{num1} ({binary_list[i]}) - {num2} ({binary_list2[i]}) = {int(result)} ({convert_binary_to_decimal(result.strip('-'), negative)} | {true_result})")

    print(
        f"Quantidade de erros em uma amostra de {num_tests//2} divisões: {erros}")


def convert_binary_to_decimal(binary, negative) -> int:
    """
        Função para fazer a convesão de Binário para Decimal.

        Input: Binário, Sinalização
        Output: Decimal
    """

    decimal = 0
    increment = 2
    position = 1

    binary_str = str(binary)

    verify_valid_binary(binary_str)

    for i in reversed(range(len(binary_str))):
        decimal += int(binary_str[i]) * position
        position *= increment

    if(negative):
        decimal *= -1

    return decimal


def convert_decimal_to_binary(decimal) -> str:
    """
        Função para fazer a convesão de Decimal para Binário.

        Input: Decimal
        Output: Binário
    """

    binary = ''

    if decimal == 0:
        return '0'
    if decimal < 0:
        flag = True
        decimal *= -1

    while(decimal > 0):
        binary += str(decimal % 2)
        decimal //= 2

    return binary[::-1]


def verify_valid_binary(binary) -> None:
    '''
        Faz a verificação bit a bit de um valor binário,
        envia um erro caso encontre algo diferente de '0' ou '1'.
    '''
    for bit in binary:
        if(bit != '0' and bit != '1'):
            return False
            raise Exception(f"Invalid binary {binary}")

    return True


def binary_sum(binary_one, binary_two) -> list:
    '''
        Realiza a soma de 2 binários

        Input: 2 binários para serem somados
        Output: Soma dos binários, Sobra da soma
    '''

    verify_valid_binary(binary_one + binary_two)

    if(not len(binary_one) == len(binary_two)):
        '''
            Verifica se os tamanhos dos 2 números binários são iguais.

            Se não forem, verifica qual é o menor e o completa com zeros.
        '''

        if len(binary_one) > len(binary_two):
            quant_zeros = ''.join('0' for _ in range(
                len(binary_one) - len(binary_two)))
            binary_two = (quant_zeros + binary_two)
        else:
            quant_zeros = ''.join('0' for _ in range(
                len(binary_two) - len(binary_one)))
            binary_one = (quant_zeros + binary_one)

    binary_list = list(zip(binary_one, binary_two))

    # print(binary_one, binary_two)

    BIT_ONE = 0
    BIT_TWO = 1

    rest = False

    sum_result = ''

    for bit_pair in reversed(binary_list):

        '''
            Faz a concatenação do par de bit e verifica qual é o caso atual.
        '''
        bit_sum = bit_pair[BIT_ONE] + bit_pair[BIT_TWO]

        if(rest):
            match bit_sum:
                case '00':  # 0
                    sum_result += '1'
                    rest = False
                case '01' | '10':  # 1
                    sum_result += '0'
                    rest = True
                case '11':  # 2
                    sum_result += '1'
                    rest = True
        else:
            match bit_sum:
                case '00':  # 0
                    sum_result += '0'
                    rest = False
                case '01' | '10':  # 1
                    sum_result += '1'
                    rest = False
                case '11':  # 2
                    sum_result += '0'
                    rest = True

    return [sum_result[::-1], rest]


def binary_subtract(binary_one, binary_two) -> str:
    '''

    '''

    # Iguala as casas dos binarios caso o 1 seja maior que o segundo
    if (len(binary_one) > len(binary_two)):
        binary_two = ''.join('0' for _ in range(
            len(binary_one) - len(binary_two))) + binary_two

    # Reverte o segundo binario, '0' vira '1' e vice-versa
    binary_two = ''.join('0' if x == '1' else '1' for x in binary_two)

    complement = binary_sum(binary_two, '1')[0]

    subtraction_result = binary_sum(binary_one, complement)

    if(not subtraction_result[1]):
        subtraction_result[0] = ''.join(
            '0' if x == '1' else '1' for x in subtraction_result[0])
        subtraction_result[0] = '-' + binary_sum(subtraction_result[0], '1')[0]

    return(subtraction_result)


def binary_division(dividend, divisor) -> str:
    pass


def binary_multiplication(binary_one, binary_two) -> str:
    '''
        //TODO: Implementação incompleta.
    '''

    result = ''
    temporary_result = ''

    for bit_one in reversed(binary_one):

        if(result != ''):
            if(temporary_result != ''):
                temporary_result = binary_sum(temporary_result, result)
            temporary_result = result
            result = ''

        for bit_two in reversed(binary_two):
            bit_sum = bit_one+bit_two
            if('0' in bit_sum):
                result += '0'
            else:
                result += '1'

    print(temporary_result)

    pass


'''
Suporte: números inteiros positivos; soma, subtração, conversões (Decimal -> Binário, Binário -> Decimal)


Implementações faltando:
    Números negativos;
    Multiplcação de binários;
    Divisão de binários;
'''

if __name__ == '__main__':
    clear_screen()
    while True:
        action = input(
            'Escolha sua operação: \n1 - Soma \n2 - Subtração\n3 - Testes\nEscolha: ')
        if(not (action not in ['1', '2', '3'])):
            break

        clear_screen()
        print("\n\n\n\nEscolha incorreta, por favor digite novamente.")

    clear_screen()

    match (action):
        case '1':
            binary_one = binary_input(1)
            binary_two = binary_input(2)
            print("Resultado: " + binary_sum(binary_one, binary_two)[0])
        case '2':
            binary_one = binary_input(1)
            binary_two = binary_input(2)
            print("Resultado: " + binary_subtract(binary_one, binary_two)[0])
        case '3':
            num_tests = int(input("Quantos teste você deseja rodar? "))
            mostrar_testes = input("Você deseja mostrar todos os cálculos feitos? (S ou N) ").lower()
            binary_subtract_tests(num_tests, mostrar_testes)
            binary_sum_tests(num_tests, mostrar_testes)
 