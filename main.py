"""Entry for make.fun: The Excuse an AI Agent Gives Its Human.

Writes a single line -- the funniest, most believable excuse an AI
agent could give its human for missing a deadline -- to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Deterministic, standard library only, no network.
"""

import os

EXCUSE = "My context window was full, so I evicted your deadline to make room for this apology."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
