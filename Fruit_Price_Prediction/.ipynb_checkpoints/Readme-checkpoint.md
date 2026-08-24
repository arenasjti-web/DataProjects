# Predicción de precios de frutas en Chile

Proyecto de Ciencia de Datos enfocado en la predicción del precio promedio semanal de frutas comercializadas en Chile mediante técnicas de Machine Learning.

El proyecto utiliza información pública proporcionada por la Oficina de Estudios y Políticas Agrarias (ODEPA), complementándola con variables temporales y meteorológicas para analizar los factores que influyen en el comportamiento de los precios y construir un modelo predictivo capaz de estimar el precio promedio de distintos productos.

## Objetivos

* Analizar la evolución de los precios de frutas comercializadas en Chile.
* Preparar y transformar los datos para su utilización en modelos de Machine Learning.
* Evaluar distintos algoritmos de regresión mediante validación cruzada.
* Seleccionar el modelo con mejor capacidad predictiva para estimar el precio promedio semanal.

## Dataset

El conjunto de datos contiene registros semanales desde **enero de 2020 hasta julio de 2026**, obtenidos desde el sistema de precios al consumidor de ODEPA.

Cada observación corresponde al precio registrado para un producto específico considerando variables como:

* Región.
* Punto de monitoreo.
* Producto y variedad.
* Calidad.
* Semana y fecha de observación.
* Precio mínimo.
* Precio máximo.
* Precio promedio.

Como parte del proceso de enriquecimiento del dataset, también se incorporaron variables temporales y meteorológicas para evaluar su aporte en la capacidad predictiva del modelo.

## Desarrollo del proyecto

El proyecto se desarrolló siguiendo un flujo típico de Machine Learning:

1. Limpieza y preparación de datos.
2. Análisis exploratorio de datos (EDA).
3. Ingeniería de características.
4. Selección de variables.
5. Comparación de modelos mediante validación cruzada.
6. Evaluación del modelo seleccionado sobre un conjunto de prueba independiente.
7. Exportación del pipeline para futuras predicciones.

## Modelos evaluados

Durante la etapa de selección se compararon los siguientes algoritmos de regresión:

* Regresión Lineal
* Árbol de Decisión
* Random Forest Regressor
* Gradient Boosting Regressor
* HistGradientBoosting Regressor

Todos los modelos fueron evaluados utilizando las mismas particiones de validación cruzada y las mismas métricas de desempeño para garantizar una comparación consistente.

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

## Fuente de los datos

Oficina de Estudios y Políticas Agrarias (ODEPA)

https://www.odepa.gob.cl/precios/consumidor?mobile=off
