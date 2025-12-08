# PRESENTACIÓN TFM - EASYMONEY
## Optimización de Captación, Retención y Rentabilidad mediante Data Science

**Duración total:** 20 minutos (4 personas × 5 min)
**Audiencia:** Especialistas en Marketing
**Objetivo:** Presentar solución de marketing basada en datos para maximizar rentabilidad

---

## 🎯 TAREA 1: CONTEXTO NEGOCIO + EDA + POWERBI (5 min)
**Presentador:** Persona 1
**Slides:** 1-7

### SLIDE 1: PORTADA
**Título:** easyMoney: Maximización de Rentabilidad mediante Analítica Predictiva
**Subtítulo:** Estrategia de Marketing Data-Driven para Optimizar Captación y Retención
**Grupo 1 - Nuclio Digital School 2025**

---

### SLIDE 2: SITUACIÓN ACTUAL - EL DESAFÍO
**Título:** easyMoney: Crisis de Rentabilidad

**Contenido:**
- **Empresa:** Plataforma multi-canal de productos financieros (4 años)
- **Problema crítico:** Fondos agotados sin EBITDA positivo
- **Presión inversores:** Lion Global exige rentabilidad AHORA
- **Cambio estratégico:** De captación agresiva → Rentabilización cartera actual

**Cifras clave:**
- 442,000 clientes activos (Mayo 2019)
- 5 familias de productos (Cuentas, Tarjetas, Pensiones, Inversión, Préstamos)
- Único proveedor: easyBanking S.A.

**Desafío:** ¿Cómo maximizar ingresos de la base actual sin invertir en captación masiva?

---

### SLIDE 3: NUESTRA SOLUCIÓN - 4 PILARES ANALÍTICOS
**Título:** Metodología: De Datos a Decisiones Comerciales

**Diagrama de flujo:**
```
[DATOS] → [ANÁLISIS] → [ESTRATEGIA] → [ACCIÓN]
```

**Los 4 pilares:**

1. **📊 EDA + CALIDAD DE DATOS (PowerBI)**
   - Exploración 442K clientes, 17 meses históricos
   - Dashboard ejecutivo para monitorización

2. **🎯 PROPENSIÓN DE COMPRA**
   - ¿Quién comprará? Modelos predictivos por producto
   - Priorización de campañas

3. **👥 SEGMENTACIÓN (CLUSTERING)**
   - ¿Cómo son? 6 perfiles de cliente
   - Personalización de mensajes

4. **💰 VALOR DEL CLIENTE**
   - ¿Dónde invertir? Priorización por margen
   - ROI de campañas

---

### SLIDE 4: POWERBI - VISIÓN 360º DEL NEGOCIO
**Título:** Dashboard Ejecutivo: Monitorización en Tiempo Real

**Contenido:**
Incluir **IMAGEN 3** (Dashboard temporal y geográfico)

**Métricas clave Mayo 2019:**
- **10,211 ventas** en el mes
- **€8.07M beneficio** acumulado
- **€606.88 margen medio** por venta

**Insights visuales:**
- **Estacionalidad:** Pico de ventas en Octubre (28K ventas)
- **Geografía:** Madrid y Málaga lideran en margen medio (€728-707)
- **Tendencia:** Caída vs 2018 (-3,000 ventas/mes promedio)

---

### SLIDE 5: POWERBI - PERFIL DEMOGRÁFICO Y TERRITORIAL
**Título:** ¿Dónde Están Nuestros Mejores Clientes?

**Contenido:**
Incluir **IMAGEN 4** (Densidad clientes + análisis demográfico)

**Hallazgos clave:**

**Por edad:**
- **296K clientes (67%) tienen 20-30 años** → Foco juventud
- Solo 82K en 30s, decrecimiento progresivo
- Oportunidad: productos diseñados para millennials

