import reflex as rx
from wedding.components.icon_section import icon_section

from wedding.components.images import image_web
from wedding.components.title_section import title_section
from wedding.pages.home.views.celebration.components.image_celebration import image_celebration
from wedding.routes import IconRoutes as icon


def celebration() -> rx.Component:
    return rx.vstack(
        title_section("Ceremonia y Celebración"),
        icon_section(icon=icon.ICON_CELEBRATION.value),
        image_celebration(),
    )
