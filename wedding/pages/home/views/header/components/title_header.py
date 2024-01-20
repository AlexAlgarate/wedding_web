import reflex as rx

from wedding.styles import Font, FontWeight


def title_header() -> rx.Component:
    return rx.flex(
        _title("¡Nos"),
        _title("casamos!"),
        direction="column",
        align="center",
        font_weight=FontWeight.MEDIUM.value,
        font_style="normal",
        font_family=Font.TITLE.value,
        margin_top="-85px",
        line_height="normal",
    )


def _title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="2xl",
        font_family=Font.TITLE.value,
        font_weight=FontWeight.MEDIUM.value,
        font_style="normal",
    )