**Por geografía:**
- **Concentración:** Madrid, Barcelona, Andalucía
- **Mayor ratio ventas/cliente:** País Vasco (0.76), Cantabria (0.70)
- **Insight:** Regiones pequeñas más efectivas que grandes ciudades

**Implicación marketing:** Campañas regionales personalizadas superan enfoque nacional genérico

---

### SLIDE 6: POWERBI - DISTRIBUCIÓN DE MÁRGENES
**Título:** Anatomía de la Rentabilidad por Producto

**Contenido:**
Incluir **IMAGEN 1** (Márgenes por venta según producto)

**Total:** 240,773 ventas analizadas

**Dos mundos diferentes:**

**Productos de BAJO margen (€20-100):**
- Cuentas: Distribución €40-80, volumen alto
- Tarjetas: Distribución €40-80, volumen medio-alto
- **Estrategia:** Productos de entrada, lead generation

**Productos de ALTO margen (€1,000-15,000):**
- Inversión: Distribución €1K-10K, pico en €2K
- Pensión: Distribución €0-15K, pico en €1K
- Préstamo: Similar a inversión
- **Estrategia:** Productos de valor, upselling prioritario

**Conclusión:** No todas las ventas valen igual → Priorizar margen vs volumen

---

### SLIDE 7: POWERBI - LA GALLINA DE LOS HUEVOS DE ORO
**Título:** ¿Qué Productos Nos Dan De Comer?

**Contenido:**
Incluir **IMAGEN 5** (Margen por familia + pie chart)

**Margen promedio por familia:**
1. **Pensión: €5,976** (79% del margen total) 🏆
2. **Préstamo: €2,284** (11%)
3. **Inversión: €1,493** (8%)
4. **Cuenta: €70** (1%)
5. **Tarjeta: €60** (1%)

**Número de clientes por familia:**
- Cuenta: 134,308 clientes (productos básicos)
- Tarjeta: 42,410 clientes
- **Pensión: 19,369 clientes** → Alto margen + bajo volumen
- Inversión: 9,238 clientes
- Préstamo: 35 clientes

**Insight crítico:**
- Pensión genera **100x más margen que Cuenta/Tarjeta**
- Solo 4.4% de clientes tienen Pensión → **ENORME POTENCIAL**
- Beneficio mensual: tendencia estable €7-14M

**Decisión estratégica:** Prioridad #1 = Venta de Planes de Pensiones

---

## 🎯 TAREA 2: MODELOS DE PROPENSIÓN (5 min)
**Presentador:** Persona 2
**Slides:** 8-13 (Slide 8: Separador | Slides 9-13: Contenido)

### SLIDE 8: SEPARADOR TAREA 2
**Título:** TAREA 2: MODELOS DE PROPENSIÓN

---

### SLIDE 9: PROPENSIÓN - ¿QUÉ ES Y POR QUÉ IMPORTA?
**Título:** Del "Spray & Pray" al Marketing de Precisión

**Problema tradicional:**
❌ Campañas masivas a toda la base
❌ Conversión <1%, ROI negativo
❌ Saturación y unsubscribes
❌ Desperdicio de recursos

**Solución: Propensión de Compra**
✅ **Predecir** quién comprará ANTES de lanzar campaña
✅ **Priorizar** clientes con mayor probabilidad
✅ **Personalizar** mensajes por perfil
✅ **Maximizar** conversión y ROI

**Cómo funciona:**
```
[Datos históricos] → [Modelo ML] → [Score 0-1] → [Segmentos acción]
```

**Variables clave consideradas:**
- Recencia: meses desde última actividad
- Frecuencia: número de productos contratados
- Comportamiento: cambios de segmento, churn risk
- Sociodemográficos: edad, salario, región
- Canal: punto de entrada del cliente

---

### SLIDE 10: METODOLOGÍA - CONSTRUCCIÓN DE MODELOS
**Título:** Tres Modelos, Tres Oportunidades

**Productos modelados:**

