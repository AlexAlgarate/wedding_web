import reflex as rx

from wedding.styles import Size
from wedding.styles.fonts import Font, FontWeight


def title_section(text: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                text,
                font_size=[
                    Size.BIG.value,
                    Size.MEDIUM_BIGGER.value,
                    Size.VERY_BIG.value,
                    Size.VERY_BIG.value,
                    Size.VERY_BIG.value,
                ],
                font_weight=FontWeight.MEDIUM.value,
                font_family=Font.TITLE.value,
                width="100%",
            ),
        ),
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
    )
