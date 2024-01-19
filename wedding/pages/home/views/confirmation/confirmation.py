import reflex as rx

from wedding import icon, url, utils
from wedding.components import (
    button,
    divider,
    icon_section,
    spacer,
    text_paragraph,
    title_section,
)


def wedding_confirmation() -> rx.Component:
    return rx.vstack(
        *spacer(spacers=1),
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        title_section(title=utils.confirmation_title),
        divider(width="50%", section=False),
        text_paragraph(text=utils.confirmation_text),
        *spacer(spacers=1),
        button(button_name=utils.confirmation_button, url=url.CONFIRMATION_URL),
    )
