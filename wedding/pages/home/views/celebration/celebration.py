import reflex as rx

from wedding import urls, utils
from wedding.components import button, card, icon_section, title_section
from wedding.routes import FileRoutes
from wedding.routes import IconRoutes as icon

from .components import image_celebration, text_celebration


def celebration() -> rx.Component:
    return card(
        icon_section(icon=icon.ICON_CELEBRATION.value),
        title_section(title=utils.celebration_title),
        image_celebration(image=FileRoutes.AGRIPINA.value, alt=utils.alt_celebration),
        text_celebration(),
        button(button_name=utils.celebration_button, url=urls.AGRIPINA_MAPS_URL),
        id="celebration_section",
    )
