from typing import Tuple, Union

import reflex as rx


def texts_lines(*texts: Union[str, Tuple[str, str]]) -> rx.Component:
    def process_item(item):
        if isinstance(item, tuple):
            text, style = item
            return rx.text(text, style=style)
        else:
            return rx.text(item)

    return [process_item(item) for item in texts]
