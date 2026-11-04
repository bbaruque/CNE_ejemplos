# -*- coding: utf-8 -*-
"""Comparación de experimentos evolutivos con estadísticas por configuración."""

from collections import defaultdict
from pathlib import Path
import sys

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
    """Crea un experimento por cada conjunto de datos y número de generaciones."""
    experimentos = []

    for archivo_datos in ARCHIVOS_DATOS:
        for numero_generaciones in NUMEROS_GENERACIONES:
            experimentos.append({
                "archivo_datos": DATA_PATH / archivo_datos,
                "parametros": {
                    "tamano_poblacion": TAMANO_POBLACION,
                    "probabilidad_cruce": PROBABILIDAD_CRUCE,
                    "probabilidad_mutacion": PROBABILIDAD_MUTACION,
                    "numero_generaciones": numero_generaciones,
                },
            })

    return experimentos


def ejecuta_experimentos(experimentos, toolbox, estadisticas):
    """Ejecuta cada configuración y conserva sus resultados."""
    resultados = []

    for posicion, experimento in enumerate(experimentos, start=1):
        parametros = experimento["parametros"]
        print(
            f"[{posicion}/{len(experimentos)}] "
            f"{experimento['archivo_datos'].name}, "
            f"{parametros['numero_generaciones']} generaciones"
        )

        ld.carga_datos(experimento["archivo_datos"])
        cs.configura_poblacion(toolbox)

        poblacion_inicial = toolbox.population(n=parametros["tamano_poblacion"])
        poblacion_final, registro = algorithms.eaSimple(
            poblacion_inicial,
            toolbox,
            cxpb=parametros["probabilidad_cruce"],
            mutpb=parametros["probabilidad_mutacion"],
            ngen=parametros["numero_generaciones"],
            verbose=False,
            stats=estadisticas,
        )

        mejor_individuo = tools.selBest(poblacion_final, 1)[0]
        resultados.append({
            "experimento": experimento,
            "poblacion_final": poblacion_final,
            "registro": registro,
            "mejor_individuo": mejor_individuo,
            "mejor_fitness": mejor_individuo.fitness.values[0],
        })

    return resultados


def analiza_resultados(resultados):
    """Muestra estadísticas finales y la evolución de cada experimento."""
    for resultado in resultados:
        experimento = resultado["experimento"]
        parametros = experimento["parametros"]
        ultima_generacion = resultado["registro"][-1]

        print(
            f"\nDatos: {experimento['archivo_datos'].name} | "
            f"Generaciones: {parametros['numero_generaciones']}"
        )
        print(f"Mejor solución: {resultado['mejor_individuo']}")
        print(f"Fitness: {resultado['mejor_fitness']:.4f}")
        print(
            "Estadísticas finales: "
            f"media={ultima_generacion['avg']:.4f}, "
            f"desviación={ultima_generacion['std']:.4f}, "
            f"mínimo={ultima_generacion['min']:.4f}, "
            f"máximo={ultima_generacion['max']:.4f}"
        )
        ee.visualiza_grafica(resultado["registro"])


def compara_experimentos(resultados):
    """Compara generaciones por separado para cada conjunto de datos."""
    fitness_por_configuracion = defaultdict(list)

    for resultado in resultados:
        experimento = resultado["experimento"]
        clave = (
            experimento["archivo_datos"].name,
            experimento["parametros"]["numero_generaciones"],
        )
        fitness_por_configuracion[clave].append(resultado["mejor_fitness"])

    promedios = {
        clave: sum(valores) / len(valores)
        for clave, valores in fitness_por_configuracion.items()
    }
    generacion_base = min(NUMEROS_GENERACIONES)

    print("\nCOMPARACIÓN POR CONJUNTO DE DATOS")
    print(
        f"{'Datos':<15} {'Generaciones':>12} "
        f"{'Fitness medio':>15} {'Mejora vs base':>16}"
    )
    print("-" * 62)

    for nombre_datos, generaciones in sorted(promedios):
        promedio = promedios[(nombre_datos, generaciones)]
        referencia = promedios.get((nombre_datos, generacion_base))
        if generaciones == generacion_base or referencia is None:
            mejora = "-"
        elif referencia == 0:
            mejora = "n/a"
        else:
            mejora = f"{(promedio - referencia) / abs(referencia) * 100:+.1f}%"

        print(
            f"{nombre_datos:<15} {generaciones:>12} "
            f"{promedio:>15.4f} {mejora:>16}"
        )


def main():
    toolbox = configura_toolbox()
    estadisticas = ee.configura_estadisticas_evolucion()
    experimentos = configura_experimentos()
    resultados = ejecuta_experimentos(experimentos, toolbox, estadisticas)
    analiza_resultados(resultados)
    compara_experimentos(resultados)


if __name__ == "__main__":
    main()
