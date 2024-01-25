from typing import Dict

import reflex as rx

from wedding import utils
from wedding.components import card, icon_section, spacer, text_section, title_section
from wedding.routes import IconRoutes as icon
from wedding.styles import Size

from .components import whatsapp_button

contact_bride = dict(
    name="Pepe",
    email="Pepitode@lospalotes.com",
)


def contact() -> rx.Component:
    """
    Create a contact information section component.

    Returns:
    - rx.Component: A Reflex component representing the contact information section.
    """

    return card(
        icon_section(icon=icon.ICON_CELEBRATION.value),
        title_section(title=utils.contact_title),
        text_section(utils.contact_text_whatsapp),
        whatsapp_button(utils.contact_bride),
        whatsapp_button(utils.contact_groom),
        text_section(utils.contact_text_email),
        emails(utils.contact_bride, utils.contact_groom),
        *spacer(spacers=4),
        # rx.button("open countdown", on_click=rx.redirect("/#countdown_section")),
        id="contact_section",
    )


def emails(*email_info: Dict[str, str]) -> rx.Component:
    email_text = [
        rx.text(
            mail_info["email"],
            font_size=[
                "1.2em",
                Size.LARGE.value,
                Size.LARGE.value,
                Size.LARGE.value,
                Size.LARGE.value,
            ],
        )
        for mail_info in email_info
    ]
    return rx.flex(*email_text, direction="column", align="center", gap="8px")
