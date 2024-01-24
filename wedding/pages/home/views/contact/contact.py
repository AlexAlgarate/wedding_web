from typing import Dict

import reflex as rx

from wedding import utils
from wedding.components import card, icon_section, spacer, text_paragraph, title_section
from wedding.routes import IconRoutes as icon

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
        text_paragraph(utils.contact_text_whatsapp),
        whatsapp_button(utils.contact_bride),
        whatsapp_button(utils.contact_groom),
        text_paragraph(utils.contact_text_email),
        copy_emails(utils.contact_groom, utils.contact_bride),
        *spacer(spacers=4),
    )


class CopyEmails(rx.State):
    def copy_emails(self, text):
        return text


def copy_emails(*email_info: Dict[str, str]) -> rx.Component:
    email_text = [
        rx.button(
            mail_info["email"], on_click=rx.set_clipboard(f"{mail_info['email']}")
        )
        for mail_info in email_info
    ]
    return rx.flex(*email_text, direction="column", align="center", gap=8)
