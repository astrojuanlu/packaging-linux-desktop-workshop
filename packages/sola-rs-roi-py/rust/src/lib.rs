use pyo3::prelude::*;

pub const PANEL_EFFICIENCY: f64 = 0.20;
pub const IRRADIANCE: f64 = 1000.0;
pub const INSTALLATION_COST_PER_M2: f64 = 300.0;

pub fn calculate_roi(
    roof_area_m2: f64,
    sun_hours_per_day: f64,
    electricity_price_eur_per_kwh: f64,
) -> f64 {
    let power_kw = IRRADIANCE * roof_area_m2 * PANEL_EFFICIENCY / 1000.0;
    let energy_per_year_kwh = power_kw * sun_hours_per_day * 365.0;
    let annual_savings_eur = energy_per_year_kwh * electricity_price_eur_per_kwh;
    let installation_cost_eur = roof_area_m2 * INSTALLATION_COST_PER_M2;

    installation_cost_eur / annual_savings_eur
}

/// A Python module implemented in Rust.
#[pymodule]
#[pyo3(name = "_sola_rs_roi_rust")]
mod sola_rs_roi_py {
    use pyo3::prelude::*;

    /// Calculates solar ROI
    #[pyfunction]
    fn calculate_roi(
        roof_area_m2: f64,
        sun_hours_per_day: f64,
        electricity_price_eur_per_kwh: f64,
    ) -> PyResult<f64> {
        Ok(super::calculate_roi(
            roof_area_m2,
            sun_hours_per_day,
            electricity_price_eur_per_kwh,
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_roi() {
        let result = calculate_roi(20.0, 5.0, 0.25);
        assert!((result - 3.287671232876712).abs() < 0.0001);
    }
}
