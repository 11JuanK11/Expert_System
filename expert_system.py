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
#creacion ambiente de CLIPS
sistemaExperto= clips.Environment()
sistemaExperto.clear()

reglaMamiferoSemiacuatico = ("(defrule reglaMamiferoSemiacuatico (Marino)(Vertebrado)(Cuadrupedo) => (assert(MamiferoSemiacuatico)))")
reglaMamiferoAcuatico = ("(defrule reglaMamiferoAcuatico (Marino)(Vertebrado)(NoCuadrupedo) => (assert(MamiferoAcuatico)))")
reglaNoVertebradoMarinoCuadrupedo = ("(defrule reglaNoVertebradoMarinoCuadrupedo (Marino)(NoVertebrado)(Cuadrupedo) => (assert(NoVertebradoMarinoCuadrupedo)))")
reglaNoMamiferoSemiacuatico = ("(defrule reglaNoMamiferoSemiacuatico (Marino)(NoVertebrado)(NoCuadrupedo) => (assert(NoMamiferoSemiacuatico)))")
reglaMamiferoTerrestre = ("(defrule reglaMamiferoTerrestre (NoMarino)(Vertebrado)(Cuadrupedo) => (assert(MamiferoTerrestre)))")
reglaNoMamiferoTerrestre = ("(defrule reglaNoMamiferoTerrestre (NoMarino)(Vertebrado)(NoCuadrupedo) => (assert(NoMamiferoTerrestre)))")
reglaVertebradoNoMarinoCuadrupedo = ("(defrule reglaVertebradoNoMarinoCuadrupedo (NoMarino)(NoVertebrado)(Cuadrupedo) => (assert(VertebradoNoMarinoCuadrupedo)))")
reglaNoVertebradoNoMarinoNoCuadrupedo = ("(defrule reglaNoVertebradoNoMarinoNoCuadrupedo (NoMarino)(NoVertebrado)(NoCuadrupedo) => (assert(NoVertebradoNoMarinoNoCuadrupedo)))")

# Creación de las reglas en el sistema experto
sistemaExperto.build(reglaMamiferoSemiacuatico)
sistemaExperto.build(reglaMamiferoAcuatico)
sistemaExperto.build(reglaNoVertebradoMarinoCuadrupedo)
sistemaExperto.build(reglaNoMamiferoSemiacuatico)
sistemaExperto.build(reglaMamiferoTerrestre)
sistemaExperto.build(reglaNoMamiferoTerrestre)
sistemaExperto.build(reglaVertebradoNoMarinoCuadrupedo)
sistemaExperto.build(reglaNoVertebradoNoMarinoNoCuadrupedo)

#ejecutar ambiente de CLIPS (!IMPORTANTE)
caracteristicas = []
caracteres_a_eliminar = "()"
for fact in sistemaExperto.facts():
    fact = str(fact).translate(str.maketrans("", "", caracteres_a_eliminar))
    caracteristicas.append(fact)

sistemaExperto.run()

