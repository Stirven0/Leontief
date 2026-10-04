# Ejercicios de Matriz de Leontief - La Guajira, Colombia

## Descripcion General

Este conjunto de tres ejercicios aplica la matriz insumo-producto de Leontief a la economia de La Guajira, Colombia, utilizando tres sectores economicos: Agricultura, Tecnologia y Servicios. Los ejercicios ilustran el uso y las bondades de esta herramienta para analizar las interacciones entre sectores y el impacto de cambios en la demanda final.

## Estructura de Ejercicios

### Ejercicio 1: Matriz de Leontief Basica
- **Carpeta**: `ejercicio1_matriz_basica/`
- **Contenido**: Calculo de coeficientes tecnicos, matriz inversa de Leontief, produccion total requerida y multiplicadores de produccion
- **Archivos**: `datos_guajira.csv`, `leontieff.py`, `resultados_leontieff.png`, `resultados.txt`, `README.md`

### Ejercicio 2: Impacto de un Aumento en la Demanda Final
- **Carpeta**: `ejercicio2_impacto_demanda/`
- **Contenido**: Evaluacion de como un aumento del 20% en la demanda de Agricultura afecta la produccion de todos los sectores
- **Archivos**: `datos_impacto.csv`, `impacto_demanda.py`, `resultados_impacto.png`, `resultados.txt`, `README.md`

### Ejercicio 3: Comparacion de Escenarios de Demanda
- **Carpeta**: `ejercicio3_escenarios/`
- **Contenido**: Comparacion de tres escenarios (conservador, base, optimista) y su efecto en la produccion requerida
- **Archivos**: `datos_escenarios.csv`, `escenarios.py`, `resultados_escenarios.png`, `resultados.txt`, `README.md`

## Fuentes de Datos

Los datos se estimaron basados en:
- DANE - Cuentas Nacionales Departamentales (PIB por sector)
- Camara de Comercio de La Guajira (Registro Mercantil)
- Estructura productiva de La Guajira (mineria, servicios publicos, agricultura)

## Metodologia General

1. **Matriz de Coeficientes Tecnicos (A)**: A = Z / X, donde Z son los flujos intersectoriales y X es la produccion total
2. **Matriz Inversa de Leontief**: (I - A)^-1, donde I es la matriz identidad
3. **Produccion Total Requerida**: X = (I - A)^-1 * D, donde D es el vector de demanda final
4. **Multiplicadores de Produccion**: Suma de cada columna de la matriz inversa de Leontief

## Resultados Principales

- **Agricultura**: Sector con menor multiplicador, enfocado en cultivos y ganaderia
- **Tecnologia**: Sector industrial con encadenamientos hacia otros sectores
- **Servicios**: Sector con mayor peso en la economia (comercio, transporte, administracion publica)

## Ejecucion

Para ejecutar cada ejercicio, navegue a la carpeta correspondiente y ejecute:

```bash
python leontieff.py          # Ejercicio 1
python impacto_demanda.py    # Ejercicio 2
python escenarios.py         # Ejercicio 3
```

## Interpretacion

La matriz de Leontief permite analizar como un cambio en la demanda final de un sector afecta la produccion total de todos los sectores de la economia. Los multiplicadores indican el impacto total (directo e indirecto) que tiene cada sector sobre el conjunto de la economia local, demostrando la interconexion entre los diferentes sectores economicos.
