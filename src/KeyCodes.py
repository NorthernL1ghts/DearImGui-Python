import glfw
from enum import Enum

class KeyCodes(Enum):
    SPACE = glfw.KEY_SPACE
    ENTER = glfw.KEY_ENTER
    ESCAPE = glfw.KEY_ESCAPE
    LEFT_ALT = glfw.KEY_LEFT_ALT
    RIGHT_ALT = glfw.KEY_RIGHT_ALT
    LEFT_SHIFT = glfw.KEY_LEFT_SHIFT
    RIGHT_SHIFT = glfw.KEY_RIGHT_SHIFT
    LEFT_CONTROL = glfw.KEY_LEFT_CONTROL
    RIGHT_CONTROL = glfw.KEY_RIGHT_CONTROL
    A = glfw.KEY_A
    B = glfw.KEY_B
    C = glfw.KEY_C
    D = glfw.KEY_D
    E = glfw.KEY_E
    F = glfw.KEY_F
    G = glfw.KEY_G
    H = glfw.KEY_H
    I = glfw.KEY_I
    J = glfw.KEY_J
    K = glfw.KEY_K
    L = glfw.KEY_L
    M = glfw.KEY_M
    N = glfw.KEY_N
    O = glfw.KEY_O
    P = glfw.KEY_P
    Q = glfw.KEY_Q
    R = glfw.KEY_R
    S = glfw.KEY_S
    T = glfw.KEY_T
    U = glfw.KEY_U
    V = glfw.KEY_V
    W = glfw.KEY_W
    X = glfw.KEY_X
    Y = glfw.KEY_Y
    Z = glfw.KEY_Z
    UP = glfw.KEY_UP
    DOWN = glfw.KEY_DOWN
    LEFT = glfw.KEY_LEFT
    RIGHT = glfw.KEY_RIGHT

    def __str__(self):
        return f"{self.name} (Code: {self.value})"
