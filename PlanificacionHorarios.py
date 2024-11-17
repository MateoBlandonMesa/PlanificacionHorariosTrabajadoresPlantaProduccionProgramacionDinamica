import numpy as np

#Creamos una lista con diccionarios con la información de cada trabajados
trabajadores = [

    {
        "nombre": "Luis",
        "habilidad": "Soldadura",
        "disponibilidad_de_horas": 40
    },
    {
        "nombre": "Ana",
        "habilidad": "Control de calidad",
        "disponibilidad_de_horas": 40
    },
    {
        "nombre": "Carlos",
        "habilidad": "Soldadura",
        "disponibilidad_de_horas": 40
    },
    {
        "nombre": "María",
        "habilidad": "Ensamblaje",
        "disponibilidad_de_horas": 40
    }

]

#Creamos una lista con diccionarios con la información los turnos
turnos = [
    {
        "requisitos_de_habilidades": ["Soldadura", "Ensamblaje"],
        "duracion_del_turno": 8,
        "prioridad": "Alta"
    },
    {
        "requisitos_de_habilidades": ["Control de calidad"],
        "duracion_del_turno": 6,
        "prioridad": "Media"
    },
    {
        "requisitos_de_habilidades": ["Soldadura"],
        "duracion_del_turno": 4,
        "prioridad": "Baja"
    },
    {
        "requisitos_de_habilidades": ["Ensamblaje"],
        "duracion_del_turno": 5,
        "prioridad": "Alta"
    }

]



#Asignamos las dimensiones de la matriz a llenar
n_trabajadores = len(trabajadores)
n_turnos = len(turnos)

#Matriz de ceros con los conteos de turnos
# indice de trabajdor (índice fila), índice del turno (índice de la columna)
conteo_trabajadores_vs_turno = np.zeros((n_trabajadores + 1, n_turnos + 1), dtype=int)

#Matriz con strings vacíos con las asignaciones de turno de cada iteración
asignaciones_trabajadores_vs_turno = np.empty((n_trabajadores + 1, n_turnos + 1), dtype=object)
asignaciones_trabajadores_vs_turno[:, :] = ""

def obtener_prioridad(prioridad):
    if prioridad == "Alta":
        return 3 # un truno de prioridad alta vale por 3 turnos
    elif prioridad == "Media":
        return 2 # un truno de prioridad media vale por 2 turnos
    else:
        return 1 # un truno de prioridad baja vale por 1


#Llenado de matriz
for i in range(1, n_trabajadores + 1):
    for j in range(1, n_turnos + 1):
        trabajador = trabajadores[i - 1]
        turno = turnos[j - 1]

        
        conteo_trabajadores_vs_turno[i][j] = conteo_trabajadores_vs_turno[i - 1][j] #traemos el valor anterior de conteo
        asignaciones_trabajadores_vs_turno[i, j] = asignaciones_trabajadores_vs_turno[i - 1, j] #traemos la asignación anterior

        #Filtro para verificar si el trabajador puede cubrir el turno
        if (trabajador["habilidad"] in turno["requisitos_de_habilidades"] and trabajador["disponibilidad_de_horas"] >= turno["duracion_del_turno"]):
            
            valor_nuevo = conteo_trabajadores_vs_turno[i - 1][j - 1] + obtener_prioridad(turno["prioridad"]) # conte de nuevo turno según la proridad


            # Actualizamos matríz de conteo y asignaciones si el nuevo valor es mejor
            if valor_nuevo > conteo_trabajadores_vs_turno[i][j]:
                conteo_trabajadores_vs_turno[i][j] = valor_nuevo
                asignacion_actual = f"{asignaciones_trabajadores_vs_turno[i - 1, j - 1]} | Trabajador: {trabajador['nombre']} - Turno: {turno}"
                asignaciones_trabajadores_vs_turno[i, j] = asignacion_actual


                trabajadores[i - 1]["disponibilidad_de_horas"] -= turno["duracion_del_turno"]

# Resultado óptimo
ponderacion_maximo_numero_de_turnos_cubiertos = conteo_trabajadores_vs_turno[n_trabajadores, n_turnos]
asignaciones_trabajadores_vs_turno_optimas = asignaciones_trabajadores_vs_turno[n_trabajadores, n_turnos]



print(f"Ponderación de máxima cantidad de turnos cubiertos según prioridad: {ponderacion_maximo_numero_de_turnos_cubiertos}")
print("'prioridad': 'Alta' -- valor por 3, 'prioridad': 'Media' -- valor por 2, 'prioridad': 'baja' -- valor por 1")
print(f"Maxima cantidad de turnos cubiertos: {len(asignaciones_trabajadores_vs_turno_optimas.strip(" | ").split(" | "))}")
print("asignaciones óptimas:")
for asignacion in asignaciones_trabajadores_vs_turno_optimas.strip(" | ").split(" | "):
    print(asignacion)