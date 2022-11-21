Escriba un programa que implemente el registro de nuevas obras de arte para el Museo del Louvre, en París, Francia.

 

En la Base de Datos se registrará la siguiente información para cada Pintura:

 

Cota: Código que representa cada una de las pinturas registradas en la Galería, conformada por 4 letras y 4 dígitos (Ejemplo de una Cota: ABCD1234). Cada pintura tiene un código único.

 

Nombre: Nombre de la pintura de máximo 30 caracteres. No puede haber varias obras registradas con el mismo nombre.

 

Precio: Estimación del valor de la obra. Expresada como una cantidad numérica real. No podrá ser negativa.


 

Status: Estado actual de la pintura dentro de la galería. Puede ser uno de 2 valores: "EN EXHIBICIÓN" o "EN MANTENIMIENTO".

 

Su registro de Pinturas debe de permitir las siguientes operaciones:

 

I Inserción de una nueva pintura a la Base de Datos: 

Deberá validar que se cumplan las condiciones mencionadas anteriormente para cada campo introducido.


II Consulta de una pintura: 

 

Se debe poder buscar una pintura por:

Cota. Utilizando un índice para ello.
Nombre. Utilizando un índice para ello.
 

III Puesta en Mantenimiento:

 

Se debe poder colocar una pintura a un estado de "EN MANTENIMIENTO". Para indicar la pintura a pasar a este estado, se debe permitir buscarla tanto por su Cota como por su Nombre.

 

IV Puesta en Exhibición:

 

Se debe poder colocar una pintura a un estado de "EN EXHIBICIÓN". Para indicar la pintura a pasar a este estado, se debe permitir buscarla tanto por su Cota como por su Nombre.

 

V Eliminación:

 

Se debe poder eliminar una pintura del sistema. (Debe ser eliminación lógica).

 

VI Compactador:

 

Debe existir una funcionalidad que permita eliminar físicamente las pinturas eliminadas lógicamente. Actualizando los índices correspondientes

 

Plataforma: Python utilizando vectores en memoria. No obstante, los datos deben poder grabarse en disco duro al finalizar la ejecución del programa en un archivo de texto, adicionalmente se deben leer desde disco los últimos datos guardados cuando el programa inicie. Para la defensa debe haber al menos 10 pinturas cargadas en el sistema.


Lapso: Deben entregar el programa fuente el día 30 de noviembre. La defensa será realizada el mismo día en el horario de 1:00 a 3:45.

 