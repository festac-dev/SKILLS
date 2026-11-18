'use strict';
const { createApp } = require('./app');
const port = Number(process.env.PORT || 8080);
if (!Number.isInteger(port) || port < 1 || port > 65535) { console.error('Invalid PORT'); process.exit(1); } // fail fast on bad config
const app = createApp({ drainDelayMs: Number(process.env.DRAIN_DELAY_MS || 0), trustProxy: process.env.TRUST_PROXY === '1' });
app.server.listen(port, () => console.log(JSON.stringify({ level: 'info', msg: 'listening', port })));
for (const sig of ['SIGTERM', 'SIGINT']) process.on(sig, async () => { await app.shutdown(); process.exit(0); });
process.on('unhandledRejection', (e) => { console.error(JSON.stringify({ level: 'error', msg: 'unhandledRejection', err: String(e) })); process.exit(1); });
