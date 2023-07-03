# NordVPN Tray Icon

This is a Python project that creates a system tray icon for managing a VPN connection using the NordVPN command-line tool. The tray icon provides a convenient interface to connect, disconnect, and view the status of the VPN connection.

## Prerequisites

Before running the project, make sure you have the NordVPN command-line tool installed. Please refer to the official NordVPN documentation for installation instructions.

## Python Version

This project is developed using Python 3.10. While it may work on other Python 3 versions, there are no guarantees. It is recommended to use Python 3.10 for optimal compatibility.

## Project Files

The project consists of the following files (non-exhaustive):

* `exposed.png`: An image file representing the "exposed" state icon.
* `protected.png`: An image file representing the "protected" state icon.
* `status_icon.xcf`: A GIMP 2.0 project file for the status icons. This file is provided for reference or modification purposes, if needed.
* `nordvpn_tray_icon.py`: The main Python file that contains the implementation of the VPN tray icon.
* `requirements.txt`: A file listing the dependencies required by the project.
* `LICENSE`: A file containing the license this project is covered under.

## Usage

To run the project, first make sure you have the required dependencies installed by executing the following command:

```bash
pip install -r requirements.txt
```

Then, execute the following command to start the application:

```bash
python nordvpn_tray_icon.py
```

This will launch the application and display a system tray icon. Right-clicking on the icon will open a menu with the following options:

* Connect: Clicking this option will connect to the NordVPN service. It will enable the kill switch and establish a VPN connection.
* Disconnect: Clicking this option will disconnect from the NordVPN service. It will disable the kill switch and terminate the VPN connection.
* Quit: Clicking this option will exit the application and remove the tray icon.

The system tray icon automatically updates its appearance based on the VPN connection status. If the VPN is connected, the icon will display a "protected" state. If the VPN is disconnected, the icon will display an "exposed" state. Left-clicking on the tray icon will display a popup with the current status information.

## Acknowledgments

This project utilizes the NordVPN command-line tool for managing NordVPN connections.

## Disclaimer

This project is not affiliated with or endorsed by NordVPN. It is an independent project created for personal use.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

**Note:** This project is provided as-is without any warranty. Use it at your own risk.
