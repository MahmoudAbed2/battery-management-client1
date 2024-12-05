import requests

BASE_URL = "http://127.0.0.1:5000"

def get_info():
    try:
        response = requests.get(f"{BASE_URL}/info")
        response.raise_for_status()
        data = response.json()
        print(f"\n--- Simuleringstid och batteristatus ---")
        print(f"Simuleringstid: {data['simulation_time']} timmar")
        print(f"Energiförbrukning: {data['total_consumption']} kWh")
        print(f"Batteriladdning: {data['battery_charge_kwh']} kWh")
    except Exception as e:
        print(f"Fel vid hämtning av information: {e}")

def get_baseload():
    try:
        response = requests.get(f"{BASE_URL}/baseload")
        response.raise_for_status()
        data = response.json()
        print(f"\n--- Hushållets energiförbrukning ---")
        print(f"Energiförbrukning: {data['baseload']} kWh")
    except Exception as e:
        print(f"Fel vid hämtning av energiförbrukning: {e}")

def get_prices():
    try:
        response = requests.get(f"{BASE_URL}/priceperhour")
        response.raise_for_status()
        data = response.json()
        print(f"\n--- Elpriser per timme ---")
        for i, price in enumerate(data['prices'], start=1):
            print(f"Timme {i}: {price} SEK/kWh")
    except Exception as e:
        print(f"Fel vid hämtning av elpriser: {e}")

def start_charging():
    try:
        response = requests.post(f"{BASE_URL}/charge", json={"command": "start"})
        response.raise_for_status()
        data = response.json()
        print(f"\n{data['status']}")
    except Exception as e:
        print(f"Fel vid start av laddning: {e}")

def stop_charging():
    try:
        response = requests.post(f"{BASE_URL}/charge", json={"command": "stop"})
        response.raise_for_status()
        data = response.json()
        print(f"\n{data['status']}")
    except Exception as e:
        print(f"Fel vid stopp av laddning: {e}")

def main():
    while True:
        print("\n--- Battery Management System ---")
        print("1. Hämta aktuell simuleringstid och batteristatus")
        print("2. Hämta hushållets energiförbrukning")
        print("3. Hämta elpriser per timme")
        print("4. Starta laddning")
        print("5. Stoppa laddning")
        print("6. Avsluta")
        print("---------------------------------")
        choice = input("Välj ett alternativ (1-6): ")
        if choice == "1":
            get_info()
        elif choice == "2":
            get_baseload()
        elif choice == "3":
            get_prices()
        elif choice == "4":
            start_charging()
        elif choice == "5":
            stop_charging()
        elif choice == "6":
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()
