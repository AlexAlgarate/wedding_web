import reflex as rx


from wedding.styles import style


def create_countdown_vstack(element: str, text_date: str) -> rx.Component:
    """
    Creates a vstack component for countdown numbers and corresponding text date.

    Args:
        element (str): The countdown element.
        text_date (str): The text date.

    Returns:
        rx.Component: The vstack component.
    """

    return rx.vstack(
        _countdown_numbers(element=element),
        _element_date(text_date=text_date),
    )


def _countdown_numbers(element: str) -> rx.Component:
    """
    Creates a text component for displaying countdown numbers.

    Args:
        element (str): The countdown element.

    Returns:
        rx.Component: The countdown numbers component.
    """

    return rx.text(
        id=element,
        style=style.COUNTDOWN_NUMBERS_STYLE,
    )


def _element_date(text_date: str) -> rx.Component:
    """
    Creates a text component for displaying countdown text date.

    Args:
        text_date (str): The text date.

    Returns:
        rx.Component: The element date component.
    """

    return rx.text(
        text_date,
        style=style.COUNTDOWN_TEXT_STYLE,
    )
