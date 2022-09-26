from time import sleep
from machine import Pin

class Key:
  def __init__(self, name):
    self.name = name
    self.active = False

row_pins = []
col_pins = []

#wiring is wonky, so last 2 columns are switched (3,1,2 instead of 3,2,1)
keys = [
    [Key(''), Key('XX'), Key('3'),Key('1'),Key('2')],
    [Key(''), Key('ST'), Key('6'),Key('4'),Key('5')],
    [Key(''), Key('ME'), Key('9'),Key('7'),Key('8')],
    [Key('FL'), Key('RD'), Key('#'),Key('*'),Key('0')]
]

for pin_num in range(4, 0, -1):
  row_pins.append(Pin(pin_num, Pin.OUT))

for pin_num in range(9, 4, -1):
  col_pins.append(Pin(pin_num, Pin.IN, Pin.PULL_DOWN))

print(row_pins)
print(col_pins)


def scan_keys():
  # turn on each row
  for row, row_pin in enumerate(row_pins):
    row_pin.on()

    # check each column to see if the key is pressed
    # and set that key to "active" in the keys matrix
    for col, col_pin in enumerate(col_pins):
      keys[row][col].active = bool(col_pin.value())

    # turn off the row
    row_pin.off()

## main loop

#starting keypad
print('------------')

while True:
  scan_keys()

  for row in keys:
    for key in row:
      if key.active:
        print(key.name, end='')
        # debounce button press  
        sleep(0.5)