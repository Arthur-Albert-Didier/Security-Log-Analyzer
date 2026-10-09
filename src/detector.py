
from collections import defaultdict
from datetime import timedelta


def detect_brute_force(
    logs: list[dict],
    threshold: int = 5,
    window_minutes: int = 5,
) -> list[dict]:
    """
    Detecta IPs com muitas falhas dentro de uma janela de tempo.
    Cada registro deve conter timestamp, ip e status.
    """
    if threshold < 1:
        raise ValueError("threshold deve ser maior que zero")

    if window_minutes < 1:
        raise ValueError("window_minutes deve ser maior que zero")

    failures_by_ip = defaultdict(list)

    for log in logs:
        if log["status"] == "FAILED":
            failures_by_ip[log["ip"]].append(log["timestamp"])

    alerts = []
    window = timedelta(minutes=window_minutes)

    for ip, timestamps in failures_by_ip.items():
        timestamps.sort()
        left = 0

        for right, current_time in enumerate(timestamps):
            while current_time - timestamps[left] > window:
                left += 1

            attempts = right - left + 1

            if attempts >= threshold:
                alerts.append({
                    "type": "POSSIBLE_BRUTE_FORCE",
                    "ip": ip,
                    "failed_attempts": attempts,
                    "window_minutes": window_minutes,
                    "first_attempt": timestamps[left],
                    "last_attempt": current_time,
                    "severity": "HIGH",
                    "message": (
                        f"{attempts} falhas de autenticação "
                        f"em até {window_minutes} minutos"
                    ),
                })

                # Um alerta por IP nesta execução.
                break

    return alerts