1. **PENSION PLAN** (Plan de Pensiones)
   - Margen: €6,071/cliente
   - Target: Clientes sin pension_plan (425K elegibles)

2. **PAYMENT CARD** (Tarjetas Crédito/Débito)
   - Margen: €60/cliente
   - Target: Clientes con 0-1 tarjetas (440K elegibles)

3. **INVESTMENT FAMILY** (Fondos, Depósitos, Valores)
   - Margen: €1,699/cliente
   - Target: Clientes sin productos inversión (431K elegibles)

**Técnica:** XGBoost (Machine Learning avanzado)
**Datos:** 17 meses históricos (2018-2019)
**Validación:** Train/Validation/Test temporal (evita data leakage)
**Desbalanceo:** Undersampling 3:1 (eventos compra <1%)

**Métricas:**
- Recall 90-97% → Capturamos casi todos los compradores
- ROC AUC 0.98-0.99 → Excelente capacidad discriminatoria

---

### SLIDE 11: RESULTADOS - SEGMENTOS DE PROPENSIÓN
**Título:** De 442K Clientes a Listas Accionables

**Segmentación por propensión (score 0-1):**

| Segmento | Threshold | Acción Marketing |
|----------|-----------|------------------|
| **TOP** | ≥0.80 | Campaña premium, incentivo alto, contacto directo |
| **HIGH** | 0.60-0.80 | Campaña estándar, incentivo medio, email+push |
| **MEDIUM** | 0.50-0.60 | Campaña soft, remarketing, contenido educativo |
| **MID-LOW** | 0.40-0.50 | Nurturing, sin inversión directa |
| **LOW** | <0.40 | No contactar (coste > beneficio) |

**Distribución clientes predichos:**

**PENSION PLAN (423,169 clientes):**
- Top (≥0.85): **8,629 clientes** (2.0%)
- High (0.7-0.85): **5,774 clientes** (1.4%)
- Medium (0.5-0.7): **3,251 clientes** (0.8%)
- **Total accionable (Top+High): 14,403 clientes**

**PAYMENT CARD (393,756 clientes):**
- Top (≥0.8): **9,775 clientes** (2.5%)
- High (0.6-0.8): **4,116 clientes** (1.0%)
- **Total accionable: 13,891 clientes**

**INVESTMENT (431,364 clientes):**
- Top (≥0.8): **8,027 clientes** (1.9%)
- High (0.6-0.8): **4,157 clientes** (1.0%)
- **Total accionable: 12,184 clientes**

---

### SLIDE 12: VALIDACIÓN - ¿FUNCIONA EN LA VIDA REAL?
**Título:** ¿Funciona en la Vida Real? SÍ

**Metodología de validación:**
- Matriz de confusión sobre datos Abril 2019 (mes no visto)
- Comparación conversión orgánica vs predicción modelo
- Cálculo conservador basado en performance real

**RESULTADOS PENSION PLAN:**

**Sin modelo (orgánico):**
- Base: 85,232 clientes totales
- Conversiones mes: 146 clientes
- **Tasa conversión: 0.17%**

**Con modelo (predicción Top+High):**
- Base contactada: 13,000 clientes (15% de la base)
- Conversiones esperadas: 502 clientes
- **Tasa conversión: 3.8%**

**Mejora:**
- **22x más conversión** (3.8% vs 0.17%)
- **Triplica captación mensual** con solo 15% de contactos
- **ROI positivo** confirmado en validación

**CONVERSIÓN POR PRODUCTO:**
| Producto | Conversión Modelo | Volumen Esperado |
|----------|-------------------|------------------|
| Pension Plan | 3.8% | 502 clientes/mes |
| Payment Card | 8.9% | 296 clientes/mes |
| Investment | 0.19% | 7 clientes/mes |

**Conclusión:** Pension Plan y Payment Card viables, Investment requiere revisión

---

### SLIDE 13: POWERBI - PROPENSIÓN × CLUSTERING
**Título:** Propensión × Clustering: Hiperpersonalización

