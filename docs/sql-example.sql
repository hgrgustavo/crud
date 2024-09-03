CREATE TABLE `client`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `cpf` TEXT NOT NULL,
    `birthdate` TEXT NOT NULL,
    `gender` TEXT NOT NULL,
    `city_id` BIGINT NOT NULL
);


ALTER TABLE
    `client` ADD INDEX `client_id_index`(`id`);
    
    
CREATE TABLE `city`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `state` TEXT NOT NULL,
    `cep` TEXT NOT NULL
);


CREATE TABLE `user`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `phone` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `username` TEXT NOT NULL,
    `password` TEXT NOT NULL
);


ALTER TABLE
    `client` ADD CONSTRAINT `client_city_id_foreign` FOREIGN KEY(`city_id`) REFERENCES `city`(`id`);
