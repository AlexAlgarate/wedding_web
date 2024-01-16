import reflex as rx

from wedding import urls as url
from wedding import utils
from wedding.components import (
    button,
    divider,
    icon_section,
    spacer,
    texts_lines,
    title_section,
)
from wedding.routes import IconRoutes as icon
from wedding.styles import style

from .components import image_celebration


def celebration() -> rx.Component:
    return rx.vstack(
        title_section(title=utils.header_celebration),
        icon_section(icon=icon.ICON_CELEBRATION.value),
        divider(width="50%"),
        image_celebration(image=url.AGRIPINA_PHOTO_URL, alt=utils.alt_celebration),
        *texts_lines(
            (utils.wedding_place, style.bold_style_bus),
            utils.wedding_address_street,
            utils.wedding_address_province,
        ),
        *spacer(spacers=2),
        button(button_name=utils.button_celebration, url=url.AGRIPINA_MAPS_URL),
        *spacer(spacers=2),
    )
