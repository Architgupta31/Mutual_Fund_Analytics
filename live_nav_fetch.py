import requests

schemes = {
    119551: "SBI Bluechip",
    120503: "ICICI Bluechip",
    118632: "Nippon Large Cap",
    119092: "Axis Bluechip",
    120841: "Kotak Bluechip"
}

print("CHECKING 5 KEY SCHEMES")
print("=" * 70)

for code, expected_name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    print("\nExpected:", expected_name)
    print("Scheme code:", code)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        api_name = data["meta"]["scheme_name"]
        records = len(data["data"])

        print("API returned:", api_name)
        print("NAV records:", records)

    else:
        print("API request failed.")

print("\n" + "=" * 70)
print("Scheme check completed!")