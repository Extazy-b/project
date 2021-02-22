from blocks import Float, Wall, Water, Space
N = 20
CELL_SIZE = 25
blocks = {" ": Float(),
          "_": Water(),
          "X": Wall(),
          "S": Float(),
          "E": Float(),
          "": Space()}
keys = {"w": 26,
        "a": 4,
        "s": 22,
        "d": 7,}
indent = 50