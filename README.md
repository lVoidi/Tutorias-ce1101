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

# Retrospectiva
Como persona que pasó este curso, quiero dar mi opinión al respecto. Desde que yo entré a la universidad, como 
persona que lleva en este mundo desde 2019, yo me temía algo que me llevaban diciendo desde hace rato. "La programación
es el campo que peor se enseña en las universidades". Siempre veia personas en foros, videos de youtube, etc, diciendo 
que los videos o los foros les habían enseñado lo que los profesores de la universidad nunca les había enseñado. Yo pensaba
que era una simple broma de internet. Cuando entré a la universidad, me encontré con la verdad: todo eso es real. 
La programación, en cualquier carrera que he visto, se enseña de manera pésima. Desde orden inadecuado de los temas 
hasta exámenes de programación en papel. Empezaré abordando cada uno de estos problemas.

## Orden inadecuado de los temas 
Cuando una persona aprende a abordar un problema que ocupa repeticiones (como por ejemplo, recorrer una lista), lo primero 
a lo que se recurre es a iteración. La iteración es lenguaje natural, es algo que hemos abordado toda la vida sin que 
nos demos cuenta (e.j, contar cuántas personas hay en la fila del banco). Sin embargo, la iteración se aborda de los 
últimos temas del curso. En cambio, el curso decidió empezar con recursividad. Por si fuera poco, los proyectos también 
tienen sus problemas.  

## Problema de la recursividad
La recursividad, inicialmente, cuenta con muchos muchos problemas:

1. La recursividad es mala. Simplemente es mala, en Python aún más (por algo te tira RecursionError). Esto no significa que sea inutil, esta misma se aplica para resolver problemas de programación dinámica 
2. Es ineficiente. 
3. Es mucho más difícil de entender que un simple bucle 

Yo siempre me pregunté: ¿Por qué?  
Se lo conté a mis amigos programadores de internet, me dijeron: ¿Por qué?  
Se lo conté a mi perro y el mismisimo perro me dijo: ¿Por qué?  

No tiene lógica. En CE, deberían observar esto detalladamente, analizar por qué tantas personas se quedan en el curso
e intercambiar iteración y recursividad. Mi cambio sería ese, y aquí cuento las razones: 
1. Es intuitivo. Las personas ya saben lo que es una repetición 
2. Es aditivo. Las personas suelen matricular este curso junto con matemáticas discretas. En MD se ve recursividad para el segundo examen. Por ende, ver recursividad después de verlo en MD facilitaría mucho el proceso. Además, recursividad si se aplica en cursos posteriores y siempre se aplica en programación, no digo que lo quiten, ver recursividad está perfecto, simplemente que lo intercambien con iteración.

**NOTA:** Para estos dos cursos, y Datos 1, pueden conseguirse el libro de Discrete Mathematics with Applications de Susanna S. Epp. Yo personalmente utilicé la cuarta edición e incluso desarrollé ejercicios basandome en ejercicios del libro. Bonito para los amantes de las Matemáticas Discretas como yo.

## Problema de los proyectos
Los proyectos también son contra intuitivos. Como mencioné en la tabla de contenidos, después de ver recursividad y tkinter,se aplica un proyecto de un juego, utilizando recursividad. Si, recursividad con tkinter y en un juego.  

Estas dos cosas no tienen sentido. Primero que todo, un juego es la mejor manera de aplicar POO en su máximo esplendor, 
un juego es POO pura, sin embargo, decieron aplicar el juego de primeras, para cortar la mayor cantidad de estudiantes posibles. Segundo, Tkinter es una herramienta que se complementa extremadamente bien con POO.  
Por no decir que tener más de 30 o 40 variables globales para hacer un juego decente no es algo... eficiente.  

En el caso de IS 2024, que fue el que cursé yo, el primer proyecto fue un bomberman recursivo y el segundo proyecto 
fue un paint con pixel art. En este caso, el paint se podía hacer perfectamente con recursividad, y bueno, el bomberman sería mucho mucho mejor haciendolo con recursividad y las iteraciones que se quisieran.

## Problema de los examenes en hojas (y los examenes de programación en general)
La programación es un campo más práctico teórico.
El buen **programador** no es el que sabe cómo hacer un árbol binario, sino el que sabe cómo desarrollarlo, implementarlo
y aplicarlo. Los exámenes de programación no tienen sentido. Yo personalmente quitaría las evaluaciones de exámenes y lo 
distribuiría en más proyectos. Un programador aprende haciendo proyectos grandes que expriman toda su capacidad de 
razonamiento lógico. 
