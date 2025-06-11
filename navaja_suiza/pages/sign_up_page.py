import reflex as rx
from navaja_suiza.components.sign_up_card import sign_up_card


def sign_up_page():
    return rx.el.div(
        sign_up_card(),
        class_name="flex flex-col items-center justify-center min-h-screen bg-gray-900 p-4 font-['Inter']",
    )