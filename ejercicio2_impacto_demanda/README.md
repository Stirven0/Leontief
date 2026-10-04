# Ejercicio 2: Impacto de un Aumento en la Demanda Final

## Descripcion

Este ejercicio evalua como un aumento del 20% en la demanda final del sector Agricultura afecta la produccion total de todos los sectores de la economia de La Guajira.

## Estructura de Archivos

- `datos_impacto.csv`: Datos de flujos intersectoriales y demanda final
- `impacto_demanda.py`: Script principal con calculos y graficos
- `resultados_impacto.png`: Graficos generados
- `resultados.txt`: Resultados numericos detallados

## Metodologia

1. Cargar datos del ejercicio 1
2. Calcular matriz de coeficientes tecnicos (A)
3. Calcular matriz inversa de Leontief (I - A)^-1
4. Aumentar 20% la demanda final del sector Agricultura
5. Calcular nueva produccion total requerida
6. Comparar produccion original vs nueva produccion
7. Generar graficos de barras comparativos

## Resultados Principales

- El aumento del 20% en demanda de Agricultura genera un efecto multiplicador en todos los sectores
- El sector Agricultura es el que mayor impacto directo recibe
- Los sectores Tecnologia y Servicios tambien se ven afectados debido a los encadenamientos productivos

## Ejecucion

```bash
python impacto_demanda.py
```
