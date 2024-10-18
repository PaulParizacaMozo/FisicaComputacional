# Práctica Laboratorio 3 - Física Computacional
## Por: Paul Parizaca Mozo

Este trabajo es parte del curso de **Física Computacional** en la Universidad Nacional de San Agustín y tiene como objetivo implementar la **Segunda Ley de Newton** para resolver problemas utilizando **Python** con una interfaz gráfica desarrollada en **Tkinter**. El programa permite calcular la **fuerza**, **masa** o **aceleración** de un objeto en función de las demás variables.

## Descripción del Programa

El programa implementa lo siguiente:
- **Cálculo de Fuerza**: Dada la masa y la aceleración, calcula la fuerza aplicada utilizando la fórmula \( F = m * a \).
- **Cálculo de Masa**: Dada la fuerza y la aceleración, calcula la masa mediante \( m = F / a \).
- **Cálculo de Aceleración**: Dada la fuerza y la masa, calcula la aceleración mediante \( a = F / m \).

El programa cuenta con una interfaz gráfica sencilla que permite ingresar los valores y muestra los resultados en tiempo real. También maneja errores comunes como entrada de datos no numéricos o división por cero, mostrando mensajes adecuados.

## Archivos Principales

- `main.py`: Archivo principal que contiene el código del programa en Python.

## Requerimientos

- **Python 3.8+**
- **Tkinter** (generalmente incluido con Python)

## Cómo Ejecutar el Programa

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/PaulParizacaMozo/FisicaComputacional.git
   cd FisicaComputacional/Laboratorio03
   ```

2. Ejecuta el script principal:
   ```bash
   python main.py
   ```

3. Interactúa con la interfaz gráfica para calcular la fuerza, masa o aceleración. Ingresa los valores correspondientes y el resultado se mostrará en pantalla.

