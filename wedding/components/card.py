from typing import Optional

import reflex as rx

from wedding.styles import style


def card(
    *components: rx.Component,
    id: Optional[str] = None,
) -> rx.Component:
    """
    Create a card component with specified components and style.

    Parameters:
    - components (rx.Component): Components to be included in the card.
    - style (Optional[Dict[str, str]]): Optional styling properties for the card.

    Returns:
    - rx.Component: A Reflex component representing the card.
    """

    return rx.flex(
        *components,
        direction="column",
        align="center",
        style=style.CARD_STYLE,
        id=id,
    )
