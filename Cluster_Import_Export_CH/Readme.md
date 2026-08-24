# Comercio Exterior de Chile — Análisis y Clustering

Análisis exploratorio y segmentación no supervisada de operaciones de **comercio exterior de Chile**, separado en dos flujos: **importaciones y exportaciones**.

El proyecto busca identificar patrones en las operaciones comerciales y construir segmentos de operaciones con características similares según su magnitud, frecuencia, valor unitario, peso, rubro empresarial, país y vía de transporte.

## Objetivos

* Explorar la estructura y distribución de las operaciones de comercio exterior.
* Identificar relaciones y patrones entre variables numéricas y categóricas.
* Detectar valores extremos y sesgos presentes en las operaciones.
* Segmentar las operaciones mediante algoritmos de clustering.
* Evaluar estadísticamente la calidad y estabilidad de las segmentaciones.
* Traducir los clusters obtenidos en perfiles de negocio interpretables.

## Metodología

El análisis se desarrolla de forma independiente para **importaciones** y **exportaciones**, siguiendo un flujo de trabajo de análisis exploratorio, preparación de datos, modelado y caracterización de resultados.

### Análisis exploratorio

Se estudian variables relacionadas con:

* `total_operacion`
* `cantidad_operacion`
* `ticket_promedio`
* `peso_total`
* `rubro_empresa`
* `empresa`
* `pais`
* `via_transporte`

El análisis considera distribuciones, estadísticas descriptivas, correlaciones, composición categórica y detección de valores atípicos para comprender la estructura de los datos antes del modelado.

### Preprocesamiento

Las variables numéricas presentan una fuerte asimetría, especialmente en monto y peso. Para reducir el efecto de operaciones excepcionalmente grandes sobre las distancias utilizadas por los algoritmos, se aplica `log1p` seguido de estandarización mediante `StandardScaler`.

Las variables categóricas se transforman mediante `OneHotEncoder`.

`empresa` se excluye del clustering debido a su alta cardinalidad, mientras que `descripcion_arancel` se conserva para análisis posteriores, pero no se utiliza directamente en el cálculo de distancias.

### Clustering

Se utiliza **MiniBatchKMeans**, una variante de K-Means adecuada para trabajar con datasets de gran tamaño.

La selección de `k` se evalúa mediante:

* **Silhouette Score**
* **Método del codo / inercia**
* **Validación cruzada**
* Comparación con **K-Prototypes** como método alternativo para datos mixtos.

En el análisis de importaciones se estudian particularmente dos configuraciones:

* **k = 2:** máxima separación estadística.
* **k = 5:** mayor granularidad y capacidad de interpretación comercial.

## Resultados — Importaciones

El dataset de importaciones contiene aproximadamente **1,57 millones de operaciones**.

El análisis muestra que la estructura de los datos está fuertemente relacionada con la **magnitud de las operaciones**, más que con grupos completamente discretos.

### k = 2

El modelo obtiene un Silhouette Score de **0,2397**, siendo la mejor configuración según esta métrica.

La segmentación distingue principalmente entre:

* operaciones de menor magnitud;
* operaciones de mayor magnitud, con mayores valores de operación, cantidad, ticket promedio y peso.

La estabilidad del resultado es alta: la validación cruzada obtiene un silhouette medio de **0,2353**, con una desviación estándar de apenas **0,0009**.

### k = 5

Aunque presenta una separación estadística menor (**silhouette = 0,1451**), k = 5 permite obtener una segmentación más útil para interpretar distintos perfiles de operación.

Los cinco perfiles identificados se caracterizan aproximadamente como:

| Cluster | Perfil                                                   |
| ------- | -------------------------------------------------------- |
| 3       | Micro-operaciones: un solo envío, bajo valor y bajo peso |
| 4       | Operaciones pequeñas y livianas                          |
| 0       | Operaciones pequeñas con peso particularmente bajo       |
| 2       | Operaciones de alto valor unitario y baja frecuencia     |
| 1       | Operaciones de alto volumen y mayor frecuencia           |

Los clusters presentan tamaños razonablemente balanceados, sin grupos residuales de tamaño marginal. La segmentación permite distinguir no solo la **magnitud**, sino también la relación entre **frecuencia de operación y valor unitario**.

### Validación con K-Prototypes

Como contraste, se aplica K-Prototypes, que permite trabajar directamente con variables numéricas y categóricas mediante una función de distancia mixta.

Con `k = 2`, K-Prototypes obtiene un silhouette de **0,2366**, prácticamente equivalente al **0,2397** obtenido por K-Means.

Esta coincidencia indica que la separación observada no depende exclusivamente del algoritmo ni del one-hot encoding, sino que refleja una característica real de la estructura de las operaciones.

Además, la composición por vía de transporte muestra una diferencia relevante entre los dos grupos: el cluster de operaciones grandes concentra principalmente transporte **marítimo (73,4%)**, mientras que el cluster de operaciones pequeñas presenta una mayor proporción de transporte **aéreo (52,0%)**.

## Conclusiones

Los resultados muestran que las operaciones de importación no forman grupos perfectamente separados, sino que presentan principalmente un **continuo de magnitud y volumen**.

Desde una perspectiva estadística, `k = 2` es la segmentación más sólida y estable. Sin embargo, para análisis comercial, `k = 5` entrega una caracterización más rica al separar operaciones según magnitud, frecuencia y valor unitario.

Por lo tanto:

* **k = 2** resulta adecuado para una clasificación simple de operaciones grandes vs. pequeñas.
* **k = 5** resulta más apropiado cuando se busca construir perfiles comerciales diferenciados.

El hecho de que ningún modelo probado supere aproximadamente un silhouette de **0,27** también constituye un resultado relevante: aumentar el número de clusters no revela grupos naturales claramente separados, sino que divide progresivamente un espectro continuo de operaciones.

## Tecnologías

* Python
* Pandas
* NumPy
* Scikit-learn
* Seaborn
* Matplotlib
* MiniBatchKMeans
* K-Prototypes
* Jupyter Notebook

## Estructura del proyecto

```text
├── Data/
│   ├── Processed/
│   └── ...
├── Notebooks/
│   ├── ...
│   └── ...
├── README.md
└── ...
```

## Alcance y próximos pasos

Entre las posibles extensiones del proyecto se consideran:

* tratar las operaciones del percentil superior como un segmento específico de operaciones excepcionales;
* profundizar la caracterización por rubro y país;
* incorporar información más detallada de productos o partidas arancelarias;
* explorar distintas ponderaciones de variables categóricas en K-Prototypes;
* evaluar métodos alternativos de clustering, como Gaussian Mixture Models;
* extender y comparar los resultados obtenidos para importaciones y exportaciones.

---

**Proyecto de Data Analysis & Unsupervised Learning**
Análisis de comercio exterior de Chile mediante exploración de datos, segmentación y validación estadística.
