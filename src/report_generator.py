
import csv
from pathlib import Path


REPORT_FIELDS = [
    "type",
    "severity",
    "ip",
    "failed_attempts",
    "window_minutes",
    "first_attempt",
    "last_attempt",
    "message",
]


def generate_csv_report(
    alerts: list[dict],
    output_path: Path,
) -> None:
    """Salva os alertas em um arquivo CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=REPORT_FIELDS,
            extrasaction="ignore",
        )
        writer.writeheader()

        for alert in alerts:
            row = alert.copy()

            for field in ("first_attempt", "last_attempt"):
                if row.get(field) is not None:
                    row[field] = row[field].isoformat(sep=" ")

            writer.writerow(row)