import reflex as rx

from wedding.components import icon_section, main_text, title_section
from wedding.routes import IconRoutes as icon


def wedding_confirmation() -> rx.Component:
    return rx.vstack(
        title_section("Confirmación"),
        icon_section(icon=icon.ICON_CONFIRMATION.value),
        main_text("Blablblá Juan es un calvo que se parece a Melitón"),
        rx.spacer(),
    )
