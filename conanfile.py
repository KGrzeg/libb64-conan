from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class Libb64Conan(ConanFile):
    name = "libb64"
    version = "0.1"

    # Optional metadata
    license = "Creative Commons Public Domain License"
    author = "Chris Venter"
    url = "https://github.com/KGrzeg/libb64-conan"
    description = "A  library of ANSI C routines for fast encoding/decoding data into and from a base64-encoded format."
    topics = ("base64", "codec", "encoder", "decoder")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True
    }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["libb64"]
