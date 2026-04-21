"""Copy GPX files from region folders to _static/gpx for the map."""
import shutil
import time
from pathlib import Path

def copy_gpx_files():
    """Recursively find and copy all GPX files to _static/gpx."""
    docs_dir = Path(__file__).parent
    static_gpx_dir = docs_dir / "_static" / "gpx"

    # Create the target directory if it doesn't exist
    static_gpx_dir.mkdir(parents=True, exist_ok=True)

    # Find all GPX files in region folders
    gpx_files = sorted(docs_dir.glob("*/gpx/*.gpx"))

    if not gpx_files:
        print("No GPX files found in region folders")
        return

    print(f"Found {len(gpx_files)} GPX files. Copying to _static/gpx/")

    for gpx_file in gpx_files:
        dest = static_gpx_dir / gpx_file.name
        try:
            shutil.copy2(gpx_file, dest)
            print(f"  [OK] {gpx_file.relative_to(docs_dir)}")
        except PermissionError:
            # File might be locked, wait a moment and retry
            time.sleep(0.5)
            try:
                shutil.copy2(gpx_file, dest)
                print(f"  [OK] {gpx_file.relative_to(docs_dir)}")
            except Exception as e:
                print(f"  [SKIP] {gpx_file.name}: {e}")
        except Exception as e:
            print(f"  [SKIP] {gpx_file.name}: {e}")

if __name__ == "__main__":
    copy_gpx_files()
