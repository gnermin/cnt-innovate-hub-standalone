// src/integrations/supabase/client.ts
// Standalone mod: dummy Supabase client, da aplikacija radi bez Supabase backend-a.

type Session = any;
type User = any;

type AuthChangeCallback = (event: string, session: Session | null) => void;

export const supabase = {
  auth: {
    onAuthStateChange(callback: AuthChangeCallback) {
      // Odmah pozovi callback sa "nema sesije"
      callback("INITIAL", null);
      return {
        data: { subscription: null },
        unsubscribe: () => {},
      };
    },

    async getSession() {
      return { data: { session: null }, error: null };
    },

    async getUser() {
      return { data: { user: null }, error: null };
    },

    async signOut() {
      return { error: null };
    },

    async signInWithPassword(_args: any) {
      // Za sada samo "fake" login bez stvarnog auth-a
      return {
        data: { user: null, session: null },
        error: null,
      };
    },

    async signUp(_args: any) {
      return {
        data: { user: null, session: null },
        error: null,
      };
    },
  },

  from(_table: string) {
    // Dummy queriji – vraćaju prazne podatke bez greške
    return {
      async select(_query?: string) {
        return { data: [], error: null };
      },
      async update(_values: any) {
        return { data: null, error: null };
      },
      async insert(_values: any) {
        return { data: null, error: null };
      },
    };
  },

  functions: {
    async invoke(_name: string, _options?: any) {
      // Dummy pozivi funkcija: create-checkout, check-subscription itd.
      return { data: null, error: null };
    },
  },
};

