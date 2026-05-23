---
type: reference
date: 2026-05-16
tags: [memoria, agentes, sistema, reference]
---

# Cómo escribir memoria de agente

Guía de best practices para escribir o actualizar memoria persistente en el universo JR. Aplica a **todo agente** del vault —Geoffrey y los previstos en [[arquitectura|arquitectura de agentes]] (Understanding Kids, Finanzas, Legal, Meta Ads, Marketing)— y a cualquier modelo que los corra (Claude, Codex, Nemotron). Existe porque la memoria que envejece mal es peor que no tener memoria: un agente repite con total confianza un dato que ya es falso.

Todo agente nuevo hereda esta guía a través de [[_AI_BOOTSTRAP]] y [[arquitectura|arquitectura de agentes]]: ningún agente escribe memoria sin antes conocer estas reglas.

---

## Principio raíz

**La memoria es una observación con fecha, no estado vivo.** Todo lo que escribas hoy puede ser falso mañana sin que la memoria se entere. Por eso la memoria nunca debe ser la *fuente* de un hecho que cambia — solo un *puntero* hacia donde ese hecho vive vivo.

> Regla de oro: si un dato puede cambiar sin que tú lo edites, no lo guardes como hecho — guarda dónde verificarlo.

---

## Caso de estudio: el vault fantasma (2026-05-16)

El Great Vault vive en **dos máquinas**, sincronizadas por Syncthing — y en cada una ocupa una ruta distinta:

| Máquina | Usuario | Ruta del vault |
|---|---|---|
| Mac Mini (origen) | `jr` | `~/documents/Great Vault` |
| Mac Pro | `jotaerre` | `~/Great Vault` |

La memoria de Claude Code corre en la Mac Pro pero decía que el vault estaba en `~/Documents/Great Vault` — ruta heredada de la Mac Mini, donde sí es válida. En la Mac Pro esa ruta resuelve a un **directorio vacío**. Cualquier agente que leyera esa memoria iba al vacío — y en el peor caso, recreaba el vault desde cero, fragmentándolo más.

La trampa: "dónde está el vault" parece un hecho único, pero **depende de la máquina**. Ni la ruta absoluta ni la relativa al home coinciden entre las dos. Hardcodear cualquiera garantiza que sea falsa en al menos una máquina.

---

## Las reglas que nacen del caso

### 1. Un hecho, un dueño canónico

Un dato concreto (ruta, número de cuenta, fecha clave) se define en **un solo archivo**. Todos los demás archivos lo *referencian con wikilink*, nunca lo *copian*. Copiar un hecho = crear un punto que envejecerá en silencio.

- ✅ "El vault y sus rutas se definen en [[_AI_BOOTSTRAP]]."
- ❌ "El vault vive en `/Users/.../Great Vault`." (en cualquier archivo que no sea el canónico)

### 2. Memoria = puntero, no copia

La memoria debe ser pequeña y redirigir. Lo que debe sobrevivir en memoria es solo aquello que es *sobre cómo operar*, no *sobre datos que cambian*.

- ✅ "Fuente de verdad: leer [[_AI_BOOTSTRAP]] al inicio de cada sesión."
- ❌ Pegar el contenido del bootstrap dentro de la memoria.

### 3. Preferir reglas y procesos sobre estados

Una afirmación de **estado** envejece ("foco actual: 7 proyectos"). Una afirmación de **regla** no ("el foco actual siempre se lee del dashboard"). Cuando puedas elegir, escribe la regla.

- ✅ "El estado de proyectos se verifica en [[dashboard]] — nunca asumir desde memoria."
- ❌ "Proyecto X está en fase de conversión." (estará en otra fase pronto)

### 4. Las rutas no son hechos — son resoluciones

En un sistema multi-máquina o multi-usuario, **ninguna ruta absoluta es universal**. El vault está en `~/documents/Great Vault` (Mac Mini) y `~/Great Vault` (Mac Pro). La memoria no debe fijar una ruta — debe decir cómo *resolverla*: variable de runtime, ruta relativa al workspace, o tabla explícita por máquina.

- ✅ "El vault está en una ruta distinta por máquina (ver tabla en bootstrap). Resolver según el host antes de leer."
- ❌ "El vault está en `/Users/jr/documents/Great Vault`." (solo cierto en una máquina)

