# pylint: disable=missing-module-docstring
# Administrador de Tareas (To-Do List)
# Este script permite al usuario gestionar una lista de tareas, guardarlas en un archivo JSON
# y cargarlas al iniciar el programa.
import json
# Archivo donde se guardarán las tareas
ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    """Carga las tareas desde el archivo JSON y devuelve la lista actualizada."""
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, comenzamos con una lista vacía
        return []
    except json.JSONDecodeError:
        # Si el archivo está corrupto, comenzamos con una lista vacía
        return []


def guardar_tareas(tareas_guardar):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas_guardar, archivo, indent=4)


def mostrar_tareas(tareas_mostrar):
    """Muestra todas las tareas con su índice y estado."""
    if not tareas_mostrar:
        print("No hay tareas en la lista.")
    else:
        print("\nLista de Tareas:")
        for i, tarea in enumerate(tareas_mostrar, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - {estado}")


def agregar_tarea(descripcion, tareas_modificar):
    """Agrega una nueva tarea a la lista y guarda los cambios."""
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas_modificar.append(tarea)
    guardar_tareas(tareas_modificar)
    print(f"Tarea '{descripcion}' agregada.")
    return tareas_modificar


def eliminar_tarea(indice, tareas_modificar):
    """Elimina una tarea según su índice y guarda los cambios."""
    try:
        tarea_eliminada = tareas_modificar.pop(indice - 1)
        guardar_tareas(tareas_modificar)
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
        return tareas_modificar
    except IndexError:
        print("Índice no válido. Por favor, selecciona un número de tarea válido.")
        return tareas_modificar


def marcar_completada(indice, tareas_modificar):
    """Marca una tarea como completada según su índice y guarda los cambios."""
    try:
        tareas_modificar[indice - 1]["completada"] = True
        guardar_tareas(tareas_modificar)
        print(
            f"Tarea '{tareas_modificar[indice - 1]['descripcion']}' marcada como completada.")
        return tareas_modificar
    except IndexError:
        print("Índice no válido. Por favor, selecciona un número de tarea válido.")
        return tareas_modificar


def main():
    """Función principal con el menú interactivo."""
    # Cargar las tareas al iniciar
    tareas = cargar_tareas()
    print("¡Bienvenido al Administrador de Tareas!")

    while True:
        print("\n=== Administrador de Tareas ===")
        print("1. Mostrar todas las tareas")
        print("2. Agregar una nueva tarea")
        print("3. Eliminar una tarea")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            descripcion = input("Ingresa la descripción de la tarea: ")
            tareas = agregar_tarea(descripcion, tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
            try:
                indice = int(
                    input("Ingresa el número de la tarea a eliminar: "))
                tareas = eliminar_tarea(indice, tareas)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "4":
            mostrar_tareas(tareas)
            try:
                indice = int(
                    input("Ingresa el número de la tarea a marcar como completada: "))
                tareas = marcar_completada(indice, tareas)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "5":
            print("¡Gracias por usar el Administrador de Tareas!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")


if __name__ == "__main__":
    main()
