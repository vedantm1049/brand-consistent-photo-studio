#!/usr/bin/env python3
"""Validate and normalize Cafe Picture Generator CSV batches."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path, PurePath


REQUIRED_COLUMNS = {"sku_name", "description", "format"}
ALL_COLUMNS = [
    "sku_name",
    "description",
    "format",
    "drink_appearance",
    "top_treatment",
    "garnish_left",
    "garnish_right",
    "garnish_back",
    "garnish_notes",
    "special_instructions",
    "output_filename",
]
FORMATS = {"hot", "iced", "frappe", "protein", "slush"}
GARNISH_COLUMNS = ("garnish_left", "garnish_right", "garnish_back")


def slug_filename(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return f"{slug}.png"


def normalize_row(row: dict[str, str]) -> dict[str, str]:
    normalized = {column: (row.get(column) or "").strip() for column in ALL_COLUMNS}
    normalized["format"] = normalized["format"].lower()
    for column in GARNISH_COLUMNS:
        if not normalized[column]:
            normalized[column] = "none"
    if not normalized["output_filename"] and normalized["sku_name"]:
        normalized["output_filename"] = slug_filename(normalized["sku_name"])
    return normalized


def validate_rows(fieldnames: list[str] | None, rows: list[dict[str, str]]) -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    fields = set(fieldnames or [])
    missing = sorted(REQUIRED_COLUMNS - fields)
    if missing:
        errors.append(f"Missing required columns: {', '.join(missing)}")

    normalized_rows: list[dict[str, str]] = []
    seen_names: dict[str, int] = {}
    seen_files: dict[str, int] = {}

    for csv_row_number, raw_row in enumerate(rows, start=2):
        row = normalize_row(raw_row)
        normalized_rows.append(row)
        label = row["sku_name"] or f"row {csv_row_number}"

        for column in REQUIRED_COLUMNS:
            if not row[column]:
                errors.append(f"Row {csv_row_number} ({label}): {column} is required")

        if row["format"] and row["format"] not in FORMATS:
            errors.append(
                f"Row {csv_row_number} ({label}): unsupported format '{row['format']}'"
            )

        name_key = row["sku_name"].casefold()
        if name_key:
            if name_key in seen_names:
                errors.append(
                    f"Row {csv_row_number} ({label}): duplicate sku_name; first used on row {seen_names[name_key]}"
                )
            else:
                seen_names[name_key] = csv_row_number

        filename = row["output_filename"]
        if filename:
            if not filename.lower().endswith(".png"):
                errors.append(f"Row {csv_row_number} ({label}): output_filename must end in .png")
            if PurePath(filename).name != filename or "/" in filename or "\\" in filename:
                errors.append(f"Row {csv_row_number} ({label}): output_filename must not contain a path")
            file_key = filename.casefold()
            if file_key in seen_files:
                errors.append(
                    f"Row {csv_row_number} ({label}): duplicate output_filename; first used on row {seen_files[file_key]}"
                )
            else:
                seen_files[file_key] = csv_row_number

        garnishes = [row[column].casefold() for column in GARNISH_COLUMNS if row[column].casefold() != "none"]
        duplicate_garnishes = sorted({item for item in garnishes if garnishes.count(item) > 1})
        if duplicate_garnishes and "repeat" not in row["garnish_notes"].casefold():
            errors.append(
                f"Row {csv_row_number} ({label}): garnish appears in multiple zones without an explicit repeat note: {', '.join(duplicate_garnishes)}"
            )

    return errors, normalized_rows


def read_csv(path: Path) -> tuple[list[str] | None, list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames, list(reader)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ALL_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="CSV batch to validate")
    parser.add_argument(
        "--write-normalized",
        type=Path,
        metavar="PATH",
        help="Write a normalized CSV when validation succeeds",
    )
    args = parser.parse_args()

    if not args.csv_file.is_file():
        print(f"ERROR: file not found: {args.csv_file}", file=sys.stderr)
        return 2

    try:
        fieldnames, rows = read_csv(args.csv_file)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: could not read CSV: {exc}", file=sys.stderr)
        return 2

    errors, normalized = validate_rows(fieldnames, rows)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if args.write_normalized:
        write_csv(args.write_normalized, normalized)
        print(f"Validated {len(normalized)} row(s); wrote {args.write_normalized}")
    else:
        print(f"Validated {len(normalized)} row(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

