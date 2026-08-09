#!/usr/bin/env python3
"""Generate the soft start/stop feedback blips used by the Custom sound theme.

Writes custom_start.wav / custom_stop.wav, which Handy reads from the app data
dir when Settings -> Sound Theme is set to "Custom" (see audio_feedback.rs).

Run with no arguments to write straight into the app data dir for this OS, or
pass an output directory:

    python scripts/gen_custom_sounds.py [outdir]

The tone is deliberately soft: a sine with a raised-cosine attack (no click), an
exponential decay, and a little second harmonic for body. Start glides up, stop
glides down, so the two are distinguishable without being loud.
"""

import math
import os
import struct
import sys
import wave

RATE = 48000


def blip(f0, f1, ms, peak=0.5, attack_ms=8.0, tau_ms=38.0, harmonic=0.18):
    """One short pitch-gliding tone, returned as a list of floats in [-1, 1]."""
    n = int(RATE * ms / 1000.0)
    attack = max(1, int(RATE * attack_ms / 1000.0))
    tau = RATE * tau_ms / 1000.0
    out = []
    phase = 0.0
    for i in range(n):
        t = i / n
        # Exponential frequency glide reads as smoother than a linear one.
        freq = f0 * (f1 / f0) ** t
        phase += 2 * math.pi * freq / RATE
        # Raised-cosine attack removes the click a hard start would produce.
        env = 0.5 - 0.5 * math.cos(math.pi * min(1.0, i / attack))
        env *= math.exp(-i / tau)
        out.append(peak * env * (math.sin(phase) + harmonic * math.sin(2 * phase)))
    return out


def write_wav(path, samples):
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        frames = b"".join(
            struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767)) for s in samples
        )
        w.writeframes(frames)
    print(f"wrote {path} ({len(samples) / RATE * 1000:.0f} ms)")


def default_outdir():
    if sys.platform == "win32":
        return os.path.join(os.environ["APPDATA"], "com.pais.handy")
    if sys.platform == "darwin":
        return os.path.expanduser("~/Library/Application Support/com.pais.handy")
    return os.path.expanduser("~/.local/share/com.pais.handy")


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else default_outdir()
    os.makedirs(outdir, exist_ok=True)
    write_wav(os.path.join(outdir, "custom_start.wav"), blip(523.25, 784.0, 105))
    write_wav(os.path.join(outdir, "custom_stop.wav"), blip(784.0, 523.25, 125))


if __name__ == "__main__":
    main()
