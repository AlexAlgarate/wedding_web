from typing import Dict

import reflex as rx

from wedding import utils
from wedding.routes import IconRoutes as icon
from wedding.styles import style


def create_whatsapp_button(*contacts: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component to display WhatsApp buttons for multiple contacts.

    Args:
        contacts (Dict[str, str]): Dictionary containing contact information.

    Returns:
        rx.Component: Reflex component displaying WhatsApp buttons.
    """

    whatsapp_buttons = [create_single_whatsapp(contact=contact) for contact in contacts]
    return rx.flex(*whatsapp_buttons, direction="column", align="center", gap="8px")


def create_single_whatsapp(contact: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component for a single WhatsApp button.

    Args:
        contact (Dict[str, str]): Dictionary containing contact information.

    Returns:
        rx.Component: Reflex component for a single WhatsApp button.
    """
    whastapp_text = f"Abrir Whatsapp con {contact.get('name')}"
    whastapp_link = f"https://wa.me/34{contact.get('phone_number').replace(' ', '')}"

    return rx.link(
        rx.button(
            rx.flex(
                rx.image(src=icon.ICON_WHATSAPP.value, alt=utils.alt_whatsapp),
                rx.text(
                    whastapp_text,
                    style=style.TEXT_WHATSAPP_STYLE,
                ),
                style=style.WHATSAPP_COMP_STYLE,
            ),
            style=style.BUTTON_WHATSAPP_STYLE,
        ),
        href=whastapp_link,
        is_external=True,
    )
