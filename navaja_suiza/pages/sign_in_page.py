import reflex as rx
from navaja_suiza.components.sign_in_card import sign_in_card


def sign_in_page():
    return rx.el.div(
        sign_in_card(),
        class_name="flex flex-col items-center justify-center min-h-screen bg-gray-900 p-4 font-['Inter']",
    )