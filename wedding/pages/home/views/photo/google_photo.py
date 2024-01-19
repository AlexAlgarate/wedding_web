import reflex as rx

from wedding import icon, url, utils
from wedding.components import (
    button,
    divider,
    icon_section,
    text_paragraph,
    title_section,
)


def wedding_google_photos() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                title_section(title=utils.title_photo),
                icon_section(icon=icon.ICON_CAMERA.value),
                divider(width="50%", section=False),
                rx.flex(
                    text_paragraph(text=utils.photo_section),
                    text_paragraph(text=utils.photo_section_2),
                    direction="column",
                    align="center",
                ),
                button(button_name=utils.button_google_photo, url=url.GOOGLE_FOTOS_URL),
            ),
            width="100%",
        )
    )
