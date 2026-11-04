# -*- coding: utf-8 -*-
"""Comparación reproducible mediante varias semillas por configuración."""

from collections import defaultdict
from pathlib import Path
import random
import sys
from statistics import mean, stdev

from deap import algorithms, base, tools

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = Path(__file__).resolve().parent / "datos"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import evol_simple.ConfiguracionSolucion as cs
import evol_simple.CicloEvolutivo as ce
import evol_simple.EstadisticasEvolucion as ee
import LecturaDatos as ld


ARCHIVOS_DATOS = ("datos1.csv", "datos2.csv", "datos3.csv")
NUMEROS_GENERACIONES = (20, 30, 40, 50)
SEMILLAS = (101, 202, 303, 404, 505, 606, 707, 808, 909, 1010)
TAMANO_POBLACION = 25
PROBABILIDAD_CRUCE = 0.75
PROBABILIDAD_MUTACION = 0.20


def configura_toolbox():
    """Configura la representación de individuos y los operadores."""
    toolbox = base.Toolbox()
    cs.configura_poblacion(toolbox)
    ce.configuracion_algoritmo(toolbox)
    return toolbox


def configura_experimentos():
    """Añade una repetición y una semilla a cada configuración de v2."""
    experimentos = []

    for archivo_datos in ARCHIVOS_DATOS:
        for numero_generaciones in NUMEROS_GENERACIONES:
            for numero_repeticion, semilla in enumerate(SEMILLAS, start=1):
                experimentos.append({
                    "archivo_datos": DATA_PATH / archivo_datos,
                    "parametros": {
                        "tamano_poblacion": TAMANO_POBLACION,
                        "probabilidad_cruce": PROBABILIDAD_CRUCE,
                        "probabilidad_mutacion": PROBABILIDAD_MUTACION,
                        "numero_generaciones": numero_generaciones,
                        "numero_repeticion": numero_repeticion,
                        "semilla": semilla,
                    },
                })

    return experimentos


def ejecuta_experimento(experimento, toolbox, estadisticas, verbose=False):
    """Ejecuta una repetición y devuelve la configuración y sus resultados."""
    parametros = experimento["parametros"]
    random.seed(parametros["semilla"])
    ld.carga_datos(experimento["archivo_datos"])
    cs.configura_poblacion(toolbox)
    poblacion_inicial = toolbox.population(n=parametros["tamano_poblacion"])

    poblacion_final, registro = algorithms.eaSimple(
        poblacion_inicial,
        toolbox,
        cxpb=parametros["probabilidad_cruce"],
        mutpb=parametros["probabilidad_mutacion"],
        ngen=parametros["numero_generaciones"],
        stats=estadisticas,
        verbose=verbose,
    )
    mejor_individuo = tools.selBest(poblacion_final, 1)[0]

    return {
        "experimento": experimento,
        "poblacion_final": poblacion_final,
        "registro": registro,
        "mejor_individuo": mejor_individuo,
        "mejor_fitness": mejor_individuo.fitness.values[0],
    }


def ejecuta_experimentos(experimentos, toolbox, estadisticas):
    """Ejecuta secuencialmente todas las configuraciones y repeticiones."""
    resultados = []

    for posicion, experimento in enumerate(experimentos, start=1):
        parametros = experimento["parametros"]
        print(
            f"[{posicion:>3}/{len(experimentos)}] "
            f"Datos={experimento['archivo_datos'].name}, "
            f"generaciones={parametros['numero_generaciones']}, "
            f"repetición={parametros['numero_repeticion']}, "
            f"semilla={parametros['semilla']}"
        )
        resultados.append(
            ejecuta_experimento(experimento, toolbox, estadisticas)
        )

    return resultados


def muestra_resultados_individuales(resultados):
    """Muestra la mejor solución obtenida en cada ejecución."""
    print("\nRESULTADOS INDIVIDUALES")
    print("=" * 80)

    for resultado in resultados:
        experimento = resultado["experimento"]
        parametros = experimento["parametros"]
        print(
            f"Datos: {experimento['archivo_datos'].name} | "
            f"Generaciones: {parametros['numero_generaciones']} | "
            f"Repetición: {parametros['numero_repeticion']} | "
            f"Semilla: {parametros['semilla']}"
        )
        print(f"Mejor solución: {resultado['mejor_individuo']}")
        print(f"Fitness: {resultado['mejor_fitness']:.6f}")
        print("-" * 80)


def resume_resultados(resultados):
    """Resume el fitness por conjunto de datos y número de generaciones."""
    fitness_por_configuracion = defaultdict(list)

    for resultado in resultados:
        experimento = resultado["experimento"]
        clave = (
            experimento["archivo_datos"].name,
            experimento["parametros"]["numero_generaciones"],
        )
        fitness_por_configuracion[clave].append(resultado["mejor_fitness"])

    print("\nRESUMEN POR CONFIGURACIÓN")
    print("=" * 80)
    print(
        f"{'Datos':<15} {'Generaciones':>12} {'Ejecuciones':>12} "
        f"{'Media':>14} {'Desv. típica':>14} {'Mínimo':>14} {'Máximo':>14}"
    )

    for (nombre_datos, generaciones), valores in sorted(
        fitness_por_configuracion.items()
    ):
        desviacion = stdev(valores) if len(valores) > 1 else 0.0
        print(
            f"{nombre_datos:<15} {generaciones:>12} {len(valores):>12} "
            f"{mean(valores):>14.6f} {desviacion:>14.6f} "
            f"{min(valores):>14.6f} {max(valores):>14.6f}"
        )


def visualiza_evolucion(resultados, nombre_datos, generaciones, repeticion=1):
    """Visualiza una ejecución concreta sin abrir una gráfica por repetición."""
    for resultado in resultados:
        experimento = resultado["experimento"]
        parametros = experimento["parametros"]
        coincide = (
            experimento["archivo_datos"].name == nombre_datos
            and parametros["numero_generaciones"] == generaciones
            and parametros["numero_repeticion"] == repeticion
        )
        if coincide:
            ee.visualiza_grafica(resultado["registro"])
            return

    print("No se encontró una ejecución con los criterios indicados.")


def main():
    toolbox = configura_toolbox()
    estadisticas = ee.configura_estadisticas_evolucion()
    experimentos = configura_experimentos()
    resultados = ejecuta_experimentos(experimentos, toolbox, estadisticas)
    muestra_resultados_individuales(resultados)
    resume_resultados(resultados)

    # Ejemplo opcional de una curva de convergencia:
    # visualiza_evolucion(resultados, "datos1.csv", 50, repeticion=1)


if __name__ == "__main__":
    main()
