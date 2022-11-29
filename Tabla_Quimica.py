import  json
import requests

print("ingresar nombre del elelemento en ingles:")

elemento = input()

response = requests.get(f'https://periodic-table-api.herokuapp.com/atomicName/{elemento}').json()

print(f"Elemento: " + elemento + "\n Simbolo: {response['symbol']}\nNombre: {response['name']}\nClase: {response['groupBlock']}\nNumero Atómico: {response['atomicNumber']}\nMasa Atomica: {response['atomicMass']}\nElectronegatividad: {response['electronegativity']}\nDensidad: {response['density']}\nEstado de Oxidación: {response['oxidationStates']}\nConfiguración Electrónica: {response['electronicConfiguration']}")