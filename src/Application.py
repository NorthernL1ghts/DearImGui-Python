import sys
import time
import threading
import platform
import os
from OpenGL import GL as gl  # Importing OpenGL module for OpenGL functions
from Window import Window
from Event import Event
from DearImGuiLayer import DearImGuiRenderer
from PerformanceTimers import PerformanceTimers
from Configuration import ApplicationConfiguration, VERSION, PLATFORM, CURRENT_CONFIGURATION

g_ApplicationRunning = True

class Application:
    s_MainThread = threading.main_thread()
    s_MainThreadID = s_MainThread.ident

    def __init__(self, config):
        self.Config = config
        self.LastUpdateTime = time.perf_counter()  # More precise time measurement
        self.UpdateInterval = 1.0 / 60.0
        self.LastEventTime = time.perf_counter()
        self.PerformanceTimers = PerformanceTimers()

        self.WindowInstance = Window(self.Config)
        if not self.WindowInstance.GetWindowInstance():
            print("Failed to create window")
            sys.exit(1)

        self.DearImGuiRenderer = DearImGuiRenderer(self.WindowInstance.GetWindowInstance())
        self.DearImGuiRenderer.SetupDearImGui()
        self.EventHandler = Event(self.WindowInstance)

        print(f"Main Thread: {self.s_MainThread}")
        print(f"Main Thread ID: {self.s_MainThreadID}")

    def GetTime(self):
        return time.perf_counter() - self.LastUpdateTime

    def Run(self):
        global g_ApplicationRunning
        while not self.WindowInstance.ShouldClose() and g_ApplicationRunning:
            current_time = time.perf_counter()
            elapsed_time = current_time - self.LastUpdateTime

            if elapsed_time >= self.UpdateInterval:
                self.EventHandler.ProcessEvents()
                self.DearImGuiRenderer.RenderUI(self.Config)

                gl.glClearColor(1.0, 0.0, 1.0, 1.0)  # Use the OpenGL function
                gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # Clear the buffer
                self.WindowInstance.SwapBuffers()

                self.LastUpdateTime = current_time

            sleep_time = self.UpdateInterval - elapsed_time
            if sleep_time > 0:
                time.sleep(sleep_time)

    def AddToSystemPath(self, directory):
        if not os.path.isdir(directory):
            print(f"Directory {directory} doesn't exist")
            return

        directory_name = os.path.basename(directory)  # Get the directory name dynamically
        current_path = os.environ.get("PATH", "")
        if directory_name not in current_path:
            if platform.system() == "Windows":
                os.environ["PATH"] += f";{directory}"
            else:
                os.environ["PATH"] += f":{directory}"
            print(f"Added {directory_name} directory to PATH")
        else:
            print(f"{directory_name} is already in the PATH")

    def GetPlatformName(self):
        return platform.system()  # Return the platform (e.g., "Windows", "Linux")


class EntryPoint:
    @staticmethod
    def Main():
        config = ApplicationConfiguration(
            application_name="DearImGui-Python",
            window_width=1280,
            window_height=720,
            application_description="An example application using Dear ImGui with GLFW and OpenGL."
        )
        app = Application(config)
        print(f"Platform: {app.GetPlatformName()}")  # This will now print the platform name

        app.AddToSystemPath("C:\\Dev\\Projects\\GitHub\\DearImGui-Python")

        app.Run()


if __name__ == "__main__":
    EntryPoint.Main()
