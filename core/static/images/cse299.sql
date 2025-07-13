-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2025 at 07:56 AM
-- Server version: 11.7.2-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cse299`
--

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `payment_method` enum('bkash') NOT NULL,
  `payment_status` enum('pending','completed','failed') NOT NULL DEFAULT 'pending',
  `paid_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_id`, `user_id`, `transaction_id`, `amount`, `payment_method`, `payment_status`, `paid_at`) VALUES
(1, 1, 'PAY-AMINA-001', 15.00, 'bkash', 'completed', '2025-07-07 05:44:02'),
(2, 2, 'PAY-RAFI-001', 15.00, 'bkash', 'completed', '2025-06-02 05:44:02'),
(3, 3, 'PAY-NABILA-001', 15.00, 'bkash', 'failed', '2025-07-11 05:44:02');

-- --------------------------------------------------------

--
-- Table structure for table `photouploads`
--

CREATE TABLE `photouploads` (
  `upload_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `image_url` varchar(2048) NOT NULL,
  `detection_result` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`detection_result`)),
  `uploaded_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `photouploads`
--

INSERT INTO `photouploads` (`upload_id`, `user_id`, `image_url`, `detection_result`, `uploaded_at`) VALUES
(1, 1, 'https://example.com/uploads/amina_acne1.jpg', '{\"disease\": \"acne\", \"confidence\": 0.88}', '2025-07-12 05:44:02'),
(2, 1, 'https://example.com/uploads/amina_clear.jpg', '{\"disease\": \"none\", \"confidence\": 0.97}', '2025-07-12 05:44:02'),
(3, 2, 'https://example.com/uploads/rafi_melanoma.jpg', '{\"disease\": \"melanoma\", \"confidence\": 0.93}', '2025-07-12 05:44:02'),
(4, 3, 'https://example.com/uploads/nabila_rosacea.jpg', '{\"disease\": \"rosacea\", \"confidence\": 0.81}', '2025-07-12 05:44:02');

-- --------------------------------------------------------

--
-- Table structure for table `subscriptions`
--

CREATE TABLE `subscriptions` (
  `subscription_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `start_date` timestamp NOT NULL,
  `end_date` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subscriptions`
--

INSERT INTO `subscriptions` (`subscription_id`, `user_id`, `start_date`, `end_date`) VALUES
(1, 1, '2025-07-07 05:44:02', '2025-08-06 05:44:02'),
(2, 2, '2025-06-02 05:44:02', '2025-07-07 05:44:02');

-- --------------------------------------------------------

--
-- Stand-in structure for view `subscriptionstatus`
-- (See below for the actual view)
--
CREATE TABLE `subscriptionstatus` (
`subscription_id` int(11)
,`user_id` int(11)
,`start_date` timestamp
,`end_date` timestamp
,`is_active` int(1)
);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password_hash`, `phone_number`, `created_at`, `updated_at`) VALUES
(1, 'Amina Rahman', 'amina@example.com', 'hashed_pwd_amina', '01711111111', '2025-07-12 05:44:02', '2025-07-12 05:44:02'),
(2, 'Rafiul Islam', 'rafi@example.com', 'hashed_pwd_rafi', '01722222222', '2025-07-12 05:44:02', '2025-07-12 05:44:02'),
(3, 'Nabila Chowdhury', 'nabila@example.com', 'hashed_pwd_nabila', '01733333333', '2025-07-12 05:44:02', '2025-07-12 05:44:02');

-- --------------------------------------------------------

--
-- Structure for view `subscriptionstatus`
--
DROP TABLE IF EXISTS `subscriptionstatus`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `subscriptionstatus`  AS SELECT `s`.`subscription_id` AS `subscription_id`, `s`.`user_id` AS `user_id`, `s`.`start_date` AS `start_date`, `s`.`end_date` AS `end_date`, current_timestamp() between `s`.`start_date` and `s`.`end_date` AS `is_active` FROM `subscriptions` AS `s` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`),
  ADD UNIQUE KEY `transaction_id` (`transaction_id`),
  ADD KEY `idx_user_id_payments` (`user_id`);

--
-- Indexes for table `photouploads`
--
ALTER TABLE `photouploads`
  ADD PRIMARY KEY (`upload_id`),
  ADD KEY `idx_user_id_photouploads` (`user_id`);

--
-- Indexes for table `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD PRIMARY KEY (`subscription_id`),
  ADD KEY `idx_user_id_subscriptions` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `photouploads`
--
ALTER TABLE `photouploads`
  MODIFY `upload_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `subscriptions`
--
ALTER TABLE `subscriptions`
  MODIFY `subscription_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `photouploads`
--
ALTER TABLE `photouploads`
  ADD CONSTRAINT `photouploads_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD CONSTRAINT `subscriptions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
