import glfw

class Window:
    def __init__(self, width=1280, height=720, title="GLFW + Dear ImGui"):
        if not glfw.init():
            raise Exception("GLFW initialization failed")

        self.width = width
        self.height = height
        self.title = title
        self.window = glfw.create_window(self.width, self.height, self.title, None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window creation failed")

        glfw.make_context_current(self.window)

    def should_close(self):
        return glfw.window_should_close(self.window)

    def poll_events(self):
        glfw.poll_events()

    def swap_buffers(self):
        glfw.swap_buffers(self.window)

    def terminate(self):
        glfw.terminate()
