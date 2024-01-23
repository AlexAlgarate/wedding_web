from typing import Dict, Optional

import reflex as rx

from wedding.styles import Size


def card(
    *components: rx.Component, style: Optional[Dict[str, str]] = None
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
        gap="8px",
        padding="16px 12px",
        margin_x=Size.MEDIUM.value,
        justify_content="center",
        border_radius="12px",
        box_shadow="0px 2px 4px 0px rgba(0, 0, 0, 0.25)",
    )
