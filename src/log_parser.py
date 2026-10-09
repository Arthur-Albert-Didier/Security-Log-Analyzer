
import ipaddress
import re
from datetime import datetime


LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2}) "
    r"IP=(?P<ip>\S+) "
    r"USER=(?P<user>\S+) "
    r"STATUS=(?P<status>SUCCESS|FAILED)$"
)


def parse_log_line(line: str) -> dict | None:
    """Converte uma linha válida em um registro estruturado."""
    line = line.strip()

    if not line:
        return None

    match = LOG_PATTERN.fullmatch(line)

    if not match:
        return None

    data = match.groupdict()

    try:
        timestamp = datetime.strptime(
            data["timestamp"], "%Y-%m-%d %H:%M:%S"
        )
        ipaddress.ip_address(data["ip"])
    except ValueError:
        return None

    return {
        "timestamp": timestamp,
        "ip": data["ip"],
        "user": data["user"],
        "status": data["status"],
    }