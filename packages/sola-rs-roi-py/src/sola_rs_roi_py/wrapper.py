# See https://www.maturin.rs/project_layout
from . import _sola_rs_roi_rust
from ._sola_rs_roi_rust import calculate_roi

__all__ = ["calculate_roi"]

__doc__ = _sola_rs_roi_rust.__doc__
