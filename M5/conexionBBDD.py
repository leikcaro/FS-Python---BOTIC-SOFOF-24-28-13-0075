#pip install mysql-connector-python

import mysql.connector

# 1. Conexión a MySQL (ajusta usuario/clave/BD según tu entorno)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",   # 👈 tu clave aquí
    database="demo_db"
)

cursor = conn.cursor()

# 2. Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    full_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
""")

# 3. CREATE - Insertar datos (parametrizado, evita SQL Injection)
cursor.execute("INSERT INTO users (email, full_name) VALUES (%s, %s)", 
               ("aadita@gmail.com", "Aada Lovelaces"))
conn.commit()

# 4. READ - Consultar datos
cursor.execute("SELECT id, email, full_name, created_at FROM users")
for row in cursor.fetchall():
    print(row)

# 5. UPDATE - Actualizar un registro
cursor.execute("UPDATE users SET full_name = %s WHERE email = %s", 
               ("Augusta Ada King (Lovelace)", "ada.lovelace@example.com"))
conn.commit()

# 6. DELETE - Eliminar un registro
cursor.execute("DELETE FROM users WHERE email = %s", 
               ("ada.lovelace@example.com",))
conn.commit()

# 7. Cerrar conexión
cursor.close()
conn.close()