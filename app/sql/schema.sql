CREATE DATABASE IF NOT EXISTS week_14_exam;

USE week_14_exam;

CREATE TABLE IF NOT EXISTS weapons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weapon_id VARCHAR(100),
    weapon_name VARCHAR(100),
    weapon_type VARCHAR(100),
    range_km INT,
    weight_kg FLOAT,
    manufacturer VARCHAR(100),
    origin_country VARCHAR(100),
    storage_location VARCHAR(100),
    year_estimated INT,
    level_risk VARCHAR(100)
);