---

## Qué SÍ y qué NO va en memoria

| Va en memoria | NO va en memoria | Dónde va entonces |
|---|---|---|
| Reglas de interacción estables | Estado operativo (foco, fases) | `wiki/dashboard.md` |
| Preferencias de comunicación | Transcripts crudos de conversación | `conversaciones/YYYY-MM-DD.md` |
| Lecciones de errores cometidos | Decisiones puntuales de JR | `wiki/decisiones/YYYY-MM.md` |
| Cómo recuperarse tras pérdida de contexto | Cambios al vault | `wiki/log/YYYY-MM.md` |
| Punteros a la fuente de verdad | Datos que cambian semanalmente | página wiki canónica |
| — | PII, credenciales, NIT, DPI, cuentas | `_sensitive.md` (nunca en memoria) |

**Prueba rápida:** si el dato no cambia una decisión futura del agente, no merece estar en memoria. Si cambia cada mes, va al vault, no a memoria.

---

## Cómo escribir un hecho que envejece bien

1. **Fecha cada afirmación.** Toda línea de memoria lleva fecha o es atemporal por diseño. Sin fecha = imposible saber si caducó.
2. **Marca lo verificable.** Si algo *debe* re-chequearse, dilo explícito: *"verificar antes de actuar — puede haber cambiado"*.
3. **Escribe la causa, no solo la regla.** "JR pidió X el 2026-05-14 porque Y" sobrevive mejor que "hacer X" — si el porqué cambia, el agente sabe que la regla cae.
4. **Una línea = una idea verificable.** Cada entrada debe poder chequearse sí/no. Si no es verificable, es relleno.
5. **Densidad.** Sin párrafos largos. Si una línea no altera una decisión futura, bórrala.

**Antes / después:**

- ❌ `El vault está en ~/Documents/Great Vault y tiene proyectos activos.`
- ✅ `2026-05-16: vault canónico definido en [[_AI_BOOTSTRAP]]. No hardcodear la ruta en otros archivos — referenciar el bootstrap.`

---

## Formato de una entrada de memoria

```
AAAA-MM-DD: [contexto breve]. Regla duradera: [qué hacer / qué no].
```

Ejemplo real bien hecho (de la memoria de Geoffrey):

> 2026-05-14: JR se frustró porque Geoffrey volvió a preguntar datos básicos. Regla duradera: antes de preguntas de onboarding, auditar bootstrap, USER, IDENTITY, AGENT, SOUL, memoria y conversación reciente. Preguntar solo lo no inferible.

Tiene fecha, causa, regla accionable y es verificable. Ese es el molde.

---

## Actualizar vs. crear

- **Actualizar** una entrada existente: cuando es el *mismo* hecho refinado o corregido.
- **Crear** entrada nueva: cuando es una lección o decisión *nueva*. No sobrescribas una lección con otra distinta.
- **Nunca** reescribir historial append-only (`log/`, `decisiones/`, `conversaciones/`).
- Al corregir un hecho caducado, no lo borres en silencio: corrígelo y, si fue un error con consecuencia, deja la lección.

---

## Checklist de auditoría de memoria (mensual)

Correr sobre cada archivo de memoria:

- [ ] ¿Hay rutas, números o fechas absolutas que deberían ser punteros? → convertir a wikilink/referencia
- [ ] ¿El mismo dato aparece en 2+ archivos? → dejar uno canónico, los demás referencian
- [ ] ¿Hay afirmaciones de estado que ya caducaron? → mover a vault o borrar
- [ ] ¿Toda entrada tiene fecha o es atemporal a propósito?
- [ ] ¿Hay transcripts crudos o relleno? → destilar o borrar
- [ ] ¿Algún dato sensible se coló fuera de `_sensitive.md`? → mover y reportar
- [ ] ¿Los punteros siguen apuntando a archivos que existen? → verificar rutas vivas

---

## Relacionado

- [[_AI_BOOTSTRAP]] — entrada única y fuente canónica de rutas
- [[arquitectura|arquitectura de agentes]] — cómo se crean y operan los agentes del vault
- [[information-hierarchy]] — capas L0–L4 de información
- [[agentes/geoffrey/memoria|memoria de Geoffrey]] — ejemplo de memoria de agente que aplica esta guía
- [[wiki/index]] · [[dashboard]]
