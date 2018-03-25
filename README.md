# PruebaRetoGlobal
Este repositorio está enfocado a la prueba del framework PyTest realizando algunos test básicos sobre el endpoint https://api.github.com/orgs/pytest-dev

Estos test se han enfocado solo para el endpoint indicado, por lo tanto la estructura del JSON deseada está almacenada en un fichero de texto con todos los campos que deberían de aparecer en el JSON(JSONstructure.txt), almacenado en el directorio prog. 
Esto es debido a que si se quiere cambiar a la estructura de usuario solo se debería de actualizar dicho fichero con los campos correspondientes

## Como correr los test
Una vez instalado PyTest y el paquete pytest-html para poder obtener el test report en html ya se puede proceder a ejecutar el test.

Para ejecutarlo hay que abrir una terminal y situarte en el directorio en el que están todos los test almacenados, en este caso es en el paquete test.

Para poder ejecutar el test se debe escribir el siguiente comando:

pytest --html=report.hmtl --self-contained-html

or

python -m pytest --html=report.hmtl --self-contained-html

Una vez ejecutado alguno de los comandos anteriores, se ejecutarán los test, se generará automáticamente el test report en html y se guardará en el mismo directorio
en el que se ha lanzado la ejecución del/los test(s)
