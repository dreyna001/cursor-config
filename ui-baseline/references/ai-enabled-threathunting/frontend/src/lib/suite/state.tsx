import { createContext, useContext, useRef, useState, useSyncExternalStore, type Dispatch, type ReactNode, type SetStateAction } from "react";
/** One provider owns one session. Reactive readers subscribe; restoration-only readers do not. */
export function createStateScope<T>(initial: () => T) {
  type Store = { read: () => T; save: Dispatch<SetStateAction<T>>; subscribe: (listener: () => void) => () => void };
  const Context = createContext<Store | null>(null);
  function Provider({ children }: { children: ReactNode }) {
    const store = useRef<Store | null>(null);
    if (!store.current) {
      let value = initial();
      const listeners = new Set<() => void>();
      store.current = {
        read: () => value,
        save: (next) => {
          const updated = typeof next === "function" ? (next as (previous: T) => T)(value) : next;
          if (Object.is(updated, value)) return;
          value = updated; listeners.forEach(listener => listener());
        },
        subscribe: (listener) => { listeners.add(listener); return () => { listeners.delete(listener); }; },
      };
    }
    return <Context.Provider value={store.current}>{children}</Context.Provider>;
  }
  function useReactiveState() {
    const store = useContext(Context);
    const state = useSyncExternalStore(store?.subscribe ?? (() => () => undefined), store?.read ?? (() => null), store?.read ?? (() => null));
    return store ? { state: state as T, save: store.save } : null;
  }
  function useSnapshot() {
    const store = useContext(Context);
    // Route restoration reads on mount. Draft writes must not rerender every consumer.
    return store ? { state: store.read(), save: store.save } : null;
  }
  return { Provider, useState: useReactiveState, useSnapshot };
}
/** Local editable state keeps normal React semantics; native validation and domain guards stay authoritative. */
export function useFormState<T>(initial: T | (() => T)) { return useState<T>(initial); }
