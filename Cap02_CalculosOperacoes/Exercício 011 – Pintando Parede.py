"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

larg = float(input('Largura da parede: '))
alt = float(input('Altura de parede: '))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {} X {} e sua área é de {} m².'.format(larg, alt, area))
print('Necessidade de {} litros de tinta. '.format(tinta))
