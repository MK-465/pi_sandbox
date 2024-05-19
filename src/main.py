from service.basic_service import DummyService


def main():
    # Call a function from another module
    service = DummyService("some name")
    result = service.sum(1, 2)
    print(f" Calculation result is: {result}")


if __name__ == "__main__":
    main()
