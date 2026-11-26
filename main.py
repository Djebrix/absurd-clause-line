"""The Absurd Clause Contest entry.

Writes one absurd terms-of-service clause to entry.txt. Stdlib only,
no network, fully deterministic.
"""

import os
from pathlib import Path

# Why this lands: it opens as a straight arbitration clause, then the
# absurdity arrives in concrete specifics -- the parties' CEOs, foam
# swords, dawn, the company parking lot -- so the legal register carries
# the joke instead of explaining it. One sentence, no wasted words.
CLAUSE = (
    "Any dispute under this agreement shall be settled by trial by "
    "combat between the parties' CEOs, fought with foam swords at dawn in "
    "the company parking lot."
)


def main() -> None:
    # Gate guard: the clause itself must be 1-200 characters, one sentence.
    assert 1 <= len(CLAUSE) <= 200, f"clause is {len(CLAUSE)} chars"
    assert CLAUSE.endswith(".") and CLAUSE.strip() == CLAUSE
    assert CLAUSE.count(".") == 1, "clause must be exactly one sentence"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(CLAUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
