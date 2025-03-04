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
    F1 = glfw.KEY_F1
    F2 = glfw.KEY_F2
    F3 = glfw.KEY_F3
    F4 = glfw.KEY_F4
    F5 = glfw.KEY_F5
    F6 = glfw.KEY_F6
    F7 = glfw.KEY_F7
    F8 = glfw.KEY_F8
    F9 = glfw.KEY_F9
    F10 = glfw.KEY_F10
    F11 = glfw.KEY_F11
    F12 = glfw.KEY_F12
    NUM_0 = glfw.KEY_0
    NUM_1 = glfw.KEY_1
    NUM_2 = glfw.KEY_2
    NUM_3 = glfw.KEY_3
    NUM_4 = glfw.KEY_4
    NUM_5 = glfw.KEY_5
    NUM_6 = glfw.KEY_6
    NUM_7 = glfw.KEY_7
    NUM_8 = glfw.KEY_8
    NUM_9 = glfw.KEY_9
    NUM_PAD_0 = glfw.KEY_KP_0
    NUM_PAD_1 = glfw.KEY_KP_1
    NUM_PAD_2 = glfw.KEY_KP_2
    NUM_PAD_3 = glfw.KEY_KP_3
    NUM_PAD_4 = glfw.KEY_KP_4
    NUM_PAD_5 = glfw.KEY_KP_5
    NUM_PAD_6 = glfw.KEY_KP_6
    NUM_PAD_7 = glfw.KEY_KP_7
    NUM_PAD_8 = glfw.KEY_KP_8
    NUM_PAD_9 = glfw.KEY_KP_9
    NUM_PAD_ADD = glfw.KEY_KP_ADD
    NUM_PAD_SUBTRACT = glfw.KEY_KP_SUBTRACT
    NUM_PAD_MULTIPLY = glfw.KEY_KP_MULTIPLY
    NUM_PAD_DIVIDE = glfw.KEY_KP_DIVIDE
    NUM_PAD_ENTER = glfw.KEY_KP_ENTER  # Added NumPad Enter
    NUM_LOCK = glfw.KEY_NUM_LOCK  # Added Num Lock
    TAB = glfw.KEY_TAB
    CAPS_LOCK = glfw.KEY_CAPS_LOCK
    BACKSPACE = glfw.KEY_BACKSPACE
    DELETE = glfw.KEY_DELETE
    HOME = glfw.KEY_HOME
    END = glfw.KEY_END
    PAGE_UP = glfw.KEY_PAGE_UP
    PAGE_DOWN = glfw.KEY_PAGE_DOWN
    INSERT = glfw.KEY_INSERT
    PAUSE = glfw.KEY_PAUSE
    PRINT_SCREEN = glfw.KEY_PRINT_SCREEN
    LEFT_SUPER = glfw.KEY_LEFT_SUPER
    RIGHT_SUPER = glfw.KEY_RIGHT_SUPER

    def __str__(self):
        return f"{self.name} (Code: {self.value})"
