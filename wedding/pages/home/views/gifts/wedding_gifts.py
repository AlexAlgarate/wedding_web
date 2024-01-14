import reflex as rx

from wedding import utils
from wedding.components import icon_section, text_section, title_section
from wedding.routes import IconRoutes as icon


def wedding_gifts() -> rx.Component:
    return rx.vstack(
        title_section(title="Lista de regalos"),
        icon_section(icon=icon.ICON_GIFT.value),
        text_section(utils.gift),
        text_section(utils.account_number),
    )
