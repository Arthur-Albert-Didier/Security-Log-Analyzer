
from datetime import datetime

from src.log_parser import parse_log_line


def test_parse_valid_log():
    line = (
        "2026-10-09 08:00:12 "
        "IP=192.168.1.10 USER=alice STATUS=SUCCESS"
    )

    result = parse_log_line(line)

    assert result is not None
    assert result["ip"] == "192.168.1.10"
    assert result["user"] == "alice"
    assert result["status"] == "SUCCESS"
    assert result["timestamp"] == datetime(
        2026, 10, 9, 8, 0, 12
    )


def test_reject_malformed_log():
    line = "This is not a valid log"

    assert parse_log_line(line) is None


def test_reject_invalid_date():
    line = (
        "2026-13-40 08:00:12 "
        "IP=192.168.1.10 USER=alice STATUS=SUCCESS"
    )

    assert parse_log_line(line) is None


def test_ignore_empty_line():
    assert parse_log_line("   ") is None

    
def test_reject_invalid_ip():
    line = (
        "2026-10-09 08:00:12 "
        "IP=999.999.999.999 USER=alice STATUS=SUCCESS"
    )

    assert parse_log_line(line) is None