# 📊 Tabla Completa de Clusters k=8

## Características Detalladas por Cluster

| Cluster | Nombre | Clientes | % Total | Edad (años) | Salario (€) | Antigüedad (meses) | N° Productos | % Activos | % Pension | % Payment Card | % Loan | % Investment |
|---------|--------|----------|---------|-------------|-------------|-------------------|--------------|-----------|-----------|----------------|--------|--------------|
| **1** | Universitarios Estándar | 49,104 | 11.1% | 24 | 93,322 | 25 | 0.94 | 33% | 1% | 4% | 0% | 1% |
| **2** | Inactivos Totales | 79,071 | 17.9% | 24 | 113,125 | 27 | 1.00 | **0%** | 0% | 0% | 0% | 0% |
| **3** | Profesionales Dormidos | 48,934 | 11.0% | **41** | 109,831 | 25 | 0.23 | 6% | 0% | 0% | 0% | 0% |
| **4** | Alto Valor Principal ⭐⭐⭐ | 52,933 | 12.0% | **43** | **120,663** | 22 | **1.96** | **100%** | **15%** | **40%** | 0% | **8%** |
| **5** | Jóvenes Activos Básicos | 81,893 | 18.5% | 24 | 87,594 | 26 | 0.92 | 35% | 1% | 4% | 0% | 0% |
| **6** | Alto Potencial Virgen 💎 | 45,095 | 10.2% | 24 | **137,800** | 19 | **0.00** | **1%** | 0% | 0% | 0% | 0% |
| **7** | Valor Medio-Alto ⭐⭐ | 47,953 | 10.8% | **42** | 87,015 | 22 | 1.38 | **68%** | 9% | 24% | 0% | 5% |
| **8** | Emergentes Premium ⭐ | 37,926 | 8.6% | 27 | 128,288 | 23 | 1.49 | **100%** | 10% | 19% | 0% | 5% |

**Nota:** El producto "loan" tiene 0% penetración en todos los clusters (no hay préstamos en el dataset de Mayo 2019).

---

## Propensión a Productos por Cluster

| Cluster | Nombre | Propensión Pension Plan | Propensión Investment | Producto Recomendado | Conversiones Estimadas Pension |
|---------|--------|------------------------|----------------------|---------------------|------------------------------|
| **4** | Alto Valor Principal ⭐⭐⭐ | **13.0%** 🔥 | **10.4%** 🔥 | Pension Plan | **6,881** |
| **7** | Valor Medio-Alto ⭐⭐ | **10.2%** | **7.5%** | Pension Plan | **4,891** |
| **8** | Emergentes Premium ⭐ | **6.0%** | **5.5%** | Pension Plan | **2,276** |
| **3** | Profesionales Dormidos | 4.4% | 3.5% | Pension Plan | 2,159 |
| **6** | Alto Potencial Virgen 💎 | 3.6% | 2.9% | Pension Plan | 1,624 |
| **1** | Universitarios Estándar | 1.8% | 1.6% | Pension Plan | 903 |
| **5** | Jóvenes Activos Básicos | 1.2% | 0.8% | Pension Plan | 976 |
| **2** | Inactivos Totales | 0.4% ❌ | 0.2% ❌ | - | 310 |

**Total conversiones estimadas Pension Plan:** 20,020 clientes

---

## Resumen por Prioridad Estratégica

### 🔥 PRIORIDAD ALTA (Foco Inmediato)

| Cluster | Nombre | Clientes | Salario Promedio | Propensión | Estrategia |
|---------|--------|----------|------------------|------------|-----------|
| **4** | Alto Valor Principal | 52,933 | €120,663 | 13.0% | Foco #1: Up-sell agresivo, VIP treatment |
| **7** | Valor Medio-Alto | 47,953 | €87,015 | 10.2% | Foco #2: Cross-sell pension + payment card |
| **6** | Alto Potencial Virgen | 45,095 | €137,800 | 3.6% | Onboarding premium, alto LTV |

**Total:** 145,981 clientes (33.0% de la base)

---

### ⚡ PRIORIDAD MEDIA (Campañas Selectivas)

