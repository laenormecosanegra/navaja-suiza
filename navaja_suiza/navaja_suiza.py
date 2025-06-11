import reflex as rx
from navaja_suiza.states.main_state import MainState
from navaja_suiza.states.chat_state import ChatState
from navaja_suiza.states.auth_state import AuthState
from navaja_suiza.pages.protected_page import protected_page
from navaja_suiza.pages.sign_in_page import sign_in_page
from navaja_suiza.pages.sign_up_page import sign_up_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    protected_page,
    route="/",
    on_load=AuthState.check_session,
)
app.add_page(sign_in_page, route="/sign-in")
app.add_page(sign_up_page, route="/sign-up")
