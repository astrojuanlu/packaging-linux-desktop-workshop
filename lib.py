PANEL_EFFICIENCY = 0.20
IRRADIANCE = 1000.0
INSTALLATION_COST_PER_M2 = 300.0


def calculate_roi(
    roof_area_m2: float, sun_hours_per_day: float, electricity_price_eur_per_kwh: float
) -> float:
    power_kw = IRRADIANCE * roof_area_m2 * PANEL_EFFICIENCY / 1000.0
    energy_per_year_kwh = power_kw * sun_hours_per_day * 365.0
    annual_savings_eur = energy_per_year_kwh * electricity_price_eur_per_kwh
    installation_cost_eur = roof_area_m2 * INSTALLATION_COST_PER_M2
    return installation_cost_eur / annual_savings_eur


if __name__ == "__main__":
    # test
    assert abs(calculate_roi(20.0, 5.0, 0.25) - 3.287671232876712) < 0.0001
