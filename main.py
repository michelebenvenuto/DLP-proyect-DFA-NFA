from direct_construction import Tree
from thomson import Thomson


print("Proyecto 1 Analizador Lexico")
print("Autor: Michele Benvenuto")
print("Carnet: 18232")
wantsToContinue = True
while wantsToContinue:
    print("Ingrese una expresion regular:")
    regex = input()
    print("Generando DFAs y NFAs...")
    thomson = Thomson(regex)
    tree = Tree(regex)
    thomsonNFA = thomson.createNfafromRegex()
    thomsonDFA = thomsonNFA.generateDFA()
    thomsonDFA.clean()
    thomsonDFA.graph("thomson DFA Render")
    treeDFA = tree.generate_DFA()
    treeDFA.clean()
    treeDFA.graph("Direct Construction Render")
    print("---------------------------------------")
    print("Automatas Generados!")
    print("Puede ver los renders resultantes en los archivos:")
    print("Thomson DFA Render")
    print("Direct Construction Render")
    print("---------------------------------------")

    continueWithSameRegex = True
    while continueWithSameRegex:
        print("Ingrese la cadena que quiere validar:")
        cadena = input()
        resultThomson = thomsonDFA.simulate(cadena)
        resultDirect = treeDFA.simulate(cadena)
        print("---------------------------------------")
        print("Segun el Automata generado por Thomson la candena pertenece? ", resultThomson)
        print("Segun el Automata generado por Construccion directa la candena pertenece? ", resultDirect)
        print("---------------------------------------")
        more = input("Validar otra cadena? [y/n]")
        if more == "n":
            continueWithSameRegex = False
    print("---------------------------------------")
    more = input("Probar otra regex? [y/n]")
    if more == "n":
        wantsToContinue = False
        print("Cerrando programa..")

