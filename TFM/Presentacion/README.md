# PRESENTACIÓN TFM - EASYMONEY
## Archivos y Guía de Uso

---

## 📁 CONTENIDO DE ESTA CARPETA

### 1. **ESTRUCTURA_PRESENTACION.md**
Documento con la estructura completa de todos los slides (24 slides en total).

**Contenido por slide:**
- Título
- Contenido detallado
- Referencias a imágenes PowerBI donde corresponda
- Estructura de 4 tareas/secciones (5 min cada una)

**Uso:**
- Abrir este documento y copiar el contenido slide por slide a PowerPoint
- Seguir la estructura exacta para mantener coherencia
- Las imágenes PowerBI están indicadas como "[Incluir IMAGEN X en slide]"

---

### 2. **GUION_MARKETING.md**
Guión de presentación desde perspectiva marketing, correlacionado con cada slide.

**Contenido:**
- Texto explicativo para leer durante la presentación
- ~5 minutos de lectura por tarea (19min 35seg total)
- Tono marketing (no técnico)
- Tips de presentación
- Manejo de preguntas frecuentes

**Uso:**
- Cada presentador lee su sección correspondiente antes de presentar
- Usar como base para preparar speech personalizado
- Practicar tiempos (no exceder 5 min por persona)

---

### 3. **README.md** (este archivo)
Guía de navegación y uso de los materiales.

---

## 🎯 ESTRUCTURA DE LA PRESENTACIÓN

### **TAREA 1 - Persona 1 (5 min)**
**Slides 1-7:** Contexto + EDA + PowerBI

**Contenido clave:**
- Situación easyMoney (crisis financiera)
- Metodología 4 pilares
- Dashboards PowerBI con insights clave
- Distribución de márgenes
- Producto estrella: Pension Plan (79% margen)

**Imágenes PowerBI a incluir:**
- **Slide 4:** IMAGEN 3 (Ventas por mes, beneficio, geografía)
- **Slide 5:** IMAGEN 4 (Densidad clientes, demografía)
- **Slide 6:** IMAGEN 1 (Márgenes por producto)
- **Slide 7:** IMAGEN 5 (Margen por familia, pie chart)

---

### **TAREA 2 - Persona 2 (5 min)**
**Slides 8-12:** Modelos de Propensión

**Contenido clave:**
- Concepto de propensión de compra
- Construcción de 3 modelos (Pension, Payment Card, Investment)
- Segmentación por propensión (Top/High/Medium/Mid-Low/Low)
- Validación: 3.8% conversión vs 0.17% orgánico (22x mejora)
- Integración propensión × clustering

**Imágenes PowerBI a incluir:**
- **Slide 12:** IMAGEN 2 (Propensión por clusters)

---

### **TAREA 3 - Persona 3 (5 min)**
**Slides 13-16:** Clustering y Segmentación

**Contenido clave:**
- Importancia de segmentación
- Los 6 perfiles de cliente identificados
- Estrategia de priorización (80% presupuesto en 32% clientes)
- Personalización de mensajes por cluster

**Clusters identificados:**
1. Particulares Sin Cuenta (10.8%)
2. Particulares Premium Digitales (21.9%) ⭐ PRIORIDAD
3. Jóvenes Recientes (16.9%)
4. Jóvenes Potenciales (25.7%)
5. Leads Jóvenes (14.4%)
6. Jóvenes Básicos Activos (10.3%) ⭐ PRIORIDAD

---

### **TAREA 4 - Persona 4 (5 min)**
**Slides 17-24:** Valor Cliente + Estrategia Comercial + Cierre

**Contenido clave:**
- Análisis ROI por producto
- 3 Escenarios de implementación (Básico/Medio/Amplio)
- Análisis de canales marketing (4 canales estrella)
- Estrategia Investment y Payment Card
- Plan de acción 90 días
- Revenue proyectado: €3M-€4.8M incrementales
- Entregables para equipo marketing
- Conclusiones y next steps

---

## 🖼️ IMÁGENES POWERBI

### Ubicación de las 5 imágenes:

