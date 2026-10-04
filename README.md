# Ejercicios de Matriz de Leontief - La Guajira, Colombia

## Descripcion General

Este conjunto de tres ejercicios aplica la matriz insumo-producto de Leontief a la economia de La Guajira, Colombia, utilizando tres sectores economicos: Agricultura, Tecnologia y Servicios. Los ejercicios ilustran el uso y las bondades de esta herramienta para analizar las interacciones entre sectores y el impacto de cambios en la demanda final.

## Requerimientos

### Software
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Dependencias Python
Instale las dependencias ejecutando:

```bash
pip install pandas numpy matplotlib seaborn
```

| Paquete | Version minima | Descripcion |
|---------|---------------|-------------|
| pandas | 1.0 | Manipulacion y analisis de datos |
| numpy | 1.20 | Calculo numerico y operaciones matriciales |
| matplotlib | 3.0 | Generacion de graficos |
| seaborn | 0.11 | Visualizacion estadistica |

## Estructura del Proyecto

```
leontieff/
├── README_general.md                  # Este archivo
├── reporte_academico.tex              # Documento LaTeX principal (normas APA 7)
├── reporte_academico.pdf              # PDF generado
├── portada.tex                         # Hoja de presentacion universitaria
├── titulo.tex                          # Pagina de titulo APA 7
├── resumen.tex                         # Resumen del trabajo
├── introduccion.tex                    # Introduccion y objetivos
├── metodologia.tex                     # Metodologia y fuentes de datos
├── resultados_ejercicio1.tex           # Resultados ejercicio 1
├── resultados_ejercicio2.tex           # Resultados ejercicio 2
├── resultados_ejercicio3.tex           # Resultados ejercicio 3
├── conclusiones.tex                    # Conclusiones
├── referencias.tex                     # Referencias en formato APA 7
├── ejercicio1_matriz_basica/           # Ejercicio 1: Matriz de Leontief basica
│   ├── datos_guajira.csv
│   ├── leontieff.py
│   ├── resultados_leontieff.png
│   ├── resultados.txt
│   └── README.md
├── ejercicio2_impacto_demanda/         # Ejercicio 2: Impacto de demanda
│   ├── datos_impacto.csv
│   ├── impacto_demanda.py
│   ├── resultados_impacto.png
│   ├── resultados.txt
│   └── README.md
└── ejercicio3_escenarios/              # Ejercicio 3: Comparacion de escenarios
    ├── datos_escenarios.csv
    ├── escenarios.py
    ├── resultados_escenarios.png
    ├── resultados.txt
    └── README.md
```

## Ejecucion de los Ejercicios

### Ejercicio 1: Matriz de Leontief Basica

Calcula la matriz de coeficientes tecnicos, la matriz inversa de Leontief, la produccion total requerida y los multiplicadores de produccion.

```bash
cd ejercicio1_matriz_basica
python leontieff.py
```

**Salida generada:**
- `resultados_leontieff.png`: Graficos de resultados
- `resultados.txt`: Resultados numericos detallados

### Ejercicio 2: Impacto de un Aumento en la Demanda Final

Evalua como un aumento del 20% en la demanda final del sector Agricultura afecta la produccion total de todos los sectores.

```bash
cd ejercicio2_impacto_demanda
python impacto_demanda.py
```

**Salida generada:**
- `resultados_impacto.png`: Graficos comparativos
- `resultados.txt`: Resultados numericos detallados

### Ejercicio 3: Comparacion de Escenarios de Demanda

Compara tres escenarios de demanda final: conservador (-10%), base (demanda actual) y optimista (+15%).

```bash
cd ejercicio3_escenarios
python escenarios.py
```

**Salida generada:**
- `resultados_escenarios.png`: Graficos de comparacion
- `resultados.txt`: Resultados numericos detallados

### Ejecucion de todos los ejercicios

Para ejecutar los tres ejercicios desde la carpeta raiz:

```bash
cd ejercicio1_matriz_basica && python leontieff.py && cd ..
cd ejercicio2_impacto_demanda && python impacto_demanda.py && cd ..
cd ejercicio3_escenarios && python escenarios.py && cd ..
```

## Generacion del Documento PDF

Para generar el documento academico en formato PDF con normas APA 7:

```bash
cd leontieff
pdflatex reporte_academico.tex
pdflatex reporte_academico.tex  # Segunda pasada para indice y referencias
```

**Requisito:** TeX Live o MikTeX instalado en el sistema.

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

- **Agricultura**: Multiplicador de 1.62, enfocado en cultivos y ganaderia
- **Tecnologia**: Multiplicador de 1.67, sector industrial con encadenamientos hacia otros sectores
- **Servicios**: Multiplicador de 1.60, sector con mayor peso en la economia (comercio, transporte, administracion publica)

## Interpretacion

La matriz de Leontief permite analizar como un cambio en la demanda final de un sector afecta la produccion total de todos los sectores de la economia. Los multiplicadores indican el impacto total (directo e indirecto) que tiene cada sector sobre el conjunto de la economia local, demostrando la interconexion entre los diferentes sectores economicos.

## Referencias

- DANE. (2023). Cuentas Nacionales Departamentales. Departamento Administrativo Nacional de Estadistica.
- Camara de Comercio de La Guajira. (2024). Informe Socioeconomico de La Guajira.
- Leontief, W. (1936). Quantitative input-output relations in the economic system of the United States. The Review of Economics and Statistics, 18(3), 105-125.
- Miller, R. E., & Blair, P. D. (2009). Input-output analysis: Foundations and extensions. Cambridge University Press.
