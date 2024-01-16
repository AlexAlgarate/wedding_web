import reflex as rx

from wedding import urls as url
from wedding import utils
from wedding.components import divider, icon_section, spacer, texts_lines, title_section
from wedding.pages.home.views.celebration.components.image_celebration import (
    image_celebration,
)
from wedding.routes import IconRoutes as icon
from wedding.styles import style


def celebration() -> rx.Component:
    return rx.vstack(
        title_section(title="Ceremonia y Celebración"),
        icon_section(icon=icon.ICON_CELEBRATION.value),
        divider(width="50%"),
        image_celebration(image=url.AGRIPINA_PHOTO_URL, alt=utils.alt_celebration),
        *texts_lines(
            (utils.wedding_place, style.bold_style_bus),
            utils.wedding_address,
            utils.wedding_schedule,
        ),
        *spacer(spacers=3),
        google_map_box(),
        *spacer(spacers=2),
    )


def google_map_box() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.html(
                url.maps,
                width="100%",
            ),
        ),
        align_items="center",
    )
