def Sum(T):
    s = 0
    for i in range(10):
        s += T[i]
    return s

def Product(T):
    P = 1
    for i in range(10):
        P = P * T[i]
    return P

def moyenne(T):
    s = Sum(T)
    M = s / 10
    return M

def sign(T):
    print("Les éléments positifs du tableau sont : ")
    for i in range(10):
        if T[i] > 0:
            print(T[i])

    print("Les éléments négatifs du tableau sont : ")
    for i in range(10):
        if T[i] < 0:
            print(T[i])


T = [0.0] * 10
for i in range(10):
    T[i] = float(input(f"Donner l'élément {i + 1} :"))

print("La somme des éléments du tableau est : ", Sum(T))
print("Le produit des éléments du tableau est : ", Product(T))
print("La moyenne des éléments du tableau est : ", moyenne(T))
sign(T)
