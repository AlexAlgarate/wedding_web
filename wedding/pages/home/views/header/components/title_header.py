import reflex as rx

from wedding.styles import Color, Font, FontWeight


def title_header() -> rx.Component:
    return rx.flex(
        _title("¡Nos"),
        _title("casamos!"),
        direction="column",
        align="center",
        margin_top="-85px",
    )


def _title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="2xl",
        font_family=Font.TITLE.value,
        font_weight=FontWeight.MEDIUM.value,
        font_style="normal",
        line_height="normal",
        color=Color.TITLE.value,
    )
