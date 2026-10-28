import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


# Target temperature tests
def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_early():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_mode_late():
    assert target_temperature("sleep", True, 23) == 18


def test_sleep_mode_normal_hours():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_morning_temperature():
    assert target_temperature("home", True, 7) == 22


def test_evening_temperature():
    assert target_temperature("home", True, 18) == 21


def test_default_temperature():
    assert target_temperature("home", True, 12) == 20


# HVAC action tests
def test_hvac_idle():
    assert hvac_action(20, 20.5, 10) == "idle"


def test_hvac_heat_boost():
    assert hvac_action(15, 20, 3) == "heat_boost"


def test_hvac_heat():
    assert hvac_action(15, 20, 10) == "heat"


def test_hvac_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool():
    assert hvac_action(25, 20, 20) == "cool"


# Energy alert tests
def test_no_readings():
    assert energy_alert([], 10) == "ok"


def test_energy_ok():
    assert energy_alert([5, 8, 9], 10) == "ok"


def test_energy_warning():
    assert energy_alert([11, 0], 10) == "warning"


def test_energy_critical():
    assert energy_alert([11, 12, 13], 10) == "critical"
