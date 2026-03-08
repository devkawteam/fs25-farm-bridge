"""Top-level runnable script for the FS25 Farm Bridge.

This exists to support legacy invocation like:

    python farm_bridge.py

The real implementation lives in the `fs25_farm_bridge` package.
"""

from fs25_farm_bridge.bridge import main


if __name__ == "__main__":
    main()
