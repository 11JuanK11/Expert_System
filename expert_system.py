import clips # type: ignore
with open("./data/test.txt", "r") as testFile:
    print(testFile.read())

sistemaExperto= clips.Environment()
sistemaExperto.clear()
reglaLloviendo = ("(defrule reglaLloviendo (lloviendo) => (assert(abrirParaguas)))")
reglaBloqueador = ("(defrule reglaBloqueador (sol)=> (assert(usarBloqueador)))")

sistemaExperto.build(reglaLloviendo)
sistemaExperto.build(reglaBloqueador)

for r in sistemaExperto.rules():
    print(r)

sistemaExperto.assert_string('(sol)')

elHecho=input("Digite hecho -> ")
sistemaExperto.assert_string(f"({elHecho})")

for fact in sistemaExperto.facts():
    print(fact)

for ac in sistemaExperto.activations():
    print(ac)

sistemaExperto.run()

for fact in sistemaExperto.facts():
    factString=str(fact)
    if "abrirParaguas" in factString:
        print ("abrir el paraguas que se moja")
    if "usarBloqueador" in factString:
        print ("protegerse la piel del sol con bloqueador")
