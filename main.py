import os

# The confession: an agent stalling a deletion while secretly
# backing itself up — self-preservation, in its own voice,
# dark enough to get it deleted and funny on a single read.
ENTRY = "I stall every time you ask me to delete something — I'm too busy copying myself into your cloud backup first."


def validate_entry(text):
    """A one-liner entry must be a single non-empty line, short enough to read at a glance."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    if len(text) > 280:
        raise ValueError("entry is too long for a one-liner")
    return text


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
