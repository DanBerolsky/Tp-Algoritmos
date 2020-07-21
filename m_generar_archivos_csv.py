import modulo_csv

def leer(archivo):
    
    """[Autor: Alfonso]
    [Ayuda: Lee el archivo linea por linea]
    """
    
    lineas = [linea.rstrip('\n') for linea in archivo]
    
    return lineas

def abro_ar(archivo):
    
    """[Autor: Alfonso]
    [Ayuda: abre un archivo]
    """

   # encoding="utf8" use eso para solucionar el error.
   #El archivo informacion_por_desarollador era el que generaba ese problema,
   #aprantemente era por que tenia otro codificacion "utf8"

    with open(archivo, encoding="utf8") as archivo_completo: 
       
        return leer(archivo_completo)

def ordenar_alfabeticamente(diccionario):
    
    """[Autor: Alfonso]
    [Ayuda: Ordena diccionario de mayor a menor, respecto las claves del mismo. Devuelvo lista de tuplas]
    """
    
    return sorted(diccionario.items(), key = lambda clave: clave[0])

def armar_csv_funciones(archivo):
    
    """[Autor: Alfonso]
    [Ayuda: abre un archivo]
    """
    
    #Declaro variables
    nombre_archivo = "fuente_unico.csv"
    datos = {}
    
    #Abro los modulos
    modulos = abro_ar(archivo)
    ultima_linea_indentada = None
    #Itero a traves de los modulos del txt
    for modulo in modulos:
        lineas = abro_ar(modulo)
        contador_def = 0
        for linea in lineas:
                  
            #Busco la linea que comienze por def para encontrar el nombre de la funcion, sus parametros y cuerpo
            if linea.startswith('def '):
                funcion = linea
                index_inicial = lineas.index(funcion) + 1
                nombre_funcion = funcion.split('def ')[1].lstrip().split('(')[0]
                parametros = "(" + funcion.split('(')[1].lstrip().split(')')[0] + ")"
                contador_def += 1
                
                if contador_def >1:
                    linea_return = linea
                    index_final = lineas.index(linea_return)
                    cuerpo = lineas[index_inicial_anterior:index_final]
                    cuerpo_sin_comment = armar_csv_comentarios(cuerpo,nombre_funcion, modulo)
                    datos[nombre_funcion_anterior] = {"Parametros de la funcion":parametros_anterior,"Nombre del modulo":modulo,"Cuerpo de la funcion":cuerpo_sin_comment}
                    contador_def = 1
                
            if linea.strip().startswith("return "):
                linea_return = linea
                index_final = lineas.index(linea_return) + 1
                cuerpo = lineas[index_inicial:index_final]
                cuerpo_sin_comment = armar_csv_comentarios(cuerpo,nombre_funcion, modulo)
                datos[nombre_funcion] = {"Parametros de la funcion":parametros,"Nombre del modulo":modulo,"Cuerpo de la funcion":cuerpo_sin_comment}
                contador_def = 0

            if linea.startswith("    "):
                ultima_linea_indentada = linea
                
            if linea == lineas[len(lineas)-1]:
                index_final = lineas.index(ultima_linea_indentada) + 1
                cuerpo = lineas[index_inicial:index_final]
                cuerpo_sin_comment = armar_csv_comentarios(cuerpo,nombre_funcion, modulo)
                datos[nombre_funcion] = {"Parametros de la funcion":parametros,"Nombre del modulo":modulo,"Cuerpo de la funcion":cuerpo_sin_comment}

            if linea.startswith('def '):
                funcion = linea
                index_inicial_anterior = lineas.index(funcion) + 1
                nombre_funcion_anterior = funcion.split('def ')[1].lstrip().split('(')[0]
                parametros_anterior = funcion.split('(')[1].lstrip().split(')')[0]

    #Ordeno el diccionario
        funciones_alfabeto = ordenar_alfabeticamente(datos)
    
    return modulo_csv.armo_csv(funciones_alfabeto,nombre_archivo, modulo)

def armar_csv_comentarios(lista_cuerpo,nombre_funcion, modulo):
    
    """[Autor: Alfonso]
    [Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]
    """ 
    #Declaracion de variables
    nombre_archivo = 'comentarios.csv'
    datos_comentarios = {}
    lista = lista_cuerpo    
    #Busco las lineas comentadas y me quedo con una lista de las lineas comentadas
    resto = [i for i in lista if '#' in i]
    lineas_multiples = lista_comentarios(lista)
    
    
    if not resto:
        lineas_comentadas = lineas_multiples 
    else:
        lineas_comentadas = lineas_multiples + resto
    
    nombre_autor,nombre_ayuda = autor_ayuda(lineas_multiples)
    
    # Cruzo las lineas comentadas con el cuerpo de la otra funcion para devolver solo las lineas del cuerpo de la
    # funcion que no tienen comentario
    cuerpo_sin_comentarios = [x for x in lista if x not in lineas_comentadas]
    
    #Itero atraves de las lineas comentadas para encontrar el autor y ayuda
            #me creo el diccionario con los campos que necesito
    datos_comentarios[nombre_funcion] = {"Nombre del autor":nombre_autor,"informacion de ayuda":nombre_ayuda,"Resto de lineas comentadas":resto}
            
    #Ordeno el diccionario, respecto sus claves
    comentarios_alfabeto = ordenar_alfabeticamente(datos_comentarios)
    #Genero el csv.
    modulo_csv.armo_csv(comentarios_alfabeto,nombre_archivo, modulo)
    
    return cuerpo_sin_comentarios



def lista_comentarios(lista):
    """[Autor: Alfonso]
    [Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]
    """ 
    
    index_lista = []
    comentarios_triples = []
    for i in lista:
        if i.strip().startswith('"""'):
            index = lista.index(i)
            index_lista.append(index)
    if index_lista:
        inicial = index_lista[0]
        final = index_lista[1]+1
        comentarios_triples = lista[inicial:final]
        
    return comentarios_triples
 
   
   
def  autor_ayuda(lista):
    """[Autor: Alfonso]
    [Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]
    """    
    nombre_autor = ""
    for i in lista:
        if 'Autor:' in i:
            nombre_autor = i.split('"""')[1].lstrip()
    b = ''.join(lista)        
    nombre_ayuda = b.replace(nombre_autor,'').replace('"""','')
    return nombre_autor, nombre_ayuda


armar_csv_funciones('programas.txt')
