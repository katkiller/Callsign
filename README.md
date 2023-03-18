# FCC Radio Callsign Lookup
This is a Python script that retrieves and displays information about a FCC radio callsign using the FCC Universal Licensing System API. The script looks up all data fields associated with the given callsign and checks if the license is currently active and not expired.

Ham Radio Callsign Lookup
This is a Python script that retrieves and displays information about a ham radio callsign using the FCC Universal Licensing System API. The script looks up all data fields associated with the given callsign and checks if the license is currently active and not expired.

## Requirements
Python 3
requests, json, datetime, and sys modules 

## Usage
Clone this repository or download callsign.py.
Install the modules using pip.
Open a terminal or command prompt in the directory where callsign.py is located.
Run the script by typing python callsign.py followed by the callsign you want to look up.
For example: python callsign.py W1AW

## Output
The script outputs the following information about the callsign:

Callsign
Licensee name
License status
License category
Service
Expiration date

## License Status
The script checks the license status and prints one of the following messages:

License is valid.
License is not valid.
License is expired.
License has been revoked.
License has been cancelled.
License application is still pending.
License application has been dismissed.

## Error Handling
The script includes error handling for the following scenarios:

* Invalid API request (incorrect API endpoint, invalid response)
* Failed to retrieve license data
* License data not found
* If an error occurs, the script will print an error message and then exit.

## Contributing
If you find any issues with the script or have suggestions for improvements, please feel free to create a pull request or open an issue.

## License
This project is licensed under the GPL-3.0 License.
