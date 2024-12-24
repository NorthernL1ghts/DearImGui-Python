import sys
import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer
from enum import Enum

g_ApplicationRunning = True

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
    TAB = glfw.KEY_TAB
    CAPS_LOCK = glfw.KEY_CAPS_LOCK
    NUM_LOCK = glfw.KEY_NUM_LOCK
    SCROLL_LOCK = glfw.KEY_SCROLL_LOCK
    PRINT_SCREEN = glfw.KEY_PRINT_SCREEN
    PAUSE = glfw.KEY_PAUSE
    INSERT = glfw.KEY_INSERT
    DELETE = glfw.KEY_DELETE
    HOME = glfw.KEY_HOME
    END = glfw.KEY_END
    PAGE_UP = glfw.KEY_PAGE_UP
    PAGE_DOWN = glfw.KEY_PAGE_DOWN
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
    UP = glfw.KEY_UP
    DOWN = glfw.KEY_DOWN
    LEFT = glfw.KEY_LEFT
    RIGHT = glfw.KEY_RIGHT

class MouseCodes(Enum):
    LEFT = glfw.MOUSE_BUTTON_LEFT
    RIGHT = glfw.MOUSE_BUTTON_RIGHT
    MIDDLE = glfw.MOUSE_BUTTON_MIDDLE

class ApplicationSpecification:
    def __init__(self, name, version, width, height, description):
        self.m_Name = name
        self.m_Version = version
        self.m_Width = width
        self.m_Height = height
        self.m_Description = description

class DearImGuiLayer:
    def __init__(self, window):
        self.m_Window = window
        self.m_Impl = None

    def InitializeImGui(self):
        imgui.create_context()
        self.m_Impl = GlfwRenderer(self.m_Window)

    def Render(self, spec):
        self.m_Impl.process_inputs()
        imgui.new_frame()

        imgui.begin("Demo Window")
        imgui.text("Hello, World!")
        imgui.text(f"App Name: {spec.m_Name}")
        imgui.text(f"Version: {spec.m_Version}")
        imgui.text(f"Description: {spec.m_Description}")
        imgui.end()

        imgui.render()
        self.m_Impl.render(imgui.get_draw_data())

    def Shutdown(self):
        self.m_Impl.shutdown()

class Event:
    def __init__(self, window):
        self.m_Window = window
        self.m_EventHandlers = []

        glfw.set_window_size_callback(self.m_Window, self.OnWindowResize)
        glfw.set_window_close_callback(self.m_Window, self.OnWindowClose)
        glfw.set_key_callback(self.m_Window, self.OnKeyEvent)
        glfw.set_mouse_button_callback(self.m_Window, self.OnMouseClick)
        glfw.set_scroll_callback(self.m_Window, self.OnScroll)

    def RegisterEventHandler(self, handler):
        self.m_EventHandlers.append(handler)

    def HandleEvents(self):
        for handler in self.m_EventHandlers:
            handler()

    def OnWindowResize(self, window, width, height):
        print(f"Window resized: {width}x{height}")
        gl.glViewport(0, 0, width, height)

    def OnWindowClose(self, window):
        self.HandleWindowCloseEvent()

    def HandleWindowCloseEvent(self):
        global g_ApplicationRunning
        print("OnWindowCloseEvent")
        g_ApplicationRunning = False

    def OnKeyEvent(self, window, key, scancode, action, mods):
        try:
            key_code = KeyCodes(key)
            self.HandleKeyEvent(key_code, action, mods)
        except ValueError:
            print(f"Unhandled key code: {key}")

    def HandleKeyEvent(self, key, action, mods):
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
        if button == MouseCodes.LEFT:
            print("Left mouse button clicked!")

    def OnScroll(self, window, xoffset, yoffset):
        self.HandleScrollEvent(xoffset, yoffset)

    def HandleScrollEvent(self, xoffset, yoffset):
        print(f"Scrolled: xoffset={xoffset}, yoffset={yoffset}")
        if yoffset > 0:
            print("Scrolled up!")
        else:
            print("Scrolled down!")

class Application:
    def __init__(self, spec):
        self.m_Spec = spec

        if not self.InitializeGLFW():
            print("Failed to initialize GLFW")
            sys.exit(1)

        self.m_Window = self.CreateWindow(self.m_Spec.m_Width, self.m_Spec.m_Height, self.m_Spec.m_Name)
        if not self.m_Window:
            glfw.terminate()
            print("Failed to create window")
            sys.exit(1)

        glfw.make_context_current(self.m_Window)

        self.m_ImGuiLayer = DearImGuiLayer(self.m_Window)
        self.m_ImGuiLayer.InitializeImGui()
        self.m_Event = Event(self.m_Window)

    def InitializeGLFW(self):
        return glfw.init()

    def CreateWindow(self, width, height, name):
        return glfw.create_window(width, height, name, None, None)

    def Run(self):
        global g_ApplicationRunning
        while not glfw.window_should_close(self.m_Window) and g_ApplicationRunning:
            glfw.poll_events()
            self.m_ImGuiLayer.Render(self.m_Spec)

            gl.glClearColor(1.0, 0.0, 1.0, 1.0)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.m_Window)

        self.m_ImGuiLayer.Shutdown()
        glfw.terminate()

class EntryPoint:
    @staticmethod
    def Main():
        spec = ApplicationSpecification(
            name="DearImGui-Python",
            version="1.0.0",
            width=1280,
            height=720,
            description="An example application using Dear ImGui with GLFW and OpenGL."
        )
        app = Application(spec)
        app.Run()

if __name__ == "__main__":
    EntryPoint.Main()
