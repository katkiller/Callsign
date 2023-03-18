import requests
import json
from datetime import datetime, date
import sys

def get_license_data(callsign):
    url = f"https://data.fcc.gov/api/license-view/basicSearch/getLicenses?searchValue={callsign}&format=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error: API request failed with status code {response.status_code}")
    data = response.json()
    if data.get('status') != "OK":
        raise Exception("Error: Failed to retrieve license data")
    licenses = data.get('Licenses', {}).get('License', [])
    if not licenses:
        raise Exception("Error: License data not found")
    license_data = licenses[0]
    return license_data

def is_license_valid(license_data):
    status = license_data['statusDesc']
    expired_date = datetime.strptime(license_data['expiredDate'], '%m/%d/%Y').date()
    today = date.today()

    if status == "Active" and expired_date >= today:
        return True
    elif status == "Expired":
        print("License is expired.")
    elif status == "Revoked":
        print("License has been revoked.")
    elif status == "Cancelled":
        print("License has been cancelled.")
    elif status == "Pending":
        print("License application is still pending.")
    elif status == "Dismissed":
        print("License application has been dismissed.")
    else:
        print("Unknown license status.")
    return False

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a ham radio callsign to look up.")
        return

    callsign = sys.argv[1]
    try:
        license_data = get_license_data(callsign)
        if license_data:
            print(f"Callsign: {license_data['callsign']}")
            print(f"Licensee: {license_data['licName']}")
            print(f"License status: {license_data['statusDesc']}")
            print(f"License category: {license_data['categoryDesc']}")
            print(f"Service: {license_data['serviceDesc']}")
            print(f"Expiration date: {license_data['expiredDate']}")

            if is_license_valid(license_data):
                print("License is valid.")
            else:
                print("License is not valid.")
        else:
            print("Unable to retrieve license data.")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
