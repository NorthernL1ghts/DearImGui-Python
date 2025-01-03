import sys
import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer
from enum import Enum
import time

g_ApplicationRunning = True

# Constant for Version
VERSION = "1.0.0"

# Key and Mouse Codes Enums
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

class MouseCodes(Enum):
    LEFT_BUTTON = glfw.MOUSE_BUTTON_LEFT
    RIGHT_BUTTON = glfw.MOUSE_BUTTON_RIGHT
    MIDDLE_BUTTON = glfw.MOUSE_BUTTON_MIDDLE

# Application Configuration Class
class AppConfiguration:
    def __init__(self, app_name, window_width, window_height, app_description):
        self.AppName = app_name
        self.Version = VERSION
        self.WindowWidth = window_width
        self.WindowHeight = window_height
        self.AppDescription = app_description

# Dear ImGui Integration Class
class DearImGuiRenderer:
    def __init__(self, window):
        self.Window = window
        self.RendererImplementation = None

    def SetupDearImGui(self):
        imgui.create_context()
        self.RendererImplementation = GlfwRenderer(self.Window)

    def RenderUI(self, config):
        self.RendererImplementation.process_inputs()
        imgui.new_frame()

        imgui.begin("Application Info")
        imgui.text(f"App Name: {config.AppName}")
        imgui.text(f"Version: {config.Version}")
        imgui.text(f"Description: {config.AppDescription}")
        imgui.end()

        imgui.render()
        self.RendererImplementation.render(imgui.get_draw_data())

    def Cleanup(self):
        self.RendererImplementation.shutdown()

# Event Handling Class
class EventHandler:
    def __init__(self, window):
        self.Window = window
        self.EventCallbacks = []

        glfw.set_window_size_callback(self.Window, self.OnWindowResize)
        glfw.set_window_close_callback(self.Window, self.OnWindowClose)
        glfw.set_key_callback(self.Window, self.OnKeyPress)
        glfw.set_mouse_button_callback(self.Window, self.OnMouseClick)
        glfw.set_scroll_callback(self.Window, self.OnMouseScroll)

    def RegisterCallback(self, callback):
        self.EventCallbacks.append(callback)

    def ProcessEvents(self):
        glfw.poll_events()  # Ensures events are processed
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
        key_name = key.name if key in KeyCodes else glfw.get_key_name(key.value, 0)
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

# Main Application Class
class Application:
    def __init__(self, config):
        self.Config = config
        self.LastUpdateTime = time.time()
        self.UpdateInterval = 1.0 / 60.0  # 60 FPS
        self.LastEventTime = time.time()

        if not self.InitializeGLFW():
            print("Failed to initialize GLFW")
            sys.exit(1)

        self.Window = self.CreateWindow(self.Config.WindowWidth, self.Config.WindowHeight, self.Config.AppName)
        if not self.Window:
            glfw.terminate()
            print("Failed to create window")
            sys.exit(1)

        glfw.make_context_current(self.Window)

        self.DearImGuiRenderer = DearImGuiRenderer(self.Window)
        self.DearImGuiRenderer.SetupDearImGui()
        self.EventHandler = EventHandler(self.Window)

        # Register default events
        self.RegisterDefaultEvents()

    def InitializeGLFW(self):
        return glfw.init()

    def CreateWindow(self, width, height, name):
        return glfw.create_window(width, height, name, None, None)

    def RegisterDefaultEvents(self):
        # Register custom events for application ticks and updates
        self.EventHandler.RegisterCallback(self.OnAppTick)
        self.EventHandler.RegisterCallback(self.OnAppUpdate)

    def OnAppTick(self):
        """Called every frame to handle logic at 60 FPS."""
        print("OnAppTick - Handle Application Logic")

    def OnAppUpdate(self):
        """Called every frame to handle updates at 60 FPS."""
        print("OnAppUpdate - Handle Updates")

    def Run(self):
        global g_ApplicationRunning
        while not glfw.window_should_close(self.Window) and g_ApplicationRunning:
            current_time = time.time()
            elapsed_time = current_time - self.LastUpdateTime

            # Only call events when enough time has passed (60 FPS)
            if elapsed_time >= self.UpdateInterval:
                self.EventHandler.ProcessEvents()

                # Update UI and application state
                self.DearImGuiRenderer.RenderUI(self.Config)

                gl.glClearColor(1.0, 0.0, 1.0, 1.0)
                gl.glClear(gl.GL_COLOR_BUFFER_BIT)
                glfw.swap_buffers(self.Window)

                # Update the last time to current
                self.LastUpdateTime = current_time

            # Ensure that sleep length is non-negative
            sleep_time = self.UpdateInterval - elapsed_time
            if sleep_time > 0:
                time.sleep(sleep_time)



# EntryPoint Class to Run the Application
class EntryPoint:
    @staticmethod
    def Main():
        config = AppConfiguration(
            app_name="DearImGui-Python",
            window_width=1280,
            window_height=720,
            app_description="An example application using Dear ImGui with GLFW and OpenGL."
        )
        app = Application(config)
        app.Run()

if __name__ == "__main__":
    EntryPoint.Main()
