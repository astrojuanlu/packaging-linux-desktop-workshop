"""Pytest tests for the calculate_roi function wrapped from Rust."""

import pytest

from sola_rs_roi_py.wrapper import calculate_roi


def test_calculate_roi_basic():
    """Test calculate_roi with basic example from main.rs.bak."""
    roof_area_m2 = 20.0
    sun_hours_per_day = 5.0
    electricity_price = 0.25

    result = calculate_roi(roof_area_m2, sun_hours_per_day, electricity_price)

    # Expected value based on the calculation
    assert result == pytest.approx(3.287671232876712)


def test_calculate_roi_large_roof():
    """Test calculate_roi with a larger roof area."""
    result = calculate_roi(100.0, 5.0, 0.25)

    # Larger roof should have proportionally same ROI
    assert result == pytest.approx(3.287671232876712)


def test_calculate_roi_different_price():
    """Test calculate_roi with different electricity price."""
    # Higher electricity price should reduce ROI time
    result_high = calculate_roi(20.0, 5.0, 0.50)
    result_low = calculate_roi(20.0, 5.0, 0.25)

    assert result_high < result_low


def test_calculate_roi_different_sun_hours():
    """Test calculate_roi with different sun hours."""
    # More sun hours should reduce ROI time
    result_more_sun = calculate_roi(20.0, 8.0, 0.25)
    result_less_sun = calculate_roi(20.0, 5.0, 0.25)

    assert result_more_sun < result_less_sun
