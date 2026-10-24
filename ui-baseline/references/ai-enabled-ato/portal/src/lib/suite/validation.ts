import { z } from "zod";
export { z };
/** Preserve schema output/defaults/transforms; never coerce a failed boundary into a success. */
export function parseWithSchema<T>(schema: { safeParse: (value: unknown) => { success: boolean; data?: T } }, value: unknown): T | null {
  const result = schema.safeParse(value);
  return result.success ? result.data ?? null : null;
}
export type FieldErrors = Record<string, string>;
export function validateFields<T>(schema: z.ZodType<T, z.ZodTypeDef, unknown>, value: unknown):
  { success: true; data: T; errors: FieldErrors } | { success: false; errors: FieldErrors } {
  const result = schema.safeParse(value);
  if (result.success) return { success: true, data: result.data, errors: {} };
  const errors: FieldErrors = {};
  for (const issue of result.error.issues) {
    const key = issue.path.join(".") || "_form";
    errors[key] ??= issue.message;
  }
  return { success: false, errors };
}
