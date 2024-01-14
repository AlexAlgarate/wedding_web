import reflex as rx


def bus_texts(*texts) -> rx.Component:
    return [rx.text(bus_text) for bus_text in texts]
