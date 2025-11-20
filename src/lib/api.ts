// src/lib/api.ts
// Helper za komunikaciju s CNT backendom (FastAPI) preko /api/... ruta

export type Event = {
  id: number;
  title: string;
  description?: string | null;
  start_date: string;   // ISO date string
  end_date?: string | null;
};

export async function getEvents(): Promise<Event[]> {
  const res = await fetch("/api/events");
  if (!res.ok) {
    throw new Error("Greška pri učitavanju događaja");
  }
  return res.json();
}

export async function createEvent(event: Omit<Event, "id">) {
  const res = await fetch("/api/events", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(event),
  });
  if (!res.ok) {
    throw new Error("Greška pri kreiranju događaja");
  }
  return res.json();
}


// --- Workshops ---

export type Workshop = {
  id: number;
  title: string;
  description?: string | null;
  date: string;
};

export async function getWorkshops(): Promise<Workshop[]> {
  const res = await fetch("/api/workshops");
  if (!res.ok) {
    throw new Error("Greška pri učitavanju radionica");
  }
  return res.json();
}

export async function createWorkshop(
  workshop: Omit<Workshop, "id">
) {
  const res = await fetch("/api/workshops", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(workshop),
  });
  if (!res.ok) {
    throw new Error("Greška pri kreiranju radionice");
  }
  return res.json();
}


// --- Newsletter ---

export type NewsletterSubscriber = {
  id: number;
  email: string;
  created_at: string;
};

export async function subscribeNewsletter(email: string) {
  const res = await fetch("/api/newsletter", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  if (!res.ok) {
    throw new Error("Greška pri prijavi na newsletter");
  }
  return res.json();
}

export async function getNewsletterSubscribers(): Promise<NewsletterSubscriber[]> {
  const res = await fetch("/api/newsletter");
  if (!res.ok) {
    throw new Error("Greška pri učitavanju prijava");
  }
  return res.json();
}