**Contenido:**
Incluir **IMAGEN 2** (Propensión por clusters y productos)

**Análisis por producto:**

**PENSION PLAN:**
- Cluster dominante: **Particulares Premium Digitales** (área top)
- También: Jóvenes Básicos Activos
- Leads Jóvenes: propensión mínima → descartar

**INVESTMENT:**
- Distribución equilibrada entre clusters
- Particulares Premium y Jóvenes Activos lideran
- Menor concentración que Pensión

**PAYMENT CARD:**
- Mayor volumen en categoría Top
- Todos los clusters presentes
- Producto más transversal

**Insight:** La combinación Propensión + Cluster permite **hiperpersonalización**:
- Mensaje A para "Particulares Premium" con propensión Top en Pensión
- Mensaje B para "Jóvenes Activos" con propensión High en Tarjeta
- Exclusión de "Leads Jóvenes" de campañas costosas

---

## 👥 TAREA 3: CLUSTERING Y SEGMENTACIÓN (5 min)
**Presentador:** Persona 3
**Slides:** 14-18 (Slide 14: Separador | Slides 15-18: Contenido)

### SLIDE 14: SEPARADOR TAREA 3
**Título:** TAREA 3: CLUSTERING Y SEGMENTACIÓN

---

### SLIDE 15: CLUSTERING - ¿POR QUÉ SEGMENTAR?
**Título:** ¿Por Qué Segmentar?

**El problema del marketing "one-size-fits-all":**
❌ Cliente de 25 años recibe oferta de plan de pensiones → Ignora
❌ Cliente premium con €80K salario recibe oferta básica → Se ofende
❌ Cliente inactivo recibe campaña de upselling → Ya se fue

**La solución: Segmentación Inteligente**
✅ **Agrupar** clientes con características similares
✅ **Personalizar** mensajes, ofertas y canales por segmento
✅ **Optimizar** inversión en los segmentos más rentables
✅ **Predecir** qué productos encajan con cada perfil

**Técnica: Clustering (Machine Learning No Supervisado)**
```
[21 variables] → [PCA 6 componentes] → [K-Means] → [6 Clusters]
```

**Variables consideradas:**
- Sociodemográficas: edad, salario, región, género, segmento
- Comportamiento: antigüedad, % meses activo, productos contratados
- Geográficas: macro región, costa, tamaño ciudad
- Productos: familias contratadas, activo con producto

---

### SLIDE 16: LOS 6 PERFILES DE CLIENTE
**Título:** Los 6 Perfiles de Cliente

**CLUSTER 1: Particulares Sin Cuenta (10.8% - 47,640 clientes)**
- **Perfil:** Clientes particulares sin cuenta bancaria activa
- **Edad promedio:** 30-40 años
- **Productos:** Mínimos o ninguno
- **Oportunidad:** Activación con producto entrada (cuenta)
- **Estrategia:** Campaña de reengagement

**CLUSTER 2: Particulares Premium Digitales (21.9% - 97,050 clientes)** 🏆
- **Perfil:** Segmento "Universitario", alta interacción digital
- **Edad promedio:** 25-35 años
- **Productos:** 2-3 familias, digitales
- **Oportunidad:** MÁXIMA para Pension Plan y Investment
- **Estrategia:** Upselling premium, contenido educativo financiero

**CLUSTER 3: Jóvenes Recientes (16.9% - 74,942 clientes)**
- **Perfil:** Clientes jóvenes recién incorporados (<12 meses)
- **Edad promedio:** 20-28 años
- **Productos:** 1 producto básico (cuenta o tarjeta)
- **Oportunidad:** Cross-selling rápido
- **Estrategia:** Onboarding acelerado, gamificación

**CLUSTER 4: Jóvenes Potenciales (25.7% - 113,726 clientes)**
- **Perfil:** Mayor cluster, jóvenes con potencial de crecimiento
- **Edad promedio:** 22-30 años
- **Productos:** 1-2 familias básicas
- **Oportunidad:** Mediano plazo (2-3 años)
- **Estrategia:** Nurturing, educación financiera

