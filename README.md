# Análisis de Datos: Titanic

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre el famoso dataset del Titanic. Incluye limpieza de datos, visualizaciones y generación de un dataset limpio listo para modelado como asi tambien la generacion de algunos graficos de referencia.

## Estructura del Proyecto

- `titanic_analysis.py`: Script principal para cargar, limpiar y analizar el dataset.
- `survival_by_gender.png`: Gráfico de supervivencia por género.
- `age_distribution.png`: Histograma de distribución de edades.
- `fare_by_class.png`: Boxplot de tarifas por clase.
- `titanic_cleaned.csv`: Dataset limpio generado por el script.

## Requisitos

- Python 3.x
- pandas
- seaborn
- matplotlib

Instala las dependencias con:

```sh
pip install pandas seaborn matplotlibData Analysis  Projects

### Ejecucion
python [titanic_analysis.py](http://_vscodecontentref_/0)

## Descripción del Análisis
* Carga de datos: Descarga el dataset desde GitHub.
* Limpieza: Imputa valores faltantes, elimina columnas irrelevantes y codifica variables categóricas.
* EDA: Estadísticas descriptivas y correlaciones.
* Visualizaciones: Supervivencia por género, distribución de edad y tarifas por clase.
* Exportación: Guarda el dataset limpio en titanic_cleaned.csv.
