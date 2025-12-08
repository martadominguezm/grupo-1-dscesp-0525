# INSTRUCCIONES PARA IMÁGENES POWERBI

---

## 📸 GESTIÓN DE LAS 5 IMÁGENES

### **Paso 1: Guardar las imágenes**

Las 5 imágenes que te proporcioné debes guardarlas con los siguientes nombres:

1. **imagen_1_margenes_distribucion.png**
   - Contenido: Márgenes por venta según producto
   - Distribución Cuenta/Tarjeta vs Inversión/Pensión/Préstamo

2. **imagen_2_propension_clusters.png**
   - Contenido: Análisis propensión por clusters
   - Pension, Investment, Payment card

3. **imagen_3_temporal_geografico.png**
   - Contenido: Ventas mayo 2019, beneficio, margen medio, tendencias

4. **imagen_4_demografico.png**
   - Contenido: Densidad clientes, rango edad, ratio ventas/cliente

5. **imagen_5_margen_familias.png**
   - Contenido: Margen medio, beneficio por mes, margen por familia, pie chart

**Guardar en:** `/Presentacion/imagenes_powerbi/`

---

## 🎯 MAPEO IMAGEN → SLIDE

### **IMAGEN 1** → **SLIDE 6**
**Título slide:** "Anatomía de la Rentabilidad por Producto"

**Posición en slide:**
- Imagen: Centro, ocupando 70% del espacio
- Título: Arriba
- Callout opcional: Flecha señalando pico de Pensión con texto "€15K margen máximo"

**Qué enfatizar al presentar:**
- Dos mundos: bajo margen (€20-100) vs alto margen (€1K-15K)
- Pensión alcanza hasta €15,000 de margen
- 1 venta Pensión = 100-250 ventas Tarjeta

---

### **IMAGEN 2** → **SLIDE 12**
**Título slide:** "Visualización: ¿Qué Clusters Tienen Mayor Propensión?"

**Posición en slide:**
- Imagen: Pantalla completa (imagen horizontal grande)
- Puede ocupar 80-90% del slide
- Título pequeño arriba

**Qué enfatizar al presentar:**
- Área rosa gigante en Pension → "Particulares Premium Digitales"
- Leads Jóvenes casi ausentes en Top → no invertir ahí
- Investment más distribuido pero sigue liderando Particulares Premium

---

### **IMAGEN 3** → **SLIDE 4**
**Título slide:** "PowerBI - Visión 360º del Negocio"

**Posición en slide:**
- Imagen: Centro-derecha, 60% del espacio
- Izquierda: Bullet points con métricas clave:
  ```
  📊 Mayo 2019:
  • 10,211 ventas
  • €8.07M beneficio
  • €606.88 margen medio

  📉 Insights:
  • Pico Octubre: 28K ventas
  • Caída vs 2018: -3K ventas/mes
  • Madrid y Málaga lideran margen
  ```

**Qué enfatizar al presentar:**
- Tendencia descendente en línea de ventas por mes
- Pico estacional en Octubre (acción: planificar campañas pre-Octubre)
- Geografía: Madrid/Málaga lideran en margen medio

---

### **IMAGEN 4** → **SLIDE 5**
**Título slide:** "PowerBI - Perfil Demográfico y Territorial"

**Posición en slide:**
- Imagen: Pantalla completa o centro grande
- Si hay espacio, añadir texto a la izquierda:
  ```
  👤 Perfil dominante:
  • 67% tienen 20-30 años
  • 296K clientes millennials

  🗺️ Geografía:
  • País Vasco: 0.76 ratio
  • Cantabria: 0.70 ratio
  • Madrid: 0.63 ratio

  💡 Insight:
  Regiones pequeñas convierten mejor
  ```

**Qué enfatizar al presentar:**
- Gráfico de edad: barra gigante en 20s
- Mapa densidad: concentración en grandes ciudades
- Paradoja: regiones pequeñas (País Vasco) convierten mejor que Madrid

---

### **IMAGEN 5** → **SLIDE 7**
**Título slide:** "PowerBI - La Gallina de los Huevos de Oro"

**Posición en slide:**
- Imagen: Centro-derecha, 65% del espacio
- Izquierda: Callout box destacado:
  ```
  🏆 PENSIÓN DOMINA:

  • 79% del margen total
  • €5,976 margen promedio
  • Solo 19,369 clientes (4.4%)

  💰 OPORTUNIDAD:

  Si subimos penetración a 10%:
  • +22,000 conversiones
  • +€132M revenue potencial
  ```

**Qué enfatizar al presentar:**
- Pie chart: 79% azul oscuro = Pensión
- Gráfico de barras margen por familia: Pensión €5,976 destacado
- Número de clientes por familia: Cuenta 134K vs Pensión 19K (brecha enorme)

---

## 🎨 FORMATO Y CALIDAD

### **Resolución recomendada:**
- Mínimo: 1920×1080 px (Full HD)
- Óptimo: 2560×1440 px o superior
- Formato: PNG (mejor calidad) o JPG (menor tamaño)

### **Ajustes en PowerPoint:**

1. **Insertar imagen:**
   - Insertar → Imágenes → Seleccionar archivo

2. **Ajustar tamaño:**
   - Arrastrar esquinas manteniendo proporción (Shift + arrastrar)
   - No distorsionar la imagen

