#BY: HACK UNDERWAY

import os
import requests
from colorama import Fore, init
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize colorama
init(autoreset=True)

# ASCII Art
ascii_art = r"""
     .              .   .'.     \   /
   \   /      .'. .' '.'   '  -=  o  =-
 -=  o  =-  .'   '              / | \
   / | \                          |
     |                            |
     |                            |
     |                      .=====|
     |=====.                |.---.|
     |.---.|                ||=o=||
     ||=o=||                ||   ||
     ||   ||                ||   ||
     ||   ||                ||___||
     ||___||                |[:::]|
jgs  |[:::]|                '-----'
     '-----'
"""

print(Fore.GREEN + ascii_art)

# Request phone number and region from the user
numero_telefonico = input(Fore.GREEN + "Por favor, introduce el número de teléfono: ")
region = input(Fore.GREEN + "Por favor, introduce la región (ej. 'pe' para Perú): ")

# Prepare the API request
url = "https://phone-number-analyzer.p.rapidapi.com/phone-number-in-google-search"
payload = {
    "number": numero_telefonico,
    "region": region
}
headers = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),  # Fetch API key from .env
    "x-rapidapi-host": "phone-number-analyzer.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Make the request and handle the response
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for non-200 status codes
    data = response.json()

    # Print the response in a readable format
    if data.get("status") == "OK":
        print(Fore.GREEN + "Consulta exitosa!")
        for item in data.get("result", []):
            title = item.get("title", "Sin título")
            url = item.get("url", "URL no disponible")
            print(f"{Fore.YELLOW}Título: {Fore.CYAN}{title}")
            print(f"{Fore.YELLOW}URL: {Fore.CYAN}{url}")
            print("-" * 50)
    else:
        print(Fore.RED + "No se encontraron resultados o hubo un problema con la consulta.")

except requests.exceptions.RequestException as e:
    print(Fore.RED + "Error en la solicitud:", e)
