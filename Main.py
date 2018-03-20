from MockLed import *
from Stringy import *

    
def main():
    stringy = get_stringy("RISH")
    
    ' shift right every 8 (or as per dimension) '
    for x in range(0, len(stringy)-1, 8):
        show_led(stringy[x:x+64])


if __name__ == "__main__":
    main()
