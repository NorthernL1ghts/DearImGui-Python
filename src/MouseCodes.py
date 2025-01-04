import glfw
from enum import Enum

class MouseCodes(Enum):
    BUTTON_LEFT = glfw.MOUSE_BUTTON_LEFT
    BUTTON_RIGHT = glfw.MOUSE_BUTTON_RIGHT
    BUTTON_MIDDLE = glfw.MOUSE_BUTTON_MIDDLE
    BUTTON_4 = glfw.MOUSE_BUTTON_4
    BUTTON_5 = glfw.MOUSE_BUTTON_5
    BUTTON_6 = glfw.MOUSE_BUTTON_6
    BUTTON_7 = glfw.MOUSE_BUTTON_7
    BUTTON_8 = glfw.MOUSE_BUTTON_8

    def __str__(self):
        return f"{self.name} (Code: {self.value})"
