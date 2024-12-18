**Ejercicio 5: Torneos de ciclismo**


**Esquema de BD:**


`TORNEO<cod_torneo, nombre_torneo, cod_corredor, cod_bicicleta, marca_bicicleta, nyap_corredor, sponsor, DNI_presidente_sponsor, DNI_medico>`


**Restricciones:**


- El código del torneo es único y no se repite para diferentes torneos. Pero los nombres de los torneos pueden repetirse entre diferentes torneos (por ejemplo, el “Tour de Francia” se desarrolla todos los años y siempre lleva el mismo nombre).
- Un corredor corre varios torneos. Tiene un código único por torneo, pero en diferentes torneos tiene diferentes códigos.
- Cada corredor tiene varias bicicletas asignadas para un torneo.
- Los cod_bicicleta pueden cambiar en diferentes torneos, pero dentro de un torneo son únicos.
- Cada bicicleta tiene una sola marca.
- Cada corredor tiene varios sponsors en un torneo, y un sponsor puede representar a varios corredores.
- Cada sponsor tiene un único presidente y un único médico.


### Paso 1: Determinar las Dependencias Funcionales (DFs)


A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales:


1. **cod_torneo → nombre_torneo**: el nombre de un torneo puede repetirse en diferentes años, pero el código de torneo (`cod_torneo`) lo identifica de forma única.


2. **cod_torneo, cod_corredor → nyap_corredor**: Cada torneo tiene varios corredores y cada corredor puede participar en numerosos torneos, y si bien el nombre no cambia, si que puede repetirse, así que `nyap_corredor` depende de la combinación de `cod_torneo, cod_corredor`


3. **cod_bicicleta → marca_bicicleta**: cada bicicleta tiene un código único dentro de un torneo y este código identifica de manera única la marca de la bicicleta dentro de ese torneo. Pero los códigos de bicicletas pueden ser distintos entre torneos por eso se debe añadir `cod_torneo` para que haya dependencia.


4. **sponsor → DNI_presidente_sponsor, DNI_medico**: cada sponsor tiene un único presidente y un único médico asociado. Hace que `DNI_presidente_sponsor` y `DNI_medico` dependan de `sponsor`.


### Paso 2: Determinar las Claves Candidatas


La clave primaria debe identificar de manera única cada fila en la tabla `TORNEO`. Según las dependencias y restricciones:


- Cada combinación de `cod_torneo`, `cod_corredor`, `cod_bicicleta y `sponsor` identifica de manera única una fila.


Por lo tanto, la **clave candidata** es:


- (`cod_torneo`, `cod_corredor`, `cod_bicicleta`, `sponsor`)


### Paso 3: Diseño en Tercera Forma Normal (3FN)


Se dividió la tabla original en seis tablas (`NOMBRE_TORNEO`, `CORREDOR`, `BICICLETA`, `SPONSOR`, `CORREDOR_SPONSOR`, `TORNEO`) para eliminar dependencias transitivas y garantizar que cada atributo no clave dependa únicamente de la clave primaria completa.


1. **Tabla `NOMBRE_TORNEO`**
   - `cod_torneo` (Clave primaria)
   - `nombre_torneo`


2. **Tabla `CORREDOR`**
   - `cod_torneo` (Clave foránea que referencia a `TORNEO`)
   - `cod_corredor`
   - `nyap_corredor`
   - Clave primaria compuesta: (`cod_torneo`, `cod_corredor`)


3. **Tabla `BICICLETA`**
   - `cod_torneo` (Clave foránea que referencia a `TORNEO`)
   - `cod_corredor` (Clave foránea que referencia a `CORREDOR`)
   - `cod_bicicleta`
   - `marca_bicicleta`
   - Clave primaria compuesta: (`cod_torneo`, `cod_bicicleta`)


4. **Tabla `SPONSOR`**
   - `sponsor` (Clave primaria)
   - `DNI_presidente_sponsor`
   - `DNI_medico`


5. **Tabla `CORREDOR_SPONSOR`**
   - `cod_torneo` (Clave foránea que referencia a `TORNEO`)
   - `cod_corredor` (Clave foránea que referencia a `CORREDOR`)
   - `sponsor` (Clave foránea que referencia a `SPONSOR`)
   - Clave primaria compuesta: (`cod_torneo`, `cod_corredor`, `sponsor`)


6. **Tabla `TORNEO`**
   - `cod_torneo` (Clave foránea que referencia a `TORNEO`)
   - `cod_corredor` (Clave foránea que referencia a `CORREDOR`)
   - `cod_bicicleta` (Clave foránea que referencia a `BICICLETA`)
   - `sponsor` (Clave foránea que referencia a `SPONSOR`)
   - Clave primaria compuesta: (`cod_torneo`, `cod_corredor`, `cod_bicicleta`, `sponsor`)
