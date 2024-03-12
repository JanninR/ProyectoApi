from prettytable import PrettyTable

def obtener_input_usuario():
    print("Bienvenido al sistema de consulta de propiedades edáficas.")
    departamento = input("Ingrese el nombre del departamento: ")
    municipio = input("Ingrese el nombre del municipio: ")
    cultivo = input("Ingrese el nombre del cultivo: ")
    limit = int(input("Ingrese el número de registros a consultar (por ejemplo, 10): "))
    
    return {"departamento": departamento, "municipio": municipio, "cultivo": cultivo, "limit": limit}

def mostrar_resultados(resultados):
    if not resultados.empty:
        columnas_mostrar = ['Departamento', 'Municipio', 'Cultivo', 'Topografia',]
        tabla_resultados = PrettyTable(columnas_mostrar)
        
        for _, row in resultados.iterrows():
            
            fila = [row[col] if col in resultados.columns else 'N/A' for col in columnas_mostrar]
            tabla_resultados.add_row(fila)
        
        print("Resultados de la consulta:")
        print(tabla_resultados)
    else:
        print("No se encontraron datos para la consulta.")

def mostrar_mediana_edaficas(mediana):
    if mediana is not None:
        tabla_mediana = PrettyTable(["Variable", "Mediana"])
        for variable, valor in mediana.items():
            tabla_mediana.add_row([variable, valor])
        print("\nLa mediana de las variables edáficas:")
        print(tabla_mediana)
    else:
        print("No se encontraron datos para calcular la mediana.")





def preguntar_otra_consulta():
    respuesta = input("¿Desea realizar otra consulta? (Ingrese 'si' o 'no'): ")
    return respuesta.lower() == 'si'