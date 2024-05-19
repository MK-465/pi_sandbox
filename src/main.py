from service.basic_service import DummyService
from service.grove_rgb_lcd import GroveRGBLCD


def main():
    # Call a function from another module
    service = DummyService("some name")
    result = service.sum(1, 2)
    print(f" Calculation result is: {result}")

    lcd = GroveRGBLCD()
    lcd.setDefault()
    print(f" SetDefault for: GroveRGBLCD")


if __name__ == "__main__":
    main()
