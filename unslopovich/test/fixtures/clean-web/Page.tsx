export default function Page({ zones }) {
  return (
    <main className="mx-auto max-w-5xl px-6">
      <h1 className="text-3xl font-medium">Zones</h1>
      <p className="text-zinc-600">17 zones, 1 waiting for nameservers</p>
      <img src="/map.png" alt="Map of edge locations serving your zones" width={960} height={480} />
      <div className="h-4 w-32 animate-pulse rounded bg-zinc-200" />
      <ul>
        {zones.map((z) => (
          <li key={z.id}>
            <a className="rounded transition-colors hover:bg-zinc-100 focus-visible:outline-2 focus-visible:outline-offset-2" href={`/zones/${z.id}`}>
              {z.name}
            </a>
            <button className="outline-none focus-visible:ring-2" onClick={() => purge(z.id)}>Purge cache</button>
          </li>
        ))}
      </ul>
    </main>
  );
}
