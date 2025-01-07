import glfw
from KeyCodes import KeyCodes
from MouseCodes import MouseCodes
from OpenGL import GL as gl  # Importing OpenGL module for OpenGL functions


class Event:
    def __init__(self, window):
        self.Window = window
        self.EventCallbacks = []
        self.SetCallbacks()

    def SetCallbacks(self):
        self.Window.SetSizeCallback(self.OnWindowResize)
        self.Window.SetCloseCallback(self.OnWindowClose)
        self.Window.SetKeyCallback(self.OnKeyPress)
        self.Window.SetMouseButtonCallback(self.OnMouseClick)
        self.Window.SetScrollCallback(self.OnMouseScroll)

    def RegisterCallback(self, callback):
        self.EventCallbacks.append(callback)

    def ProcessEvents(self):
        self.Window.PollEvents()
        for callback in self.EventCallbacks:
            callback()

    def OnWindowResize(self, window, width, height):
        print(f"Window resized: {width}x{height}")
        gl.glViewport(0, 0, width, height)

    def OnWindowClose(self, window):
        print("Window is closing")
        glfw.set_window_should_close(window, glfw.TRUE)

    def OnKeyPress(self, window, key, scancode, action, mods):
        try:
            key_code = KeyCodes(key)
            self.HandleKeyPressEvent(key_code, action, mods)
        except ValueError:
            print(f"Unhandled key code: {key}")

    def HandleKeyPressEvent(self, key, action, mods):
        key_name = key.name if key in KeyCodes else glfw.get_key_name(key, 0)
        action_name = self.GetActionName(action)
        print(f"Key event: {key_name}, action: {action_name}, mods: {mods}")

    def GetActionName(self, action):
        action_names = {
            glfw.PRESS: "Press",
            glfw.RELEASE: "Release",
            glfw.REPEAT: "Repeat"
        }
        return action_names.get(action, "Unknown")

    def OnMouseClick(self, window, button, action, mods):
        if action == glfw.PRESS:
            self.HandleMouseClickEvent(MouseCodes(button))

    def HandleMouseClickEvent(self, button):
        button_name = button.name if button in MouseCodes else "Unknown"
        print(f"Mouse button clicked: {button_name}")

    def OnMouseScroll(self, window, xoffset, yoffset):
        self.HandleMouseScrollEvent(xoffset, yoffset)

    def HandleMouseScrollEvent(self, xoffset, yoffset):
        print(f"Scrolled: xoffset={xoffset}, yoffset={yoffset}")