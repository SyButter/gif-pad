import time
import board
import busio
import displayio
import adafruit_ili9341
import gifio

# Release any displays that may be in use
displayio.release_displays()

# SPI configuration (adjust pins as needed)
spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)

tft_cs = board.GP17
tft_dc = board.GP20
tft_reset = board.GP21

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
display = adafruit_ili9341.ILI9341(display_bus, width=240, height=320, rotation=270)

# Load GIF from storage
gif = gifio.OnDiskGif("/gifs/demo.gif")

# Display group for the GIF
frame_sprite = displayio.TileGrid(gif.bitmap, pixel_shader=gif.pixel_shader)
main_group = displayio.Group()
main_group.append(frame_sprite)

display.show(main_group)

while True:
    try:
        gif.next_frame()
    except OSError:
        # Restart the animation when the last frame is reached
        gif.reset()
        gif.next_frame()
    frame_sprite.bitmap = gif.bitmap
    time.sleep(gif.frame_delay / 1000)

