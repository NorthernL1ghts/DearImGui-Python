from enum import Enum
import platform

VERSION = "1.0.0"
ARCHITECTURE = "X64"

class Configuration(Enum):
    DEBUG = "Debug"
    RELEASE = "Release"
    DIST = "Dist"

CURRENT_CONFIGURATION = Configuration.DEBUG

PLATFORM = {
    "Windows": "PLATFORM_WINDOWS",
    "Linux": "PLATFORM_LINUX",
    "Darwin": "PLATFORM_MACOS"
}.get(platform.system(), "PLATFORM_UNKNOWN")

class ApplicationConfiguration:
    def __init__(self, application_name, window_width, window_height, application_description):
        self.Name = application_name
        self.Version = VERSION
        self.WindowWidth = window_width
        self.WindowHeight = window_height
        self.ApplicationDescription = application_description
