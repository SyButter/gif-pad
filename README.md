# gif-pad

This repository contains CircuitPython code for playing GIF animations on the Hiletgo 2.2" ILI9341 SPI display using the Waveshare RP2040-Plus board.

## Hardware wiring

Connect the display to the RP2040-Plus using the following pins (adjust as needed):

| Display Pin | RP2040-Plus Pin |
|-------------|-----------------|
| VCC         | 3V3             |
| GND         | GND             |
| SCK         | GP18            |
| MOSI        | GP19            |
| MISO        | GP16 (unused)   |
| CS          | GP17            |
| DC          | GP20            |
| RESET       | GP21            |
| LED         | 3V3             |

## Setup

1. Download the Adafruit CircuitPython library bundle corresponding to your CircuitPython version.
2. Copy the following libraries from the bundle into the `lib` directory on the CIRCUITPY drive:
   - `adafruit_ili9341.mpy`
   - `adafruit_gifio.mpy`
   - `adafruit_imageload.mpy`
   - `adafruit_bus_device`
3. Copy `code.py` from this repository to the root of the CIRCUITPY drive.
4. Create a `gifs` directory on the CIRCUITPY drive and place your GIF file there named `demo.gif` (or update the path in `code.py`).
5. Eject the drive. The board will automatically run `code.py` and display the GIF.

## Notes

The display orientation and pin assignments can be changed in `code.py` if your wiring differs. Large GIF files may require more memory than available on the board.
