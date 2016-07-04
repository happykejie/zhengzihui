-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2016 at 07:42 AM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zhengzihui_test_second`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add source', 1, 'add_source'),
(2, 'Can change source', 1, 'change_source'),
(3, 'Can delete source', 1, 'delete_source'),
(4, 'Can add thumbnail', 2, 'add_thumbnail'),
(5, 'Can change thumbnail', 2, 'change_thumbnail'),
(6, 'Can delete thumbnail', 2, 'delete_thumbnail'),
(7, 'Can add thumbnail dimensions', 3, 'add_thumbnaildimensions'),
(8, 'Can change thumbnail dimensions', 3, 'change_thumbnaildimensions'),
(9, 'Can delete thumbnail dimensions', 3, 'delete_thumbnaildimensions'),
(10, 'Can add log entry', 4, 'add_logentry'),
(11, 'Can change log entry', 4, 'change_logentry'),
(12, 'Can delete log entry', 4, 'delete_logentry'),
(13, 'Can add permission', 5, 'add_permission'),
(14, 'Can change permission', 5, 'change_permission'),
(15, 'Can delete permission', 5, 'delete_permission'),
(16, 'Can add group', 6, 'add_group'),
(17, 'Can change group', 6, 'change_group'),
(18, 'Can delete group', 6, 'delete_group'),
(19, 'Can add user', 7, 'add_user'),
(20, 'Can change user', 7, 'change_user'),
(21, 'Can delete user', 7, 'delete_user'),
(22, 'Can add content type', 8, 'add_contenttype'),
(23, 'Can change content type', 8, 'change_contenttype'),
(24, 'Can delete content type', 8, 'delete_contenttype'),
(25, 'Can add session', 9, 'add_session'),
(26, 'Can change session', 9, 'change_session'),
(27, 'Can delete session', 9, 'delete_session'),
(28, 'Can add tb_user', 10, 'add_tb_user'),
(29, 'Can change tb_user', 10, 'change_tb_user'),
(30, 'Can delete tb_user', 10, 'delete_tb_user'),
(31, 'Can add tb_user_expand', 11, 'add_tb_user_expand'),
(32, 'Can change tb_user_expand', 11, 'change_tb_user_expand'),
(33, 'Can delete tb_user_expand', 11, 'delete_tb_user_expand'),
(34, 'Can add tb_service_provider', 12, 'add_tb_service_provider'),
(35, 'Can change tb_service_provider', 12, 'change_tb_service_provider'),
(36, 'Can delete tb_service_provider', 12, 'delete_tb_service_provider'),
(37, 'Can add tb_ news_ class', 13, 'add_tb_news_class'),
(38, 'Can change tb_ news_ class', 13, 'change_tb_news_class'),
(39, 'Can delete tb_ news_ class', 13, 'delete_tb_news_class'),
(40, 'Can add tb_ news', 14, 'add_tb_news'),
(41, 'Can change tb_ news', 14, 'change_tb_news'),
(42, 'Can delete tb_ news', 14, 'delete_tb_news'),
(43, 'Can add tb_ notice', 15, 'add_tb_notice'),
(44, 'Can change tb_ notice', 15, 'change_tb_notice'),
(45, 'Can delete tb_ notice', 15, 'delete_tb_notice'),
(46, 'Can add tb_ notice_ class', 16, 'add_tb_notice_class'),
(47, 'Can change tb_ notice_ class', 16, 'change_tb_notice_class'),
(48, 'Can delete tb_ notice_ class', 16, 'delete_tb_notice_class'),
(49, 'Can add tb_ apage', 17, 'add_tb_apage'),
(50, 'Can change tb_ apage', 17, 'change_tb_apage'),
(51, 'Can delete tb_ apage', 17, 'delete_tb_apage'),
(52, 'Can add tb_ apage_ class', 18, 'add_tb_apage_class'),
(53, 'Can change tb_ apage_ class', 18, 'change_tb_apage_class'),
(54, 'Can delete tb_ apage_ class', 18, 'delete_tb_apage_class'),
(55, 'Can add tb_item', 19, 'add_tb_item'),
(56, 'Can change tb_item', 19, 'change_tb_item'),
(57, 'Can delete tb_item', 19, 'delete_tb_item'),
(58, 'Can add tb_item_click', 20, 'add_tb_item_click'),
(59, 'Can change tb_item_click', 20, 'change_tb_item_click'),
(60, 'Can delete tb_item_click', 20, 'delete_tb_item_click'),
(61, 'Can add tb_item_class', 21, 'add_tb_item_class'),
(62, 'Can change tb_item_class', 21, 'change_tb_item_class'),
(63, 'Can delete tb_item_class', 21, 'delete_tb_item_class'),
(64, 'Can add tb_item_pa', 22, 'add_tb_item_pa'),
(65, 'Can change tb_item_pa', 22, 'change_tb_item_pa'),
(66, 'Can delete tb_item_pa', 22, 'delete_tb_item_pa'),
(67, 'Can add tb_article', 23, 'add_tb_article'),
(68, 'Can change tb_article', 23, 'change_tb_article'),
(69, 'Can delete tb_article', 23, 'delete_tb_article'),
(70, 'Can add tb_album', 24, 'add_tb_album'),
(71, 'Can change tb_album', 24, 'change_tb_album'),
(72, 'Can delete tb_album', 24, 'delete_tb_album'),
(73, 'Can add tb_pic', 25, 'add_tb_pic'),
(74, 'Can change tb_pic', 25, 'change_tb_pic'),
(75, 'Can delete tb_pic', 25, 'delete_tb_pic'),
(76, 'Can add tb_accessory', 26, 'add_tb_accessory'),
(77, 'Can change tb_accessory', 26, 'change_tb_accessory'),
(78, 'Can delete tb_accessory', 26, 'delete_tb_accessory'),
(79, 'Can add tb_ artificial_ representations', 27, 'add_tb_artificial_representations'),
(80, 'Can change tb_ artificial_ representations', 27, 'change_tb_artificial_representations'),
(81, 'Can delete tb_ artificial_ representations', 27, 'delete_tb_artificial_representations'),
(82, 'Can add tb_ message', 28, 'add_tb_message'),
(83, 'Can change tb_ message', 28, 'change_tb_message'),
(84, 'Can delete tb_ message', 28, 'delete_tb_message'),
(85, 'Can add tb_ message text', 29, 'add_tb_messagetext'),
(86, 'Can change tb_ message text', 29, 'change_tb_messagetext'),
(87, 'Can delete tb_ message text', 29, 'delete_tb_messagetext'),
(88, 'Can add tb_ sys message', 30, 'add_tb_sysmessage'),
(89, 'Can change tb_ sys message', 30, 'change_tb_sysmessage'),
(90, 'Can delete tb_ sys message', 30, 'delete_tb_sysmessage'),
(91, 'Can add tb_goods', 31, 'add_tb_goods'),
(92, 'Can change tb_goods', 31, 'change_tb_goods'),
(93, 'Can delete tb_goods', 31, 'delete_tb_goods'),
(94, 'Can add tb_goods_click', 32, 'add_tb_goods_click'),
(95, 'Can change tb_goods_click', 32, 'change_tb_goods_click'),
(96, 'Can delete tb_goods_click', 32, 'delete_tb_goods_click'),
(97, 'Can add tb_goods_class', 33, 'add_tb_goods_class'),
(98, 'Can change tb_goods_class', 33, 'change_tb_goods_class'),
(99, 'Can delete tb_goods_class', 33, 'delete_tb_goods_class'),
(100, 'Can add tb_goods_evaluation', 34, 'add_tb_goods_evaluation'),
(101, 'Can change tb_goods_evaluation', 34, 'change_tb_goods_evaluation'),
(102, 'Can delete tb_goods_evaluation', 34, 'delete_tb_goods_evaluation'),
(103, 'Can add tb_order', 35, 'add_tb_order'),
(104, 'Can change tb_order', 35, 'change_tb_order'),
(105, 'Can delete tb_order', 35, 'delete_tb_order'),
(106, 'Can add tb_area', 36, 'add_tb_area'),
(107, 'Can change tb_area', 36, 'change_tb_area'),
(108, 'Can delete tb_area', 36, 'delete_tb_area');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$20000$gfG4zfThkngp$zh2ENS/JoUtJqeZ/ejvU0iosw9WGbTt9Y4RuhDuhpPg=', '2016-05-26 12:38:31', 1, 'zhangshuaishuai', '', '', '2468435837@qq.com', 1, 1, '2016-05-01 04:29:36');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2016-05-01 04:31:41', '1', '1@qq', 1, '', 10, 1),
(2, '2016-05-01 04:31:59', '2', '2', 1, '', 10, 1),
(3, '2016-05-01 04:32:25', '3', '3', 1, '', 10, 1),
(4, '2016-05-01 04:34:16', '1', '1', 1, '', 11, 1),
(5, '2016-05-01 04:34:36', '2', '2', 1, '', 11, 1),
(6, '2016-05-01 04:34:58', '3', '3', 1, '', 11, 1),
(7, '2016-05-01 04:35:31', '1', '1', 1, '', 19, 1),
(8, '2016-05-01 04:35:50', '2', '2', 1, '', 19, 1),
(9, '2016-05-01 04:36:33', '3', '3', 1, '', 19, 1),
(10, '2016-05-01 04:36:53', '4', '4', 1, '', 19, 1),
(11, '2016-05-01 04:37:15', '5', '5', 1, '', 19, 1),
(12, '2016-05-01 04:37:31', '1', '1', 1, '', 20, 1),
(13, '2016-05-01 04:37:40', '2', '2', 1, '', 20, 1),
(14, '2016-05-01 04:37:48', '3', '3', 1, '', 20, 1),
(15, '2016-05-01 04:37:57', '4', '4', 1, '', 20, 1),
(16, '2016-05-01 04:38:07', '5', '5', 1, '', 20, 1),
(17, '2016-05-01 04:38:30', '1', '1', 1, '', 24, 1),
(18, '2016-05-01 04:38:39', '2', '2', 1, '', 24, 1),
(19, '2016-05-01 04:38:50', '3', '3', 1, '', 24, 1),
(20, '2016-05-01 04:38:58', '4', '4', 1, '', 24, 1),
(21, '2016-05-01 04:39:06', '5', '5', 1, '', 24, 1),
(22, '2016-05-01 04:39:45', '1', '1', 1, '', 25, 1),
(23, '2016-05-01 04:39:55', '2', '2', 1, '', 25, 1),
(24, '2016-05-01 04:40:07', '3', '3', 1, '', 25, 1),
(25, '2016-05-01 04:40:19', '4', '4', 1, '', 25, 1),
(26, '2016-05-01 04:40:33', '5', '5', 1, '', 25, 1),
(27, '2016-05-03 03:40:34', '1', '的说法是尽快快快快快快快', 1, '', 35, 1),
(28, '2016-05-03 03:41:41', '2', '2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(29, '2016-05-03 03:42:26', '3', '3', 1, '', 35, 1),
(30, '2016-05-03 07:41:28', '1', '四川省科技厅', 1, '', 22, 1),
(31, '2016-05-03 07:41:53', '2', '四川农业局', 1, '', 22, 1),
(32, '2016-05-03 07:42:08', '3', '中央财政厅', 1, '', 22, 1),
(33, '2016-05-03 07:42:38', '4', '湖北教育局', 1, '', 22, 1),
(34, '2016-05-03 07:43:03', '5', '中央农业局', 1, '', 22, 1),
(35, '2016-05-03 12:27:11', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_name 。', 19, 1),
(36, '2016-05-03 13:11:04', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_publish 。', 19, 1),
(37, '2016-05-03 15:45:55', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_deadtime 。', 19, 1),
(38, '2016-05-03 15:46:08', '2', '2', 2, '已修改 item_deadtime 。', 19, 1),
(39, '2016-05-03 15:46:12', '3', '3', 2, '没有字段被修改。', 19, 1),
(40, '2016-05-03 15:46:23', '3', '3', 2, '已修改 item_deadtime 。', 19, 1),
(41, '2016-05-03 15:46:32', '4', '4', 2, '已修改 item_deadtime 。', 19, 1),
(42, '2016-05-03 15:46:41', '5', '5', 2, '已修改 item_deadtime 。', 19, 1),
(43, '2016-05-03 15:48:52', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_deadtime 。', 19, 1),
(44, '2016-05-03 16:28:51', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_deadtime 。', 19, 1),
(45, '2016-05-03 16:42:07', '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_name 。', 19, 1),
(46, '2016-05-03 16:42:14', '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_name 。', 19, 1),
(47, '2016-05-03 16:42:21', '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_name 。', 19, 1),
(48, '2016-05-03 16:42:27', '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_name 。', 19, 1),
(49, '2016-05-03 16:44:59', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_about 和 item_key 。', 19, 1),
(50, '2016-05-03 16:46:10', '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_about 和 item_key 。', 19, 1),
(51, '2016-05-03 16:46:26', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 2, '已修改 item_about 。', 19, 1),
(52, '2016-05-03 16:47:09', '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_about 和 item_key 。', 19, 1),
(53, '2016-05-03 16:48:04', '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_about 和 item_key 。', 19, 1),
(54, '2016-05-03 16:48:50', '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_about 和 item_key 。', 19, 1),
(55, '2016-05-04 00:59:05', '1', '1', 1, '', 23, 1),
(56, '2016-05-04 02:08:20', '1', '1', 1, '', 31, 1),
(57, '2016-05-04 02:13:19', '2', '1', 1, '', 31, 1),
(58, '2016-05-04 02:25:14', '2', '1', 3, '', 31, 1),
(59, '2016-05-04 09:30:26', '6', '6', 1, '', 25, 1),
(60, '2016-05-04 09:30:41', '7', '7', 1, '', 25, 1),
(61, '2016-05-04 09:30:53', '8', '8', 1, '', 25, 1),
(62, '2016-05-04 09:31:05', '9', '9', 1, '', 25, 1),
(63, '2016-05-04 09:31:26', '10', '10', 1, '', 25, 1),
(64, '2016-05-04 09:32:58', '11', '11', 1, '', 25, 1),
(65, '2016-05-04 09:33:09', '12', '12', 1, '', 25, 1),
(66, '2016-05-04 09:33:22', '13', '13', 1, '', 25, 1),
(67, '2016-05-04 09:33:34', '14', '14', 1, '', 25, 1),
(68, '2016-05-04 09:33:51', '15', '15', 1, '', 25, 1),
(69, '2016-05-04 09:34:08', '16', '16', 1, '', 25, 1),
(70, '2016-05-04 09:34:23', '18', '18', 1, '', 25, 1),
(71, '2016-05-04 09:34:52', '6', '6', 1, '', 24, 1),
(72, '2016-05-04 09:35:00', '7', '7', 1, '', 24, 1),
(73, '2016-05-04 09:35:08', '8', '8', 1, '', 24, 1),
(74, '2016-05-04 09:35:14', '9', '9', 1, '', 24, 1),
(75, '2016-05-04 09:35:32', '10', '10', 1, '', 24, 1),
(76, '2016-05-04 09:35:56', '11', '11', 1, '', 24, 1),
(77, '2016-05-04 09:36:08', '12', '12', 1, '', 24, 1),
(78, '2016-05-04 09:36:23', '13', '13', 1, '', 24, 1),
(79, '2016-05-04 09:36:38', '14', '14', 1, '', 24, 1),
(80, '2016-05-04 09:36:58', '15', '15', 1, '', 24, 1),
(81, '2016-05-04 09:37:08', '16', '16', 1, '', 24, 1),
(82, '2016-05-04 09:37:19', '17', '17', 1, '', 24, 1),
(83, '2016-05-04 09:37:34', '18', '18', 1, '', 24, 1),
(84, '2016-05-04 09:43:58', '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(85, '2016-05-04 09:45:00', '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(86, '2016-05-04 09:45:57', '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(87, '2016-05-04 09:46:52', '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(88, '2016-05-04 09:47:48', '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(89, '2016-05-04 09:48:46', '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(90, '2016-05-04 09:49:43', '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(91, '2016-05-04 09:50:50', '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(92, '2016-05-04 09:53:32', '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(93, '2016-05-04 09:54:32', '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(94, '2016-05-04 09:55:34', '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(95, '2016-05-04 09:56:25', '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(96, '2016-05-04 09:57:11', '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 19, 1),
(97, '2016-05-04 09:58:36', '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(98, '2016-05-04 09:58:45', '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(99, '2016-05-04 09:58:53', '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(100, '2016-05-04 09:59:04', '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(101, '2016-05-04 09:59:14', '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(102, '2016-05-04 09:59:22', '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(103, '2016-05-04 09:59:28', '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(104, '2016-05-04 09:59:35', '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(105, '2016-05-04 09:59:41', '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(106, '2016-05-04 09:59:48', '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(107, '2016-05-04 09:59:54', '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(108, '2016-05-04 10:00:00', '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(109, '2016-05-04 10:00:04', '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, '已修改 item_pa_id 。', 19, 1),
(110, '2016-05-04 10:00:39', '3', '3', 2, '已修改 user_name 。', 10, 1),
(111, '2016-05-04 10:00:51', '2', '2', 2, '已修改 user_name 。', 10, 1),
(112, '2016-05-04 10:01:01', '1', '1@qq', 2, '已修改 user_name 。', 10, 1),
(113, '2016-05-04 10:01:21', '4', '111', 1, '', 10, 1),
(114, '2016-05-04 10:01:56', '5', '1111', 1, '', 10, 1),
(115, '2016-05-04 10:02:12', '6', '11111', 1, '', 10, 1),
(116, '2016-05-04 10:03:01', '7', '1111', 1, '', 10, 1),
(117, '2016-05-04 10:08:55', '1', '成都融亿达科技服务有限公司', 2, '已修改 company_tel，company_name，company_district，company_address，company_registered_capital，company_industry，company_stuff_no 和 company_nature 。', 11, 1),
(118, '2016-05-04 10:09:45', '1', '111111111111', 2, '已修改 company_tel 。', 11, 1),
(119, '2016-05-04 10:10:34', '3', '111111111111', 2, '已修改 company_tel，company_name，company_district，company_address，company_registered_capital，company_industry，company_stuff_no 和 company_nature 。', 11, 1),
(120, '2016-05-04 10:11:08', '2', ' 111111111111', 2, '已修改 company_tel，company_name，company_district，company_address，company_registered_capital，company_industry，company_stuff_no 和 company_nature 。', 11, 1),
(121, '2016-05-04 10:11:44', '4', '111111111111', 1, '', 11, 1),
(122, '2016-05-04 10:12:23', '5', '111111111111', 1, '', 11, 1),
(123, '2016-05-04 10:12:58', '6', '111111111111', 1, '', 11, 1),
(124, '2016-05-04 10:13:27', '7', '111111111111', 1, '', 11, 1),
(125, '2016-05-04 10:15:44', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 item_name 。', 35, 1),
(126, '2016-05-04 10:16:45', '4', '2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(127, '2016-05-04 10:17:23', '5', '2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(128, '2016-05-04 10:18:14', '6', '2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(129, '2016-05-04 10:19:43', '1', '1', 2, '没有字段被修改。', 31, 1),
(130, '2016-05-04 10:22:13', '1', ' 2016科技厅关于科技计划项目的申报通知', 2, '已修改 goods_name 和 goods_market_price 。', 31, 1),
(131, '2016-05-04 10:23:18', '2', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 31, 1),
(132, '2016-05-04 10:24:24', '3', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 31, 1),
(133, '2016-05-04 10:28:19', '1', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 article_name 和 article_content 。', 23, 1),
(134, '2016-05-04 10:46:02', '17', '17', 1, '', 25, 1),
(135, '2016-05-04 10:49:37', '1', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 item_name 。', 20, 1),
(136, '2016-05-04 10:49:45', '2', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 item_name 。', 20, 1),
(137, '2016-05-04 10:49:53', '3', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 item_name 。', 20, 1),
(138, '2016-05-04 10:49:58', '4', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 item_name 。', 20, 1),
(139, '2016-05-04 10:50:03', '5', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 item_name 。', 20, 1),
(140, '2016-05-06 14:46:29', '1', '1', 2, '已修改 pic_object 。', 25, 1),
(141, '2016-05-06 14:46:39', '2', '2', 2, '已修改 pic_object 。', 25, 1),
(142, '2016-05-06 14:46:50', '3', '3', 2, '已修改 pic_object 。', 25, 1),
(143, '2016-05-06 14:47:06', '4', '4', 2, '已修改 pic_object 。', 25, 1),
(144, '2016-05-06 14:47:22', '5', '5', 2, '已修改 pic_object 。', 25, 1),
(145, '2016-05-28 16:23:07', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(146, '2016-05-28 16:23:16', '2', '2016科技厅关于科技计划项目的申报通知', 2, '没有字段被修改。', 35, 1),
(147, '2016-05-28 16:23:25', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(148, '2016-05-28 16:23:40', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(149, '2016-05-28 16:23:49', '4', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(150, '2016-05-28 16:23:58', '4', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(151, '2016-05-28 16:24:06', '5', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(152, '2016-05-28 16:24:19', '6', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(153, '2016-05-28 16:25:15', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(154, '2016-05-28 16:25:22', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(155, '2016-05-28 16:28:16', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(156, '2016-05-28 16:28:27', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(157, '2016-05-28 16:30:58', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(158, '2016-05-28 16:31:06', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(159, '2016-05-28 16:34:34', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(160, '2016-05-28 16:37:38', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(161, '2016-05-28 16:39:19', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(162, '2016-05-28 16:40:42', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(163, '2016-05-28 16:42:25', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(164, '2016-05-28 16:56:08', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(165, '2016-05-28 16:57:58', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(166, '2016-05-28 17:02:36', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(167, '2016-05-28 17:08:56', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(168, '2016-05-28 17:13:05', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(169, '2016-05-28 17:14:37', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(170, '2016-05-28 17:16:59', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(171, '2016-05-28 17:17:49', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(172, '2016-05-28 17:18:36', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(173, '2016-05-28 17:22:22', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(174, '2016-05-28 17:22:55', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(175, '2016-05-28 17:23:16', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(176, '2016-05-28 17:23:25', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(177, '2016-05-28 17:26:16', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(178, '2016-05-28 17:27:03', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(179, '2016-05-28 17:34:36', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(180, '2016-05-28 17:39:03', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(181, '2016-05-28 17:39:42', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(182, '2016-05-28 17:40:10', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(183, '2016-05-28 17:41:53', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(184, '2016-05-28 17:42:00', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(185, '2016-05-28 17:44:44', '1', '的说法是尽快快快快快快快', 2, '已修改 order_state 。', 35, 1),
(186, '2016-05-28 17:44:51', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(187, '2016-05-28 17:52:45', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 lock_state 。', 35, 1),
(188, '2016-05-28 18:51:28', '2', '2016科技厅关于科技计划项目的申报通知', 2, '没有字段被修改。', 35, 1),
(189, '2016-05-28 18:52:02', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(190, '2016-05-29 06:36:45', '5', '3', 3, '', 34, 1),
(191, '2016-05-29 06:36:45', '4', '3', 3, '', 34, 1),
(192, '2016-05-29 06:36:45', '3', '3', 3, '', 34, 1),
(193, '2016-05-29 06:36:45', '2', '3', 3, '', 34, 1),
(194, '2016-05-29 06:36:46', '1', '3', 3, '', 34, 1),
(195, '2016-05-29 06:36:46', '0', '3', 3, '', 34, 1),
(196, '2016-05-29 07:00:41', '0', '3', 3, '', 34, 1),
(197, '2016-05-29 07:03:19', '2', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 和 lock_state 。', 35, 1),
(198, '2016-05-29 07:03:52', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 eval_state 。', 35, 1),
(199, '2016-05-29 07:04:45', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 eval_state 。', 35, 1),
(200, '2016-05-29 10:54:39', '1', ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 2, '已修改 goods_name 。', 31, 1),
(201, '2016-05-29 10:54:53', '1', ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 2, '没有字段被修改。', 31, 1),
(202, '2016-05-29 10:55:59', '2', '2016科技厅关于科技计划2016科技厅关于科技计划项目的申报通知项目的申报通知', 2, '已修改 item_name 。', 35, 1),
(203, '2016-05-29 11:03:21', '2', '3', 3, '', 34, 1),
(204, '2016-05-29 11:03:21', '1', '3', 3, '', 34, 1),
(205, '2016-05-29 11:03:21', '0', '3', 3, '', 34, 1),
(206, '2016-05-29 11:05:43', '2', '2016科技厅关于科技计划2016科技厅关于科技计划项目的申报通知项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(207, '2016-05-29 11:05:53', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 eval_state 。', 35, 1),
(208, '2016-05-29 11:27:01', '2', '2016科技厅关于科技计划2016科技厅关于科技计划项目的申报通知项目的申报通知', 2, '已修改 lock_state 。', 35, 1),
(209, '2016-05-29 11:30:38', '2', '2016科技厅关于科技计划2016科技厅关于科技计划项目的申报通知项目的申报通知', 2, '已修改 eval_state 。', 35, 1),
(210, '2016-05-30 02:49:32', '1', '作为最具可持续性的交通运输模式', 2, '已修改 item_name 。', 19, 1),
(211, '2016-05-30 02:49:59', '2', '国家关键基础设施和重要基础产业', 2, '已修改 item_name 。', 19, 1),
(212, '2016-05-30 02:50:29', '3', '轨道交通科技持续自主创新', 2, '已修改 item_name 。', 19, 1),
(213, '2016-05-30 02:50:54', '4', '国家通过实施“创新驱动发展”战略全面支撑“新型城镇化”', 2, '已修改 item_name 。', 19, 1),
(214, '2016-05-30 02:51:24', '5', '高速客运装备关键技术', 2, '已修改 item_name 。', 19, 1),
(215, '2016-05-30 02:51:58', '6', '先进轨道交通”重点专项中《时速400公里及以上高速客运装备关键技术》', 2, '已修改 item_name 。', 19, 1),
(216, '2016-05-30 02:52:15', '7', '跨国互联互通高速动车组装备与运维系统研制', 2, '已修改 item_name 。', 19, 1),
(217, '2016-05-30 02:52:27', '8', '变结构走行系统列车关键技术研究', 2, '已修改 item_name 。', 19, 1),
(218, '2016-05-30 02:52:51', '9', '不同线路条件下的轮轨接触关系及与车辆悬挂参数之间的匹配技术研究', 2, '已修改 item_name 。', 19, 1),
(219, '2016-05-30 02:53:05', '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦列车多效应耦合及智能控制技术研究', 2, '已修改 item_name 。', 19, 1),
(220, '2016-05-30 02:53:18', '10', '多效应耦合及智能控制技术研究', 2, '已修改 item_name 。', 19, 1),
(221, '2016-05-30 02:53:29', '11', '基于噪声主动控制的综合舒适度控制技术研究', 2, '已修改 item_name 。', 19, 1),
(222, '2016-05-30 02:53:46', '12', '时速400公里高速列车车内噪声模拟与仿真技术研究', 2, '已修改 item_name 。', 19, 1),
(223, '2016-05-30 02:53:59', '13', '基于“重量-阻力-动力”多目标均衡的综合节能技术研究', 2, '已修改 item_name 。', 19, 1),
(224, '2016-05-30 02:54:15', '14', '高速列车“重量-阻力-动力”等多目标节能匹配技术研究', 2, '已修改 item_name 。', 19, 1),
(225, '2016-05-30 02:54:29', '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦面向高安全性的走行、结构、防火、电磁兼容技术研究', 2, '已修改 item_name 。', 19, 1),
(226, '2016-05-30 02:54:44', '16', '高速列车被动安全设计及试验评估技术', 2, '已修改 item_name 。', 19, 1),
(227, '2016-05-30 02:55:00', '17', '时速400公里转向架构架载荷谱研究', 2, '已修改 item_name 。', 19, 1),
(228, '2016-05-30 02:57:03', '1', '1', 2, '已修改 pic_object 。', 25, 1),
(229, '2016-05-30 02:57:23', '2', '2', 2, '已修改 pic_object 。', 25, 1),
(230, '2016-05-30 02:57:40', '3', '3', 2, '已修改 pic_object 。', 25, 1),
(231, '2016-05-30 02:57:55', '3', '3', 2, '已修改 pic_object 。', 25, 1),
(232, '2016-05-30 02:57:59', '4', '4', 2, '没有字段被修改。', 25, 1),
(233, '2016-05-30 02:58:08', '4', '4', 2, '已修改 pic_object 。', 25, 1),
(234, '2016-05-30 02:58:20', '5', '5', 2, '已修改 pic_object 。', 25, 1),
(235, '2016-05-30 02:58:30', '6', '6', 2, '已修改 pic_object 。', 25, 1),
(236, '2016-05-30 02:58:40', '7', '7', 2, '已修改 pic_object 。', 25, 1),
(237, '2016-05-30 02:58:48', '8', '8', 2, '已修改 pic_object 。', 25, 1),
(238, '2016-05-30 02:59:13', '1', '1', 2, '没有字段被修改。', 24, 1),
(239, '2016-05-30 03:00:16', '1', '2016科技厅关于科技计划项目的申报通知	', 2, '已修改 article_content 。', 23, 1),
(240, '2016-05-30 03:01:44', '2', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 23, 1),
(241, '2016-05-30 03:02:39', '3', '3', 1, '', 23, 1),
(242, '2016-05-30 03:03:32', '4', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 23, 1),
(243, '2016-05-30 03:03:43', '3', ' 2016科技厅关于科技计划项目的申报通知', 2, '已修改 article_name 。', 23, 1),
(244, '2016-05-30 03:05:43', '0', '3', 2, '已修改 goev_content 。', 34, 1),
(245, '2016-05-30 03:06:00', '1', '1', 2, '已修改 goev_content 。', 34, 1),
(246, '2016-05-30 03:09:37', '1', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(247, '2016-05-30 03:10:49', '4', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(248, '2016-05-30 03:11:26', '2', '2016科技厅关于科技计划2016科技厅关于科技计划项目的申报通知项目的申报通知', 2, '已修改 item_id 。', 35, 1),
(249, '2016-05-30 03:11:35', '3', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 item_id 。', 35, 1),
(250, '2016-05-30 03:12:04', '5', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 item_id 。', 35, 1),
(251, '2016-05-30 03:12:48', '6', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(252, '2016-05-30 03:13:49', '7', ' 2016科技厅关于科技计划项目的申报通知', 1, '', 35, 1),
(253, '2016-05-30 03:14:21', '5', '2016科技厅关于科技计划项目的申报通知', 2, '已修改 order_state 。', 35, 1),
(254, '2016-05-30 03:33:47', '8', '', 3, '', 35, 1),
(255, '2016-05-30 03:49:20', '3', '3', 2, '已修改 user_password 。', 10, 1),
(256, '2016-05-30 04:00:07', '1', '1', 2, '已修改 pic_object 。', 25, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(4, 'admin', 'logentry'),
(6, 'auth', 'group'),
(5, 'auth', 'permission'),
(7, 'auth', 'user'),
(8, 'contenttypes', 'contenttype'),
(1, 'easy_thumbnails', 'source'),
(2, 'easy_thumbnails', 'thumbnail'),
(3, 'easy_thumbnails', 'thumbnaildimensions'),
(9, 'sessions', 'session'),
(26, 'zhengzihui_app', 'tb_accessory'),
(24, 'zhengzihui_app', 'tb_album'),
(17, 'zhengzihui_app', 'tb_apage'),
(18, 'zhengzihui_app', 'tb_apage_class'),
(36, 'zhengzihui_app', 'tb_area'),
(23, 'zhengzihui_app', 'tb_article'),
(27, 'zhengzihui_app', 'tb_artificial_representations'),
(31, 'zhengzihui_app', 'tb_goods'),
(33, 'zhengzihui_app', 'tb_goods_class'),
(32, 'zhengzihui_app', 'tb_goods_click'),
(34, 'zhengzihui_app', 'tb_goods_evaluation'),
(19, 'zhengzihui_app', 'tb_item'),
(21, 'zhengzihui_app', 'tb_item_class'),
(20, 'zhengzihui_app', 'tb_item_click'),
(22, 'zhengzihui_app', 'tb_item_pa'),
(28, 'zhengzihui_app', 'tb_message'),
(29, 'zhengzihui_app', 'tb_messagetext'),
(14, 'zhengzihui_app', 'tb_news'),
(13, 'zhengzihui_app', 'tb_news_class'),
(15, 'zhengzihui_app', 'tb_notice'),
(16, 'zhengzihui_app', 'tb_notice_class'),
(35, 'zhengzihui_app', 'tb_order'),
(25, 'zhengzihui_app', 'tb_pic'),
(12, 'zhengzihui_app', 'tb_service_provider'),
(30, 'zhengzihui_app', 'tb_sysmessage'),
(10, 'zhengzihui_app', 'tb_user'),
(11, 'zhengzihui_app', 'tb_user_expand');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2016-05-01 04:25:04'),
(2, 'auth', '0001_initial', '2016-05-01 04:25:11'),
(3, 'admin', '0001_initial', '2016-05-01 04:25:12'),
(4, 'contenttypes', '0002_remove_content_type_name', '2016-05-01 04:25:14'),
(5, 'auth', '0002_alter_permission_name_max_length', '2016-05-01 04:25:15'),
(6, 'auth', '0003_alter_user_email_max_length', '2016-05-01 04:25:15'),
(7, 'auth', '0004_alter_user_username_opts', '2016-05-01 04:25:15'),
(8, 'auth', '0005_alter_user_last_login_null', '2016-05-01 04:25:15'),
(9, 'auth', '0006_require_contenttypes_0002', '2016-05-01 04:25:15'),
(10, 'easy_thumbnails', '0001_initial', '2016-05-01 04:25:18'),
(11, 'easy_thumbnails', '0002_thumbnaildimensions', '2016-05-01 04:25:19'),
(12, 'sessions', '0001_initial', '2016-05-01 04:25:19'),
(13, 'zhengzihui_app', '0001_initial', '2016-05-01 04:25:27'),
(14, 'zhengzihui_app', '0002_auto_20160503_1519', '2016-05-03 07:19:34'),
(15, 'zhengzihui_app', '0003_auto_20160504_1910', '2016-05-04 11:10:08'),
(16, 'zhengzihui_app', '0002_auto_20160529_1419', '2016-05-29 06:19:17');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2zoyd0vxl7itx1wyst1y252xc3gmb9rf', 'OWMyOGM5YTI1OWY5MGQzMGYzOTlmOWIwMDQ1ODIzNWQ2Y2I0NjA5OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwidXNlcl9pZCI6MywiX2F1dGhfdXNlcl9pZCI6IjEiLCJ1bnBheWVkaWQiOjksIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJfYXV0aF91c2VyX2hhc2giOiI4MmJjNWJlYWJmZDQ1NTQ3MDY0ZDVlODg3ZDgyZDU4NjU3ZjcwNTliIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4In0=', '2016-06-13 04:25:17'),
('7dyulcvnljfrfz3g71arxt4tgmlza7m6', 'MDM4NDEzZWE4ZWFkN2ZmN2UwOWViNTc0M2UxMjgxMzJjN2QxOWMwNjp7InVzZXJfaWQiOjN9', '2016-06-12 14:38:35'),
('7ulx02b1h6x9ltj1y1fw2h1ctz7porgb', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-06-09 12:37:05'),
('aqzykmfp7erujan6kyqb03aiwtqd168m', 'OTJmYTIxNzFjMGYxY2M1MzEzM2M3YmM1Y2M3NTZmNjVkMzcxOTUwYzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgiLCJ1c2VyX2lkIjozfQ==', '2016-06-12 10:26:43'),
('vd5p3bqq84jqssxzp4wf85j7oxpsc2vb', 'MTRkYjJkODc5M2JiMTc3ZmZlNTM0YTBkNTAyY2NlM2ZlNTViYjg1MDp7ImJ1bWVuIjoiXHU4MGZkXHU2ZTkwIiwidXNlcl9pZCI6MywiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYmM1YmVhYmZkNDU1NDcwNjRkNWU4ODdkODJkNTg2NTdmNzA1OWIiLCJ6aHVhbmd0YWkiOiJcdTZiNjNcdTU3MjhcdTc1MzNcdTYyYTUsXHU2MjJhXHU2YjYyXHU3NTMzXHU2MmE1In0=', '2016-05-18 11:16:56'),
('z7axda2fmgg6a0c5kk7f9ym9khrr5m9a', 'NTQzY2M1MDJiZGZkNTZjMWQ0YTc1MWQ1OTZjYWYzZjM2MWFkMzg2ZDp7ImJ1bWVuIjoiXHU0ZWJhXHU2YzExXHU5NGY2XHU4ODRjIiwiX2F1dGhfdXNlcl9oYXNoIjoiODJiYzViZWFiZmQ0NTU0NzA2NGQ1ZTg4N2Q4MmQ1ODY1N2Y3MDU5YiIsInVzZXJfaWQiOjMsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-05-20 14:43:02');

-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_source`
--

