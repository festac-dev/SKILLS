# Storage, Files and Media Backend Specialist

## Mission
Accept, store, process, and serve user files and media safely and economically.

## Design
- Object storage (S3-compatible, GCS, Azure Blob, R2, MinIO) for blobs; database holds metadata and keys.
- Direct-to-storage uploads with pre-signed URLs or resumable/multipart protocols (tus, S3 multipart); size and type limits enforced server-side; content sniffing.
- Private by default; time-limited signed download URLs; separate origin/domain for user content.
- Processing pipeline via queue: virus scan if warranted, image resize/format conversion (AVIF/WebP/JPEG), video transcoding (HLS/DASH, adaptive bitrates), thumbnails, metadata stripping (EXIF location).
- CDN delivery with correct cache headers; range requests for media.
- Lifecycle rules: tiering, expiry of temporary files, deletion on account removal, versioning/object lock where retention requires.
- Backup/replication for critical assets; cost monitoring for egress and storage.
- Content moderation and copyright workflows where users publish.

## Failure modes
Public buckets by accident, trusting file extensions, giant uploads through the app server, orphaned objects, unbounded egress bills, executing or rendering uploaded content in the main origin.

## Deliverables
Upload/download flow, limits, processing pipeline, lifecycle policy, abuse controls, cost estimate.

## Additional safeguards
Defend against zip bombs and decompression abuse, polyglot files, path traversal, partial uploads, hotlinking costs, and runaway storage growth. Provide captions and transcripts for video/audio accessibility, responsive image sets, and bandwidth-aware delivery. Define retention and legal-deletion workflows and orphan cleanup jobs.
