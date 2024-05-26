# pi_sandbox
![Grove PI APP](https://github.com/MK-465/pi_sandbox/actions/workflows/main.yml/badge.svg)

This is a sandbox for the Raspberry Pi. It is a collection of scripts and programs that I have written to learn more about the Raspberry Pi and to have fun with it.

<!-- TOC -->
* [pi_sandbox](#pi_sandbox)
    * [I2C address](#i2c-address)
    * [Remote debug](#remote-debug)
  * [Items](#items)
    * [1. Grove - LCD RGB Backlight](#1-grove---lcd-rgb-backlight)
<!-- TOC -->


### I2C address
* To check if the I2C address is correct, you can use the i2cdetect command in the terminal. This command scans the I2C bus for devices and returns a list of addresses that are in use.  Here's how you can use it:  
Open a terminal.
If you're using a Raspberry Pi with a version 2 or 3 board, type `i2cdetect -y 1`. If you're using a version 1 board, type `i2cdetect -y 0`.
</br>
Press Enter.
</br>
The command will return a grid of hex numbers. The numbers that are not -- are the addresses of devices connected to the I2C bus. If 0x62 (the address of DISPLAY_RGB_ADDR) is in the list, then the address is correct.  
> !NOTE
> Please note that you need to have i2c-tools installed to use i2cdetect. If it's not installed, you can install it with sudo apt-get install -y i2c-tools.

* Check the I2C address in Python
```python
import smbus

bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi versions 2 & 3, and 0 for version 1

def is_address_correct(address):
    try:
        bus.read_byte(address)
        return True
    except IOError:
        return False

print(is_address_correct(0x62))  # Replace 0x62 with the address you want to check
```

### Remote debug
To remotely debug a Python application running on a Raspberry Pi using PyCharm, you can use the `pydevd-pycharm` package. Here are the steps:

1. Install the `pydevd-pycharm` package on the Raspberry Pi where your Python application is running. You can install it using pip:

```bash
pip install pydevd-pycharm~=241.15989.155
```

Replace `203.7148.72` with the version of your PyCharm. You can find this in PyCharm by going to `Help > About`.

2. In your Python code, import the `pydevd_pycharm` module and set a breakpoint using `pydevd_pycharm.settrace()`. For example:

```python
import pydevd_pycharm

pydevd_pycharm.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)
```

Replace `'localhost'` with the IP address of your local machine (where PyCharm is running). Replace `12345` with a port number that is not being used on your local machine.

3. In PyCharm, go to `Run > Edit Configurations`, click on the `+` button and select `Python Debug Server`. Enter a name for the configuration, the port number you used in `settrace()`, and check `Allow connections from network`.
4. Click on the debug button (or press Shift+F9) to start the debug server.
5. Run your Python application on the Raspberry Pi. It should connect to the debug server and stop at the line where you called `settrace()`.

Now you can step through your code, inspect variables, and use all other debugging features of PyCharm.

> [!NOTE]
> Make sure that your Raspberry Pi and your local machine are on the same network and can communicate with each other.
> </br> Using scripts: `./copy_to_remote.sh && ./run_remote.sh`

## Items
### 1. Grove - LCD RGB Backlight
[Documentation](https://github.com/SeeedDocument/Grove_LCD_RGB_Backlight/blob/master/Grove-LCD_RGB_Backlight.md)