**CLUSTER 5: Leads Jóvenes (14.4% - 63,795 clientes)**
- **Perfil:** Clientes jóvenes en fase de captación
- **Edad promedio:** 18-25 años
- **Productos:** 0-1 básico
- **Oportunidad:** Baja en corto plazo
- **Estrategia:** Bajo coste, contenido, esperar maduración

**CLUSTER 6: Jóvenes Básicos Activos (10.3% - 45,756 clientes)**
- **Perfil:** Jóvenes con productos básicos pero activos
- **Edad promedio:** 25-32 años
- **Productos:** Account + Payment card activos
- **Oportunidad:** Alta para Investment
- **Estrategia:** Upselling mid-tier

---

### SLIDE 17: ESTRATEGIA DE SEGMENTACIÓN
**Título:** Matriz de Priorización: Propensión × Cluster

**Matriz de Priorización: Propensión × Cluster**

**🎯 PRIORIDAD MÁXIMA (invertir recursos):**
1. **Particulares Premium Digitales** (Cluster 2)
   - Propensión Top: Pensión + Investment
   - Margen esperado: €6K-1.7K por conversión
   - Acción: Campaña premium multi-producto

2. **Jóvenes Básicos Activos** (Cluster 6)
   - Propensión High: Investment + Tarjeta
   - Margen esperado: €1.7K-60
   - Acción: Campaña digital agresiva

**⚠️ PRIORIDAD MEDIA (optimizar coste):**
3. **Jóvenes Recientes** (Cluster 3)
   - Propensión Medium: Tarjeta
   - Margen esperado: €60
   - Acción: Cross-selling automatizado bajo coste

**❌ DESCARTAR (no invertir):**
4. **Leads Jóvenes** (Cluster 5)
   - Propensión Low en todos productos
   - ROI negativo
   - Acción: Nurturing pasivo, sin campañas activas

5. **Particulares Sin Cuenta** (Cluster 1)
   - Inactivos, difícil reactivación
   - Acción: Campaña final de reengagement, luego desinversión

**Resultado:**
- Concentración del **80% del presupuesto** en **32% de clientes** (Clusters 2+6)
- Exclusión del **25% de clientes de bajo valor** (Clusters 1+5)

---

### SLIDE 18: PERSONALIZACIÓN POR CLUSTER
**Título:** Mismo Producto, Diferente Historia

**Ejemplo: Campaña PENSION PLAN**

**Para "Particulares Premium Digitales":**
- **Mensaje:** "Optimiza tu futuro financiero: Plan de Pensiones con ventajas fiscales"
- **Tono:** Profesional, datos, beneficio fiscal
- **Canal:** Email ejecutivo + app notification
- **Incentivo:** Asesoría gratuita personalizada

**Para "Jóvenes Básicos Activos":**
- **Mensaje:** "Tu yo del futuro te lo agradecerá: Empieza tu plan de pensiones con 50€/mes"
- **Tono:** Cercano, aspiracional, simple
- **Canal:** Push app + Instagram ads
- **Incentivo:** Bono de bienvenida €50

**Para "Leads Jóvenes":**
- **Mensaje:** —NO CONTACTAR— (coste > beneficio)
- **Alternativa:** Contenido orgánico educativo (blog, redes)

**Resultado esperado:**
- **Conversion rate 3-5x superior** vs campaña genérica
- **Menor unsubscribe rate** por relevancia
- **Mejor brand perception** (mensajes adaptados)

---

## 💰 TAREA 4: VALOR DEL CLIENTE + ESTRATEGIA COMERCIAL (5 min)
**Presentador:** Persona 4
**Slides:** 19-26 (Slide 19: Separador | Slides 20-26: Contenido)

