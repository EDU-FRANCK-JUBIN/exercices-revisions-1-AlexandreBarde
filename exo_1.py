nbr_lignes = int(input("Nombre de lignes ? "))

i = 0

lines_tmp = nbr_lignes

nbr_caractere = 1

ligne_string = ""
20
while i != nbr_lignes:
    ligne_string = ""
    for j in range(lines_tmp):
        ligne_string = ligne_string + " "
        if j >= lines_tmp - 1:
            for y in range(nbr_caractere):
                ligne_string = ligne_string + "^"
    i = i + 1
    nbr_caractere = nbr_caractere + 2
    lines_tmp = lines_tmp - 1
    print(ligne_string)

