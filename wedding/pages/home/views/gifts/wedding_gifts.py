import reflex as rx

from wedding import utils
from wedding.components import icon_section, text_paragraph, title_section
from wedding.routes import IconRoutes as icon


def wedding_gifts() -> rx.Component:
    return rx.vstack(
        title_section(title="Lista de regalos"),
        icon_section(icon=icon.ICON_GIFT.value),
        text_paragraph(utils.gift),
        text_paragraph(utils.account_number),
    )
