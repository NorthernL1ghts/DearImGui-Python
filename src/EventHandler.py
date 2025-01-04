import glfw
from KeyCodes import KeyCodes
from MouseCodes import MouseCodes

class EventHandler:
    def __init__(self, window):
        self.Window = window
        self.EventCallbacks = []
        self.SetCallbacks()

    def SetCallbacks(self):
        glfw.set_window_size_callback(self.Window, self.OnWindowResize)
        glfw.set_window_close_callback(self.Window, self.OnWindowClose)
        glfw.set_key_callback(self.Window, self.OnKeyPress)
        glfw.set_mouse_button_callback(self.Window, self.OnMouseClick)
        glfw.set_scroll_callback(self.Window, self.OnMouseScroll)

    def RegisterCallback(self, callback):
        self.EventCallbacks.append(callback)

    def ProcessEvents(self):
        glfw.poll_events()
        for callback in self.EventCallbacks:
            callback()

    def OnWindowResize(self, window, width, height):
        print(f"Window resized: {width}x{height}")
        gl.glViewport(0, 0, width, height)

    def OnWindowClose(self, window):
        global g_ApplicationRunning
        print("Window is closing")
        g_ApplicationRunning = False

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
        if key == KeyCodes.SPACE and action_name == "Press":
            print("Space key was pressed!")
        elif key == KeyCodes.ENTER and action_name == "Press":
            print("Enter key was pressed!")

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
        if button == MouseCodes.LEFT_BUTTON:
            print("Left mouse button clicked!")

    def OnMouseScroll(self, window, xoffset, yoffset):
        self.HandleMouseScrollEvent(xoffset, yoffset)

    def HandleMouseScrollEvent(self, xoffset, yoffset):
        print(f"Scrolled: xoffset={xoffset}, yoffset={yoffset}")
        if yoffset > 0:
            print("Scrolled up!")
        else:
            print("Scrolled down!")
