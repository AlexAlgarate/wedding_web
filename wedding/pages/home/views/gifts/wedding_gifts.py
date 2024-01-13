import reflex as rx

from wedding import utils
from wedding.components import icon_section, main_text, title_section
from wedding.routes import IconRoutes as icon


def wedding_gifts() -> rx.Component:
    return rx.vstack(
        title_section("Lista de regalos"),
        icon_section(icon=icon.ICON_GIFT.value),
        main_text(utils.gift),
        main_text(utils.account_number),
    )
