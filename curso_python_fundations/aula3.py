# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))

# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))

# print('Final do programa!')


# a = int(input('Entre com um valor: '))
# resto = a % 2

# if resto == 0:
#     print('O número é par')
# else:
#     print('O número é ímpar')


# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))

# resto_a = a % 2
# resto_b = b % 2

# if resto_a == 0 or resto_b == 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')

# if resto_a == 0 or not resto_b > 0:  # o not serve para negar algo que é falso
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')



a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Vodê digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Vodê digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Vodê digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Vodê digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('foi informado alguma nota errada')