import reflex as rx

from wedding.styles import style


def main_button(button_name: str, url: str, **args) -> rx.Component:
    """
    Creates a main button component with a link.

    Args:
        button_name (str): The text to display on the button.
        url (str): The URL the button links to.
        **args: Additional arguments for the button.

    Returns:
        rx.Component: The main button component.
    """

    return rx.link(
        rx.button(button_name, style=style.MAIN_BUTTON_STYLE),
        href=url,
        is_external=True,
    )
