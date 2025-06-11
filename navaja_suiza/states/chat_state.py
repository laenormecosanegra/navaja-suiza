import reflex as rx
from typing import TypedDict
import asyncio


class Message(TypedDict):
    text: str
    is_ai: bool


class ChatState(rx.State):
    messages: list[Message] = []
    typing: bool = False
    current_chat_input: str = ""

    @rx.event
    def clear_messages(self):
        self.typing = False
        self.messages = []

    @rx.event
    def send_message(self, form_data: dict):
        message = form_data["message"].strip()
        if not message or self.typing:
            return
        self.messages.append(
            {"text": message, "is_ai": False}
        )
        self.messages.append({"text": "", "is_ai": True})
        self.typing = True
        self.current_chat_input = ""
        return ChatState.generate_response

    @rx.event(background=True)
    async def generate_response(self):
        await asyncio.sleep(0.5)
        response_text = (
            "Esta es una respuesta simulada de la IA. "
        )
        if self.messages and len(self.messages) > 1:
            user_message = self.messages[-2]["text"].lower()
            if "hola" in user_message:
                response_text += "¡Hola!"
            elif (
                "cómo estás" in user_message
                or "como estas" in user_message
            ):
                response_text += (
                    "Soy una simulación, ¡pero estoy bien!"
                )
            else:
                response_text += f"Dijiste: '{self.messages[-2]['text']}'"
        streamed_text = ""
        for char in response_text:
            streamed_text += char
            async with self:
                if self.messages and self.typing:
                    self.messages[-1][
                        "text"
                    ] = streamed_text
            await asyncio.sleep(0.03)
        async with self:
            self.typing = False

    @rx.event
    def set_current_chat_input(self, value: str):
        self.current_chat_input = value