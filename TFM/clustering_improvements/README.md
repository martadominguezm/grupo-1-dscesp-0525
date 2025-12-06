# 🚀 Clustering Improvements - Tarea 3 Optimizada

Esta carpeta contiene las mejoras y optimizaciones del clustering original.

## 📂 Estructura

```
clustering_improvements/
├── notebooks/              # Notebooks de análisis y mejoras
│   ├── 01_cluster_optimization.ipynb       # Optimización de número de clusters
│   ├── 02_feature_engineering.ipynb        # Feature engineering avanzado
│   ├── 03_alternative_algorithms.ipynb     # DBSCAN, Hierarchical, etc.
│   ├── 04_cluster_profiling.ipynb          # Perfiles interpretativos
│   ├── 05_propensity_integration.ipynb     # Integración con modelos de propensión
│   └── 06_visualizations.ipynb             # Visualizaciones avanzadas
├── data/                   # Datos procesados
├── models/                 # Modelos entrenados mejorados
├── reports/                # Reportes y análisis
└── visualizations/         # Gráficos y dashboards
```

## 🎯 Mejoras Implementadas

### 1. Optimización de Clusters
- Métricas: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz
- Comparación de 4-10 clusters
- Análisis de estabilidad

### 2. Feature Engineering
- Recovery de variables eliminadas (entry_channel, gender)
- Variables de interacción entre productos
- Tendencias temporales de actividad
- Valor del cliente (CLV aproximado)

### 3. Algoritmos Alternativos
- K-Means optimizado
- DBSCAN (detección de outliers)
- Hierarchical Clustering (dendrogramas)
- Gaussian Mixture Models

### 4. Interpretabilidad
- Nombres de negocio para clusters
- Perfiles detallados por cluster
- Matriz de propensión por producto
- Recomendaciones de acción

### 5. Integración con Propensión
- Cluster como feature en modelos
- Score promedio por cluster
- Estrategias de campaña personalizadas

### 6. Visualizaciones
- t-SNE / UMAP en 2D/3D
- Dashboards interactivos
- Heatmaps de características
- Análisis de transiciones

## 📊 Archivos Originales (NO MODIFICADOS)

Los archivos originales se mantienen intactos en:
- `TFM/clustering/clustering_model.ipynb`
- `TFM/clustering/clustering_isma.ipynb`

## 🔧 Cómo usar

1. Ejecutar notebooks en orden numérico
2. Cada notebook es independiente pero se recomienda secuencia
3. Los resultados se guardan en carpetas correspondientes

## 📅 Historial

- **2024-12-05**: Estructura inicial creada
- **En progreso**: Implementación de mejoras
