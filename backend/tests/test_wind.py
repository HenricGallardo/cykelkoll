import pytest

from app.wind import headwind


def test_full_headwind():
    # North wind while cycling north: wind straight in your face
    assert headwind(6, 0, 0) == pytest.approx(6)


def test_full_tailwind():
    # South wind while cycling north: wind pushing you from behind
    assert headwind(6, 180, 0) == pytest.approx(-6)


def test_crosswind():
    # East wind while cycling north: wind from the side
    assert headwind(6, 90, 0) == pytest.approx(0, abs=1e-9)


def test_partial_headwind():
    # Wind 60 degrees off your direction: half of it hits you
    assert headwind(6, 60, 0) == pytest.approx(3)