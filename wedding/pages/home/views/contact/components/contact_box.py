import reflex as rx

from wedding.components import card
from wedding.styles import Size

from .email_icon import send_email_icon
from .whatsapp_icon import send_whastapp_icon
from .whatsapp_text import send_email_text, send_whastapp_text


def contact_box(name: str, email: str, phone_number: str) -> rx.Component:
    """
    Create a contact box component with information for a person.

    Parameters:
    - name (str): The name of the person.
    - email (str): The email address of the person.
    - phone_number (str): The phone number of the person.

    Returns:
    - rx.Component: A Reflex component representing the contact box.
    """

    return card(
        rx.hstack(
            rx.span(name, font_weight="bold", margin_right="5%"),
            rx.vstack(
                rx.hstack(
                    send_whastapp_text(phone_number),
                    send_whastapp_icon(phone_number.replace(" ", "")),
                ),
                rx.hstack(send_email_text(email), send_email_icon(email)),
                padding=Size.MEDIUM_SMALL.value,
            ),
        ),
    )
