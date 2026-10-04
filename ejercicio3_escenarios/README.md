# Ejercicio 3: Comparacion de Escenarios de Demanda Final

## Descripcion

Este ejercicio compara tres escenarios de demanda final (conservador, base, optimista) y calcula la produccion total requerida para cada uno, permitiendo visualizar el impacto de diferentes politicas economicas o choques externos.

## Estructura de Archivos

- `datos_escenarios.csv`: Datos de flujos intersectoriales y demanda final
- `escenarios.py`: Script principal con calculos y graficos
- `resultados_escenarios.png`: Graficos generados
- `resultados.txt`: Resultados numericos detallados

## Metodologia

1. Cargar datos del ejercicio 1
2. Calcular matriz de coeficientes tecnicos (A)
3. Calcular matriz inversa de Leontief (I - A)^-1
4. Definir 3 escenarios de demanda final:
   - Conservador: -10% en todos los sectores
   - Base: demanda actual
   - Optimista: +15% en todos los sectores
5. Calcular produccion requerida para cada escenario
6. Generar tabla comparativa y graficos de barras agrupadas

## Resultados Principales

- El escenario conservador muestra una reduccion en la produccion de todos los sectores
- El escenario base refleja la situacion actual de la economia
- El escenario optimista muestra un aumento significativo en la produccion requerida
- Los multiplicadores de Leontief amplifican el impacto de los cambios en la demanda

## Ejecucion

```bash
python escenarios.py
```