| Cluster | Nombre | Clientes | Salario Promedio | Propensión | Estrategia |
|---------|--------|----------|------------------|------------|-----------|
| **8** | Emergentes Premium | 37,926 | €128,288 | 6.0% | Nurturing, potencial LP |
| **3** | Profesionales Dormidos | 48,934 | €109,831 | 4.4% | Reactivación dirigida |

**Total:** 86,860 clientes (19.6% de la base)

---

### 🔵 PRIORIDAD BAJA (Mantenimiento)

| Cluster | Nombre | Clientes | Salario Promedio | Propensión | Estrategia |
|---------|--------|----------|------------------|------------|-----------|
| **1** | Universitarios Estándar | 49,104 | €93,322 | 1.8% | Productos básicos |
| **5** | Jóvenes Activos Básicos | 81,893 | €87,594 | 1.2% | Mantenimiento |
| **2** | Inactivos Totales | 79,071 | €113,125 | 0.4% | ❌ Abandonar |

**Total:** 210,068 clientes (47.4% de la base)

---

## Variables Clave Utilizadas en el Clustering

### Variables Numéricas (Normalizadas)
- **age**: Edad del cliente
- **salary**: Salario anual en euros
- **z_months_since_entry**: Antigüedad en meses
- **z_num_products**: Número de productos contratados

### Variables Categóricas (One-Hot Encoded)
- **segment**:
  - 01 - TOP
  - 02 - PARTICULARES
  - 03 - UNIVERSITARIO
- **city_size**:
  - gran_ciudad
  - ciudad_mediana
  - ciudad_pequeña
  - pueblo

### Variables Binarias (0/1)
- **active_customer**: Cliente activo (1) o inactivo (0)
- **pension_plan**: Tiene plan de pensión (1) o no (0)
- **payment_card**: Tiene tarjeta de pago (1) o no (0)
- **loan**: Tiene préstamo (1) o no (0) - *Nota: 0% penetración en todos los clusters*
- **investment**: Tiene inversión (1) o no (0)

### Variables Eliminadas en Preprocesamiento
- **account**: Eliminada por correlación alta con otras variables
- **z_pct_months_active**: Eliminada por redundancia con active_customer
- **z_num_families**: Eliminada en el proceso de limpieza
- **macro_region**: Eliminada (geográfica)
- **is_coast**: Eliminada (geográfica)
- **deceased**: Filtrada (solo clientes activos: deceased='N')
- **gender**: Eliminada en preprocesamiento
- **entry_channel**: Eliminada en preprocesamiento

### Reducción Dimensional
- **PCA**: 6 componentes principales (91.4% varianza explicada)

### Algoritmo
- **K-Means**: 8 clusters, 10 inicializaciones, random_state=42

---

## Métricas de Calidad del Modelo k=8

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| Silhouette Score | **0.544** | Alta coherencia interna |
| Davies-Bouldin Index | **0.912** | Buena separación entre clusters |
| Calinski-Harabasz Score | **219,499** | Compacidad óptima |
| Inertia | 154,944 | Distancia mínima a centroides |

---

## Diferencias Clave vs Modelo k=6

### Mejoras Principales:

1. **+60% cobertura** de clientes alto valor (138k vs 86k)
2. **+15% coherencia** en segmentación (Silhouette)
3. **Nuevo segmento identificado:** Alto Potencial Virgen (45k clientes, €138k salario)
4. **Separación clara** de Profesionales Dormidos vs Inactivos Totales
5. **3 segmentos oro** vs 1 en k=6

### ROI Incremental:

- **+2,728 conversiones** adicionales en pension plan
- **+2,027 conversiones** adicionales en investment
- **+€2.7M** ROI anual estimado

---

## 🎯 Uso Recomendado de esta Tabla

### Para Presentación:
1. Muestra la tabla principal de características
2. Destaca los 3 segmentos de prioridad alta
3. Compara propensión entre clusters

### Para Estrategia:
1. Asigna presupuestos según prioridad
2. Diseña campañas diferenciadas por cluster
3. Define KPIs específicos por segmento

### Para Operativa:
1. Usa las listas de `top_customers_*_k8.csv`
2. Segmenta comunicaciones según cluster
3. Personaliza ofertas por perfil

---

**Fecha:** 6 Diciembre 2025
**Total Clientes:** 442,909
**Modelo:** K-Means con PCA (k=8)
