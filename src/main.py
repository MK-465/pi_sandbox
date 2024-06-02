from service.grove_rgb_lcd import GroveRGBLCD


def main():
    # Call a function from another module
    lcd = GroveRGBLCD()
    lcd.setDefault()
    print(f" SetDefault for: GroveRGBLCD!")


if __name__ == "__main__":
    main()
