import reflex as rx

from wedding import utils
from wedding.components import (
    card,
    divider,
    icon_section,
    spacer,
    text_paragraph,
    title_section,
)
from wedding.routes import IconRoutes as icon

from .components import contact_box


def contact() -> rx.Component:
    """
    Create a contact information section component.

    Returns:
    - rx.Component: A Reflex component representing the contact information section.
    """

    return card(
        icon_section(icon=icon.ICON_CELEBRATION.value),
        title_section(title=utils.contact_title),
        divider(width="50%", section=False),
        text_paragraph(utils.contact_text_two),
        contact_box(**utils.contact_bride),
        contact_box(**utils.contact_groom),
        *spacer(spacers=4),
    )
