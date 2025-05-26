# 🎲 Juego de Trenes

CLAUDIA PATRICIA CASTAÑEDA BERMUDEZ
- LAURA VALENTINA TORRES CÁRDENAS <laura.torres-c@mail.escuelaing.edu.co>
- JUAN SEBASTIÁN GUAYAZÁN CLAVIJO <juan.guayazan-c@mail.escuelaing.edu.co>   
Algoritmos y Programación (ISIS AYPR-62 LEC y AYPR-6201 LAB)   
Decanatura Ingeniería de Sistemas → Centro de Estudios de Fundamentos de Computación    
Ingeniería de Sistemas y Matemáticas    
Escuela Colombiana de Ingeniería Julio Garavito    
2023-2

## 🧩 Descripción del Juego

El *Juego de Trenes* es un juego de mesa digital para **dos jugadores**, cuyo objetivo es ordenar de forma **ascendente** una lista de **siete cartas** numeradas entre **1 y 100**. En cada turno, los jugadores lanzan un **dado de 5 caras** que determina la acción a realizar sobre sus cartas.

## 🎯 Objetivo del Juego

El primer jugador que logre ordenar sus cartas de forma ascendente gana la partida. El juego implementa funciones que simulan el dado, modifican las cartas, validan si una carta está asegurada y permiten ejecutar operaciones estratégicas como intercambios o rotaciones.

## 🎲 Opciones del Dado

1. Cambiar la **primera carta (izquierda)** por una nueva al azar.
2. Cambiar la **carta de la mitad** por una nueva al azar.
3. Cambiar la **última carta (derecha)** por una nueva al azar.
4. **Asegurar** una carta.
5. **Elegir una acción libremente** entre:

   * Intercambiar dos cartas contiguas.
   * Intercambiar dos cartas separadas por dos cartas intermedias (no disponible para las últimas tres cartas).
   * Rotar todas las cartas una posición a la derecha.
   * Rotar todas las cartas una posición a la izquierda.

Las cartas aseguradas **no pueden ser modificadas** por el dado.

## 🛠 Reglas y Restricciones de Implementación

* ✅ El trabajo fue realizado en **parejas**.
* ✅ Solo se utilizaron **strings y listas** como estructuras de datos.
* ❌ No se utilizaron estructuras como diccionarios (`dict`), ni funciones como `sorted()`, `sort()`, `enumerate()`, entre otras del core de Python.
* ✅ Todos los movimientos del juego fueron implementados mediante **funciones propias**.

## 📁 Estructura del Repositorio

* `Tren.py` — Código fuente principal con la lógica del juego.
* `README.md` — Este archivo con información completa del proyecto.

## 🚀 Instrucciones para Ejecutar

1. Clona este repositorio.

2. Abre una terminal o consola y ubícate en el directorio del proyecto.

3. Ejecuta el archivo `Tren.py` con Python 3:

   ```bash
   python Tren.py
   ```

4. Sigue las instrucciones en pantalla para jugar.
