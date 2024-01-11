import reflex as rx
from wedding.components.main_text import main_text

from wedding.components.title_section import title_section
from wedding.routes import IconRoutes as icon
from wedding.components.icon_section import icon_section


def wedding_confirmation() -> rx.Component:
    return rx.vstack(
        title_section("Confirmación"),
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        main_text("Blablblá Juan es un calvo que se parece a Melitón"),
        rx.spacer(),
    )
