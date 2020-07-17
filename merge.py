def escribir(linea, archivo):
    archivo.write(linea + "\n")

def merge_2(modulo1, modulo2, modulo_a_escribir):
    modulo1 = open(modulo1)
    modulo2 = open(modulo2)
    linea1 = modulo1.readline()
    linea2 = modulo2.readline()

    with open(modulo_a_escribir, "w") as escritura:
        while linea1 != "" and linea2 != "":
        
            if linea1 < linea2:
                escritura.write(linea1 + "\n")
                linea1 = modulo1.readline()
            elif linea1 > linea2:
                escritura.write(linea2 + "\n")
                linea2 = modulo2.readline()
        if linea1:
            while linea1:
                escribir(linea1, escritura)
                linea1 = modulo1.readline()
        elif linea2:
            while linea2:
                escribir(linea2, escritura)
                linea2 = modulo2.readline()
    modulo1.close()
    modulo2.close()


def ciclar_modulos(lista_modulos):
    if len(lista_modulos[-1]) % 2 != 0:
        ult_elemento_impar = lista_modulos[-1].remove(lista_modulos[-1][-1])
        index = 1
        lista_modulos.append([])
        while (index <= len(lista_modulos[-2])) and len(lista_modulos[-2]) > 1:
            nombre_a_escribir = str(index) + ".csv"
            merge_2(lista_modulos[-2][index], lista_modulos[-2][index - 1], nombre_a_escribir)
            index += 2    
            lista_modulos[-1].append(nombre_a_escribir)
        lista_modulos[-1].append(ult_elemento_impar)
    else:
        index = 1
        lista_modulos.append([])
        while (index <= len(lista_modulos[-2])) and len(lista_modulos[-2]) > 1:
            nombre_a_escribir = str(index) + ".csv"
            merge_2(lista_modulos[-2][index], lista_modulos[-2][index - 1], nombre_a_escribir)
            index += 2    
            lista_modulos[-1].append(nombre_a_escribir)
        