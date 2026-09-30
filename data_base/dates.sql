CREATE DATABASE IF NOT EXISTS hotel_duerme_bien
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hotel_duerme_bien;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- almacena el hash bcrypt (60 caracteres), nunca texto plano
    rol ENUM('administrador', 'encargado') NOT NULL
);

CREATE TABLE IF NOT EXISTS habitaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_habitacion INT UNIQUE NOT NULL,
    capacidad INT NOT NULL,
    orientacion VARCHAR(50),
    estado ENUM('disponible', 'ocupada', 'mantenimiento') DEFAULT 'disponible'
);

CREATE TABLE IF NOT EXISTS huespedes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    rut VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS asignaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    habitacion_id INT NOT NULL,
    huesped_id INT NOT NULL,
    costo_total DECIMAL(10,2) DEFAULT 20000.00,
    CONSTRAINT fk_asignacion_habitacion
        FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id),
    CONSTRAINT fk_asignacion_huesped
        FOREIGN KEY (huesped_id) REFERENCES huespedes(id)
);