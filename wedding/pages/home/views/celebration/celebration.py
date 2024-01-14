import reflex as rx

from wedding.components import icon_section, title_section
from wedding.pages.home.views.celebration.components.image_celebration import (
    image_celebration,
)
from wedding.routes import IconRoutes as icon


def celebration() -> rx.Component:
    return rx.vstack(
        title_section(title="Ceremonia y Celebración"),
        icon_section(icon=icon.ICON_CELEBRATION.value),
        image_celebration(),
    )
