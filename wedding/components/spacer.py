import reflex as rx


def spacer(spacers: int) -> rx.Component:
    return [rx.spacer() for _ in range(spacers)]
