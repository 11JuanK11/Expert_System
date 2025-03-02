import clips # type: ignore
with open("./data/animals.txt", "r") as testFile:
    print(testFile.read())

#creacion ambiente de CLIPS
sistemaExperto= clips.Environment()
sistemaExperto.clear()

# 
reglaCuadrupedos = ("(defrule reglaCuadrupedo (CuatroPatas) => (assert(Cuadrupedo)))")
reglaMarino = ("(defrule reglaMarino (ViveEnMar)=> (assert(Marino)))")
reglaVertebrados = ("(defrule reglaVertebrados (Columna) => (assert(Vertebrado)))")
reglaMarinoCuatroPatas = ("(defrule reglaMarinoCuatroPatas (ViveEnMar)(CuatroPatas) => (assert(MarinoCuatroPatas)))")
reglaMamiferoTerrestre = ("(defrule reglaMamiferoTerrestre (Vertebrado)(CuatroPatas)=> (assert(MamiferoTerrestre)))")
reglaMamiferoAcuatico = ("(defrule reglaMamiferoAcuatico (Marino)(Vertebrado) => (assert(MamiferoAcuatico)))")
reglaMamiferoSemiacuatico = ("(defrule reglaMamiferoSemiacuatico (Marino)(Vertebrado)(Cuadrupedo) => (assert(MamiferoSemiacuatico)))")

# Reglas en negativo
reglaNoCuadrupedos = ("(defrule reglaNoCuadrupedo (NoCuatroPatas) => (assert(NoCuadrupedo)))")
reglaNoMarino = ("(defrule reglaNoMarino (NoViveEnMar) => (assert(NoMarino)))")
reglaNoVertebrados = ("(defrule reglaNoVertebrados (NoColumna) => (assert(NoVertebrado)))")
reglaNoMarinoCuatroPatas = ("(defrule reglaNoMarinoCuatroPatas (NoViveEnMar)(NoCuatroPatas) => (assert(NoMarinoCuatroPatas)))")
reglaNoMamiferoTerrestre = ("(defrule reglaNoMamiferoTerrestre (Vertebrado)(NoCuatroPatas) => (assert(NoMamiferoTerrestre)))")
reglaNoMamiferoAcuatico = ("(defrule reglaNoMamiferoAcuatico (NoViveEnMar)(Vertebrado) => (assert(NoMamiferoAcuatico)))")
reglaNoMamiferoSemiacuatico = ("(defrule reglaNoMamiferoSemiacuatico (NoViveEnMar)(Vertebrado)(NoCuadrupedo) => (assert(NoMamiferoSemiacuatico)))")

# Nuevas reglas para "Marino y CuatroPatas" y sus negaciones

# Creación de las reglas en el sistema experto
sistemaExperto.build(reglaCuadrupedos)
sistemaExperto.build(reglaMarino)
sistemaExperto.build(reglaVertebrados)
sistemaExperto.build(reglaMarinoCuatroPatas)
sistemaExperto.build(reglaMamiferoTerrestre)
sistemaExperto.build(reglaMamiferoAcuatico)
sistemaExperto.build(reglaMamiferoSemiacuatico)
sistemaExperto.build(reglaNoCuadrupedos)
sistemaExperto.build(reglaNoMarino)
sistemaExperto.build(reglaNoVertebrados)
sistemaExperto.build(reglaNoMarinoCuatroPatas)
sistemaExperto.build(reglaNoMamiferoTerrestre)
sistemaExperto.build(reglaNoMamiferoAcuatico)
sistemaExperto.build(reglaNoMamiferoSemiacuatico)
#Mostrar las reglas ya creadas
for r in sistemaExperto.rules():
    print(r)

#quemar las afirmaciones
sistemaExperto.assert_string('(sol)')

#ingresar afirmaciones
elHecho=input("Digite hecho -> ")
sistemaExperto.assert_string(f"({elHecho})")

#mostrar hechos creados
for fact in sistemaExperto.facts():
    print(fact)

#que reglas ya se han activado dependiendo de las afirmaciones que se hayan ingresado
for ac in sistemaExperto.activations():
    print(ac)

#ejecutar ambiente de CLIPS (!IMPORTANTE)
sistemaExperto.run()

#Dependiendo de los hechos, hacer una cosa
for fact in sistemaExperto.facts():
    factString=str(fact)
    if "cuadrupedo" in factString:
        print ("Tiene 4 patas")
    if "marino" in factString:
        print ("Vive mayormente en el mar")