### SLIDE 19: SEPARADOR TAREA 4
**Título:** TAREA 4: VALOR DEL CLIENTE Y ESTRATEGIA

---

### SLIDE 20: VALOR DEL CLIENTE - EL ROI LO ES TODO
**Título:** No Se Trata de Vender Más, Sino de Vender Mejor

**Concepto: Customer Lifetime Value (CLV) = Margen**

**Ranking de productos por margen promedio:**
1. **Pension Plan: €6,071** → 1 conversión = 100 conversiones de tarjeta
2. **Investment: €1,699** → 1 conversión = 28 conversiones de tarjeta
3. **Loan: €2,284** → Volumen bajísimo (35 clientes), descartado
4. **Payment Card: €60** → Alto volumen, bajo valor
5. **Account: €70** → Producto commodity, no diferenciador

**Cálculo de impacto:**
```
ROI Campaña = (Conversiones × Margen) - Coste Campaña
```

**Ejemplo Payment Card:**
- Conversión: 296 clientes × €60 = €17,760
- Coste campaña: ~€15,000 (staff, herramientas, creatividad)
- **ROI: €2,760 (18%)** → Apenas rentable

**Ejemplo Pension Plan:**
- Conversión: 502 clientes × €6,071 = €3,047,642
- Coste campaña: ~€50,000 (personalización, incentivos)
- **ROI: €2,997,642 (6,000%)** → EXTREMADAMENTE RENTABLE

**Conclusión:** **1 venta de Pensión = 100 ventas de Tarjeta** en términos de margen

---

### SLIDE 21: ESCENARIOS PROPUESTOS - PENSION PLAN
**Título:** ¿Cuánto Podemos Ganar? (Pension Plan)

**BASE DE CÁLCULO:**
- Modelo entrenado y validado
- Conversión real: 3.8% (validación Abril 2019)
- Margen promedio: €6,071/cliente

**ESCENARIO 1: BÁSICO (solo Top propensión)**
- Clientes contactados: **8,629** (2% base total)
- Conversiones esperadas: 328 clientes (3.8%)
- Revenue incremental: **€1,991,288**
- Incremento vs orgánico (€800K): **+149%**

**ESCENARIO 2: MEDIO (Top + High)**
- Clientes contactados: **14,403** (3.4% base)
- Conversiones esperadas: 547 clientes (3.8%)
- Revenue incremental: **€3,320,837**
- Incremento vs orgánico: **+315%**

**ESCENARIO 3: AMPLIO (Top + High + Medium)**
- Clientes contactados: **17,654** (4% base)
- Conversiones esperadas: 671 clientes (3.8%)
- Revenue incremental: **€4,073,641**
- Incremento vs orgánico: **+409%**

**RECOMENDACIÓN:**
- **Comenzar con Escenario 2 (Top+High):** €3.3M revenue, muestra manejable
- Si tasa conversión ≥3.5% en primeras 2 semanas → Expandir a Escenario 3
- Si tasa conversión <3% → Revisar mensajes, no expandir base

**Con captación de Leads (adicional):**
- Targeting agresivo en Cluster 5 (Leads Jóvenes): +€33K (marginal)
- **No recomendado:** ROI negativo si consideramos coste adquisición

---

### SLIDE 22: ANÁLISIS DE CANALES DE MARKETING
**Título:** Optimización de Canales: No Todos Convierten Igual

**PROBLEMA ACTUAL:**
- easyMoney usa múltiples canales sin diferenciación
- Conversión dispersa, difícil optimizar presupuesto

**ANÁLISIS DE DATOS HISTÓRICOS:**

**Canales de ALTA conversión (>10% Pension Plan):**
1. **Canal KAT: 22% conversión** 🏆
   - Descripción: [Canal de alto rendimiento]
   - Acción: Priorizar 40% presupuesto

2. **Canal 003: 18% conversión**
   - Descripción: [Canal digital especializado]
   - Acción: Priorizar 25% presupuesto

