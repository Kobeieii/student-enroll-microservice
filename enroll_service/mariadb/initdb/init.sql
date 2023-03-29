CREATE TABLE `enroll` (
    `id` int NOT NULL,
    `name` varchar(255) NOT NULL,
    `subjectid` varchar(255) DEFAULT NULL,
    `term` int NOT NULL,
    `year` int NOT NULL,
    PRIMARY KEY (`id`, `subjectid`, `term`, `year`)
)ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;