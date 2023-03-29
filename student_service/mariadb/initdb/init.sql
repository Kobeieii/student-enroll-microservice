CREATE TABLE `students` (
    `id` int NOT NULL,
    `firstname` varchar(50) NOT NULL,
    `lastname` varchar(50) DEFAULT NULL,
    `email` varchar(50) NOT NULL,
    PRIMARY KEY (`id`)
)ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `students` ADD PRIMARY KEY (`id`);
ALTER TABLE `students` MODIFY COLUMN id INT auto_increment;