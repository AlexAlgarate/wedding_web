import reflex as rx


def send_whastapp_text(phone_number: str) -> rx.Component:
    """
    Create a text component with a link to send a WhatsApp message.

    Parameters:
    - phone_number (str): The phone number to which the WhatsApp message should be sent.

    Returns:
    - rx.Component: A Reflex component representing the text with a WhatsApp link.
    """

    return rx.link(
        rx.text(phone_number),
        href=f"https://wa.me/34{phone_number}",
        is_external=True,
        _hover={},
    )


def send_email_text(email: str) -> rx.Component:
    """
    Create a text component with a link to compose an email.

    Parameters:
    - email (str): The email address to which the email should be sent.

    Returns:
    - rx.Component: A Reflex component representing the text with an email link.
    """

    return rx.link(rx.text(email), href=f"mailto:{email}", is_external=True, _hover={})
