from typing import Dict, Optional, Tuple, Union
import reflex as rx


def bus_texts(*texts: Union[str, tuple]) -> rx.Component:
    def process_item(item):
        if isinstance(item, tuple):
            text, style = item
            return rx.text(text, style=style)
        else:
            return rx.text(item)

    return [process_item(item) for item in texts]
