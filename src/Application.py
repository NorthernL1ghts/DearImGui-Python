import glfw
from OpenGL.GL import *
import imgui
from imgui.integrations.glfw import GlfwRenderer
from DearImGuiLayer import DearImGuiLayer

class Application:
    def __init__(self):
        if not glfw.init():
            raise Exception("GLFW initialization failed")

        self.window = glfw.create_window(1280, 720, "GLFW + Dear ImGui", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window creation failed")

        glfw.make_context_current(self.window)
        imgui.create_context()
        self.imgui_layer = DearImGuiLayer()
        self.impl = GlfwRenderer(self.window)

    def run(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.impl.process_inputs()
            imgui.new_frame()

            color = self.imgui_layer.render()

            glClearColor(*color, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)

        self.shutdown()

    def shutdown(self):
        self.impl.shutdown()
        glfw.terminate()

if __name__ == "__main__":
    app = Application()
    app.run()