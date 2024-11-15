import os

from platformio.builder.tools.piolib import ArduinoLibBuilder

Import("env")

# This workaround bypasses circular dependencies issue between
# Adafruit_ZeroDMA and Adafruit_TinyUSB_Arduino libs by
# adding necessary include paths to the Adafruit_ZeroDMA
# build environment

framework_dir = env.PioPlatform().get_package_dir(
    "framework-arduino-samd-adafruit"
)
spi_lb = ArduinoLibBuilder(env, os.path.join(framework_dir, "libraries", "SPI"))
tinusb_lb = ArduinoLibBuilder(
    env, os.path.join(framework_dir, "libraries", "Adafruit_TinyUSB_Arduino")
)

if "USE_TINYUSB" in env.get("CPPDEFINES", []):
    env.AppendUnique(
        CPPPATH=spi_lb.get_include_dirs() + tinusb_lb.get_include_dirs()
    )
