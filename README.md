### Pasos a seguir
1. Solicitar creación de PostgreSQL en Compartiloh
2. Conectarse a la base de datos
3. Crear tabla 

````
CREATE TABLE IF NOT EXISTS ping_timestamps (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
````
4. Solicitar ejecución de Servidor WEB con la url https://github.com/compartiLOH/usecase-ws-and-db
5. Agregar variables de entorno según valores otorgados por el sistema y configurados por el usuario
- DB_HOST=host-compartiloh
- DB_PORT=puerto-compartiloh
- DB_USER=user-bdd
- DB_PASSWORD=pwd-bdd
- DB_NAME="postgres"
