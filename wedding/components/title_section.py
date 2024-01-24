import reflex as rx

from wedding.styles import Color, Font, FontHeight, FontWeight


def title_section(title: str) -> rx.Component:
    return rx.heading(
        title,
        size="xl",
        font_weight=FontWeight.MEDIUM.value,
        text_align="center",
        width="100%",
        letter_spacing="0.0125rem",
        line_height=FontHeight.MEDIUM.value,
        font_family=Font.TITLE.value,
        color=Color.TITLE.value,
    )
