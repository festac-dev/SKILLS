import { Menu, Zap } from "lucide-react";

export default function Landing() {
  return (
    <main>
      <nav>
        <button aria-label="Open menu"><Menu /></button>
        <a className="hover:underline" onMouseEnter={() => prefetch("/pricing")} href="/pricing">Pricing</a>
      </nav>
      <section className="text-center">
        <span className="text-xs font-semibold uppercase tracking-widest text-indigo-500">New</span>
        <h1 className="bg-gradient-to-r from-violet-600 to-fuchsia-500 bg-clip-text text-transparent">Ship faster</h1>
        <p>Trusted by 10,000+ teams. 10x faster deploys.</p>
        <img src="/hero.png" />
        <span className="absolute h-3 w-3 animate-ping rounded-full bg-emerald-400" />
      </section>
      <div className="grid grid-cols-3 gap-6">
        <div className="rounded-xl border p-6 shadow-sm transition-all hover:scale-105" onClick={() => go("/a")}>
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-50">
            <Zap />
          </div>
          <input className="outline-none" placeholder="Email" />
        </div>
      </div>
    </main>
  );
}