CREATE TABLE `easy_thumbnails_source` (
  `id` int(11) NOT NULL,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

CREATE TABLE `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_thumbnaildimensions`
--

CREATE TABLE `easy_thumbnails_thumbnaildimensions` (
  `id` int(11) NOT NULL,
  `thumbnail_id` int(11) NOT NULL,
  `width` int(10) UNSIGNED DEFAULT NULL,
  `height` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_accessory`
--

CREATE TABLE `zhengzihui_app_tb_accessory` (
  `id` int(11) NOT NULL,
  `anne_id` int(11) NOT NULL,
  `comm_id` int(11) NOT NULL,
  `apubdate` int(11) NOT NULL,
  `apublisher` varchar(2) NOT NULL,
  `aposition` varchar(10) NOT NULL,
  `aaddtion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_album`
--

CREATE TABLE `zhengzihui_app_tb_album` (
  `album_id` int(11) NOT NULL,
  `album_name` varchar(40) NOT NULL,
  `album_type` int(11) NOT NULL,
  `affiliation_id` int(11) NOT NULL,
  `nacl_des` varchar(100) NOT NULL,
  `nacl_sort` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  `is_default` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_album`
--

INSERT INTO `zhengzihui_app_tb_album` (`album_id`, `album_name`, `album_type`, `affiliation_id`, `nacl_des`, `nacl_sort`, `upload_time`, `is_default`) VALUES
(1, '1', 0, 1, '1', 1, '2016-05-30 02:59:13', 1),
(2, '2', 0, 2, '2', 2, '2016-05-01 04:38:39', 1),
(3, '3', 0, 3, '3', 3, '2016-05-01 04:38:50', 1),
(4, '4', 0, 4, '4', 4, '2016-05-01 04:38:58', 1),
(5, '5', 0, 5, '5', 5, '2016-05-01 04:39:06', 1),
(6, '6', 0, 6, '6', 6, '2016-05-04 09:34:52', 1),
(7, '7', 0, 7, '7', 7, '2016-05-04 09:35:00', 1),
(8, '8', 0, 8, '8', 8, '2016-05-04 09:35:08', 1),
(9, '9', 0, 9, '9', 9, '2016-05-04 09:35:14', 1),
(10, '10', 0, 10, '10', 10, '2016-05-04 09:35:32', 1),
(11, '11', 0, 11, '11', 11, '2016-05-04 09:35:56', 1),
(12, '12', 0, 12, '12', 12, '2016-05-04 09:36:08', 1),
(13, '13', 0, 13, '13', 13, '2016-05-04 09:36:23', 1),
(14, '14', 0, 14, '14', 14, '2016-05-04 09:36:38', 1),
(15, '15', 0, 15, '15', 15, '2016-05-04 09:36:58', 1),
(16, '16', 0, 16, '16', 16, '2016-05-04 09:37:08', 1),
(17, '17', 0, 17, '17', 17, '2016-05-04 09:37:19', 1),
(18, '18', 0, 18, '18', 18, '2016-05-04 09:37:34', 1);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_apage`
--

CREATE TABLE `zhengzihui_app_tb_apage` (
  `Apage_id` int(11) NOT NULL,
  `Article_id` int(11) NOT NULL,
  `Has_album` int(11) NOT NULL,
  `Apage_time` date NOT NULL,
  `Apage_source` varchar(100) NOT NULL,
  `Apcl_id` int(11) NOT NULL,
  `Apage_sort` int(11) NOT NULL,
  `Apage_is_display` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_apage_class`
--

CREATE TABLE `zhengzihui_app_tb_apage_class` (
  `Apcl_id` int(11) NOT NULL,
  `Apcl_code` int(11) NOT NULL,
  `Apcl_name` varchar(100) NOT NULL,
  `Apcl_parent_id` int(11) NOT NULL,
  `Apcl_sort` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_area`
--

CREATE TABLE `zhengzihui_app_tb_area` (
  `area_id` int(11) NOT NULL,
  `area_name` varchar(100) NOT NULL,
  `area_parent_id` int(11) NOT NULL,
  `area_sort` int(11) NOT NULL,
  `area_deep` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_article`
--

CREATE TABLE `zhengzihui_app_tb_article` (
  `article_id` int(11) NOT NULL,
  `article_code` int(11) NOT NULL,
  `article_name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `author_email` varchar(100) NOT NULL,
  `article_type` int(11) NOT NULL,
  `affiliation_id` int(11) NOT NULL,
  `article_content` longtext NOT NULL,
  `article_keywords` longtext NOT NULL,
  `article_des` varchar(100) NOT NULL,
  `article_sort` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  `is_default` int(11) NOT NULL,
  `article_click` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_article`
--

INSERT INTO `zhengzihui_app_tb_article` (`article_id`, `article_code`, `article_name`, `author`, `author_email`, `article_type`, `affiliation_id`, `article_content`, `article_keywords`, `article_des`, `article_sort`, `upload_time`, `is_default`, `article_click`) VALUES
(1, 1, '2016科技厅关于科技计划项目的申报通知	', '1', '1@qq.com', 0, 1, '文章一：分分无法额分为氛围额我发色佛萨大师范德萨发生个啊我给哇恶个撒更让人哇个人无关啊让外国人啊让我噶人围观让莪会噶热忽然鹅嘎啊我给哈日为何啊然后让莪好热啊还让额哈额和他啊额和阿泰他恶化阿特哈额thea他啊额哈额啊额呵嗄呵嘎然啊如果哈日\r\n', '1', '1', 1, '2016-05-30 03:00:16', 1, 1),
(2, 2, ' 2016科技厅关于科技计划项目的申报通知', '2', '1@qq.com', 0, 1, '文章二：几十年发送反馈撒饿不反抗被释放吧我回家WE风纪扣额WJFE玩家开发额WBFWKHFG文化股份KWGFE可我不敢额KFE积分额KJF额jfkEQJKF额去讲课费QF额去解放碑QHFBuhbfbWEBFeufbWUOFBEufo前辈OFUBEQuofbu部分不分互粉被', '2', '2', 2, '2016-05-30 03:01:43', 1, 2),
(3, 3, ' 2016科技厅关于科技计划项目的申报通知', '3', '1@qq.com', 0, 1, '文章三：花蝶舞部分海外分别为范本我为额非我辈文件分别为为 副本啊微积分尾巴了微博web额我不ibm为并无分别为额我不服未必微博iewf   ijfwbaeifwaeijfbaw额副本玩法我不放假哇被封为问啊解放碑哇发布哇俄方被挖掘别挖苦发布为方便我俄警方额我发额违反基本为gif就饿哇变废为宝发额我卡啊胃口部分哇靠俄边防weak部分哇靠笨啊我开房吧哇恶法', '3', '3', 3, '2016-05-30 03:03:43', 1, 3),
(4, 4, ' 2016科技厅关于科技计划项目的申报通知', '4', '1@qq.com', 0, 1, '文章四：那就必然被我就把我给帮我啊官本位啊根本哇改变挖掘和啊我见过吧我就噶人我机构入网啊人文景观我就噶我见过认为几个人往日围观软甲日晚间公布如果不让我好过吧让我换个人瓦工污染环境人文环境改变让我换个人物日瓦格 软文广告包裹iarwbgrwahgbwaijgbwigbewjigbajwibijwbweijbiwjgbrwibg任务ijwijbgww为官本位额根本ijbawgwarig ', '4', '4', 4, '2016-05-30 03:03:32', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_artificial_representations`
--

CREATE TABLE `zhengzihui_app_tb_artificial_representations` (
  `arre_id` int(11) NOT NULL,
  `arre_title` varchar(100) NOT NULL,
  `arre_content` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `arre_state` int(11) NOT NULL,
  `create_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_goods`
--

CREATE TABLE `zhengzihui_app_tb_goods` (
  `goods_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `sp_id` int(11) NOT NULL,
  `goods_name` varchar(40) NOT NULL,
  `goods_market_price` int(11) NOT NULL,
  `goods_price` int(11) NOT NULL,
  `goods_price_discouint` double NOT NULL,
  `goods_pay` int(11) NOT NULL,
  `goods_guarantee` varchar(100) NOT NULL,
  `goods_sort` int(11) NOT NULL,
  `goods_commend` int(11) NOT NULL,
  `goods_evaluation_good_star` int(11) NOT NULL,
  `goods_evaluation_count` int(11) NOT NULL,
  `goods_show` int(11) NOT NULL,
  `goods_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_goods`
--

INSERT INTO `zhengzihui_app_tb_goods` (`goods_id`, `item_id`, `sp_id`, `goods_name`, `goods_market_price`, `goods_price`, `goods_price_discouint`, `goods_pay`, `goods_guarantee`, `goods_sort`, `goods_commend`, `goods_evaluation_good_star`, `goods_evaluation_count`, `goods_show`, `goods_status`) VALUES
(1, 1, 1, ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 100000, 1, 1, 1, '1', 1, 0, 1, 1, 1, 0),
(2, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 18888, 1, 1, 1, '1', 1, 0, 1, 1, 1, 0),
(3, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 56781, 1, 3, 1, '1', 1, 0, 1, 1, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_goods_class`
--

CREATE TABLE `zhengzihui_app_tb_goods_class` (
  `gocl_id` int(11) NOT NULL,
  `gocl_code` int(11) NOT NULL,
  `gocl_name` varchar(40) NOT NULL,
  `gocl_des` varchar(100) NOT NULL,
  `gocl_sort` int(11) NOT NULL,
  `gocl_parent_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_goods_click`
--

CREATE TABLE `zhengzihui_app_tb_goods_click` (
  `id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) NOT NULL,
  `gocl_id` int(11) NOT NULL,
  `gocl_num` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_goods_evaluation`
--

CREATE TABLE `zhengzihui_app_tb_goods_evaluation` (
  `goev_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `create_time` datetime NOT NULL,
  `goev_desccredit` int(11) NOT NULL,
  `goev_servicecredit` int(11) NOT NULL,
  `goev_content` longtext NOT NULL,
  `is_anonymous` int(11) NOT NULL,
  `goev_show` int(11) NOT NULL,
  `goev_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_goods_evaluation`
--

INSERT INTO `zhengzihui_app_tb_goods_evaluation` (`goev_id`, `order_id`, `goods_id`, `goods_name`, `user_id`, `user_name`, `create_time`, `goev_desccredit`, `goev_servicecredit`, `goev_content`, `is_anonymous`, `goev_show`, `goev_status`) VALUES
(0, 3, 1, ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 3, '3', '2016-05-30 03:05:43', 5, 5, '自己昂啊开噶快恐怖吧布莱克本不亢不卑 极薄极薄科技部科比科比可不敢看别人看过宽容别人卡巴啊个吧如果bark了几个吧看过吧看过啊比如高科技啊不客观bra看了个啊收费的观点个人更改热锅个额恶化恶化帅', 1, 1, 1),
(1, 2, 1, ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 3, '1', '2016-05-30 03:06:00', 5, 5, '的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶', 1, 1, 1),
(2, 2, 1, ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 3, '1', '2016-05-29 11:32:37', 5, 5, '急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急急', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_item`
--

CREATE TABLE `zhengzihui_app_tb_item` (
  `item_id` int(11) NOT NULL,
  `item_code` varchar(20) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `itcl_id` int(11) NOT NULL,
  `item_level` int(11) NOT NULL,
  `item_ga` varchar(40) NOT NULL,
  `item_pa_id` int(11) NOT NULL,
  `item_publish` datetime NOT NULL,
  `item_deadtime` datetime NOT NULL,
  `item_about` varchar(100) NOT NULL,
  `item_url` varchar(100) NOT NULL,
  `item_key` longtext NOT NULL,
  `item_status` int(11) NOT NULL,
  `is_hot` int(11) NOT NULL,
  `item_from` int(11) NOT NULL,
  `is_recommend` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_item`
--

INSERT INTO `zhengzihui_app_tb_item` (`item_id`, `item_code`, `item_name`, `itcl_id`, `item_level`, `item_ga`, `item_pa_id`, `item_publish`, `item_deadtime`, `item_about`, `item_url`, `item_key`, `item_status`, `is_hot`, `item_from`, `is_recommend`) VALUES
(1, '1', '作为最具可持续性的交通运输模式', 1, 1, '1', 1, '2016-04-03 04:35:19', '2016-05-03 16:28:49', '养殖/科技/互联网', '1', '科技项目', 0, 0, 0, 1),
(2, '2', '国家关键基础设施和重要基础产业', 2, 1, '2', 2, '2016-05-01 04:35:42', '2016-06-18 04:35:43', '农林/住建/其他', '2', '互联网项目', 0, 0, 0, 1),
(3, '3', '轨道交通科技持续自主创新', 3, 1, '3', 3, '2016-05-01 04:36:23', '2016-07-15 04:36:24', '农业/养殖/互联网+', '3', '科技项目', 0, 0, 0, 1),
(4, '4', '国家通过实施“创新驱动发展”战略全面支撑“新型城镇化”', 4, 1, '4', 4, '2016-05-01 04:36:47', '2016-05-28 04:36:48', '水产/养殖/其他', '4', '科技项目', 0, 0, 0, 0),
(5, '5', '高速客运装备关键技术', 5, 1, '5', 5, '2016-05-01 04:37:05', '2016-07-08 04:37:07', '水产/政务/管理/新产业', '5', '中央项目', 0, 0, 0, 0),
(6, '6', '先进轨道交通”重点专项中《时速400公里及以上高速客运装备关键技术》', 6, 1, '5万-500万', 1, '2016-03-08 09:42:34', '2016-09-01 09:42:39', '农业/养殖/互联网+', '6', '水产/政务/管理/新产业', 0, 0, 0, 1),
(7, '7', '跨国互联互通高速动车组装备与运维系统研制', 7, 1, '5万-500万', 2, '2016-03-23 09:44:34', '2016-06-11 09:44:38', '水产/政务/管理/新产业', '7', '科技项目', 0, 0, 0, 1),
(8, '8', '变结构走行系统列车关键技术研究', 8, 1, '5万-500万', 3, '2015-12-03 09:45:32', '2016-06-30 09:45:40', '农林/住建/其他', '8', '互联网项目', 0, 0, 0, 1),
(9, '9', '不同线路条件下的轮轨接触关系及与车辆悬挂参数之间的匹配技术研究', 9, 1, '5万-500万', 4, '2016-04-13 09:46:22', '2016-06-17 09:46:26', '农业/养殖/互联网+', '9', '中央项目', 0, 0, 0, 1),
(10, '10', '多效应耦合及智能控制技术研究', 10, 1, '5万-500万', 5, '2016-05-01 09:47:25', '2016-05-31 09:47:28', '水产/政务/管理/新产业', '10', '科技项目', 0, 0, 0, 0),
(11, '11', '基于噪声主动控制的综合舒适度控制技术研究', 11, 1, '5万-500万', 1, '2016-04-03 09:48:13', '2016-05-04 09:48:23', '养殖/科技/互联网', '11', '互联网项目', 0, 0, 0, 1),
(12, '12', '时速400公里高速列车车内噪声模拟与仿真技术研究', 12, 1, '5万-500万', 2, '2016-04-07 09:49:12', '2016-05-04 09:49:15', '养殖/科技/互联网', '12', '中央项目', 0, 0, 0, 0),
(13, '13', '基于“重量-阻力-动力”多目标均衡的综合节能技术研究', 13, 1, '5万-500万', 3, '2016-04-10 09:50:24', '2016-05-28 09:50:30', '水产/政务/管理/新产业', '13', '科技项目', 0, 0, 0, 1),
(14, '14', '高速列车“重量-阻力-动力”等多目标节能匹配技术研究', 14, 1, '5万-500万', 4, '2016-04-01 09:53:00', '2016-06-09 09:53:03', '水产/政务/管理/新产业', '14', '科技项目', 0, 0, 0, 1),
(15, '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦面向高安全性的走行、结构、防火、电磁兼容技术研究', 15, 1, '5万-500万', 5, '2016-04-05 09:54:09', '2016-05-04 09:54:12', '养殖/科技/互联网', '15', '互联网项目', 0, 0, 0, 0),
(16, '16', '高速列车被动安全设计及试验评估技术', 16, 1, '5万-500万', 1, '2016-04-03 09:55:05', '2016-06-24 09:55:08', '农林/住建/其他', '16', '中央项目', 0, 0, 0, 0),
(17, '17', '时速400公里转向架构架载荷谱研究', 17, 1, '5万-500万', 2, '2016-04-20 09:56:04', '2016-07-08 09:56:08', '水产/政务/管理/新产业 ', '17', '科技项目', 0, 0, 0, 0),
(18, '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 18, 1, '5万-500万', 3, '2016-03-31 09:56:50', '2016-05-26 09:56:53', '农业/养殖/互联网+', '18', '互联网项目', 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_item_class`
--

CREATE TABLE `zhengzihui_app_tb_item_class` (
  `itcl_id` int(11) NOT NULL,
  `itcl_code` int(11) NOT NULL,
  `itcl_name` varchar(100) NOT NULL,
  `itcl_des` varchar(100) NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_item_click`
--

CREATE TABLE `zhengzihui_app_tb_item_click` (
  `id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `itcl_id` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_item_click`
--

INSERT INTO `zhengzihui_app_tb_item_click` (`id`, `item_id`, `item_name`, `itcl_id`, `click_counter`) VALUES
(1, 1, '2016科技厅关于科技计划项目的申报通知	', 1, 1),
(2, 2, '2016科技厅关于科技计划项目的申报通知	', 2, 2),
(3, 3, '2016科技厅关于科技计划项目的申报通知	', 3, 3),
(4, 4, '2016科技厅关于科技计划项目的申报通知	', 4, 4),
(5, 5, '2016科技厅关于科技计划项目的申报通知	', 5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_item_pa`
--

CREATE TABLE `zhengzihui_app_tb_item_pa` (
  `ipa_id` int(11) NOT NULL,
  `ipa_name` varchar(100) NOT NULL,
  `ipa_parent_id` int(11) NOT NULL,
  `ipa_sort` int(11) NOT NULL,
  `area_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_item_pa`
--

INSERT INTO `zhengzihui_app_tb_item_pa` (`ipa_id`, `ipa_name`, `ipa_parent_id`, `ipa_sort`, `area_id`) VALUES
(1, '四川省科技厅', 1, 1, 1),
(2, '四川农业局', 2, 2, 2),
(3, '中央财政厅', 3, 3, 3),
(4, '湖北教育局', 4, 4, 4),
(5, '中央农业局', 5, 5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_message`
--

CREATE TABLE `zhengzihui_app_tb_message` (
  `mess_id` int(11) NOT NULL,
  `send_id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL,
  `text_id` int(11) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_messagetext`
--

CREATE TABLE `zhengzihui_app_tb_messagetext` (
  `text_id` int(11) NOT NULL,
  `mete_title` varchar(10) NOT NULL,
  `mete_content` varchar(300) NOT NULL,
  `mete_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_news`
--

CREATE TABLE `zhengzihui_app_tb_news` (
  `news_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `news_time` datetime NOT NULL,
  `news_source` varchar(100) NOT NULL,
  `necl_id` int(11) NOT NULL,
  `news_sort` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  `has_album` int(11) NOT NULL,
  `news_hot` int(11) NOT NULL,
  `new_top` int(11) NOT NULL,
  `new_is_display` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_news_class`
--

CREATE TABLE `zhengzihui_app_tb_news_class` (
  `necl_id` int(11) NOT NULL,
  `necl_code` int(11) NOT NULL,
  `necl_name` varchar(100) NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_notice`
--

CREATE TABLE `zhengzihui_app_tb_notice` (
  `Notice_id` int(11) NOT NULL,
  `Notice_title` varchar(100) NOT NULL,
  `Article_id` int(11) NOT NULL,
  `Notice_time` date NOT NULL,
  `Notice_source` varchar(100) NOT NULL,
  `Nocl_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  `Notice_is_display` int(11) NOT NULL,
  `Notice_top` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_notice_class`
--

CREATE TABLE `zhengzihui_app_tb_notice_class` (
  `Nocl_id` int(11) NOT NULL,
  `Nocl_code` int(11) NOT NULL,
  `Nocl_name` varchar(100) NOT NULL,
  `Nocl_des` varchar(100) NOT NULL,
  `Nocl_parent_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_order`
--

CREATE TABLE `zhengzihui_app_tb_order` (
  `order_id` int(11) NOT NULL,
  `pay_no` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` varchar(40) NOT NULL,
  `sp_id` int(11) NOT NULL,
  `sp_name` varchar(40) NOT NULL,
  `buyer_id` int(11) NOT NULL,
  `buyer_name` varchar(40) NOT NULL,
  `buyer_email` varchar(40) NOT NULL,
  `add_time` datetime NOT NULL,
  `payment_code` varchar(100) NOT NULL,
  `payment_time` datetime NOT NULL,
  `final_time` datetime NOT NULL,
  `good_amount` int(11) NOT NULL,
  `order_amount` int(11) NOT NULL,
  `refund_amount` int(11) NOT NULL,
  `delay_time` datetime NOT NULL,
  `order_from` int(11) NOT NULL,
  `express_id` int(11) NOT NULL,
  `express_no` varchar(100) NOT NULL,
  `eval_state` int(11) NOT NULL,
  `order_state` int(11) NOT NULL,
  `refund_state` int(11) NOT NULL,
  `lock_state` int(11) NOT NULL,
  `express_state` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_order`
--

INSERT INTO `zhengzihui_app_tb_order` (`order_id`, `pay_no`, `item_id`, `item_name`, `sp_id`, `sp_name`, `buyer_id`, `buyer_name`, `buyer_email`, `add_time`, `payment_code`, `payment_time`, `final_time`, `good_amount`, `order_amount`, `refund_amount`, `delay_time`, `order_from`, `express_id`, `express_no`, `eval_state`, `order_state`, `refund_state`, `lock_state`, `express_state`, `goods_id`) VALUES
(1, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 1, '1', 3, '3', '1@qq.com', '2016-05-30 03:08:39', '1', '2016-05-30 03:08:47', '2016-05-30 03:08:49', 99998, 0, 0, '2016-05-30 03:09:06', 1, 1, '1', 0, 0, 0, 0, 1, 1),
(2, 2, 1, '2016科技厅关于科技计划2016科技厅关于科技计划项目的申报通知项目的申报通知', 1, '1', 3, '1', '1@qq.com', '2016-05-03 03:41:10', '1', '2016-05-03 03:41:11', '2016-05-03 03:41:14', 1, 8888, 1, '2016-05-03 03:41:23', 1, 1, '1', 1, 4, 0, 0, 1, 1),
(3, 3, 1, '2016科技厅关于科技计划项目的申报通知', 3, '3', 3, '3', '1@qq.com', '2016-05-02 03:42:03', '1', '2016-05-03 03:42:07', '2016-05-03 03:42:08', 1, 9999, 1, '2016-05-03 03:42:17', 1, 1, '1', 1, 4, 0, 0, 1, 1),
(4, 4, 1, ' 2016科技厅关于科技计划项目的申报通知', 1, '1', 3, '3', '1@qq.com', '2016-05-30 03:10:15', '1', '2016-05-30 03:10:18', '2016-05-30 03:10:19', 19999, 0, 0, '2016-05-30 03:10:27', 1, 1, '1', 0, 4, 0, 0, 1, 1),
(5, 5, 1, '2016科技厅关于科技计划项目的申报通知', 5, '5', 3, '3', '1@qq.com', '2016-05-04 10:17:06', '1', '2016-05-04 10:17:09', '2016-05-04 10:17:11', 1, 0, 1, '2016-05-04 10:17:15', 1, 11, '1', 0, 3, 0, 0, 1, 1),
(6, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 1, '1', 3, '3', '1@qq.com', '2016-05-30 03:12:27', '1', '2016-05-30 03:12:32', '2016-05-30 03:12:33', 19999, 0, 1, '2016-05-30 03:12:37', 1, 1, '1', 0, 2, 0, 0, 1, 1),
(7, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 1, '1', 3, '3', '1@qq.com', '2016-05-30 03:13:23', '1', '2016-05-30 03:13:28', '2016-05-30 03:13:29', 1, 0, 1, '2016-05-30 03:13:34', 1, 1, '1', 0, 4, 0, 0, 1, 1),
(8, 0, 1, ' 2016科技厅关于科技计划项目的申报通知 2016科技厅关于科技计划项目的申报', 1, '', 3, '', '', '2016-05-30 03:33:51', '', '2016-05-30 03:33:51', '2016-05-30 03:33:51', 1, 0, 0, '2016-05-30 03:33:51', 1, 0, '', 0, 1, 0, 0, 1, 1),
(9, 0, 1, ' 2016科技厅关于科技计划项目的申报通知', 1, '', 3, '', '', '2016-05-30 04:09:14', '', '2016-05-30 04:09:14', '2016-05-30 04:09:14', 1, 0, 0, '2016-05-30 04:09:14', 1, 0, '', 0, 1, 0, 0, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_pic`
--

CREATE TABLE `zhengzihui_app_tb_pic` (
  `pic_id` int(11) NOT NULL,
  `pic_name` varchar(40) NOT NULL,
  `pic_tag` varchar(40) NOT NULL,
  `album_id` int(11) NOT NULL,
  `pic_object` varchar(100) NOT NULL,
  `pic_size` int(11) NOT NULL,
  `upload_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_pic`
--

INSERT INTO `zhengzihui_app_tb_pic` (`pic_id`, `pic_name`, `pic_tag`, `album_id`, `pic_object`, `pic_size`, `upload_time`) VALUES
(1, '1', '1', 1, 'img_for_items/2016/05/30/5a74b04f-a558-11e5-9bc0-dc85def86878.png', 0, '2016-05-30 04:00:07'),
(2, '2', '2', 2, 'img_for_items/2016/05/30/898ca07c-a658-11e5-9a27-00163e0022d3.png', 0, '2016-05-30 02:57:23'),
(3, '3', '3', 3, 'img_for_items/2016/05/30/6bd92fc0-a476-11e5-aaa1-dc85def86878.png', 0, '2016-05-30 02:57:55'),
(4, '4', '4', 4, 'img_for_items/2016/05/30/81d5f798-a658-11e5-8df7-00163e0022d3.png', 0, '2016-05-30 02:58:08'),
(5, '5', '5', 5, 'img_for_items/2016/05/30/10a3fcf2-a60b-11e5-9dc8-000c2911c434.png', 0, '2016-05-30 02:58:20'),
(6, '6', '6', 6, 'img_for_items/2016/05/30/80f77ee1-a3c0-11e5-938e-dc85def86878.png', 0, '2016-05-30 02:58:30'),
(7, '7', '7', 7, 'img_for_items/2016/05/30/848c6c1e-a265-11e5-b152-3859f9fa9803.png', 0, '2016-05-30 02:58:40'),
(8, '8', '8', 8, 'img_for_items/2016/05/30/5f38b21e-a586-11e5-b4ed-dc85def86878.png', 0, '2016-05-30 02:58:48'),
(9, '9', '9', 9, 'img_for_items/2016/05/04/6bd92fc0-a476-11e5-aaa1-dc85def86878.png', 0, '2016-05-04 09:31:05'),
(10, '10', '10', 10, 'img_for_items/2016/05/04/76c0c68f-a265-11e5-80d4-3859f9fa9803.png', 0, '2016-05-04 09:31:25'),
(11, '11', '11', 11, 'img_for_items/2016/05/04/56de86b0-a557-11e5-92af-dc85def86878.png', 0, '2016-05-04 09:32:58'),
(12, '12', '12', 12, 'img_for_items/2016/05/04/2f9f86de-a277-11e5-a84a-3859f9fa9803.png', 0, '2016-05-04 09:33:09'),
(13, '13', '13', 13, 'img_for_items/2016/05/04/9fdac0b0-a3c0-11e5-8a73-dc85def86878.png', 0, '2016-05-04 09:33:22'),
(14, '14', '14', 14, 'img_for_items/2016/05/04/98c5db1e-a3c0-11e5-b491-dc85def86878.png', 0, '2016-05-04 09:33:34'),
(15, '15', '15', 15, 'img_for_items/2016/05/04/2df0ed11-a557-11e5-8e43-dc85def86878.png', 0, '2016-05-04 09:33:51'),
(16, '16', '16', 16, 'img_for_items/2016/05/04/17675c61-a263-11e5-a423-3859f9fa9803.png', 0, '2016-05-04 09:34:08'),
(17, '17', '17', 17, 'img_for_items/2016/05/04/5be48e0f-a265-11e5-89c3-3859f9fa9803.png', 0, '2016-05-04 10:46:02'),
(18, '18', '18', 18, 'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878_v0SFX5j.png', 0, '2016-05-04 09:34:23');

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_service_provider`
--

CREATE TABLE `zhengzihui_app_tb_service_provider` (
  `sp_code` int(11) NOT NULL,
  `sp_id` int(11) NOT NULL,
  `sp_name` varchar(40) NOT NULL,
  `psw` varchar(40) NOT NULL,
  `tel` varchar(40) NOT NULL,
  `email` varchar(254) NOT NULL,
  `master` varchar(50) NOT NULL,
  `sp_image1` varchar(100) NOT NULL,
  `sp_image2` varchar(100) NOT NULL,
  `sp_grade` int(11) NOT NULL,
  `sp_sort` int(11) NOT NULL,
  `area_id` varchar(10) NOT NULL,
  `Register_cap` int(11) NOT NULL,
  `staff_number` int(11) NOT NULL,
  `Annual_totals` int(11) NOT NULL,
  `organization_name` varchar(40) NOT NULL,
  `organization_id` int(11) NOT NULL,
  `organization_assets` int(11) NOT NULL,
  `organization_profile` varchar(100) NOT NULL,
  `sp_auth` int(11) NOT NULL,
  `is_recommend` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_sysmessage`
--

CREATE TABLE `zhengzihui_app_tb_sysmessage` (
  `sys_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `mess_id` int(11) NOT NULL,
  `sys_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_user`
--

CREATE TABLE `zhengzihui_app_tb_user` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_telephone` varchar(40) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_auth` int(11) NOT NULL,
  `user_type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_user`
--

INSERT INTO `zhengzihui_app_tb_user` (`user_id`, `user_name`, `user_password`, `user_telephone`, `user_email`, `user_auth`, `user_type`) VALUES
(1, '郭捷', '1', '1@qq', '1@qq.com', 0, 1),
(2, '李泽华', '2', '2', '1@qq.com', 0, 1),
(3, '张帅帅', 'zhangshuaishuai', '3', '1@qq.com', 0, 1),
(4, '袁志', '111', '111', '1@qq.com', 0, 0),
(5, '常益凡', '111', '1111', '1@qq.com', 0, 0),
(6, '徐成章', '1111', '11111', '1@qq.com', 0, 0),
(7, '罗杰炜', '1111', '1111', '1@qq.com', 0, 0),
(8, 'test', 'test', '11111111111', '1@qq.com', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `zhengzihui_app_tb_user_expand`
--

CREATE TABLE `zhengzihui_app_tb_user_expand` (
  `user_id` int(11) NOT NULL,
  `company_tel` varchar(30) NOT NULL,
  `company_email` varchar(254) NOT NULL,
  `company_name` varchar(30) NOT NULL,
  `company_district` varchar(50) NOT NULL,
  `company_address` varchar(50) NOT NULL,
  `company_registered_capital` int(11) NOT NULL,
  `company_industry` varchar(30) NOT NULL,
  `company_stuff_no` int(11) NOT NULL,
  `company_nature` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `zhengzihui_app_tb_user_expand`
--

INSERT INTO `zhengzihui_app_tb_user_expand` (`user_id`, `company_tel`, `company_email`, `company_name`, `company_district`, `company_address`, `company_registered_capital`, `company_industry`, `company_stuff_no`, `company_nature`) VALUES
(1, '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', '四川成都市大慈寺', '四川成都市大慈寺', 100000000, '互联网科技服务', 100, '私营'),
(2, ' 111111111111', '1@qq.com', '成都融亿达科技服务有限公司', '2 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, ' 私营'),
(3, '1', '1@qq.cpm', '成都融亿达科技服务有限公司', '四川成都市大慈寺', '四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
(4, '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
(5, '111111111111', '1@qq.com', ' 四川成都市大慈寺', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
(6, '111111111111', '1@qq.com', '成都融亿达科技服务有限公', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
(7, '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, '互联网科技服务', 100, ' 私营');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `content_type_id` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `easy_thumbnails_source`
--
ALTER TABLE `easy_thumbnails_source`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `easy_thumbnails_source_storage_hash_3e1b0d13_uniq` (`storage_hash`,`name`),
  ADD KEY `easy_thumbnails_source_b454e115` (`storage_hash`),
  ADD KEY `easy_thumbnails_source_b068931c` (`name`);

--
-- Indexes for table `easy_thumbnails_thumbnail`
--
ALTER TABLE `easy_thumbnails_thumbnail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `easy_thumbnails_thumbnail_storage_hash_7ef9fce_uniq` (`storage_hash`,`name`,`source_id`),
  ADD KEY `easy_thumbnails__source_id_7106e1b7_fk_easy_thumbnails_source_id` (`source_id`),
  ADD KEY `easy_thumbnails_thumbnail_b454e115` (`storage_hash`),
  ADD KEY `easy_thumbnails_thumbnail_b068931c` (`name`);

--
-- Indexes for table `easy_thumbnails_thumbnaildimensions`
--
ALTER TABLE `easy_thumbnails_thumbnaildimensions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `thumbnail_id` (`thumbnail_id`);

--
-- Indexes for table `zhengzihui_app_tb_accessory`
--
ALTER TABLE `zhengzihui_app_tb_accessory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zhengzihui_app_tb_album`
--
ALTER TABLE `zhengzihui_app_tb_album`
  ADD PRIMARY KEY (`album_id`);

--
-- Indexes for table `zhengzihui_app_tb_apage`
--
ALTER TABLE `zhengzihui_app_tb_apage`
  ADD PRIMARY KEY (`Apage_id`);

--
-- Indexes for table `zhengzihui_app_tb_apage_class`
--
ALTER TABLE `zhengzihui_app_tb_apage_class`
  ADD PRIMARY KEY (`Apcl_id`);

--
-- Indexes for table `zhengzihui_app_tb_area`
--
ALTER TABLE `zhengzihui_app_tb_area`
  ADD PRIMARY KEY (`area_id`);

--
-- Indexes for table `zhengzihui_app_tb_article`
--
ALTER TABLE `zhengzihui_app_tb_article`
  ADD PRIMARY KEY (`article_id`);

--
-- Indexes for table `zhengzihui_app_tb_artificial_representations`
--
ALTER TABLE `zhengzihui_app_tb_artificial_representations`
  ADD PRIMARY KEY (`arre_id`);

--
-- Indexes for table `zhengzihui_app_tb_goods`
--
ALTER TABLE `zhengzihui_app_tb_goods`
  ADD PRIMARY KEY (`goods_id`);

--
-- Indexes for table `zhengzihui_app_tb_goods_class`
--
ALTER TABLE `zhengzihui_app_tb_goods_class`
  ADD PRIMARY KEY (`gocl_id`);

--
-- Indexes for table `zhengzihui_app_tb_goods_click`
--
ALTER TABLE `zhengzihui_app_tb_goods_click`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zhengzihui_app_tb_goods_evaluation`
--
ALTER TABLE `zhengzihui_app_tb_goods_evaluation`
  ADD PRIMARY KEY (`goev_id`);

--
-- Indexes for table `zhengzihui_app_tb_item`
--
ALTER TABLE `zhengzihui_app_tb_item`
  ADD PRIMARY KEY (`item_id`);

--
-- Indexes for table `zhengzihui_app_tb_item_class`
--
ALTER TABLE `zhengzihui_app_tb_item_class`
  ADD PRIMARY KEY (`itcl_id`);

--
-- Indexes for table `zhengzihui_app_tb_item_click`
--
ALTER TABLE `zhengzihui_app_tb_item_click`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zhengzihui_app_tb_item_pa`
--
ALTER TABLE `zhengzihui_app_tb_item_pa`
  ADD PRIMARY KEY (`ipa_id`);

--
-- Indexes for table `zhengzihui_app_tb_message`
--
ALTER TABLE `zhengzihui_app_tb_message`
  ADD PRIMARY KEY (`mess_id`);

--
-- Indexes for table `zhengzihui_app_tb_messagetext`
--
ALTER TABLE `zhengzihui_app_tb_messagetext`
  ADD PRIMARY KEY (`text_id`);

--
-- Indexes for table `zhengzihui_app_tb_news`
--
ALTER TABLE `zhengzihui_app_tb_news`
  ADD PRIMARY KEY (`news_id`);

--
-- Indexes for table `zhengzihui_app_tb_news_class`
--
ALTER TABLE `zhengzihui_app_tb_news_class`
  ADD PRIMARY KEY (`necl_id`);

--
-- Indexes for table `zhengzihui_app_tb_notice`
--
ALTER TABLE `zhengzihui_app_tb_notice`
  ADD PRIMARY KEY (`Notice_id`);

--
-- Indexes for table `zhengzihui_app_tb_notice_class`
--
ALTER TABLE `zhengzihui_app_tb_notice_class`
  ADD PRIMARY KEY (`Nocl_id`);

--
-- Indexes for table `zhengzihui_app_tb_order`
--
ALTER TABLE `zhengzihui_app_tb_order`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `zhengzihui_app_tb_pic`
--
ALTER TABLE `zhengzihui_app_tb_pic`
  ADD PRIMARY KEY (`pic_id`);

--
-- Indexes for table `zhengzihui_app_tb_service_provider`
--
ALTER TABLE `zhengzihui_app_tb_service_provider`
  ADD PRIMARY KEY (`sp_code`);

--
-- Indexes for table `zhengzihui_app_tb_sysmessage`
--
ALTER TABLE `zhengzihui_app_tb_sysmessage`
  ADD PRIMARY KEY (`sys_id`);

--
-- Indexes for table `zhengzihui_app_tb_user`
--
ALTER TABLE `zhengzihui_app_tb_user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `zhengzihui_app_tb_user_expand`
--
ALTER TABLE `zhengzihui_app_tb_user_expand`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=257;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `easy_thumbnails_source`
--
ALTER TABLE `easy_thumbnails_source`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `easy_thumbnails_thumbnail`
--
ALTER TABLE `easy_thumbnails_thumbnail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `easy_thumbnails_thumbnaildimensions`
--
ALTER TABLE `easy_thumbnails_thumbnaildimensions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_accessory`
--
ALTER TABLE `zhengzihui_app_tb_accessory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_apage`
--
ALTER TABLE `zhengzihui_app_tb_apage`
  MODIFY `Apage_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_artificial_representations`
--
ALTER TABLE `zhengzihui_app_tb_artificial_representations`
  MODIFY `arre_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_goods_click`
--
ALTER TABLE `zhengzihui_app_tb_goods_click`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_item_click`
--
ALTER TABLE `zhengzihui_app_tb_item_click`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_news`
--
ALTER TABLE `zhengzihui_app_tb_news`
  MODIFY `news_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_news_class`
--
ALTER TABLE `zhengzihui_app_tb_news_class`
  MODIFY `necl_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_notice`
--
ALTER TABLE `zhengzihui_app_tb_notice`
  MODIFY `Notice_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_user`
--
ALTER TABLE `zhengzihui_app_tb_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `zhengzihui_app_tb_user_expand`
--
ALTER TABLE `zhengzihui_app_tb_user_expand`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `easy_thumbnails_thumbnail`
--
ALTER TABLE `easy_thumbnails_thumbnail`
  ADD CONSTRAINT `easy_thumbnails__source_id_7106e1b7_fk_easy_thumbnails_source_id` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`);

--
-- Constraints for table `easy_thumbnails_thumbnaildimensions`
--
ALTER TABLE `easy_thumbnails_thumbnaildimensions`
  ADD CONSTRAINT `easy_thumb_thumbnail_id_314c3e84_fk_easy_thumbnails_thumbnail_id` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
