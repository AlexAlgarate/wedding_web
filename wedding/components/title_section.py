import reflex as rx

from wedding.styles.fonts import Font, FontWeight


def title_section(title: str) -> rx.Component:
    return rx.heading(
        title,
        size="2xl",
        font_weight=FontWeight.MEDIUM.value,
        font_family=Font.TITLE.value,
        text_align="center",
        width="100%",
    )