3. **Posición:**
   - Usar guías de PowerPoint para alinear
   - Herramientas → Alinear → Alinear al centro/medio

4. **Calidad:**
   - Clic derecho en imagen → Formato de imagen → Compresión
   - Desmarcar "Comprimir imágenes" para mantener calidad

5. **Recorte (si necesario):**
   - Si la imagen tiene bordes blancos o información no relevante
   - Herramientas de imagen → Recortar

---

## 🖼️ ALTERNATIVAS SI NO TIENES LAS IMÁGENES

Si por alguna razón no puedes usar las imágenes PowerBI originales, puedes:

### **Opción A: Recrear gráficos básicos en PowerPoint**

Usa los datos mencionados en ESTRUCTURA_PRESENTACION.md para crear:
- Gráficos de barras (margen por familia)
- Gráficos de línea (ventas por mes)
- Pie chart (79% Pensión, 11% Préstamo, 8% Inversión, 2% Tarjeta/Cuenta)
- Mapas de España con colores (herramienta: Flourish, DataWrapper)

### **Opción B: Usar placeholders**

Mientras consigues las imágenes, inserta:
- Rectángulo gris con texto "[IMAGEN POWERBI: Análisis X]"
- Mantienes la estructura de la presentación
- Reemplazas después con imágenes reales

### **Opción C: Screenshots de notebooks**

Si tienes acceso a los notebooks del proyecto:
- Abrir `/TFM/use_case/propensity_and_clustering_union.ipynb`
- Ejecutar celdas de visualización
- Hacer screenshot y usar esas imágenes

---

## 📋 CHECKLIST FINAL DE IMÁGENES

Antes de la presentación, verifica:

- [ ] Las 5 imágenes están guardadas con nombres claros
- [ ] Calidad de imagen es alta (no pixeladas al proyectar)
- [ ] Imágenes están insertadas en los slides correctos
- [ ] Tamaño y posición son apropiados (no demasiado pequeñas)
- [ ] Texto en las imágenes es legible desde el fondo de la sala
- [ ] No hay recortes accidentales de información importante
- [ ] Colores de las imágenes son consistentes con diseño de slides
- [ ] Has practicado señalar elementos específicos en cada imagen

---

## 💡 TIPS PARA PRESENTAR CON IMÁGENES

### **Al mostrar cada imagen:**

1. **Pausa 2-3 segundos:** Deja que la audiencia procese visualmente

2. **Guía la mirada:**
   - "Miren aquí en la parte superior..."
   - "Este gráfico de la izquierda muestra..."
   - "Fíjense en esta línea azul que..."

3. **No leas la imagen:** La audiencia puede ver, tú interpreta
   - ❌ "Como ven, el margen de Pensión es €5,976"
   - ✅ "Pensión genera 100 veces más margen que tarjeta, aquí lo ven"

4. **Usa puntero láser o cursor:** Si presentas en remoto, usa herramientas de anotación

5. **Conecta imagen con acción:**
   - "Y por eso nuestra estrategia prioriza Pensión"
   - "Este dato nos llevó a descartar Investment temporalmente"

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### **Problema: Imagen se ve borrosa al proyectar**
**Solución:** Usar imagen de mayor resolución o recrear gráfico en PowerPoint

### **Problema: Imagen demasiado grande, no cabe en slide**
**Solución:** Recortar partes menos relevantes o dividir en 2 slides

### **Problema: Colores de imagen no coinciden con diseño de presentación**
**Solución:** Aplicar filtro de color en PowerPoint (Formato de imagen → Correcciones)

### **Problema: Texto en imagen es muy pequeño**
**Solución:** Usar zoom de PowerPoint durante presentación (Ctrl + rueda mouse) o recrear gráfico con texto más grande

### **Problema: No tengo las imágenes originales**
**Solución:** Usar Opción A o C descritas arriba (recrear o screenshots de notebooks)

---

## 📊 DATOS CLAVE POR SI NECESITAS RECREAR GRÁFICOS

### **Margen por familia de producto:**
- Pensión: €5,976
- Préstamo: €2,284
- Inversión: €1,493
- Cuenta: €70
- Tarjeta: €60

### **Número de clientes por familia:**
- Cuenta: 134,308
- Tarjeta: 42,410
- Pensión: 19,369
- Inversión: 9,238
- Préstamo: 35

### **Contribución al margen (pie chart):**
- Pensión: 79%
- Préstamo: 11%
- Inversión: 8%
- Tarjeta: 1%
- Cuenta: 1%

### **Ventas mayo 2019:**
- Total: 10,211 ventas
- Beneficio acumulado: €8.07M
- Margen medio: €606.88

### **Distribución clientes por edad:**
- <20 años: 3K
- 20-30 años: 296K (67%)
- 30-40 años: 82K
- 40-50 años: 49K
- 50-60 años: 24K
- 60+ años: 11K

### **Ratio ventas/cliente por comunidad:**
- País Vasco: 0.76
- Cantabria: 0.70
- Ceuta: 0.68
- Islas Baleares: 0.66
- Canarias: 0.64
- Madrid: 0.63

---

**¡Listo para integrar las imágenes! 🎨**

Con estas instrucciones, las imágenes PowerBI se convertirán en el apoyo visual perfecto para tu narrativa de marketing.
