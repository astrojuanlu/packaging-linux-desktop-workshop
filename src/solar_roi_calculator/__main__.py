import toga
from toga.widgets.base import Widget
from travertino.constants import COLUMN, LEFT, ROW
from sola_rs_roi_py.wrapper import calculate_roi


def build(app: toga.App) -> Widget:
    # Create boxes for layout
    roof_area_box = toga.Box()
    sun_hours_box = toga.Box()
    electricity_price_box = toga.Box()
    result_box = toga.Box()
    box = toga.Box()

    # Create input fields with default values from test_calculate_roi_basic
    roof_area_input = toga.TextInput(value="20.0")
    sun_hours_input = toga.TextInput(value="5.0")
    electricity_price_input = toga.TextInput(value="0.25")

    # Create labels
    roof_area_label = toga.Label("Roof area (m²)", text_align=LEFT)
    sun_hours_label = toga.Label("Sun hours/day", text_align=LEFT)
    electricity_price_label = toga.Label("Price (€/kWh)", text_align=LEFT)
    result_label = toga.Label("ROI: ---", text_align=LEFT)

    def calculate(widget):
        try:
            roof_area = float(roof_area_input.value)
            sun_hours = float(sun_hours_input.value)
            electricity_price = float(electricity_price_input.value)

            roi_years = calculate_roi(roof_area, sun_hours, electricity_price)
            result_label.text = f"ROI: {roi_years:.2f} years"
        except ValueError:
            result_label.text = "ROI: Invalid input"
        except Exception as e:
            result_label.text = f"ROI: Error - {str(e)}"

    button = toga.Button("Calculate", on_press=calculate)

    # Add widgets to boxes
    roof_area_box.add(roof_area_input)
    roof_area_box.add(roof_area_label)

    sun_hours_box.add(sun_hours_input)
    sun_hours_box.add(sun_hours_label)

    electricity_price_box.add(electricity_price_input)
    electricity_price_box.add(electricity_price_label)

    result_box.add(result_label)

    box.add(roof_area_box)
    box.add(sun_hours_box)
    box.add(electricity_price_box)
    box.add(result_box)
    box.add(button)

    # Apply styles
    box.style.update(direction=COLUMN, margin=10, gap=10)
    roof_area_box.style.update(direction=ROW, gap=10)
    sun_hours_box.style.update(direction=ROW, gap=10)
    electricity_price_box.style.update(direction=ROW, gap=10)
    result_box.style.update(direction=ROW, gap=10)

    roof_area_input.style.update(flex=1)
    sun_hours_input.style.update(flex=1)
    electricity_price_input.style.update(flex=1)
    roof_area_label.style.update(width=150)
    sun_hours_label.style.update(width=150)
    electricity_price_label.style.update(width=150)
    result_label.style.update(flex=1)

    button.style.update(margin_top=5)

    return box


def main():
    return toga.App(
        "Solar ROI Calculator",
        "org.beeware.toga.examples.solar",
        startup=build,  # ty:ignore[invalid-argument-type]
    )


def run():
    main().main_loop()


if __name__ == "__main__":
    run()
