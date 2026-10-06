"""Execute every notebook in a fresh kernel without changing source notebooks."""
from pathlib import Path
import sys

import nbformat
from nbclient import NotebookClient


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    paths = sorted((root / "Notebooks").glob("*.ipynb"))
    if not paths:
        print("No notebooks found", file=sys.stderr)
        return 1
    failures = []
    for path in paths:
        print(f"RUN {path.name}", flush=True)
        try:
            notebook = nbformat.read(path, as_version=4)
            NotebookClient(
                notebook, timeout=180, kernel_name="python3",
                resources={"metadata": {"path": str(path.parent)}},
            ).execute()
        except Exception as error:
            failures.append(path.name)
            print(f"FAIL {path.name}: {error}", file=sys.stderr, flush=True)
        else:
            print(f"PASS {path.name}", flush=True)
    print(f"{len(paths) - len(failures)}/{len(paths)} notebooks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
