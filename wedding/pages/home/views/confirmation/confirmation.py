import reflex as rx

from wedding import url, utils
from wedding.components import (
    button,
    divider,
    icon_section,
    spacer,
    text_paragraph,
    title_section,
)
from wedding.routes import IconRoutes as icon


def wedding_confirmation(a: int, b: int) -> rx.Component:
    return rx.vstack(
        *spacer(spacers=1),
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        title_section(title=utils.confirmation_title),
        divider(width="50%"),
        text_paragraph(text=utils.confirmation_text),
        *spacer(spacers=1),
        button(button_name=utils.confirmation_button, url=url.CONFIRMATION_URL),
        rx.cond(
            operacion(a, b),
            rx.text("EL NUMERO ES MAYOR"),
            rx.text("EL NUMERO ES MENOR"),
        )
    )


def operacion(a: int, b: int) -> bool:
    return a > b
