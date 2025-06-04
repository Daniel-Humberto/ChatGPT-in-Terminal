# 🧠 ChatGPT in Terminal

Este proyecto permite interactuar con los modelos de lenguaje de OpenAI (como `gpt-3.5-turbo` o `gpt-4o`) directamente desde la terminal. El script está escrito en Python e incluye un menú interactivo para seleccionar modelos, ajustar parámetros como la temperatura y el límite de tokens, y mantener una conversación en tiempo real con el asistente de IA.

---

## 🚀 Características

- Soporte para varios modelos de OpenAI.
- Menú interactivo desde terminal.
- Personalización de parámetros:
  - **Temperatura** (`temperature`): control de creatividad de la IA.
  - **Máximo de tokens** (`max_tokens`): longitud máxima de la respuesta.
- Historial contextual de conversación.
- Salida con comandos `exit` o `quit`.

---

## 📦 Requisitos

- Python 3.7 o superior
- Paquete `openai` instalado

Instalación del paquete:

```bash
pip install openai