**IMAGEN 1:** Márgenes por venta según producto
- Gráficos de distribución: Cuenta/Tarjeta vs Inversión/Pensión/Préstamo
- Total: 240,773 ventas
- **Usar en:** Slide 6

**IMAGEN 2:** Análisis propensión por clusters
- 3 productos: Pension, Investment, Payment card
- Distribución por rangos (Top, High, Medium, Mid-Low)
- Suma de clientes por cluster
- **Usar en:** Slide 12

**IMAGEN 3:** Análisis temporal y geográfico
- Ventas mayo 2019: 10,211
- Beneficio: €8.07M
- Margen medio: 606.88
- Tendencias mensuales 2018-2019
- Mapa ventas por provincia
- **Usar en:** Slide 4

**IMAGEN 4:** Análisis demográfico y geográfico
- Densidad de clientes (mapa España)
- Clientes por rango de edad (296K en 20s)
- Ratio ventas/cliente por comunidad autónoma
- Número de ventas por comunidad
- **Usar en:** Slide 5

**IMAGEN 5:** Análisis de margen y productos
- Margen medio: 606.88
- Beneficio por mes (tendencia temporal)
- Margen por familia de producto (Pensión €5,976)
- Número de clientes por familia
- Margen por producto individual
- Pie chart: Qué productos nos han dado de comer (79% Pensión)
- **Usar en:** Slide 7

---

## 📝 CÓMO CREAR LA PRESENTACIÓN POWERPOINT

### **Opción 1: Manual (Recomendada para control total)**

1. **Abrir PowerPoint** y crear presentación en blanco

2. **Aplicar diseño corporativo:**
   - Colores: Azul corporativo easyMoney
   - Fuente: Arial o Helvetica (profesional, limpia)
   - Layouts: Título + contenido, 2 columnas, imagen completa

3. **Crear slides según ESTRUCTURA_PRESENTACION.md:**
   - Copiar título de cada slide
   - Copiar contenido (bullet points, tablas, etc.)
   - Ajustar formato según necesidad

4. **Insertar imágenes PowerBI:**
   - Guardar las 5 imágenes como archivos .png o .jpg
   - Insertarlas en los slides indicados
   - Ajustar tamaño para visibilidad

5. **Añadir transiciones suaves** entre slides (opcional)

6. **Guardar como:** `Presentacion_TFM_easyMoney_Grupo1.pptx`

---

### **Opción 2: Usando herramientas de conversión Markdown → PowerPoint**

**Herramientas recomendadas:**
- **Marp:** https://marp.app/ (convierte Markdown a slides)
- **Pandoc:** `pandoc ESTRUCTURA_PRESENTACION.md -o presentacion.pptx`
- **Google Slides:** Importar desde Google Docs (copiar MD → Docs → Slides)

**Limitación:** Las imágenes tendrás que insertarlas manualmente después.

---

### **Opción 3: Usar IA para generación automática**

**Herramientas:**
- **Gamma.app:** Pega el contenido de ESTRUCTURA_PRESENTACION.md
- **Beautiful.ai:** Genera slides desde texto estructurado
- **Slidesgo + ChatGPT:** Prompt con contenido del MD

---

## 🎤 PREPARACIÓN PARA PRESENTAR

### **Para cada presentador:**

1. **Leer tu sección del GUION_MARKETING.md:**
   - Tarea 1: Persona 1
   - Tarea 2: Persona 2
   - Tarea 3: Persona 3
   - Tarea 4: Persona 4

2. **Practicar en voz alta:**
   - Objetivo: ~5 minutos por sección
   - Usar timer
   - Ajustar velocidad si excedes tiempo

3. **Familiarizarse con los slides:**
   - Saber qué slide corresponde a cada parte del guión
   - Practicar transiciones entre slides
   - Conocer las imágenes PowerBI (qué muestran, qué enfatizar)

4. **Preparar transición a siguiente persona:**
   - Última frase de cada sección pasa el turno suavemente
   - Ya está escrita en el guión

