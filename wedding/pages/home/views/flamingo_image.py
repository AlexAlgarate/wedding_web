import reflex as rx

from wedding.routes import FileRoutes as file


def flamingo_header() -> rx.Component:
    return rx.image(src=file.FLAMINGO.value, opacity="0.5", height="auto", width="auto")
