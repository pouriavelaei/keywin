# KeyWin

KeyWin is a Python script designed to activate Windows using a KMS server.

## Warning

This script is for educational purposes only. Using it may violate Microsoft's software license agreement. Ensure compliance with your organization's policies before use.

## Features

- Automatic Windows activation using a KMS server
- Runs with administrator privileges
- Error handling and appropriate messaging

## Requirements

- Windows 10 or later
- Python 3.6+

## Usage

1. Download or clone this repository.
2. Right-click `keywin.py` and select "Run as administrator".
3. The script will attempt to activate Windows using the specified KMS server.
4. Activation result will be displayed in the command prompt.

## How it works

1. Checks for admin rights and requests them if necessary
2. Sets KMS server using `slmgr /skms`
3. Activates Windows using `slmgr /ato`

## Disclaimer

Use of this script may violate Microsoft's terms of service. The author takes no responsibility for misuse or illegal use of this code. Use at your own risk.

## License

[GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)