3. **Canal 007: 15% conversión**
   - Descripción: [Canal con buenos resultados]
   - Acción: Priorizar 20% presupuesto

4. **Canal KFC: 12% conversión**
   - Descripción: [Canal estable]
   - Acción: Mantener 15% presupuesto

**Canales de BAJA conversión (<5%):**
- Resto de canales: Conversión promedio 2-4%
- **Acción:** Reducir a mantenimiento mínimo o eliminar

**ESTRATEGIA:**
- **Concentrar 100% presupuesto en 4 canales estrella**
- Conversión esperada global: **16.75%** (promedio ponderado)
- vs situación actual: **6%** promedio todos los canales
- **Mejora: 2.8x conversión solo por optimización de canal**

**Aplicación práctica:**
```
Campaña Pension Plan Escenario Medio:
- 14,403 clientes × 16.75% = 2,413 conversiones (vs 547 esperadas)
- Revenue: €14,649,323 (vs €3.3M)
```
→ **Si optimizamos canales, podríamos 4x el revenue proyectado**

---

### SLIDE 23: INVESTMENT Y PAYMENT CARD - ANÁLISIS
**Título:** ¿Qué Hacer con Investment y Payment Card?

**INVESTMENT FAMILY:**
- **Conversión actual: 0.19%** (7 clientes de 3,684 contactados)
- **Revenue esperado Escenario Top:** €40,000 (solo top propensión)
- **Coste campaña estimado:** €25,000
- **ROI: +€15,000 (60%)** → Apenas positivo

**Diagnóstico:**
- Modelo funciona técnicamente (AUC 0.99)
- Problema: conversión real extremadamente baja
- Posibles causas:
  - Productos no competitivos vs mercado
  - Falta de confianza en marca para inversión
  - Timing económico (2019 pre-crisis)

**Recomendación:**
- **NO priorizar Investment a corto plazo**
- Reevaluar producto/oferta antes de campañas
- Alternativa: Co-marketing con easyBanking

---

**PAYMENT CARD:**
- **Conversión actual: 8.9%** (296 clientes)
- **Revenue esperado Escenario Amplio:** €832,860
- **Coste campaña:** €150,000 (incentivos, creatividad)
- **ROI: +€682,860 (455%)** → Positivo pero limitado por bajo margen

**Diagnóstico:**
- Alta conversión, bajo margen (€60/cliente)
- Producto útil para engagement, no rentabilidad directa
- Cross-sell a otros productos posterior

**Recomendación:**
- **Campaña Payment Card como estrategia secundaria**
- Foco: enganche y cross-sell a Pension/Investment
- Usar como "producto anzuelo" en Clusters 3 y 4 (jóvenes)
- Budget: 20% del total (vs 60% Pension Plan)

---

### SLIDE 24: ESTRATEGIA COMERCIAL INTEGRADA
**Título:** Plan de Acción: 3 Meses para Rentabilidad

**FASE 1: MES 1 - QUICK WINS (Pension Plan)**
- **Acción:** Lanzar campaña Pension Plan Escenario Medio
- **Target:** 14,403 clientes (Top + High propensión)
- **Clusters:** Particulares Premium Digitales (70%) + Jóvenes Básicos Activos (30%)
- **Canales:** KAT (40%), 003 (30%), 007 (30%)
- **Mensajes:** 2 variantes personalizadas por cluster
- **Objetivo:** 500+ conversiones, €3M revenue
- **KPIs:** Conversión ≥3.5%, CAC <€100, ROI >2,500%

**FASE 2: MES 2 - ESCALADO**
- **Acción:** Expandir a Escenario Amplio si Fase 1 exitosa
- **Target:** +3,251 clientes (Medium propensión)
- **Objetivo:** +750 conversiones totales acumuladas, €4.5M revenue
- **Nueva acción:** Lanzar Payment Card en Clusters 3+4 (jóvenes)
- **Objetivo Payment Card:** 400 conversiones, €900K revenue

