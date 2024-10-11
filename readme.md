# Sistema de Compartición de Claves Criptográficas - Esquema de Shamir

## Descripción
Este proyecto implementa el esquema de Shamir para compartir una clave criptográfica entre **n** usuarios, permitiendo que solo **k** de ellos puedan reconstruir la clave original. La implementación está basada en aritmética modular y utiliza técnicas de criptografía modernas.

## Tabla de Contenidos
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Guía de Uso de menu.py](#guía-de-uso-de-menupy)


## Características
- Compartición de clave utilizando el esquema de Shamir.
- Recuperación de la clave original a partir de un subconjunto de usuarios.
- Implementación eficiente utilizando aritmética modular.

## Tecnologías Utilizadas
- Python 3.x
- Bibliotecas: [incluir aquí las bibliotecas que estés utilizando, por ejemplo, `numpy`, `cryptography`, etc.]

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Gerson-art/Proyecto_Shamir_Secret_Sharing.git



```markdown
# Guía de Uso de menu.py

`menu.py` es el punto de entrada para interactuar con la implementación del esquema de Shamir en Python. A través de este menú, los usuarios pueden dividir un secreto, reconstruirlo a partir de shares generados, y obtener el polinomio utilizado en el proceso. A continuación, se detallan las funcionalidades disponibles y cómo utilizarlas.

## Requisitos Previos

Antes de ejecutar `menu.py`, asegúrate de tener instalado Python y las bibliotecas necesarias:

- `sympy`
- `numpy`

Puedes instalar las bibliotecas requeridas utilizando `pip`:

```bash
pip install sympy numpy
```

## Ejecución del Programa

Para ejecutar el programa, navega hasta el directorio que contiene `menu.py` y utiliza el siguiente comando:

```bash
python menu.py
```

## Opciones del Menú

Al ejecutar `menu.py`, se presentará el siguiente menú de opciones:

```
1. Dividir secreto
2. Reconstruir secreto
3. Obtener polinomio a partir de shares
4. Salir
```

### Opción 1: Dividir Secreto

1. Selecciona la opción `1` y presiona `Enter`.
2. Se te pedirá ingresar:
   - **Secreto**: Un número entero que deseas dividir.
   - **Umbral**: Un número entero que representa cuántos shares son necesarios para reconstruir el secreto.
   - **Número de Shares**: Cuántas partes se generarán a partir del secreto.
3. El programa generará un número primo aleatorio y dividirá el secreto en el número especificado de shares.
4. Se mostrará el umbral utilizado, el número primo aleatorio y los shares generados.

### Opción 2: Reconstruir Secreto

1. Selecciona la opción `2` y presiona `Enter`.
2. Introduce los shares en el formato `(x1,y1), (x2,y2), ... ,(xn,yn)` separados por comas.
3. Se te pedirá ingresar:
   - **Umbral**: El mismo umbral utilizado para dividir el secreto.
   - **Número primo**: El número primo utilizado durante la división.
4. El programa seleccionará aleatoriamente el número especificado de shares y reconstruirá el secreto, mostrando el resultado.

### Opción 3: Obtener Polinomio a Partir de Shares

1. Selecciona la opción `3` y presiona `Enter`.
2. Introduce los shares en el formato `(x1,y1), (x2,y2), ... ,(xn,yn)` separados por comas.
3. Se te pedirá ingresar:
   - **Umbral**: El umbral utilizado para dividir el secreto.
   - **Número primo**: El número primo utilizado durante la división.
4. El programa seleccionará aleatoriamente el número especificado de shares y devolverá el polinomio reconstruido.

### Opción 4: Salir

1. Selecciona la opción `4` y presiona `Enter` para cerrar el programa.

