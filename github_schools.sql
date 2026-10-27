CREATE DATABASE IF NOT EXISTS github_schools;
USE github_schools;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    civilite VARCHAR(20) NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    nationalite VARCHAR(100) NOT NULL,
    adresse TEXT NOT NULL,
    code_postal VARCHAR(20) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    pays VARCHAR(100) NOT NULL,
    telephone VARCHAR(30) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    niveau_profil VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);