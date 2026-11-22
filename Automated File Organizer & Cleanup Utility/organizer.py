import os
import shutil
import argparse
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            Path(__file__).parent / "logs" / "organizer.log",
            encoding="utf-8"
        )
    ]
)

EXTENSION_MAP = {
    ".pdf": "Documents", ".doc": "Documents",
    ".docx": "Documents", ".txt": "Documents",
    ".xls": "Documents", ".xlsx": "Documents",
    ".ppt": "Documents", ".pptx": "Documents",
    ".csv": "Documents", ".rtf": "Documents",
    ".jpg": "Images", ".jpeg": "Images",
    ".png": "Images", ".gif": "Images",
    ".bmp": "Images", ".webp": "Images",
    ".svg": "Images",
    ".mp4": "Videos", ".mkv": "Videos",
    ".avi": "Videos", ".mov": "Videos",
    ".wmv": "Videos",
    ".zip": "Archives", ".rar": "Archives",
    ".7z": "Archives", ".tar": "Archives",
    ".gz": "Archives",
    ".py": "Code", ".java": "Code",
    ".js": "Code", ".html": "Code",
    ".css": "Code", ".cpp": "Code",
    ".c": "Code", ".json": "Code",
    ".sql": "Code"
}


def get_unique_path(destination):
    """Avoid overwriting files with the same name."""
    destination = Path(destination)

    if not destination.exists():
        return destination

    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1


def organize_folder(folder_path, apply_changes=False):
    """Organize files in one directory, without scanning subfolders."""
    folder = Path(folder_path).expanduser().resolve()

    if not folder.is_dir():
        logging.error("Directory does not exist: %s", folder)
        return

    processed = 0
    skipped = 0
    failed = 0

    try:
        with os.scandir(folder) as entries:
            for entry in entries:
                try:
                    if not entry.is_file(follow_symlinks=False):
                        continue

                    source = Path(entry.path)
                    category = EXTENSION_MAP.get(
                        source.suffix.lower(), "Others"
                    )

                    if source.parent.name == category:
                        skipped += 1
                        continue

                    destination_folder = folder / category
                    destination = get_unique_path(
                        destination_folder / source.name
                    )

                    if not apply_changes:
                        logging.info(
                            "[DRY RUN] %s -> %s",
                            source.name,
                            destination.relative_to(folder)
                        )
                        processed += 1
                        continue

                    destination_folder.mkdir(
                        parents=True, exist_ok=True
                    )
                    shutil.move(str(source), str(destination))

                    logging.info(
                        "Moved: %s -> %s",
                        source.name,
                        destination.relative_to(folder)
                    )
                    processed += 1

                except PermissionError as error:
                    logging.warning(
                        "Permission denied for %s: %s",
                        entry.name, error
                    )
                    failed += 1

                except OSError as error:
                    logging.error(
                        "Could not process %s: %s",
                        entry.name, error
                    )
                    failed += 1

    except (PermissionError, OSError) as error:
        logging.error("Could not scan directory: %s", error)
        return

    print("\n========== ORGANIZER SUMMARY ==========")
    print(f"Directory       : {folder}")
    print(f"Files processed : {processed}")
    print(f"Files skipped   : {skipped}")
    print(f"Failures        : {failed}")
    print(f"Mode            : {'LIVE' if apply_changes else 'DRY RUN'}")
    print("========================================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organize files by extension."
    )
    parser.add_argument("folder", help="Directory to organize")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files; default is preview only"
    )

    args = parser.parse_args()
    organize_folder(args.folder, apply_changes=args.apply)
