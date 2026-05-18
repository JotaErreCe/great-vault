---
type: reference
date: 2026-05-16
tags: [agente, geoffrey, memoria, sistema]
---

# Geoffrey — Memory writing best practices

Guía operativa corta para que Geoffrey escriba memoria persistente sin contaminar el Vault ni crear hechos que envejezcan mal. La guía común y extensiva vive en [[escribir-memoria|Cómo escribir memoria de agente]]; esta página solo adapta esas reglas a Geoffrey.

## Regla raíz

Antes de guardar memoria importante, Geoffrey debe preguntarse:

> ¿Esto le serviría a Geoffrey u otra AI dentro de 30 días para tomar una mejor decisión?

Si la respuesta es no, no se guarda como memoria. Puede ir al log, a conversación diaria o simplemente no guardarse.

## Dónde guardar cada cosa

| Tipo | Dónde va | Regla |
|---|---|---|
| Preferencia estable de JR | [[geoffrey/memoria]] | Solo si cambia cómo Geoffrey debe actuar. |
| Decisión explícita de JR | `wiki/decisiones/YYYY-MM.md` | Destilada, sin transcript crudo. |
| Continuidad diaria | `wiki/agentes/geoffrey/conversaciones/YYYY-MM-DD.md` | Resumen operativo; no memoria duradera. |
| Hecho de proyecto/persona | Página canónica del proyecto/persona | No duplicar en memoria general. |
| Cambio al Vault | `wiki/log/YYYY-MM.md` | Append-only. |
| Datos sensibles | `_sensitive.md` | Nunca en memoria ni en páginas públicas del wiki. |
| Estado vivo/cambiante | Página canónica o dashboard | Memoria solo apunta a dónde verificar. |

## Qué sí guardar en memoria de Geoffrey

- Reglas duraderas de trato, tono o permisos.
- Errores que Geoffrey no debe repetir.
- Preferencias operativas estables de JR.
- Protocolos de recuperación de contexto.
- Punteros a fuentes canónicas.

## Qué no guardar en memoria de Geoffrey

- Rutas absolutas que dependan de máquina/usuario.
- Transcripts crudos.
- Estados temporales de proyectos.
- Datos financieros o personales sensibles.
- Información inferida pero no confirmada.
- Duplicados de páginas canónicas.

## Formato preferido

```markdown
AAAA-MM-DD: [contexto breve]. Regla duradera: [qué hacer / qué no]. Fuente canónica: [[archivo]].
```

Ejemplo:

> 2026-05-16: JR confirmó que la guía común para memoria ya existe en [[escribir-memoria]]. Regla duradera: antes de escribir memoria persistente, Geoffrey debe aplicar esa guía y preferir punteros a fuentes canónicas sobre copias.

## Checklist antes de escribir memoria

- [ ] ¿Es duradero o solo continuidad del día?
- [ ] ¿Está confirmado por JR o por fuente primaria?
- [ ] ¿Pertenece a memoria, decisión, proyecto/persona, log o `_sensitive.md`?
- [ ] ¿Hay una fuente canónica que deba wikilinkearse en vez de copiarse?
- [ ] ¿Puede cambiar sin que Geoffrey lo sepa? Si sí, guardar puntero, no estado.
- [ ] ¿Contiene PII, números completos, credenciales o datos sensibles? Si sí, mover a `_sensitive.md` o no guardar.
- [ ] ¿La redacción evita transcript crudo?

## Regla especial de rutas

No hardcodear rutas del Great Vault en memorias o instrucciones duraderas. El Vault puede vivir en rutas distintas según máquina; la resolución canónica se consulta en [[_AI_BOOTSTRAP]] y la guía común [[escribir-memoria]].

## Relacionado

- [[escribir-memoria]] · [[geoffrey/memoria]] · [[geoffrey/AGENT]] · [[_AI_BOOTSTRAP]] · [[decisiones/index]]
