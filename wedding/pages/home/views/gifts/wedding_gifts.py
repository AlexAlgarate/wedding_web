import reflex as rx

from wedding import utils
from wedding.components import card, divider, icon_section, text_section, title_section
from wedding.routes import IconRoutes as icon


def wedding_gifts() -> rx.Component:
    """
    Create a component for displaying wedding gift information.

    Returns:
    - rx.Component: A Reflex component representing the wedding gifts section.

    This component includes an icon, title, and paragraphs with information about wedding gifts.
    """

    return card(
        icon_section(icon=icon.ICON_GIFT.value),
        title_section(title="Lista de regalos"),
        divider(width="50%", section=False),
        text_section(utils.gift_text),
        text_section(utils.account_number_text),
        id="gift_section",
    )
