import imgui
from imgui.integrations.glfw import GlfwRenderer

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
        imgui.text(f"Application Name: {config.Name}")
        imgui.text(f"Version: {config.Version}")
        imgui.text(f"Description: {config.ApplicationDescription}")
        imgui.end()

        imgui.render()
        self.RendererImplementation.render(imgui.get_draw_data())

    def Cleanup(self):
        self.RendererImplementation.shutdown()
