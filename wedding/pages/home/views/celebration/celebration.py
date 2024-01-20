import reflex as rx

from wedding import icon, url, utils
from wedding.components import button, card, divider, icon_section, title_section
from wedding.routes import FileRoutes

from .components import image_celebration, text_celebration


def celebration() -> rx.Component:
    return card(
        title_section(title=utils.celebration_title),
        icon_section(icon=icon.ICON_CELEBRATION.value),
        divider(width="50%", section=False),
        image_celebration(image=FileRoutes.AGRIPINA.value, alt=utils.alt_celebration),
        text_celebration(),
        button(button_name=utils.celebration_button, url=url.AGRIPINA_MAPS_URL),
    )
