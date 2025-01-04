import glfw
import OpenGL.GL as gl

class Window:
    def __init__(self, config):
        self.Config = config
        self.WindowInstance = None
        self.Initialize()

    def Initialize(self):
        if not glfw.init():
            print("GLFW initialization failed")
            return

        self.WindowInstance = glfw.create_window(
            self.Config.WindowWidth,
            self.Config.WindowHeight,
            self.Config.Name,
            None,
            None
        )

        if not self.WindowInstance:
            glfw.terminate()
            print("Failed to create GLFW window!")
            return

        glfw.make_context_current(self.WindowInstance)
        gl.glClearColor(1.0, 0.0, 1.0, 1.0)  # Set default clear color

    def ShouldClose(self):
        return glfw.window_should_close(self.WindowInstance)

    def SwapBuffers(self):
        glfw.swap_buffers(self.WindowInstance)

    def PollEvents(self):
        glfw.poll_events()

    def SetSizeCallback(self, callback):
        glfw.set_window_size_callback(self.WindowInstance, callback)

    def SetCloseCallback(self, callback):
        glfw.set_window_close_callback(self.WindowInstance, callback)

    def SetKeyCallback(self, callback):
        glfw.set_key_callback(self.WindowInstance, callback)

    def SetMouseButtonCallback(self, callback):
        glfw.set_mouse_button_callback(self.WindowInstance, callback)

    def SetScrollCallback(self, callback):
        glfw.set_scroll_callback(self.WindowInstance, callback)

    def GetWindowInstance(self):
        return self.WindowInstance
