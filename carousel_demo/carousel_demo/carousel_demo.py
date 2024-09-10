"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rx_carousel.carousel import carousel
from rxconfig import config

import reflex as rx

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Test your custom component by editing ", rx.code(filename)),
            carousel(
                rx.button("Button 1", color="primary"),
                rx.button("Button 2", color="secondary"),
                rx.button("Button 3", color="tertiary"),
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
