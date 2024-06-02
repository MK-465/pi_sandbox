import sys
sys.path.insert(0, '/home/pi/projects/grove_sandbox/pi_sandbox/resources/di_i2c.py')
sys.path.insert(1, '/home/pi/projects/grove_sandbox/pi_sandbox/resources/di_mutex.py')
sys.path.insert(2, '/home/pi/projects/grove_sandbox/pi_sandbox/resources/grovepi.py')
sys.path.insert(3, '/home/pi/projects/grove_sandbox/pi_sandbox/resources/')
sys.path.insert(4, '/home/pi/projects/grove_sandbox/pi_sandbox/resources/*')

from service.grove_rgb_lcd import GroveRGBLCD


def main():
    lcd = GroveRGBLCD()
    lcd.setDefault()
    print(f" SetDefault for: GroveRGBLCD!")


if __name__ == "__main__":
    main()