5. **Anticipar preguntas:**
   - Revisar sección "Manejo de Preguntas" en GUION_MARKETING.md
   - Preparar respuestas breves (30-60 seg)

---

## ⏱️ TIEMPOS DE PRESENTACIÓN

| Tarea | Presentador | Slides | Tiempo | Contenido Principal |
|-------|-------------|--------|--------|---------------------|
| 1 | Persona 1 | 1-7 | ~5 min | Contexto + EDA + PowerBI |
| 2 | Persona 2 | 8-12 | ~5 min | Propensión |
| 3 | Persona 3 | 13-16 | ~5 min | Clustering |
| 4 | Persona 4 | 17-24 | ~5 min | ROI + Estrategia |
| **TOTAL** | | **24 slides** | **~20 min** | |

**Margen:** +30 segundos de buffer para transiciones y respiración

---

## 📊 CORRELACIÓN SLIDES ↔ GUIÓN

Cada sección del guión está marcada con **[SLIDE X]** para indicar qué slide debe estar visible al leer esa parte.

**Ejemplo:**
```
### [SLIDE 4-5] POWERBI - VISIÓN 360º
"Ahora déjenme mostrarles lo que descubrimos..."
```

→ Al llegar a esta parte del guión, debes estar mostrando el Slide 4 (luego avanzar a Slide 5).

---

## 🎨 RECOMENDACIONES DE DISEÑO

### **Slides de datos/números:**
- Usar gráficos visuales cuando sea posible
- Destacar números clave en grande (€6,071, 3.8%, 22x)
- Colores: Verde para positivo, Rojo para negativo, Azul para neutral

### **Slides de estrategia:**
- Bullet points cortos (máximo 6 por slide)
- Iconos para representar conceptos (🎯 target, 💰 dinero, 👥 clientes)
- Tablas para comparaciones (Escenarios, ROI, etc.)

### **Slides con imágenes PowerBI:**
- Imagen debe ocupar 60-70% del slide
- Dejar espacio para título arriba
- Opcional: Añadir callouts (flechas) para destacar insights

### **Slides de conclusiones:**
- Usar checkmarks ✅ para logros
- Lista numerada para next steps
- Fondo contrastante para destacar

---

## 📦 ENTREGABLES FINALES

Al terminar, deberías tener:

1. ✅ **Presentación PowerPoint (.pptx)** con 24 slides y 5 imágenes PowerBI integradas
2. ✅ **GUION_MARKETING.md** impreso o en tablet para cada presentador
3. ✅ **Archivos de backup:**
   - Versión PDF de la presentación (por si falla proyector)
   - Imágenes PowerBI individuales (alta resolución)
   - Datasets scored (.csv) si los piden en preguntas

---

## 🚀 NEXT STEPS

### **Inmediato (Hoy):**
- [ ] Crear presentación PowerPoint siguiendo ESTRUCTURA_PRESENTACION.md
- [ ] Insertar 5 imágenes PowerBI en slides correspondientes
- [ ] Distribuir GUION_MARKETING.md a cada presentador

### **Esta semana:**
- [ ] Cada presentador lee y practica su sección (5 min)
- [ ] Ensayo completo del grupo (20 min + Q&A)
- [ ] Ajustar tiempos si alguna sección se excede
- [ ] Preparar respuestas a preguntas técnicas

### **Día de la presentación:**
- [ ] Llegar 15 min antes para setup
- [ ] Probar proyector y laptop
- [ ] Tener backup en USB + versión PDF
- [ ] Respirar, confiar en el trabajo hecho, y ejecutar

---

## 📞 CONTACTO

Si tienes dudas sobre el contenido técnico:
- Revisar notebooks en `/TFM/` del proyecto
- Consultar diccionario de datos en `/TFM/data/datasets_TFM + diccionario/`

Si tienes dudas sobre la presentación:
- Revisar este README
- Revisar estructura y guión

---

**¡Éxito con la presentación! 🎉**

El trabajo está hecho. Los datos son sólidos. La estrategia es clara.
Ahora solo queda comunicarlo con confianza.
