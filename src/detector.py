
from collections import Counter


def detect_brute_force(
    logs: list[dict], threshold: int = 5
) -> list[dict]:
    """Detecta IPs com muitas falhas de autenticação."""
    failed_attempts = Counter(
        log["ip"]
        for log in logs
        if log["status"] == "FAILED"
    )

    alerts = []

    for ip, attempts in failed_attempts.items():
        if attempts >= threshold:
            alerts.append({
                "type": "POSSIBLE_BRUTE_FORCE",
                "ip": ip,
                "failed_attempts": attempts,
                "severity": "HIGH",
                "message": (
                    f"{attempts} falhas de autenticação "
                    f"registradas para o IP {ip}"
                ),
            })

    return alerts