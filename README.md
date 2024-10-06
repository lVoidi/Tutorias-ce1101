# Tutorias de Introducción a la Programación (CE1101)
En este repositorio, guardo todas mis clases, ejercicios y recursos disponibles. La idea de hacer este repositorio 
Open Source es para que las personas estudiantes del curso de Introducción a la Programacion tengan una mayor 
facilidad para accederlos.

# Contenidos
El curso aborda los siguientes temas, en orden:
1. Recursividad
    1. Recursividad de pila 
    2. Recursividad de cola 
    3. Recursividad simple
2. Estructuras de Datos simples 
    1. Listas 
    2. Matrices
3. Interfaces gráficas con tkinter
    1. Creación de una interfaz simple 
        1. Implementación de una animación utilizando hilos de manera implícita
        2. Manejo de assets (imágenes, sonidos)
    2. Proyecto de un juego, el cual aborda
        1. Uso de un bucle principal e hilos
        2. Manejo de assets (imágenes, sonidos)
        3. Gestión de archivos
4. Iteración 
    1. Bucle while
        1. Recorrer números utilizando while 
    2. Bucle for 
        1. Concepto de iterable 
        2. Manejo de listas y matrices 
5. Introducción Programación Orientada a Objetos (POO/OOP) simple 
6. Proyecto de POO

# Recursos 
## Cheatsheet de comandos útiles 
Hago esta sección para mostrar una lista de comandos de terminal que son increíblemente útiles para la vida diaria. Acostúmbrense a la terminal, no le tengan miedo. Si pueden, acostúmbrense a usar una terminal Unix-based como Git Bash (la cual utiliza bash), la de Mac o una de Linux. 
### Cambiar de directorio 
```sh 
cd <directorio>

# Ejemplo para Windows 
# Recuerden que en windows pueden agarrar la dirección de un directorio 
# directamente desde el file manager 
cd OneDrive/Documentos 

# Ejemplo para Unix-based (MacOS o Linux) 
cd ~/Documents/
```
### Mostrar los archivos en un directorio 
```sh 
# Windows 
dir 

# Unix 
ls 
```

### Mostrar el directorio en el que estamos trabajando
```sh
pwd 
```

### Copiar 

```sh 
cp <archivo> <nuevo directorio>
```

### Mover 
```sh
mv <archivo> <nuevo lugar> 
```

### Remover un archivo 
```sh 
rm <archivo>

# Remueve un directorio y todos los archivos dentro de forma recursiva
rm -rf <directorio>
```

## Comandos de git 
Git es una herramienta útil y gratuita. Recuerden que utilizar git para todos nuestros programas es muy útil y no cuesta nada, solo nos puede traer ventajas. 

### Autenticación 
Recomiendo crear claves pgp propias para firmar sus commits. Aquí les dejo unos tutoriales paso por paso oficiales de Github para configurar esto. 
1. [Generating a new GPG key](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)
2. [Associating an email with your GPG key](https://docs.github.com/en/authentication/managing-commit-signature-verification/associating-an-email-with-your-gpg-key)
3. [Telling Git about your signing key](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)
Cuando hacen esto, sus commits saldrán firmados en Github, una vez hacen el push. Si están en Windows, pueden ejecutar los comandos en Git Bash y les debería servir (a mi me sirvió el mismo tutorial para Linux en git bash).

### Iniciar un repositorio 
> Nota: Cuidado con los directorios en los que crean un repositorio, cuidado se les ocurre meter todo su home en un repositorio de git y luego hacer git add * o algo así. El resultado no es agradable
```sh 
git init 
```
Si se equivocan en su repositorio y lo ocupan borrar, lo más rápido y sencillo es hacer: 
```sh 
rm -rf .git 
```

### Configuración global 
```sh 
git config --global user.name "nombre"
git config --global user.email "Correo con el que firman"
```

### Agregar archivos 
Estos son los archivos que queremos que git les realice un seguimiento.
> Nota: Recomiendo crear un archivo .gitignore. Esto depende del framework/lenguaje/plataforma en el que estén trabajando. En google pueden encontrar muchos templates.

```sh 
git add <archivos> 

# Ejemplo 
git add main.py README.md imagen.jpg source/

# Ejemplo para agregar todos los archivos 
git add *
```

### Agregar un cambio 
Cuando queremos agregar un cambio, hacemos git commit 
```sh 
git commit <archivos> -m "mensaje explicativo del commit" 

# Commit a todos los archivos
git commit -a -m "pequeños cambios"  # +2190 -1203 
```

### Agregar un origen remoto 
Esto es util cuando queremos subir nuestro repositorio a Github. Para esto, creamos un repositorio de github vacío y hacemos el siguiente comando. 
```sh 
git remote add origin <link de git>

# Ejemplo para agregar un origen remoto a github y de una vez subir los cambios 
git remote add origin https://github.com/lVoidi/test.git

# Hace que la rama principal sea <main> para que coincida con github 
git branch -M main

# Pushea la rama main
git push -u origin main
```

