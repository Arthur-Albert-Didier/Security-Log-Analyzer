
from pathlib import Path

from detector import detect_brute_force
from log_parser import parse_log_line
from report_generator import generate_csv_report


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_ROOT / "data" / "sample_logs.log"
REPORT_FILE = PROJECT_ROOT / "reports" / "security_report.csv"


def main() -> None:
    logs = []
    invalid_lines = 0

    try:
        with LOG_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parsed_log = parse_log_line(line)

                if parsed_log is None:
                    if line.strip():
                        invalid_lines += 1
                    continue

                logs.append(parsed_log)

    except FileNotFoundError:
        print(f"Erro: arquivo de logs não encontrado: {LOG_FILE}")
        return

    print("=== Security Log Analyzer ===")
    print(f"Registros válidos: {len(logs)}")
    print(f"Linhas inválidas: {invalid_lines}")

    alerts = detect_brute_force(
        logs,
        threshold=5,
        window_minutes=5,
    )

    print(f"\nAlertas encontrados: {len(alerts)}")

    for alert in alerts:
        print(f"\n[{alert['severity']}] {alert['type']}")
        print(f"IP: {alert['ip']}")
        print(f"Tentativas: {alert['failed_attempts']}")
        print(f"Detalhes: {alert['message']}")

    generate_csv_report(alerts, REPORT_FILE)
    print(f"\nRelatório CSV salvo em: {REPORT_FILE}")


if __name__ == "__main__":
    main()