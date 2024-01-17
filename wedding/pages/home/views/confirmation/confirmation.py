import reflex as rx

from wedding import url, utils
from wedding.components import (
    button,
    divider,
    icon_section,
    text_paragraph,
    title_section,
)
from wedding.routes import IconRoutes as icon


def wedding_confirmation() -> rx.Component:
    return rx.vstack(
        title_section(title="Confirmación"),
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        divider(width="50%"),
        text_paragraph(text=utils.confirmation_text),
        rx.spacer(),
        button(button_name=utils.confirmation_button, url=url.CONFIRMATION_URL),
    )
