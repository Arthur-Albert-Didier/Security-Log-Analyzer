
from datetime import datetime, timedelta

import pytest

from src.detector import detect_brute_force


BASE_TIME = datetime(2026, 10, 9, 8, 0, 0)


def make_failed_logs(
    ip: str,
    count: int,
    interval_seconds: int = 30,
) -> list[dict]:
    return [
        {
            "ip": ip,
            "status": "FAILED",
            "timestamp": BASE_TIME
            + timedelta(seconds=i * interval_seconds),
        }
        for i in range(count)
    ]


def test_detect_five_failures_within_window():
    logs = make_failed_logs("192.168.1.15", 5)

    alerts = detect_brute_force(logs)

    assert len(alerts) == 1
    assert alerts[0]["ip"] == "192.168.1.15"
    assert alerts[0]["failed_attempts"] == 5
    assert alerts[0]["type"] == "POSSIBLE_BRUTE_FORCE"


def test_no_alert_below_threshold():
    logs = make_failed_logs("192.168.1.15", 4)

    assert detect_brute_force(logs) == []


def test_failures_outside_window_do_not_trigger_alert():
    logs = make_failed_logs(
        "192.168.1.15",
        5,
        interval_seconds=180,
    )

    assert detect_brute_force(logs) == []


def test_successful_log_does_not_count_as_failure():
    logs = [
        {
            "ip": "192.168.1.15",
            "status": "SUCCESS",
            "timestamp": BASE_TIME + timedelta(seconds=i),
        }
        for i in range(10)
    ]

    assert detect_brute_force(logs) == []


def test_detect_multiple_suspicious_ips():
    logs = (
        make_failed_logs("192.168.1.15", 5)
        + make_failed_logs("192.168.1.20", 6)
    )

    alerts = detect_brute_force(logs)

    assert len(alerts) == 2
    assert {alert["ip"] for alert in alerts} == {
        "192.168.1.15",
        "192.168.1.20",
    }


def test_invalid_threshold_is_rejected():
    with pytest.raises(ValueError):
        detect_brute_force([], threshold=0)


def test_invalid_window_is_rejected():
    with pytest.raises(ValueError):
        detect_brute_force([], window_minutes=0)