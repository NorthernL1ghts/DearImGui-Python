from OpenGL.GL import *
import imgui
from imgui.integrations.glfw import GlfwRenderer
from DearImGuiLayer import DearImGuiLayer
from Window import Window

class Application:
    def __init__(self):
        self.window = Window()
        imgui.create_context()
        self.imgui_layer = DearImGuiLayer()
        self.impl = GlfwRenderer(self.window.window)

    def run(self):
        while not self.window.should_close():
            self.window.poll_events()
            self.impl.process_inputs()
            imgui.new_frame()

            color = self.imgui_layer.render()

            glClearColor(*color, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            self.window.swap_buffers()

        self.shutdown()

    def shutdown(self):
        self.impl.shutdown()
        self.window.terminate()

if __name__ == "__main__":
    app = Application()
    app.run()
