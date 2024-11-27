import imgui

class DearImGuiLayer:
    def __init__(self):
        self.color = [0.2, 0.2, 0.2]  # Default color set to dark gray

    def render(self):
        imgui.set_next_window_size(400, 100)  # Width, Height
        imgui.begin("Color Customization")
        changed, self.color = imgui.color_edit3("Background Color", *self.color)
        imgui.end()
        return self.color
