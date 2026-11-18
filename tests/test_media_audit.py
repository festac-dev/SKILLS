"""Test optional media checks against a real, locally generated fixture."""

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("media_audit", ROOT / "scripts/media_audit.py")
media = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(media)


class MediaParsingTests(unittest.TestCase):
    def test_rational_frame_rate_and_unknown_rate(self):
        self.assertAlmostEqual(media.frame_rate("30000/1001"), 29.97002997)
        self.assertIsNone(media.frame_rate("0/0"))

    def test_silence_is_not_reported_as_finite_loudness(self):
        self.assertEqual(media.loudness_values('{"input_i":"-inf","input_tp":"-inf"}'),
                         {"integrated_lufs": None, "true_peak_dbtp": None})

    def test_album_art_does_not_count_as_the_video(self):
        with self.assertRaisesRegex(ValueError, "No video"):
            media.summarize_probe({"streams": [{"codec_type": "video", "disposition": {"attached_pic": 1}}]})

    def test_primary_video_metadata_ignores_album_art(self):
        result = media.summarize_probe({"streams": [
            {"index": 0, "codec_type": "video", "disposition": {"attached_pic": 1}},
            {"index": 2, "codec_type": "video", "width": 320, "height": 180}]})
        self.assertEqual(result["video_stream_index"], 2)
        self.assertEqual(result["width"], 320)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "Local FFmpeg and ffprobe required")
class MediaIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.folder = Path(cls.temp.name)
        cls.source = cls.folder / "test clip.mp4"
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-f", "lavfi", "-i",
                        "testsrc2=size=320x180:rate=30", "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000",
                        "-t", "1.2", "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", str(cls.source)], check=True, capture_output=True, timeout=60)
        cls.original_hash = hashlib.sha256(cls.source.read_bytes()).hexdigest()

    def audit(self, *args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = media.main([str(self.source), *args])
        self.assertEqual(hashlib.sha256(self.source.read_bytes()).hexdigest(), self.original_hash)
        return code, json.loads(output.getvalue())

    def test_no_forced_dimensions_or_duration(self):
        code, report = self.audit()
        self.assertEqual(code, 0, report)
        self.assertEqual(report["metadata"]["width"], 320)
        self.assertEqual(report["metadata"]["audio_streams"], 1)

    def test_explicit_contract_and_complete_decode(self):
        code, report = self.audit("--width", "320", "--height", "180", "--fps", "30",
                                  "--video-codec", "h264", "--require-audio", "--decode")
        self.assertEqual(code, 0, report)
        self.assertEqual(report["checks"]["decode"], "passed")

    def test_mismatched_contract_fails(self):
        code, report = self.audit("--width", "1920", "--min-duration", "60")
        self.assertEqual(code, 1)
        self.assertEqual(len(report["errors"]), 2)

    def test_measures_audio_and_rejects_unmet_peak_target(self):
        code, report = self.audit("--loudness")
        self.assertEqual(code, 0, report)
        self.assertIsInstance(report["loudness"]["integrated_lufs"], float)
        stricter_peak = report["loudness"]["true_peak_dbtp"] - 2
        code, report = self.audit("--max-true-peak", str(stricter_peak))
        self.assertEqual(code, 1)
        self.assertTrue(any("True peak" in e for e in report["errors"]))

    def test_frames_are_extracted_and_not_overwritten(self):
        destination = self.folder / "frames"
        code, report = self.audit("--sample-times", "0,0.6", "--frames-dir", str(destination))
        self.assertEqual(code, 0, report)
        original = {p: Path(p).read_bytes() for p in report["frames"]}
        self.assertEqual(len(original), 2)
        code, report = self.audit("--sample-times", "0,0.6", "--frames-dir", str(destination))
        self.assertEqual(code, 1)
        self.assertTrue(any("already exists" in e for e in report["errors"]))
        self.assertTrue(all(Path(p).read_bytes() == data for p, data in original.items()))

    def test_invalid_timestamps_write_no_frames(self):
        destination = self.folder / "invalid"
        code, report = self.audit("--sample-times", "nan,0.6", "--frames-dir", str(destination))
        self.assertEqual(code, 1)
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
