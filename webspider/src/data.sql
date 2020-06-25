/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : data

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-06-25 17:54:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for salaries
-- ----------------------------
DROP TABLE IF EXISTS `salaries`;
CREATE TABLE `salaries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `salary` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of salaries
-- ----------------------------

-- ----------------------------
-- Table structure for urls
-- ----------------------------
DROP TABLE IF EXISTS `urls`;
CREATE TABLE `urls` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of urls
-- ----------------------------
INSERT INTO `urls` VALUES ('1', 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=');
INSERT INTO `urls` VALUES ('2', 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=');
INSERT INTO `urls` VALUES ('3', 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,3.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=');
