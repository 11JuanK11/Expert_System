def comparar_caracteristicas(caracteristicas, animal):
    nombre, caracteristicas_animal = animal.split(":")
    caracteristicas_animal = caracteristicas_animal.split(", ")
    contador_coincidencias = 0
    for caracteristica in caracteristicas:
        for caracteristica_animal in caracteristicas_animal:
            if caracteristica == caracteristica_animal:
                contador_coincidencias += 1
    if contador_coincidencias == 3:
        return nombre

def buscar_animal_por_caracteristicas(caracteristicas):
    animales = []
    with open("./data/animals.txt", "r", encoding="utf-8") as files:
        for linea in files:
            linea = linea.strip()
            if linea:  
                animal = comparar_caracteristicas(caracteristicas, linea)
                if animal:
                    animales.append(animal)
    return animales

import clips # type: ignore

caracteres_a_eliminar = "()"
reglas_sistema_experto = []
reglas_sistema_experto.append("(defrule reglaMamiferoSemiacuatico (Marino)(Vertebrado)(Cuadrupedo) => (assert(MamiferoSemiacuatico)))")
reglas_sistema_experto.append("(defrule reglaMamiferoAcuatico (Marino)(Vertebrado)(NoCuadrupedo) => (assert(MamiferoAcuatico)))")
reglas_sistema_experto.append("(defrule reglaNoVertebradoMarinoCuadrupedo (Marino)(NoVertebrado)(Cuadrupedo) => (assert(NoVertebradoMarinoCuadrupedo)))")
reglas_sistema_experto.append("(defrule reglaNoMamiferoSemiacuatico (Marino)(NoVertebrado)(NoCuadrupedo) => (assert(NoMamiferoSemiacuatico)))")
reglas_sistema_experto.append("(defrule reglaMamiferoTerrestre (NoMarino)(Vertebrado)(Cuadrupedo) => (assert(MamiferoTerrestre)))")
reglas_sistema_experto.append("(defrule reglaNoMamiferoTerrestre (NoMarino)(Vertebrado)(NoCuadrupedo) => (assert(NoMamiferoTerrestre)))")
reglas_sistema_experto.append("(defrule reglaNoVertebradoNoMarinoCuadrupedo (NoMarino)(NoVertebrado)(Cuadrupedo) => (assert(NoVertebradoNoMarinoCuadrupedo)))")
reglas_sistema_experto.append("(defrule reglaNoVertebradoNoMarinoNoCuadrupedo (NoMarino)(NoVertebrado)(NoCuadrupedo) => (assert(NoVertebradoNoMarinoNoCuadrupedo)))")

def inicializar_ambiente():
    sistemaExperto = clips.Environment()
    sistemaExperto.clear()
    for regla in reglas_sistema_experto:
        sistemaExperto.build(regla)
    return sistemaExperto

def caracteristicas_de_busqueda(sistemaExperto):
    caracteristicas = []
    for fact in sistemaExperto.facts():
        fact = str(fact).translate(str.maketrans("", "", caracteres_a_eliminar))
        caracteristicas.append(fact)
    return caracteristicas

def ejecutar_ambiente(sistemaExperto):
    resultados_sistema_experto = {"clasificacion": "", "animales": []}
    print(sistemaExperto.activations())
    
    sistemaExperto.run()
    print(sistemaExperto.activations())
    for fact in sistemaExperto.facts():
        factString = str(fact)
        factString = factString.translate(str.maketrans("", "", caracteres_a_eliminar))
        if "MamiferoSemiacuatico" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Semiacuaticos"
        if "MamiferoAcuatico" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Acuaticos"
        if "NoVertebradoMarinoCuadrupedo" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Semiacuaticos y No Vertebrados"
        if "NoMamiferoSemiacuatico" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Marinos, No Vertebrados y No Cuadrupedos"
        if "MamiferoTerrestre" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Terrestres, Vertebrados y Cuadrupedos"
        if "NoMamiferoTerrestre" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Terrestres, No Cuadrupedos y Vertebrados"
        if "NoVertebradoNoMarinoCuadrupedo" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Invertebrados, Terrestres y Cuadrupedos"
        if "NoVertebradoNoMarinoNoCuadrupedo" == factString:
            resultados_sistema_experto["clasificacion"] = "Animales Invertebrados, Terrestres y No Cuadrupedos"
    print("Resultado de la clasificación: ", resultados_sistema_experto["clasificacion"])
    resultados_sistema_experto["animales"] = buscar_animal_por_caracteristicas(caracteristicas_de_busqueda(sistemaExperto))
    return resultados_sistema_experto

