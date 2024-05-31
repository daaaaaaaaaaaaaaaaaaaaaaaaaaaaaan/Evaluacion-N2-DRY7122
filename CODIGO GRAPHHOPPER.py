import requests

API_KEY = "dff48862-0c48-4c73-885c-7b914496b8fa"
BASE_URL = "https://graphhopper.com/api/1"

def calcular_distancia(ciudad_origen, ciudad_destino):
    url = f"{BASE_URL}/geocode?key={API_KEY}&q={ciudad_origen}"
    response = requests.get(url)
    origen = response.json()["hits"][0]

    url = f"{BASE_URL}/geocode?key={API_KEY}&q={ciudad_destino}"
    response = requests.get(url)
    destino = response.json()["hits"][0]

    url = f"{BASE_URL}/route?point={origen['point']['lat']},{origen['point']['lng']}&point={destino['point']['lat']},{destino['point']['lng']}&vehicle=car&key={API_KEY}"
    response = requests.get(url)
    datos_ruta = response.json()["paths"][0]

    distancia_km = datos_ruta["distance"] / 1000
    duracion_seg = datos_ruta["time"] / 1000
    duracion_horas = duracion_seg / 3600

    consumo_litros = distancia_km * 0.08  # Ejemplo de consumo de combustible: 8 litros por cada 100 km

    print(f"\nDistancia entre {ciudad_origen} y {ciudad_destino}: {distancia_km:.2f} km")
    print(f"Duración del viaje: {int(duracion_horas)} horas, {int(duracion_seg/60)%60} minutos, {int(duracion_seg)%60} segundos")
    print(f"Combustible requerido: {consumo_litros:.2f} litros")

    print("\nNarrativa del viaje:")
    for instruccion in datos_ruta["instructions"]:
        print(instruccion["text"])

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular distancia entre Santiago y Puerto Varas")
        print("2. Calcular distancia entre dos ciudades")
        print("q. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_distancia("Santiago", "Puerto Varas")
        elif opcion == "2":
            ciudad_origen = input("Ingrese la ciudad de origen: ")
            ciudad_destino = input("Ingrese la ciudad de destino: ")
            calcular_distancia(ciudad_origen, ciudad_destino)
        elif opcion.lower() == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()