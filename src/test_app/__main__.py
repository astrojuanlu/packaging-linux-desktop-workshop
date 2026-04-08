import toga
from toga.app import App
from toga.widgets.base import Widget

from test_lib import hello


def build(app: App) -> Widget:
    box = toga.Box()

    button = toga.Button("Hello world!", on_press=lambda w: print(hello() + "!!!"))
    button.style.margin = 50
    button.style.flex = 1
    box.add(button)

    return box


def create_app():
    return toga.App(
        "Test App",
        "org.canonical.test-toga-app",
        startup=build,
    )


def main():
    app = create_app()
    app.main_loop()


if __name__ == "__main__":
    main()
