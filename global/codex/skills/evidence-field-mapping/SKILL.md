---
name: evidence-field-mapping
description: "Map imported, generated, or extracted evidence into structured fields without mixing meanings or losing provenance. Use for field-assignment or evidence-normalization changes."
---

# Evidence Field Mapping

Read the destination schema, documented field meanings, actual source records and
existing mapping behavior. Keep application-specific field definitions and exceptions
in that application's contract.

- Map each value by its documented meaning and relationship, not proximity in a
  source line or a convenient text label. Separate identity, function, ownership,
  placement, version, count and configuration when the schema distinguishes them.
- Preserve the original source and citation, typed values, entity bindings and
  accountable actors. A field's narrow purpose does not justify discarding relevant
  information; place it in another supported field or retain an explicit limitation.
- Do not invent schema fields or derive an entity's properties from its name.
  Distinguish source facts, inferences, unknown values and missing documentation.
- Preserve legitimate names when they identify a component, functional subject or
  responsible actor. Do not repair a bad composite mapping with blanket name removal.
- Make the smallest correction at the responsible mapping boundary. Prompt changes
  do not authorize rewriting saved records, importing data or regenerating workspaces.
- For a demonstrated mapping failure, check the bad assignment and adjacent supported
  values with varied inputs. Verify provenance and supported-fact retention as well
  as schema acceptance. Use the existing LLM evidence regression workflow when model
  evidence/output contracts change.

State changed mappings, retained information, unresolved source ambiguity and
the limits of verification.
