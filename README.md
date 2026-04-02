----------------------------------------------------------------------------
|                 Cdogios para QR Dinamico y Qr Estatico.                  |
----------------------------------------------------------------------------

Qr Dinamico:
Incluye 2 versiones probadas de forma LOCAL (Tradicional y Hibrida), la forma
traicional esta conectada a una base de datos local + Xampp, y la version
hibrida esta conectada a una Api Key (TinyUrl).

v1A: Versión Tradicional
Esta version fue pensada y diseñada para simular un "servidor real", donde
el codigo QR estuviese enlazado y en dado caso si el servidor se apaga, el 
qr dejaria de funcionar. [Requiere que este en linea].

v1B: Version Hibrida
Funciona gracias a una API Key (TinyURL) y una base de datos local, donde el
codigo se conecta con la API para actualizar el estado del QR, como podria ser
modificar la información de a donde redirige o eliminar el codigo qr.
--> Esta versión permite que el codigo exista sin la necesidad de estar siempre 
conectado con el servidor, por lo que si no se necesita modificar, actuara como
QR Estatico.

Qr Estatico:
Misma version que la v01, sin cambios en su funcionalidad. Es la opción "practica"
y segura para generar codigos QR Permanentes o que rara vez vayan a ser editados.

------------------------

Version de Prueba - Puede contener Errores | 02/04/2026

By: Vicente Aguilar
