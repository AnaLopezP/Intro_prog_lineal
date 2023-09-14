#importamos la librería necesaria
from ortools.linear_solver import pywraplp

#Creamos el solucionador que usaremos más adelante
solucionador = pywraplp.Solver("Maximiza el poder del ejército", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Creamos las variables
espadachin = solucionador.IntVar(0, solucionador.infinity(), "espadachín") #Los dos primeros argumentos indican que la variable va de 0 a infinito
arquero = solucionador.IntVar(0, solucionador.infinity(), "arquero")
jinete = solucionador.IntVar(0, solucionador.infinity(), "jinete")

#Añadimos las ecuaciones que indican los gastos por guerrero
solucionador.Add(140*jinete + 80*arquero + 60*espadachin <= 1200) #Gasto de comida por guerrero
solucionador.Add(10*arquero + 20*espadachin <= 800) #Gasto de madera por guerrero
solucionador.Add(100*jinete + 40*arquero <= 600) #Gasto de oro por guerrero

#Añadimos la función que queremos maximizar 
solucionador.Maximize(230*jinete + 95*arquero + 70*espadachin) #Es el poder que da cada guerrero, queremos el num de guerreros que maximice la función

#Ahora que ya tenemos todo, resolvemos el problema (primero se intenta, que igual no se puede)
estado = solucionador.Solve()

#Enseñamos los resultados si se han encontrado
if estado == pywraplp.Solver.OPTIMAL:
    print("---------------SOLUCIÓN----------------")
    print("\n")
    print(f"Poder óptimo = {solucionador.Objective().Value()}")
    print("\n")
    print("EJERCITO:")
    print(f"- Espadachines = {espadachin.solution_value()}")
    print(f"- Arqueros = {arquero.solution_value()}")
    print(f"- Jinetes = {jinete.solution_value()}")