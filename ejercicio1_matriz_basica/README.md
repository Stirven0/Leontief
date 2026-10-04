# Ejercicio de Matriz de Leontief - La Guajira, Colombia

## Descripcion

Este ejercicio aplica la matriz insumo-producto de Leontief a la economia de La Guajira, Colombia, utilizando tres sectores economicos: Agricultura, Tecnologia y Servicios.

## Estructura de Archivos

- `datos_guajira.csv`: Datos de flujos intersectoriales y demanda final (en miles de millones de pesos)
- `leontieff.py`: Script principal con calculos y generacion de graficos
- `resultados_leontieff.png`: Graficos generados (matriz A, inversa de Leontief, multiplicadores)
- `resultados.txt`: Resultados numericos detallados

## Fuentes de Datos

Los datos se estimaron basados en:
- DANE - Cuentas Nacionales Departamentales (PIB por sector)
- Cámara de Comercio de La Guajira (Registro Mercantil)
- Estructura productiva de La Guajira (mineria, servicios publicos, agricultura)

## Metodologia

1. **Matriz de Coeficientes Tecnicos (A)**: Se calcula como A = Z / X, donde Z son los flujos intersectoriales y X es la produccion total.

2. **Matriz Inversa de Leontief**: Se calcula como (I - A)^-1, donde I es la matriz identidad.

3. **Produccion Total Requerida**: Se calcula como X = (I - A)^-1 * D, donde D es el vector de demanda final.

4. **Multiplicadores de Produccion**: Se calculan como la suma de cada columna de la matriz inversa de Leontief.

## Resultados Principales

- **Agricultura**: Sector con menor multiplicador, enfocado en cultivos y ganaderia
- **Tecnologia**: Sector industrial con encadenamientos hacia otros sectores
- **Servicios**: Sector con mayor peso en la economia (comercio, transporte, administracion publica)

## Ejecucion

```bash
python leontieff.py
```

## Interpretacion

La matriz de Leontief permite analizar como un cambio en la demanda final de un sector afecta la produccion total de todos los sectores de la economia. Los multiplicadores indican el impacto total (directo e indirecto) que tiene cada sector sobre el conjunto de la economia local.
