---
type: reference
date: 2026-05-02
tags: [templates, system, reference]
---

# Templates — Guía y ejemplos

Colección de plantillas reutilizables para crear notas nuevas en el vault. Cada plantilla es un esqueleto que copias y adaptas a tu caso específico.

---

## 📋 Índice de plantillas

- [[daily-note]] — esqueleto de nota diaria
- [[proyecto]] — esqueleto de proyecto
- [[persona]] — esqueleto de contacto
- [[research]] — esqueleto de investigación
- [[canva-project]] — esqueleto de diseño Canva

---

## 📋 Plantillas disponibles

### 1. Daily Note — [[daily-note]]

**Uso:** Una nota por día. Captura de objetivos, ideas, completados.

**Ejemplo real (estructura):**

```markdown
---
type: daily
date: 2026-05-02
tags: [daily]
---

# 2026-05-02

## 🎯 Objetivos

- Terminar diplomado-autismo-2026 identidad visual
- Revisar finanzas febrero 2026

## 🧠 Ideas / Pensamientos

- UK necesita separar IS financieramente
- Canva de entidades debe estar centralizado

## ✅ Completado

- [x] Actualizar understanding-kids.md con staff real
- [x] Crear uk-catalogo.md

## 💡 Ideas que surgieron

- #idea Sistema de tracking para formaciones pasadas
- #idea Dashboard de finanzas por unidad (UK Clínica vs UK Formación)

## 🔗 Referencias

- [[understanding-kids]] — staff actualizado
- [[diplomado-autismo-2026]] — identidad visual cerrada
- [[dashboard]] — próximas prioridades
```

---

### 2. Proyecto — [[proyecto]]

**Uso:** Un archivo por proyecto activo, pausado o archivado.

**Ejemplo real (estructura completa):**

```markdown
---
type: project
date: 2026-04-13
estado: activo
fecha-inicio: 2026-04-18
fecha-objetivo: 2026-08-03
  - proyecto
  - estado/activo
  - tema/marketing
  - prioridad/alta
---

# Diplomado Internacional de Autismo 2026

Campaña de lanzamiento del Diplomado Internacional de Autismo 2026 para [[understanding-kids]].

---

## 📝 Descripción

Diplomado virtual internacional para profesionales. 21 sesiones en 5 meses. Enfoque neuroafirmativo.

---

## 🎯 Objetivos

1. Posicionar como formación aspiracional y confiable
2. Generar inscripciones vía formulario + WhatsApp
3. Construir autoridad con dream team de expositoras

---

## 📌 Decisiones clave

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-04-20 | Línea gráfica AUT26_EXP_TS01_opt2_publish | Referencia visual profesional |
| 2026-04-13 | UK lidera, IS apoya | UK tiene mayor audiencia |

---

## ✅ Próximos pasos

- [ ] Confirmar precio y cuotas
- [ ] Crear formulario corto de interés
- [ ] Definir tracking UTM completo

---

## 🔗 Relacionado

- [[understanding-kids]] — marca que lanza
- [[integracion-sensorial]] — participa como apoyo
- [[monica]] — aprueba contenido clínico
- [[diplomado-autismo-2026]] — este proyecto
```

---

### 3. Persona — [[persona]]

**Uso:** Contactos clave (clientes, socios, mentores, amigos, familia).

**Ejemplo real (estructura):**

```markdown
---
type: person
date: 2026-04-30
rol: Directora y terapeuta
empresa: Understanding Kids
relacion: familiar / socio
ultima-interaccion: 2026-05-02
  - persona
  - relacion/socio
---

# Mónica Samayoa González

Alias: Mónica

---

## 📝 Resumen

Directora y terapeuta encargada de [[understanding-kids]]. Co-toma decisiones con [[jr]]. Aprueba todo contenido clínico/técnico antes de publicar.

---

## 💬 Conversaciones / Notas

- **2026-05-02:** Actualización masiva de UK — staff real desde Pagos/2026, finanzas feb 2026
- **2026-04-30:** Decisión: IS sin separación financiera aún; se evaluará si es posible

---

## 🎯 Oportunidades / Ideas

- Expandir Formación (mejor margen por hora)
- Desarrollar UK en el Aula (B2B colegios)

---

## 📋 Datos de contacto

| Medio | Contacto |
|-------|----------|
| WhatsApp | +502 XXXX XXXX |
| Email | monica@kidsunderstanding.com |

---

## 🔗 Relacionado

- [[understanding-kids]] — proyecto principal
- [[integracion-sensorial]] — aprueba contenido IS
- [[jr]] — co-operador
```

---

### 4. Research — [[research]]

**Uso:** Investigaciones, artículos, aprendizajes aplicables.

**Ejemplo real (estructura):**

```markdown
---
type: research
date: 2026-04-30
fuente: https://www.100moffers.com/
relevancia: alta
  - research
  - tema/marketing
  - tema/negocios
---

# $100M Offers — Hormozi

---

## 📝 Resumen

Estrategia de pricing y packaging de productos/servicios para maximizar ingresos. Aplica a [[crisol-tcg]], [[understanding-kids]] formación, y [[propi]].

---

## 💡 Insights principales

- Pricing no es matemática, es psicología — posiciona por valor, no por costo
- Empaquetar múltiples niveles (bronze/silver/gold) aumenta conversión general
- El 80% de ingresos viene del 20% de ofertas — optimizar ese 20%

---

## 🛠 Aplicación práctica

- [[diplomado-autismo-2026]] → crear niveles de acceso (early-bird, standard, VIP)
- [[understanding-kids]] formación → separar precios por cliente (profesionales vs familias)
- [[crisol-tcg]] → bundle TCG + asesoría + acceso a comunidad

---

## 📚 Fuentes

- [100M Offers by Alex Hormozi](https://www.100moffers.com/)
- Aplicación en contexto Guatemala: markup 2-3x vs mercado típico

---

## 🔗 Relacionado

- [[atomic-habits]] — otro research aplicable
- [[diplomado-autismo-2026]] — proyecto donde aplica
- [[crisol-tcg]] — estrategia de pricing
```

---

### 5. Canva Project — [[canva-project]]

**Uso:** Documentar diseños de Canva con su estilo, paleta, tipografía, mood y propósito. Sirve como referencia para que Style Agent o nuevos diseños mantengan coherencia.

Incluye campos para:
- Colores (principal, secundario, acento, fondo)
- Tipografía (títulos, cuerpo, acento)
- Mood / estética
- Referencias visuales
- Propósito y audiencia
- Notas para Style Agent

---

## 🚀 Cómo usar estas plantillas

1. **Copia el contenido** de la plantilla correspondiente en `_templates/`
2. **Reemplaza los placeholders** (corchetes, valores genéricos)
3. **Adapta a tu contexto** — mantén la estructura, cambia el contenido
4. **Enlaza a notas existentes** — usa `[[nombre-exacto]]` en minúsculas
5. **Guarda en carpeta correcta** — `daily-notes/YYYY-MM-DD.md`, `proyectos/activos/nombre.md`, etc.

---

## 📌 Reglas clave al crear notas

- **Frontmatter OBLIGATORIO** — cada nota debe tener YAML al inicio
- **Sección "🔗 Relacionado" obligatoria** — excepto daily notes
- **Wikilinks reales** — enlaza a notas que existen, no inventadas
- **Tags consistentes** — usa los del sistema en `_CLAUDE.md`
- **Nombres en minúsculas con guiones** — `mi-nota-nueva.md`

---

## 🔗 Relacionado

- [[_CLAUDE]] — convenciones completas del vault
- [[index]] — catálogo maestro
- [[dashboard]] — vista operativa
