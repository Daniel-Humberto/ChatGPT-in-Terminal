import os
import openai

# API OpenAI
openai.api_key = os.environ.get("OpenAI_API_KEY")

def chat_with_gpt(model, temperature, max_tokens):
    """
    Interactúa con el modelo GPT-3.5 o GPT-4 a través de la API de OpenAI.
    """
    messages = [
        {"role": "system", "content": "You are chatting with an AI assistant."}
    ]
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Saliendo del chat...")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = openai.Completion.create(
                engine=model,  # Replace model with engine
                prompt="\n".join([msg["content"] for msg in messages]),
                temperature=temperature,
                max_tokens=max_tokens,
                stop=None,  # Optional stop sequence to end conversation
            )
            assistant_message = response.choices[0].text.strip()
            print(f"AI: {assistant_message}")
            messages.append({"role": "assistant", "content": assistant_message})

        except openai.APIError as e:
            print(f"Error con OpenAI: {str(e)}")
        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")


def get_valid_temperature():
    """
    Solicita al usuario una temperatura válida entre 0.0 y 1.0.
    """
    while True:
        try:
            temperature = float(input("Introduce la temperatura (0.0 a 1.0): "))
            if 0.0 <= temperature <= 1.0:
                return temperature
            else:
                print("La temperatura debe estar entre 0.0 y 1.0.")
        except ValueError:
            print("Entrada no válida. Debe ser un número entre 0.0 y 1.0.")

def get_valid_max_tokens():
    """
    Solicita al usuario un número máximo de tokens válido entre 1 y 2048.
    """
    while True:
        try:
            max_tokens = int(input("Introduce el número máximo de tokens (1 a 2048): "))
            if 1 <= max_tokens <= 2048:
                return max_tokens
            else:
                print("El número máximo de tokens debe estar entre 1 y 2048.")
        except ValueError:
            print("Entrada no válida. Debe ser un número entre 1 y 2048.")

def display_main_menu():
    """
    Muestra el menú principal y retorna la opción elegida por el usuario.
    """
    models = {
        '1': "gpt-3.5-turbo",
        '2': "gpt-3.5-turbo-0125",
        '3': "gpt-3.5-turbo-1106",
        '4': "gpt-3.5-turbo-16k",
        '5': "gpt-4o-mini",
        '6': "gpt-4o-mini-2024-07-18"
    }

    print("\n--- Menú Principal ---")
    for key, model in models.items():
        print(f"{key}. {model}")
    print("7. Salir")

    choice = input("Elige una opción: ")
    return choice, models.get(choice)

def main_menu():
    """
    Menú principal que permite al usuario seleccionar el modelo y configurar parámetros.
    """
    while True:
        choice, model = display_main_menu()

        if model:
            print(f"Seleccionaste el modelo {model}.")
            temperature = get_valid_temperature()
            max_tokens = get_valid_max_tokens()
            chat_with_gpt(model, temperature, max_tokens)
        elif choice == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main_menu()