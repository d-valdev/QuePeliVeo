# QuePeliVeo
![qpv-preview](https://github.com/user-attachments/assets/1a2987b5-6b7c-415b-8c9d-e0f5cf1c48fd)

Puedes ver el progreso de esta aplicación desplegada en https://www.quepeliveo.es

## Índice de contenidos

- [Introducción](#Introducción)
- [Tecnologías](#Tecnologías)
- [Como utilizarla](#Como-utilizarla)
- [Funcionamiento](#Funcionamiento)
- [Despliegue](#Despliegue)
- [Próximamente](#Próximamente)

## Introducción.

Bienvenidos a este proyecto personal de desarollo FullStack. En el, desarollamos una aplicación web destinada a generar recomendaciones sobre películas en base a peticiones en lenguaje natural. A lo largo de este documento se tratará de explicar su naturaleza, utilización y funcionamiento.

## Tecnologías

Se emplearán las siguientes tecnologías:

*Frontend*
- HTML
- CSS
- JS
- Bootstrap

*Backend*
- Python
- Libreria flask

*Servidor*
- Nginx
- Ubuntu
- Docker

## Como utilizarla

Su uso es simple: en la pantalla principal tan solo debemos seleccionar cuantas recomendaciones deseamos. A la derecha, escribiremos la petición en lenguaje natural. Por ejemplo: 2 opciones con "De miedo ganadoras de Óscar" o "Para ver con tu pareja" (o tu perro).

![example_search](https://github.com/user-attachments/assets/ff9b1c8e-09d3-4cbe-8991-8ed9c7a209ff)


Esto, nos genera tantas tarjetas como recomendaciones hayamos seleccionado. Las tarjetas contendrán datos como título, año de lanzamiento, cartel original o enlace a su página de IMDb.

![example_result](https://github.com/user-attachments/assets/8c732be8-5058-4438-8688-5ba3dc06f4c5)

## Funcionamiento

El funcionamiento está basado en la utilización de APIs propias y de terceros. 
1. El frontend realiza la petición a nuestra API propia desarollada en _app.py_ a través del puerto establecido (5000 en nuestro caso).
2. Nuestra API se comunica con la API externa mediante la lógica implementada en _recomendador.py_ y realiza peticiones a una IA (gemma-2b-it de HF) encargada de devolver las recomendaciones en formato JSON.
3. Los datos son enviados a _buscador.py_, encargado de buscar la información de estas películas en otra API externa (TMDb).
4. Para ambos casos, es necesario el uso de autenticación mediante token.
5. Una vez obtenidos los datos, estos son extraidos, transformados y manipulados con nuestra API propia desarrollada en _app.py_. Aquí se les da una forma deseable y estructurada, eliminando gran cantidad de parámettros innecesarios.
6. Los datos son enviados al frontend a través del puerto establecido.

## Despliegue

Esta aplicación está actualmente desplegada en https://www.quepeliveo.es. Actualmente, se encuentra en fase de desarrollo por lo que muchas de las funcionalidades no están implementadas, pero puedes divertirte utilizando el recomendador de peliculas sin ningun problema! :)

## Próximamente

En estos momentos se está trabajando para implementar un sistema de usuarios en el que se pueda llevar un registro personal de películas vistas, listas personalizadas, etc... estate atento para más! 🔥

