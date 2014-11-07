Diseño modular dirigido por pruebas
===================================
![pycones2014 Zaragoza](http://2014.es.pycon.org/static/img/pycones2014.svg) 
![pyladies spain](https://pbs.twimg.com/profile_images/523981704998842369/Oy3DVPVr_400x400.png)

Restricciones
-------------

* Haz lo más simple que pueda funcionar
* Escribe el mejor código que puedas
* No hagas más de lo que pide la funcionalidad
* No introduzcas infraestructura si la funcionalidad no lo pide explícitamente
* No dependas de librerías si la funcionalidad no lo pide explícitamente

Flujo
-----
* Evalua el impacto de cada funcionalidad
* Realiza los cambios que necesites para que la funcionalidad sea facil de introducir
* Introduce la funcionalidad

Documentación herramientas testing
----------------------------------

* [Mamba](http://nestorsalceda.github.io/mamba/#overview)
* [Expects](http://expects.readthedocs.org/en/v0.5.0/matchers.html)
* [Doublex](http://python-doublex.readthedocs.org/en/latest/)
* [Doublex-Expects](https://github.com/jaimegildesagredo/doublex-expects#matchers)

Iteración I: 10 minutos
-----------------------

Un usuario puede registrarse con un nombre de usuario.

Por ejemplo: @foolano

Si otra persona se ha registrado usando ese mismo nombre de usuario se produce
un error.


Iteración II: 20 minutos
------------------------

Un usuario puede seguir a otros usuarios.

Para hacerlo basta con conocer el nickname del usuario al que se quiere seguir.

Cualquiera debe poder consultar a quien sigue un determinado usuario conociendo
su nickname.


Iteración III: 20 minutos
-------------------------

Los registros de usuarios así como las listas de usuarios seguidos deben
almacenarse de forma durable

Más restricciones:
------------------

* Situar el código escrito hasta ahora dentro de un paquete llamado "core"
* Usar el código escrito hasta ahora como si fuese una librería externa
* El código de esta iteración debe estar en un paquete diferente
* Ese paquete puede tener *una única dependencia* del "core"

Iteración IV: 30 minutos
------------------------

Crear un mecanismo de entrega HTTP que permita acceder a la funcionalidad
desarrollada hasta ahora.

Iteración V: 20 minutos
-----------------------

Un usuario puede publicar "cós"

El resto de usuarios deben poder consultar todos los "cós" que un usuario con un
determinado "nickname" ha escrito

Iteración IV: 40 minutos
------------------------

Poner esta nueva funcionalidad disponible en el mecanismo de entrega.

Garantizar la durabilidad de los datos.