**FASE 3: MES 3 - OPTIMIZACIÓN Y CROSS-SELL**
- **Acción:** Analizar resultados y refinar modelos
- **Nueva estrategia:** Cross-sell Pension a compradores Payment Card (conversión 15%)
- **Revisión Investment:** Reevaluar oferta, testar nuevos mensajes
- **Objetivo:** Establecer proceso repetible mensual

**REVENUE PROYECTADO 3 MESES:**
- Pension Plan: €4.5M - €6M
- Payment Card: €900K - €1.2M
- **Total: €5.4M - €7.2M** (vs €2.4M orgánico = **+€3M - €4.8M incrementales**)

---

### SLIDE 25: ENTREGABLES PARA MARKETING
**Título:** Entregables Para Marketing - Listo Para Usar

**FICHEROS PROVISTOS AL EQUIPO:**

**1. Base de Datos Scored (Excel/CSV)**
- **df_pension_plan_scored.csv:** 423,169 clientes
  - Columnas: pk_cid, propensity_score, propensity_range, cluster_name
  - Ordenado: Mayor a menor probabilidad
  - Filtrado: Excluye clientes que ya tienen producto

- **df_payment_card_scored.csv:** 393,756 clientes
- **df_inversion_family_scored.csv:** 431,364 clientes

**Uso:**
- Importar directo a CRM (Salesforce, HubSpot)
- Conectar con plataforma email (Klaviyo, Mailchimp)
- Segmentar por propensity_range (Top/High/Medium)

**2. Dashboard PowerBI Interactivo**
- Monitorización tiempo real de campañas
- Filtros por cluster, propensión, geografía
- KPIs: conversión, revenue, CAC, ROI

**3. Guía de Mensajes Personalizados**
- Templates por Cluster × Producto
- Líneas de asunto testeadas
- CTAs optimizados

**4. Calendario de Campañas**
- Timing óptimo según estacionalidad
- Frecuencia de contacto por segmento
- Plan de A/B testing

**INTEGRACIÓN:**
- APIs disponibles para scoring en tiempo real de nuevos clientes
- Reentrenamiento trimestral de modelos con nuevos datos
- Soporte técnico durante implementación

---

### SLIDE 26: CONCLUSIONES Y RECOMENDACIONES
**Título:** De la Crisis a la Rentabilidad en 90 Días

**LO QUE HEMOS DEMOSTRADO:**

✅ **Datos como activo estratégico:**
- 442K clientes contienen €50M+ en revenue no realizado
- Analítica predictiva identifica dónde está ese valor

✅ **Priorización basada en margen:**
- Pension Plan (€6K margen) debe ser 80% del esfuerzo
- Payment Card/Investment son secundarios

✅ **Segmentación accionable:**
- 6 perfiles de cliente con estrategias diferenciadas
- Concentración del 80% presupuesto en 32% clientes (Clusters 2+6)

✅ **Propensión predictiva:**
- Conversión 3.8% vs 0.17% orgánico = **22x mejora**
- Modelos validados en producción

✅ **Optimización de canales:**
- 4 canales estrella (KAT, 003, 007, KFC) con conversión 12-22%
- Eliminación de canales de bajo rendimiento

**IMPACTO ESPERADO:**
- **Revenue incremental: €3M - €4.8M en 3 meses**
- **ROI: 2,500% - 6,000%** (Pension Plan)
- **Path to profitability:** Alcanzar EBITDA positivo en Q3 2019

**SIGUIENTES PASOS:**
1. Aprobación plan comercial por CEO (esta semana)
2. Preparación creatividades y ofertas (semana 2)
3. Integración ficheros en plataforma marketing (semana 3)
4. **Lanzamiento Fase 1: Día 22** (1 mes desde hoy)

---

**NOTA:** La presentación tiene 27 slides en total. El slide 27 está reservado para preguntas y cierre (sin contenido fijo).
