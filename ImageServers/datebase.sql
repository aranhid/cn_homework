CREATE DATABASE `images_servers`;

USE `images_servers`;

CREATE TABLE `images` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `file` VARCHAR(255) NOT NULL,
    `server` VARCHAR(255) NOT NULL,
    PRIMARY KEY `id` (`id`)
);

INSERT INTO `images` 
    (`file`, `server`) 
VALUES
    ('image1.jpg', 'imageserver1'),
    ('image2.jpg', 'imageserver2'),
    ('image3.jpg', 'imageserver3');