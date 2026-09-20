CREATE DATABASE IF NOT EXISTS hotel_duerme_bien;
USE hotel_duerme_bien;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol ENUM('administrador', 'encargado') NOT NULL
);

CREATE TABLE habitaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_habitacion INT UNIQUE NOT NULL,
    capacidad INT NOT NULL,
    orientacion VARCHAR(50) NOT NULL,
    estado ENUM('disponible', 'ocupada', 'mantenimiento') DEFAULT 'disponible'
);

CREATE TABLE huespedes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    run VARCHAR(20) UNIQUE NOT NULL,
    nombre_completo VARCHAR(150) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE asignaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    habitacion_id INT NOT NULL,
    pasajero_responsable_id INT NOT NULL,
    fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    costo_total DECIMAL(10, 2) NOT NULL, 
    FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id),
    FOREIGN KEY (pasajero_responsable_id) REFERENCES pasajeros(id)
);