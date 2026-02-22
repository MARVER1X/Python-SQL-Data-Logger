-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.4.3 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for calculator_db
CREATE DATABASE IF NOT EXISTS `calculator_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `calculator_db`;


-- This ensures the old tables are cleared out
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS users;

-- Dumping structure for table calculator_db.logs
CREATE TABLE IF NOT EXISTS `logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `calculation` text,
  `result` text,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table calculator_db.logs: ~4 rows (approximately)
INSERT INTO `logs` (`log_id`, `user_id`, `calculation`, `result`, `timestamp`) VALUES
	(1, 1, '10.5 + 5.5', '16.0', '2026-02-19 00:32:26'),
	(2, 1, '90.0 sin', '1.0', '2026-02-19 00:33:19'),
	(3, 1, 'Expression: (10 + 5) * 2', '30', '2026-02-19 00:34:02'),
	(4, 1, '70.0 cos', '0.3420201433256688', '2026-02-19 01:37:59');

-- Dumping structure for table calculator_db.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- =========================================================================
-- SECURITY NOTE FOR REVIEWERS: 
-- Passwords below are stored in plain text strictly for local testing 
-- and portfolio demonstration purposes so reviewers can easily log in. 
-- In a production CI/CD pipeline, these would be securely hashed 
-- (e.g., bcrypt / SHA-256) prior to database insertion.
-- =========================================================================

-- Dumping data for table calculator_db.users: ~0 rows (approximately)
INSERT INTO `users` (`user_id`, `username`, `password`) VALUES
	(1, 'admin', 'pass123'),
	(2, 'user', 'pass345');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

