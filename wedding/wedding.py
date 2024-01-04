import reflex as rx

from wedding import utils
from wedding.pages.contact.contact import contact
from wedding.pages.home.home import index
from wedding.routes import Route
from wedding.styles import style

app = rx.App(stylesheets=style.STYLESHEETS, style=style.BASE_STYLE)

# app.add_page(index, title=utils.title_main, description=utils.description_main)
# app.add_page(route=Route.CONTACT.value, title=utils.title_contact, description=utils.description_contact)

app.compile()
