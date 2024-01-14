import reflex as rx

from wedding import urls, utils
from wedding.components import button, icon_section, text_section, title_section
from wedding.routes import IconRoutes as icon


def wedding_confirmation() -> rx.Component:
    return rx.vstack(
        title_section(title="Confirmación"),
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        text_section(text=utils.main_text_confirmation),
        rx.spacer(),
        button(button_name=utils.button_confirmation, url=urls.CONFIRMATION_URL),
    )
