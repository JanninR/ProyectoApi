from ui_module import obtener_input_usuario, mostrar_resultados, mostrar_mediana_edaficas
from api_module import obtener_datos

def main():
    while True:
        input_usuario = obtener_input_usuario()
        resultados, mediana_edaficas = obtener_datos(input_usuario["departamento"], input_usuario["municipio"], input_usuario["cultivo"], input_usuario["limit"])

        if resultados is not None:
            mostrar_resultados(resultados)
            mostrar_mediana_edaficas(mediana_edaficas)

        otra_consulta = input("¿Desea realizar otra consulta? (Ingrese 'si' o 'no'): ").lower()
        if otra_consulta != 'si':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()



