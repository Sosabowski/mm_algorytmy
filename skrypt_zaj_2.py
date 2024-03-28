'''
import this
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(rok)
oceny = [4, 3, 5, 2, 5, 4]

pierwsza = oceny[0]

ostatnia = oceny[-1]

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')


imie, nazwisko, *_, zawod = info
print(imie)
print(nazwisko)
print(zawod)


dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, (jezyk, wersja, *opis) = dane
print("Rok: ", rok)
print("Język: ", jezyk)
print("Wersja: ", wersja)
print("Opis wersji: ", opis)
'''
####DWA
'''
a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(a)
print(b)

c=a[:]
c[0] = 'nowa wartość'
print(a)
print(b)
print(c)

x = y = 10
y = y + 1
print(x)
print(y)

##TRZY

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]
print(K)
print(L)
print(M)
print(N)

'''
##CZTERY
'''
imiona = ['Anna', 'Jan', 'Ewa', 'Maciek']
oceny = [5, 4, 3,]

pairs = zip(imiona, oceny)

for imie, ocena in pairs:
    print(f"{imie} - {ocena}")
#W przypadku gdy listy będą miały różną długość, to  zostaną one "wyrównane".


def kwadrat(x):
    return x ** 2

liczby = [1, 2, 3, 4, 5]

squares_list = list(map(kwadrat, liczby))

print(squares_list)
'''
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg

lista_przed = [1, 2, 3]
print("Lista przed:", lista_przed)
zmien_wartosc(lista_przed)
print("Lista po:", lista_przed)

int_przed = 123
print("Integer przed:", int_przed)
int_po = zmien_wartosc(int_przed)
print("Integer po:", int_po)

