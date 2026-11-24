"""Write one funny autocorrect fail to /output/entry.txt.

The program writes a single fixed one-line text: a formal message to a
boss in which autocorrect turned "definitely" into "defiantly". No input,
no network, no randomness -- the output is identical on every run.
"""

import os

ENTRY = "Dear Mr. Thompson, I wanted to confirm I will defiantly attend tomorrow's board meeting and present the quarterly figures as requested."

def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
