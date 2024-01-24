import reflex as rx

from wedding import urls, utils
from wedding.components import button, card, icon_section, text_paragraph, title_section
from wedding.routes import IconRoutes as icon


def wedding_confirmation() -> rx.Component:
    return card(
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        title_section(title=utils.confirmation_title),
        text_paragraph(text=utils.confirmation_text),
        button(button_name=utils.confirmation_button, url=urls.CONFIRMATION_URL),
    )
