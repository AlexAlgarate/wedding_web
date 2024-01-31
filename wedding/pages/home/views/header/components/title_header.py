import reflex as rx

from wedding.styles import style


def title_header() -> rx.Component:
    return rx.flex(
        _title("¡Nos"),
        _title("casamos!"),
        direction="column",
        align="center",
        margin_top="-85px",
    )


def _title(text: str) -> rx.Component:
    return rx.heading(text, size="2xl", style=style.TEXT_HEADER_STYLE)
