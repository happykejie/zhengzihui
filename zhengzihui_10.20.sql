-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.11-log - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 zhengzihui_test_second 的数据库结构
CREATE DATABASE IF NOT EXISTS `zhengzihui_test_second` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `zhengzihui_test_second`;


-- 导出  表 zhengzihui_test_second.auth_group 结构
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.auth_group 的数据：~0 rows (大约)
DELETE FROM `auth_group`;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_group_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.auth_group_permissions 的数据：~0 rows (大约)
DELETE FROM `auth_group_permissions`;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_permission 结构
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=175 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.auth_permission 的数据：~163 rows (大约)
DELETE FROM `auth_permission`;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
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
	(28, 'Can add 用户扩展信息', 10, 'add_tb_user_expand'),
	(29, 'Can change 用户扩展信息', 10, 'change_tb_user_expand'),
	(30, 'Can delete 用户扩展信息', 10, 'delete_tb_user_expand'),
	(31, 'Can add 用户', 11, 'add_tb_user'),
	(32, 'Can change 用户', 11, 'change_tb_user'),
	(33, 'Can delete 用户', 11, 'delete_tb_user'),
	(34, 'Can add 服务提供商', 12, 'add_tb_service_provider'),
	(35, 'Can change 服务提供商', 12, 'change_tb_service_provider'),
	(36, 'Can delete 服务提供商', 12, 'delete_tb_service_provider'),
	(37, 'Can add 新闻类别', 13, 'add_tb_news_class'),
	(38, 'Can change 新闻类别', 13, 'change_tb_news_class'),
	(39, 'Can delete 新闻类别', 13, 'delete_tb_news_class'),
	(40, 'Can add 新闻', 14, 'add_tb_news'),
	(41, 'Can change 新闻', 14, 'change_tb_news'),
	(42, 'Can delete 新闻', 14, 'delete_tb_news'),
	(43, 'Can add 公告 ', 15, 'add_tb_notice'),
	(44, 'Can change 公告 ', 15, 'change_tb_notice'),
	(45, 'Can delete 公告 ', 15, 'delete_tb_notice'),
	(46, 'Can add 公告类别', 16, 'add_tb_notice_class'),
	(47, 'Can change 公告类别', 16, 'change_tb_notice_class'),
	(48, 'Can delete 公告类别', 16, 'delete_tb_notice_class'),
	(49, 'Can add 单页表', 17, 'add_tb_apage'),
	(50, 'Can change 单页表', 17, 'change_tb_apage'),
	(51, 'Can delete 单页表', 17, 'delete_tb_apage'),
	(52, 'Can add 单页分类表', 18, 'add_tb_apage_class'),
	(53, 'Can change 单页分类表', 18, 'change_tb_apage_class'),
	(54, 'Can delete 单页分类表', 18, 'delete_tb_apage_class'),
	(55, 'Can add 项目详情表', 19, 'add_tb_item'),
	(56, 'Can change 项目详情表', 19, 'change_tb_item'),
	(57, 'Can delete 项目详情表', 19, 'delete_tb_item'),
	(58, 'Can add 项目点击表', 20, 'add_tb_item_click'),
	(59, 'Can change 项目点击表', 20, 'change_tb_item_click'),
	(60, 'Can delete 项目点击表', 20, 'delete_tb_item_click'),
	(61, 'Can add 项目发布机构表', 21, 'add_tb_item_pa'),
	(62, 'Can change 项目发布机构表', 21, 'change_tb_item_pa'),
	(63, 'Can delete 项目发布机构表', 21, 'delete_tb_item_pa'),
	(64, 'Can add tb_shoucang_item', 22, 'add_tb_shoucang_item'),
	(65, 'Can change tb_shoucang_item', 22, 'change_tb_shoucang_item'),
	(66, 'Can delete tb_shoucang_item', 22, 'delete_tb_shoucang_item'),
	(67, 'Can add tb_shoucang_goods', 23, 'add_tb_shoucang_goods'),
	(68, 'Can change tb_shoucang_goods', 23, 'change_tb_shoucang_goods'),
	(69, 'Can delete tb_shoucang_goods', 23, 'delete_tb_shoucang_goods'),
	(70, 'Can add 地区表', 24, 'add_tb_area'),
	(71, 'Can change 地区表', 24, 'change_tb_area'),
	(72, 'Can delete 地区表', 24, 'delete_tb_area'),
	(73, 'Can add 项目分类', 25, 'add_tb_item_class'),
	(74, 'Can change 项目分类', 25, 'change_tb_item_class'),
	(75, 'Can delete 项目分类', 25, 'delete_tb_item_class'),
	(76, 'Can add 文章表', 26, 'add_tb_article'),
	(77, 'Can change 文章表', 26, 'change_tb_article'),
	(78, 'Can delete 文章表', 26, 'delete_tb_article'),
	(79, 'Can add 相册表', 27, 'add_tb_album'),
	(80, 'Can change 相册表', 27, 'change_tb_album'),
	(81, 'Can delete 相册表', 27, 'delete_tb_album'),
	(82, 'Can add 图片表', 28, 'add_tb_pic'),
	(83, 'Can change 图片表', 28, 'change_tb_pic'),
	(84, 'Can delete 图片表', 28, 'delete_tb_pic'),
	(85, 'Can add 其他附件表', 29, 'add_tb_accessory'),
	(86, 'Can change 其他附件表', 29, 'change_tb_accessory'),
	(87, 'Can delete 其他附件表', 29, 'delete_tb_accessory'),
	(88, 'Can add 人工申述表', 30, 'add_tb_artificial_representations'),
	(89, 'Can change 人工申述表', 30, 'change_tb_artificial_representations'),
	(90, 'Can delete 人工申述表', 30, 'delete_tb_artificial_representations'),
	(91, 'Can add 站内短信表', 31, 'add_tb_message'),
	(92, 'Can change 站内短信表', 31, 'change_tb_message'),
	(93, 'Can delete 站内短信表', 31, 'delete_tb_message'),
	(94, 'Can add 站内短信内容表', 32, 'add_tb_messagetext'),
	(95, 'Can change 站内短信内容表', 32, 'change_tb_messagetext'),
	(96, 'Can delete 站内短信内容表', 32, 'delete_tb_messagetext'),
	(97, 'Can add 系统信息表', 33, 'add_tb_sysmessage'),
	(98, 'Can change 系统信息表', 33, 'change_tb_sysmessage'),
	(99, 'Can delete 系统信息表', 33, 'delete_tb_sysmessage'),
	(100, 'Can add 服务商信息表', 34, 'add_tb_goods'),
	(101, 'Can change 服务商信息表', 34, 'change_tb_goods'),
	(102, 'Can delete 服务商信息表', 34, 'delete_tb_goods'),
	(103, 'Can add 服务商点击表', 35, 'add_tb_goods_click'),
	(104, 'Can change 服务商点击表', 35, 'change_tb_goods_click'),
	(105, 'Can delete 服务商点击表', 35, 'delete_tb_goods_click'),
	(106, 'Can add 服务商分类表', 36, 'add_tb_goods_class'),
	(107, 'Can change 服务商分类表', 36, 'change_tb_goods_class'),
	(108, 'Can delete 服务商分类表', 36, 'delete_tb_goods_class'),
	(109, 'Can add 服务商评价表', 37, 'add_tb_goods_evaluation'),
	(110, 'Can change 服务商评价表', 37, 'change_tb_goods_evaluation'),
	(111, 'Can delete 服务商评价表', 37, 'delete_tb_goods_evaluation'),
	(112, 'Can add 订单表', 38, 'add_tb_order'),
	(113, 'Can change 订单表', 38, 'change_tb_order'),
	(114, 'Can delete 订单表', 38, 'delete_tb_order'),
	(115, 'Can add tb_companyuser', 39, 'add_tb_companyuser'),
	(116, 'Can change tb_companyuser', 39, 'change_tb_companyuser'),
	(117, 'Can delete tb_companyuser', 39, 'delete_tb_companyuser'),
	(118, 'Can add tb_customcompany', 40, 'add_tb_customcompany'),
	(119, 'Can change tb_customcompany', 40, 'change_tb_customcompany'),
	(120, 'Can delete tb_customcompany', 40, 'delete_tb_customcompany'),
	(121, 'Can add 待测服务信息表', 41, 'add_tb_goods_wfc'),
	(122, 'Can change 待测服务信息表', 41, 'change_tb_goods_wfc'),
	(123, 'Can delete 待测服务信息表', 41, 'delete_tb_goods_wfc'),
	(124, 'Can add f require info', 42, 'add_frequireinfo'),
	(125, 'Can change f require info', 42, 'change_frequireinfo'),
	(126, 'Can delete f require info', 42, 'delete_frequireinfo'),
	(127, 'Can add tb_balist', 43, 'add_tb_balist'),
	(128, 'Can change tb_balist', 43, 'change_tb_balist'),
	(129, 'Can delete tb_balist', 43, 'delete_tb_balist'),
	(130, 'Can add 后台用户', 44, 'add_tb_back_user'),
	(131, 'Can change 后台用户', 44, 'change_tb_back_user'),
	(132, 'Can delete 后台用户', 44, 'delete_tb_back_user'),
	(133, 'Can add 政资信息共享', 45, 'add_shareinformation'),
	(134, 'Can change 政资信息共享', 45, 'change_shareinformation'),
	(135, 'Can delete 政资信息共享', 45, 'delete_shareinformation'),
	(136, 'Can add 政资信息发布人', 46, 'add_linker'),
	(137, 'Can change 政资信息发布人', 46, 'change_linker'),
	(138, 'Can delete 政资信息发布人', 46, 'delete_linker'),
	(139, 'Can add push_info', 47, 'add_push_info'),
	(140, 'Can change push_info', 47, 'change_push_info'),
	(141, 'Can delete push_info', 47, 'delete_push_info'),
	(142, 'Can add sc_item', 48, 'add_sc_item'),
	(143, 'Can change sc_item', 48, 'change_sc_item'),
	(144, 'Can delete sc_item', 48, 'delete_sc_item'),
	(145, 'Can add 项目点击表', 49, 'add_sc_item_click'),
	(146, 'Can change 项目点击表', 49, 'change_sc_item_click'),
	(147, 'Can delete 项目点击表', 49, 'delete_sc_item_click'),
	(148, 'Can add 相册表', 50, 'add_sc_album'),
	(149, 'Can change 相册表', 50, 'change_sc_album'),
	(150, 'Can delete 相册表', 50, 'delete_sc_album'),
	(151, 'Can add 图片表', 51, 'add_sc_pic'),
	(152, 'Can change 图片表', 51, 'change_sc_pic'),
	(153, 'Can delete 图片表', 51, 'delete_sc_pic'),
	(154, 'Can add 文章表', 52, 'add_sc_article'),
	(155, 'Can change 文章表', 52, 'change_sc_article'),
	(156, 'Can delete 文章表', 52, 'delete_sc_article'),
	(157, 'Can add tb_ba_for_merchant_superivisor', 53, 'add_tb_ba_for_merchant_superivisor'),
	(158, 'Can change tb_ba_for_merchant_superivisor', 53, 'change_tb_ba_for_merchant_superivisor'),
	(159, 'Can delete tb_ba_for_merchant_superivisor', 53, 'delete_tb_ba_for_merchant_superivisor'),
	(160, 'Can add 图片表', 54, 'add_tb_rongzi_fuwu_pic'),
	(161, 'Can change 图片表', 54, 'change_tb_rongzi_fuwu_pic'),
	(162, 'Can delete 图片表', 54, 'delete_tb_rongzi_fuwu_pic'),
	(163, 'Can add 融资服务商', 55, 'add_tb_rongzi_fuwu_sp'),
	(164, 'Can change 融资服务商', 55, 'change_tb_rongzi_fuwu_sp'),
	(165, 'Can delete 融资服务商', 55, 'delete_tb_rongzi_fuwu_sp'),
	(166, 'Can add tb_rongzi_fuwu_service', 56, 'add_tb_rongzi_fuwu_service'),
	(167, 'Can change tb_rongzi_fuwu_service', 56, 'change_tb_rongzi_fuwu_service'),
	(168, 'Can delete tb_rongzi_fuwu_service', 56, 'delete_tb_rongzi_fuwu_service'),
	(169, 'Can add tb_rongzi_item', 57, 'add_tb_rongzi_item'),
	(170, 'Can change tb_rongzi_item', 57, 'change_tb_rongzi_item'),
	(171, 'Can delete tb_rongzi_item', 57, 'delete_tb_rongzi_item'),
	(172, 'Can add sp_inservice_area', 58, 'add_sp_inservice_area'),
	(173, 'Can change sp_inservice_area', 58, 'change_sp_inservice_area'),
	(174, 'Can delete sp_inservice_area', 58, 'delete_sp_inservice_area');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_user 结构
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.auth_user 的数据：~0 rows (大约)
DELETE FROM `auth_user`;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$24000$vrePNmsfkowk$6tslXw/PW6FIHwaJdhn4t6OnDNvnyOVyTDv4FD0tInI=', '2016-07-19 08:42:44', 1, 'admin', '', '', 'oeiro@qq.com', 1, 1, '2016-07-19 08:42:36');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_user_groups 结构
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.auth_user_groups 的数据：~0 rows (大约)
DELETE FROM `auth_user_groups`;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_user_user_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.auth_user_user_permissions 的数据：~0 rows (大约)
DELETE FROM `auth_user_user_permissions`;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_admin_log 结构
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.django_admin_log 的数据：~0 rows (大约)
DELETE FROM `django_admin_log`;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_content_type 结构
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.django_content_type 的数据：~55 rows (大约)
DELETE FROM `django_content_type`;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(4, 'admin', 'logentry'),
	(6, 'auth', 'group'),
	(5, 'auth', 'permission'),
	(7, 'auth', 'user'),
	(8, 'contenttypes', 'contenttype'),
	(1, 'easy_thumbnails', 'source'),
	(2, 'easy_thumbnails', 'thumbnail'),
	(3, 'easy_thumbnails', 'thumbnaildimensions'),
	(42, 'fr_app', 'frequireinfo'),
	(50, 'fr_app', 'sc_album'),
	(52, 'fr_app', 'sc_article'),
	(48, 'fr_app', 'sc_item'),
	(49, 'fr_app', 'sc_item_click'),
	(51, 'fr_app', 'sc_pic'),
	(9, 'sessions', 'session'),
	(46, 'zhengzihui_app', 'linker'),
	(47, 'zhengzihui_app', 'push_info'),
	(45, 'zhengzihui_app', 'shareinformation'),
	(58, 'zhengzihui_app', 'sp_inservice_area'),
	(29, 'zhengzihui_app', 'tb_accessory'),
	(27, 'zhengzihui_app', 'tb_album'),
	(17, 'zhengzihui_app', 'tb_apage'),
	(18, 'zhengzihui_app', 'tb_apage_class'),
	(24, 'zhengzihui_app', 'tb_area'),
	(26, 'zhengzihui_app', 'tb_article'),
	(30, 'zhengzihui_app', 'tb_artificial_representations'),
	(53, 'zhengzihui_app', 'tb_ba_for_merchant_superivisor'),
	(44, 'zhengzihui_app', 'tb_back_user'),
	(43, 'zhengzihui_app', 'tb_balist'),
	(39, 'zhengzihui_app', 'tb_companyuser'),
	(40, 'zhengzihui_app', 'tb_customcompany'),
	(34, 'zhengzihui_app', 'tb_goods'),
	(36, 'zhengzihui_app', 'tb_goods_class'),
	(35, 'zhengzihui_app', 'tb_goods_click'),
	(37, 'zhengzihui_app', 'tb_goods_evaluation'),
	(41, 'zhengzihui_app', 'tb_goods_wfc'),
	(19, 'zhengzihui_app', 'tb_item'),
	(25, 'zhengzihui_app', 'tb_item_class'),
	(20, 'zhengzihui_app', 'tb_item_click'),
	(21, 'zhengzihui_app', 'tb_item_pa'),
	(31, 'zhengzihui_app', 'tb_message'),
	(32, 'zhengzihui_app', 'tb_messagetext'),
	(14, 'zhengzihui_app', 'tb_news'),
	(13, 'zhengzihui_app', 'tb_news_class'),
	(15, 'zhengzihui_app', 'tb_notice'),
	(16, 'zhengzihui_app', 'tb_notice_class'),
	(38, 'zhengzihui_app', 'tb_order'),
	(28, 'zhengzihui_app', 'tb_pic'),
	(54, 'zhengzihui_app', 'tb_rongzi_fuwu_pic'),
	(56, 'zhengzihui_app', 'tb_rongzi_fuwu_service'),
	(55, 'zhengzihui_app', 'tb_rongzi_fuwu_sp'),
	(57, 'zhengzihui_app', 'tb_rongzi_item'),
	(12, 'zhengzihui_app', 'tb_service_provider'),
	(23, 'zhengzihui_app', 'tb_shoucang_goods'),
	(22, 'zhengzihui_app', 'tb_shoucang_item'),
	(33, 'zhengzihui_app', 'tb_sysmessage'),
	(11, 'zhengzihui_app', 'tb_user'),
	(10, 'zhengzihui_app', 'tb_user_expand');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_migrations 结构
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.django_migrations 的数据：~47 rows (大约)
DELETE FROM `django_migrations`;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2016-07-27 07:15:40'),
	(2, 'auth', '0001_initial', '2016-07-27 07:15:40'),
	(3, 'admin', '0001_initial', '2016-07-27 07:15:41'),
	(4, 'contenttypes', '0002_remove_content_type_name', '2016-07-27 07:15:41'),
	(5, 'auth', '0002_alter_permission_name_max_length', '2016-07-27 07:15:41'),
	(6, 'auth', '0003_alter_user_email_max_length', '2016-07-27 07:15:41'),
	(7, 'auth', '0004_alter_user_username_opts', '2016-07-27 07:15:41'),
	(8, 'auth', '0005_alter_user_last_login_null', '2016-07-27 07:15:41'),
	(9, 'auth', '0006_require_contenttypes_0002', '2016-07-27 07:15:41'),
	(10, 'easy_thumbnails', '0001_initial', '2016-07-27 07:15:41'),
	(11, 'easy_thumbnails', '0002_thumbnaildimensions', '2016-07-27 07:15:41'),
	(12, 'sessions', '0001_initial', '2016-07-27 07:15:41'),
	(13, 'zhengzihui_app', '0001_initial', '2016-07-27 07:15:42'),
	(14, 'zhengzihui_app', '0002_auto_20160901_0132', '2016-09-01 01:33:10'),
	(15, 'zhengzihui_app', '0003_auto_20160901_0136', '2016-09-01 01:36:07'),
	(16, 'zhengzihui_app', '0004_auto_20160901_0933', '2016-09-01 09:35:07'),
	(17, 'zhengzihui_app', '0005_auto_20160901_0933', '2016-09-01 09:35:07'),
	(18, 'zhengzihui_app', '0006_tb_goods_goods_fanli', '2016-09-01 09:35:08'),
	(19, 'zhengzihui_app', '0007_auto_20160901_0950', '2016-09-01 09:50:26'),
	(20, 'zhengzihui_app', '0008_auto_20160901_1129', '2016-09-01 11:29:54'),
	(21, 'zhengzihui_app', '0009_auto_20160901_1131', '2016-09-01 11:31:05'),
	(22, 'zhengzihui_app', '0010_auto_20160901_1141', '2016-09-01 11:41:56'),
	(23, 'zhengzihui_app', '0011_auto_20160901_1144', '2016-09-01 11:44:54'),
	(24, 'admin', '0002_logentry_remove_auto_add', '2016-09-02 05:03:39'),
	(25, 'auth', '0007_alter_validators_add_error_messages', '2016-09-02 05:03:40'),
	(26, 'zhengzihui_app', '0002_tb_order_has_pay', '2016-09-02 05:59:51'),
	(27, 'zhengzihui_app', '0003_tb_order_finish_percentage', '2016-09-02 08:08:40'),
	(28, 'zhengzihui_app', '0004_tb_notice_notice_short_content', '2016-09-03 12:28:09'),
	(29, 'fr_app', '0001_initial', '2016-09-10 08:33:35'),
	(30, 'fr_app', '0002_auto_20160730_1105', '2016-09-10 08:33:35'),
	(31, 'fr_app', '0003_auto_20160730_1230', '2016-09-10 08:33:35'),
	(32, 'zhengzihui_app', '0002_tb_balist', '2016-09-10 08:33:35'),
	(33, 'zhengzihui_app', '0003_tb_balist_ba_belong', '2016-09-10 08:33:35'),
	(34, 'zhengzihui_app', '0004_tb_goods_goods_area', '2016-09-10 08:33:35'),
	(35, 'zhengzihui_app', '0005_tb_balist_ba_time', '2016-09-10 13:27:38'),
	(36, 'zhengzihui_app', '0006_tb_balist_ba_ftime', '2016-09-12 03:41:28'),
	(37, 'zhengzihui_app', '0007_tb_goods_evaluation_location', '2016-09-12 11:24:18'),
	(38, 'zhengzihui_app', '0007_tb_back_user', '2016-09-19 02:53:14'),
	(39, 'zhengzihui_app', '0008_merge', '2016-09-19 02:53:14'),
	(40, 'zhengzihui_app', '0009_linker_shareinformation', '2016-09-19 02:53:15'),
	(41, 'zhengzihui_app', '0010_auto_20160919_0548', '2016-09-19 05:48:48'),
	(42, 'zhengzihui_app', '0011_push_info', '2016-09-19 08:09:59'),
	(43, 'zhengzihui_app', '0002_tb_service_provider_sp_address', '2016-09-20 12:35:12'),
	(44, 'zhengzihui_app', '0002_auto_20161013_1649', '2016-10-13 08:50:46'),
	(45, 'zhengzihui_app', '0002_auto_20161018_1032', '2016-10-19 23:17:50'),
	(46, 'zhengzihui_app', '0003_auto_20161020_0717', '2016-10-19 23:18:56'),
	(47, 'zhengzihui_app', '0004_auto_20161020_0732', '2016-10-19 23:32:30'),
	(48, 'zhengzihui_app', '0005_sp_inservice_area', '2016-10-19 23:39:13');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_session 结构
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.django_session 的数据：~33 rows (大约)
DELETE FROM `django_session`;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('49nrhv16js51c196nndrxuocwy7ii7nf', 'ZDFhM2M2N2JiMTZjN2IwOWE1ZmI2YTAxZTFhMGQ2OTNmMWZjOWY3Yzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJzZWFyY2hfY29udGVudCI6Ilx1NTE3Ylx1NmI5NiJ9', '2016-10-31 08:18:12'),
	('4f5mpio9ula0pskfpo7emo11w7uor5i6', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-08 02:34:08'),
	('4oy50am4450gquu65n6rv5178qamq732', 'YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-26 12:47:49'),
	('4wmm56o2l1o07zqc77tokrcv1u36kh4h', 'YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-05 08:43:26'),
	('63zeqfqqyfysbhepkvf3ymxl4z4li07e', 'MzIyZTE2NjhmMTNmNGM4Njk2MTdjMmZlZWQ0OThiYmI1Yjk2NWQ5Mzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiZm9yX3NvcnRfaXRlbWlkIjoxLCJqaWJpZSI6Ilx1NTE2OFx1OTBlOCJ9', '2016-10-28 09:56:00'),
	('7meh46fget24szd6zl1y0x2ewcfacgr9', 'ODIwZWEwMjg3NWFmODVlZmVlNTdmODlhNDk1NTVmZDI3NWE1NTBhMTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJmb3Jfc29ydF9pdGVtaWQiOjEsInpodWFuZ3RhaSI6Ilx1NTE2OFx1OTBlOCJ9', '2016-08-08 02:32:09'),
	('7qganljyjdteufpclr2zgya0lweb31dr', 'NDRiOWVjMmJjZTUwYTYyYjIxNWUyOTk1NGVjYjFjMzRlYjZlODJjNzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImppYmllIjoiXHU1MTY4XHU5MGU4IiwiZm9yX3NvcnRfaXRlbWlkIjoxLCJfYXV0aF91c2VyX2hhc2giOiIwMGVjMmNjMmNlOTIzMWNmOTM0YTk1NmJmMDUzNTU3NTcyYjI5ZDgxIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4In0=', '2016-08-02 13:47:25'),
	('7wtcpe5m2w9gocwire5pfn16baqg191g', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-08 02:36:12'),
	('8cnjppe9td9g8l2p5476l2ka3jce2tly', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-10-31 23:30:25'),
	('8mqzg7nc4l4qbws0a0z7nn02ou3879ny', 'MmMyYWRiMmY0MTgxYzRjMTZlNTM5ZWM2ZTU5ZDgxOTk5ZjU5ZGE3ODp7ImZvcl9zb3J0X2l0ZW1pZCI6MX0=', '2016-09-15 11:09:32'),
	('9dp6w2jpzdshzbwazoipe3bfvnxohly2', 'MmMyYWRiMmY0MTgxYzRjMTZlNTM5ZWM2ZTU5ZDgxOTk5ZjU5ZGE3ODp7ImZvcl9zb3J0X2l0ZW1pZCI6MX0=', '2016-09-14 02:03:29'),
	('9rooe4o0xd1zgrvg2gcx7w2i4cz31zj0', 'ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-10 07:54:27'),
	('9v3d5j0e9mkc1papf5sj78hxf7but63n', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-10-26 22:09:49'),
	('ayfwmhi2pyb2amamddqfx0hzrfe5iu2x', 'ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-12 01:50:29'),
	('fb32vczafm3s4un0vm6tt7hgrk41rdfw', 'ZWViNTEyZGQ5MzFlMjc4YTI3ZjIyZjg4MGI0M2MzYTc5NTFhYWRhNTp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-14 01:51:07'),
	('g74t7umm0bkaxfi5i4jawotb2946jwbd', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-13 10:53:09'),
	('gd580dkz0eyrrr11wafgqjbsyftxgmbg', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-10 07:36:30'),
	('joww0tnnuyzx64fizw66yju46nsr89v4', 'ZWViNTEyZGQ5MzFlMjc4YTI3ZjIyZjg4MGI0M2MzYTc5NTFhYWRhNTp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-27 08:47:56'),
	('jte5918udzemcttox2lib7ct4x4tleq6', 'YTNlN2I3NzhhYzgwMDg3YWFhYzJkZWU2MGRjZGQxNmU4OWJlOWUzZDp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJmb3Jfc29ydF9pdGVtaWQiOjEsInpodWFuZ3RhaSI6Ilx1NTE2OFx1OTBlOCJ9', '2016-10-04 12:14:45'),
	('jyh3e3h927q7oog3vywep3l99g2zwnl7', 'MzIyZTE2NjhmMTNmNGM4Njk2MTdjMmZlZWQ0OThiYmI1Yjk2NWQ5Mzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiZm9yX3NvcnRfaXRlbWlkIjoxLCJqaWJpZSI6Ilx1NTE2OFx1OTBlOCJ9', '2016-08-08 09:09:32'),
	('l9nn59s7a5ap3mzjjhvru9bmkdnz2zww', 'ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-05 02:44:08'),
	('nqm97t1ub2p75ti774pan024x3bon6a4', 'YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-10-23 02:20:27'),
	('phc6fb7clhmsu5scv2pjm5rq6t71ktu5', 'OWMyYTI1ZmFkMzA1ZmNkNGNmOTU5YTVlMWY3YmRhMDk2NDliYWY0MDp7ImJ1bWVuIjoiXHU3OWQxXHU2MjgwXHU2YzQ3Olx1NzlkMVx1NjI4MC9cdTU5MjdcdTY1NzBcdTYzNmUvXHU2NmY0XHU1OTFhIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiZm9yX3NvcnRfaXRlbWlkIjoxLCJqaWJpZSI6Ilx1NTE2OFx1OTBlOCIsInNlYXJjaF9jb250ZW50IjoiIn0=', '2016-10-06 06:37:21'),
	('qy5mld7xggy4og300tz0xrr1soi20f1d', 'ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-12 01:51:11'),
	('rx2skr0pks0psj8zcg2n95gmgj3l9t1n', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-10 07:35:13'),
	('soc0ewzrtb57paef5y0i2h1w87o0rxg3', 'YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-10-22 01:14:45'),
	('t55odyzfjrf4oewehidfei9l3idpcxbq', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-10 07:21:35'),
	('u1dlowsx3fj2flr9u5dy36ixb28o2sq7', 'ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==', '2016-10-23 05:53:41'),
	('ujrqepvum9v5hy7hvullymige53l6rk5', 'Y2ZiNGYyZGI2NjdlNjdjNzkxYjIzMDljMDViMjFiMWUxYzQ2ZjczYzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiZmlyc3RfcGFnZSI6MCwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJmb3Jfc29ydF9pdGVtaWQiOjF9', '2016-09-19 09:00:12'),
	('v4hb70vg8u8vdeqki0lph37wbvuqueyk', 'MjFlODlmMTFhNmZmYTk5OTg1ZTA2OTFjNTE4MDQ2ZTAwYTU0NzJkNjp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJyb25nemlfZmlyc3RjbGFzcyI6Ilx1ODBhMVx1Njc0M1x1ODc4ZFx1OGQ0NCIsImZvcl9zb3J0X2l0ZW1pZCI6MSwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4Iiwicm9uZ3ppX2ZpbHRlcmtleXMiOiJcdTUxNjhcdTkwZTgifQ==', '2016-11-02 22:26:13'),
	('v8x6esqk69i3vzixb23qh9pl1pz9iep0', 'ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-08-10 08:08:11'),
	('wx2peycobkerdqro2ir6nwdag0hlrr27', 'YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==', '2016-09-13 11:44:16'),
	('y3felqj8n9k2wc85vow7st4fy0oi158f', 'OTVhMGVhNTYyMGIyMzBlYWNjMTU0OGE0NmQ4ZDBlZWU5MDg3ZTdkZTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiZmlyc3RjbGFzcyI6ImJ1bWVuX2NsYXNzMSIsImppYmllIjoiXHU1MTY4XHU5MGU4Iiwicm9uZ3ppX2ZpcnN0Y2xhc3MiOiJcdTgwYTFcdTY3NDNcdTg3OGRcdThkNDQiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgiLCJyb25nemlfZmlsdGVya2V5cyI6Ilx1NTkyOVx1NGY3Zlx1NjI5NVx1OGQ0NCJ9', '2016-10-27 13:36:10');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.easy_thumbnails_source 结构
CREATE TABLE IF NOT EXISTS `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_storage_hash_40116450c1e4f2ed_uniq` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_source_b068931c` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.easy_thumbnails_source 的数据：~0 rows (大约)
DELETE FROM `easy_thumbnails_source`;
/*!40000 ALTER TABLE `easy_thumbnails_source` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_source` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.easy_thumbnails_thumbnail 结构
CREATE TABLE IF NOT EXISTS `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_thumbnail_storage_hash_66cc758d07ef9fce_uniq` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thu_source_id_50b260de7106e1b7_fk_easy_thumbnails_source_id` (`source_id`),
  KEY `easy_thumbnails_thumbnail_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_b068931c` (`name`),
  CONSTRAINT `easy_thu_source_id_50b260de7106e1b7_fk_easy_thumbnails_source_id` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.easy_thumbnails_thumbnail 的数据：~0 rows (大约)
DELETE FROM `easy_thumbnails_thumbnail`;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.easy_thumbnails_thumbnaildimensions 结构
CREATE TABLE IF NOT EXISTS `easy_thumbnails_thumbnaildimensions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thumbnail_id` int(11) NOT NULL,
  `width` int(10) unsigned DEFAULT NULL,
  `height` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thumbnail_id` (`thumbnail_id`),
  CONSTRAINT `ea_thumbnail_id_29ad34faceb3c17c_fk_easy_thumbnails_thumbnail_id` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.easy_thumbnails_thumbnaildimensions 的数据：~0 rows (大约)
DELETE FROM `easy_thumbnails_thumbnaildimensions`;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.fr_app_frequireinfo 结构
CREATE TABLE IF NOT EXISTS `fr_app_frequireinfo` (
  `info_id` int(11) NOT NULL AUTO_INCREMENT,
  `mobile_num` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `require_type` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `require_describe` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `news_time` datetime NOT NULL,
  PRIMARY KEY (`info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.fr_app_frequireinfo 的数据：~0 rows (大约)
DELETE FROM `fr_app_frequireinfo`;
/*!40000 ALTER TABLE `fr_app_frequireinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `fr_app_frequireinfo` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_linker 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_linker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `linkname` varchar(20) NOT NULL,
  `linkemail` varchar(254) NOT NULL,
  `linkadress` varchar(30) NOT NULL,
  `linktelphon` varchar(11) NOT NULL,
  `remarks` longtext NOT NULL,
  `secret` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_linker 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_linker`;
/*!40000 ALTER TABLE `zhengzihui_app_linker` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_linker` (`id`, `linkname`, `linkemail`, `linkadress`, `linktelphon`, `remarks`, `secret`) VALUES
	(1, 'yz', 'dks@qq.com', 'sdk', 'sk', 'dks', 'YES');
/*!40000 ALTER TABLE `zhengzihui_app_linker` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_push_info 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_push_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `push_item_id` int(11) NOT NULL,
  `push_to_user` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_push_info 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_push_info`;
/*!40000 ALTER TABLE `zhengzihui_app_push_info` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_push_info` (`id`, `push_item_id`, `push_to_user`) VALUES
	(8, 3, 1),
	(9, 1, 9);
/*!40000 ALTER TABLE `zhengzihui_app_push_info` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_shareinformation 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_shareinformation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectname` varchar(20) NOT NULL,
  `projectdirect` varchar(20) NOT NULL,
  `projectneed` varchar(30) NOT NULL,
  `projectprocess` longtext NOT NULL,
  `projectmanage` varchar(20) NOT NULL,
  `projectlink` varchar(20) NOT NULL,
  `projectsecret` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_shareinformation 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_shareinformation`;
/*!40000 ALTER TABLE `zhengzihui_app_shareinformation` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_shareinformation` (`id`, `projectname`, `projectdirect`, `projectneed`, `projectprocess`, `projectmanage`, `projectlink`, `projectsecret`) VALUES
	(1, '可爱', '是打开', '耷拉到沙发', '尔瓦而', '任务而', '12133', 'N1');
/*!40000 ALTER TABLE `zhengzihui_app_shareinformation` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_sp_inservice_area 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_sp_inservice_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `privince` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `distr` varchar(100) DEFAULT NULL,
  `xianfen` varchar(100) DEFAULT NULL,
  `sp_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_sp_inservice_area 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_sp_inservice_area`;
/*!40000 ALTER TABLE `zhengzihui_app_sp_inservice_area` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_sp_inservice_area` (`id`, `privince`, `city`, `distr`, `xianfen`, `sp_id`) VALUES
	(1, NULL, '北京市市辖区', '东城区', '默认县份', 3),
	(2, '北京市', '北京市市辖区', '东城区', '默认县份', 3),
	(3, '内蒙古自治区', '呼和浩特市', '新城区', '默认县份', 3);
/*!40000 ALTER TABLE `zhengzihui_app_sp_inservice_area` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_accessory 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_accessory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anne_id` int(11) NOT NULL,
  `comm_id` int(11) NOT NULL,
  `apubdate` int(11) NOT NULL,
  `apublisher` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `aposition` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `aaddtion` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_accessory 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_accessory`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_accessory` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_accessory` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_album 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_album` (
  `album_id` int(11) NOT NULL,
  `album_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `album_type` int(11) NOT NULL,
  `affiliation_id` int(11) NOT NULL,
  `nacl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nacl_sort` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  `is_default` int(11) NOT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_album 的数据：~18 rows (大约)
DELETE FROM `zhengzihui_app_tb_album`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_album` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_album` (`album_id`, `album_name`, `album_type`, `affiliation_id`, `nacl_des`, `nacl_sort`, `upload_time`, `is_default`) VALUES
	(1, '1', 0, 1, '1', 1, '2016-05-01 04:38:30', 1),
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
/*!40000 ALTER TABLE `zhengzihui_app_tb_album` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_apage 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_apage` (
  `Apage_id` int(11) NOT NULL AUTO_INCREMENT,
  `Article_id` int(11) NOT NULL,
  `Has_album` int(11) NOT NULL,
  `Apage_time` date NOT NULL,
  `Apage_source` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Apcl_id` int(11) NOT NULL,
  `Apage_sort` int(11) NOT NULL,
  `Apage_is_display` int(11) NOT NULL,
  PRIMARY KEY (`Apage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_apage 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_apage`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_apage_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_apage_class` (
  `Apcl_id` int(11) NOT NULL,
  `Apcl_code` int(11) NOT NULL,
  `Apcl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Apcl_parent_id` int(11) NOT NULL,
  `Apcl_sort` int(11) NOT NULL,
  PRIMARY KEY (`Apcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_apage_class 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_apage_class`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_area 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_area` (
  `area_id` int(11) NOT NULL,
  `area_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `area_parent_id` int(11) NOT NULL,
  `area_sort` int(11) NOT NULL,
  `area_deep` int(11) NOT NULL,
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_area 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_area`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_area` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_article 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_article` (
  `article_id` int(11) NOT NULL,
  `article_code` int(11) NOT NULL,
  `article_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `author` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `author_email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `article_type` int(11) NOT NULL,
  `affiliation_id` int(11) NOT NULL,
  `article_content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `article_keywords` longtext COLLATE utf8_unicode_ci NOT NULL,
  `article_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `article_sort` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  `is_default` int(11) NOT NULL,
  `article_click` int(11) NOT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_article 的数据：~3 rows (大约)
DELETE FROM `zhengzihui_app_tb_article`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_article` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_article` (`article_id`, `article_code`, `article_name`, `author`, `author_email`, `article_type`, `affiliation_id`, `article_content`, `article_keywords`, `article_des`, `article_sort`, `upload_time`, `is_default`, `article_click`) VALUES
	(1, 1, '2016科技厅关于科技计划项目的申报通知	', '1', '1@qq.com', 0, 1, '     近日，四川省教育考试院来函批复，同意西华大学今年将22个本科专业调整到本科一批次录取。加上去年纳入本科一批次招生的21个专业，2016年西华大学共有43个专业纳入本科一批次在川招生，预计该校普通本科一本批次招生计划将占普通本科总计划数的60%。', '1', '1', 1, '2016-05-07 11:18:51', 1, 1),
	(2, 2, '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '1111@sina.com', 0, 2, '金正恩在讲话中高度肯定了朝鲜在今年1月份的核试验和2月份的火箭发射所取得的“前所未有”的伟大成就。\r\n　　朝鲜劳动党第七次全国代表大会6日在平壤开幕，朝中社当天曾发布一万多字的长篇报道称“开发小型核弹头是送给劳动党七大的礼物”。\r\n　　报道称，开发小型核弹头、弹道火箭重返大气层环境模拟试验取得成功、进行高功率固体火箭发动机地上点火及级间分离试验、进行新型洲际弹道火箭大功率发动机地上点火试验是朝鲜国防科技人员向劳动党七大献礼。\r\n　　此前，金正恩的西装照片几乎只出现在朝鲜对外公布的领导人官方照片中。\r\n　　韩国电视台对朝鲜电视台金正恩的讲话做了报道评论。韩国分析人士认为，朝鲜劳动党七大日程表一开始就未包含进行第五次核试验。而朝鲜是否举行第五次核试验，这也是韩国方面此前最担心的事情。', '111111111111111111111111111', '1', 1, '2016-05-07 11:20:34', 1, 1),
	(3, 3, '3', '3', '1111@sina.com', 0, 3, '从去年开始，川内不少老牌二本院校就将大批二本专业调整至一本招生，今年这一趋势仍在继续，再加上去年四川合并二、三本批次，各个批次的界限越来越模糊，这背后将会给考生们带来什么样的影响？考生们在志愿填报上应有哪些应对之策？记者采访了相关专家。', '3', '3', 3, '2016-05-07 11:19:51', 1, 3);
/*!40000 ALTER TABLE `zhengzihui_app_tb_article` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_artificial_representations 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_artificial_representations` (
  `arre_id` int(11) NOT NULL AUTO_INCREMENT,
  `arre_title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `arre_content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `arre_state` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`arre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_artificial_representations 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_artificial_representations`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_artificial_representations` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_artificial_representations` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_back_user 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_back_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_telephone` varchar(40) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_auth` int(11) NOT NULL,
  `user_type` int(11) NOT NULL,
  `last_login` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_back_user 的数据：~1 rows (大约)
DELETE FROM `zhengzihui_app_tb_back_user`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_back_user` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_back_user` (`user_id`, `user_name`, `user_password`, `user_telephone`, `user_email`, `user_auth`, `user_type`, `last_login`) VALUES
	(1, 'yz', '123', '5654645', 'skjkd@', 1, 2, '2016-10-17 08:07:06'),
	(2, 'test', '123456', '13231', '', 1, 2, '2016-09-21 20:34:26');
/*!40000 ALTER TABLE `zhengzihui_app_tb_back_user` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_balist 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_balist` (
  `ba_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_no` int(11) NOT NULL,
  `ba_sta` int(11) NOT NULL,
  `ba_belong` int(11) NOT NULL,
  `ba_time` datetime DEFAULT NULL,
  `ba_ftime` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`ba_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_balist 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_tb_balist`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_balist` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_balist` (`ba_id`, `order_no`, `ba_sta`, `ba_belong`, `ba_time`, `ba_ftime`) VALUES
	(1, 105597, 1, 1, NULL, NULL),
	(2, 3551, 2, 0, '2016-09-19 17:20:16', NULL);
/*!40000 ALTER TABLE `zhengzihui_app_tb_balist` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_companyuser 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_companyuser` (
  `companyUserId` int(11) NOT NULL AUTO_INCREMENT,
  `companyUserName` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserPassword` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyName` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyLocation` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyAddress` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyCapital` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyPeople` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyIndustry` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserCompanyNature` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserContactName` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserPhone` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserTelephone` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserEmail` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`companyUserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_companyuser 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_companyuser`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_companyuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_companyuser` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_customcompany 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_customcompany` (
  `company_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `custom_hangye` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `custom_bumen` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `custom_jiebie` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `wanted_guquan` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `wanted_rongzi` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `wanted_ziben` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `self_des` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `item_des` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `self_file` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `item_file` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `conclusion` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_customcompany 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_tb_customcompany`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_customcompany` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_customcompany` (`company_id`, `custom_hangye`, `custom_bumen`, `custom_jiebie`, `wanted_guquan`, `wanted_rongzi`, `wanted_ziben`, `self_des`, `item_des`, `self_file`, `item_file`, `conclusion`) VALUES
	('2016', '建筑业', '监管汇：人民银行／银监／质监／保监／证监／药监／安监／统计／更多', '中央', '风险投资', '银行', '创业板', 'niaho ', 'nihao ', '', '', '水产'),
	('9', '采矿业', '政府机关／直属事业单位', '市级', '天使投资', '全部', '全部', '', '', '', '', '水产');
/*!40000 ALTER TABLE `zhengzihui_app_tb_customcompany` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods` (
  `goods_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) NOT NULL,
  `sp_id` int(11) NOT NULL,
  `goods_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `goods_market_price` int(11) NOT NULL,
  `goods_code` int(11) DEFAULT NULL,
  `goods_payahead` int(11) NOT NULL,
  `goods_awardafter` int(11) DEFAULT NULL,
  `goods_accept_starttime` datetime DEFAULT NULL,
  `goods_accept_endtime` datetime DEFAULT NULL,
  `goods_price` int(11) NOT NULL,
  `goods_price_discouint` double NOT NULL,
  `goods_pay` int(11) NOT NULL,
  `goods_guarantee` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `goods_sort` int(11) NOT NULL,
  `goods_commend` int(11) NOT NULL,
  `goods_evaluation_good_star` int(11) NOT NULL,
  `goods_evaluation_count` int(11) NOT NULL,
  `goods_show` int(11) NOT NULL,
  `goods_status` int(11) NOT NULL,
  `cont` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `exa` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `steps` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fea` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `smod` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `goods_fanli` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `goods_awardmid` int(11) DEFAULT NULL,
  `goods_area` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods 的数据：~3 rows (大约)
DELETE FROM `zhengzihui_app_tb_goods`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods` (`goods_id`, `item_id`, `sp_id`, `goods_name`, `goods_market_price`, `goods_code`, `goods_payahead`, `goods_awardafter`, `goods_accept_starttime`, `goods_accept_endtime`, `goods_price`, `goods_price_discouint`, `goods_pay`, `goods_guarantee`, `goods_sort`, `goods_commend`, `goods_evaluation_good_star`, `goods_evaluation_count`, `goods_show`, `goods_status`, `cont`, `exa`, `steps`, `fea`, `smod`, `goods_fanli`, `goods_awardmid`, `goods_area`) VALUES
	(1, 1, 1, 'service_ 2016科技厅关于科技计划项目的申报通知', 100000, 3, 10000, 10000, '2016-07-19 17:20:16', '2017-09-19 17:20:14', 300, 1, 1, '1', 1, 0, 1, 1, 0, 0, 'a', 'a', 'a', '', '', '100', 0, '北京'),
	(2, 3, 1, 'service_ 2016科技厅关于科技计划项目的申报通知', 18888, 2, 1000, 1000, '2016-07-19 17:20:10', '2017-09-19 17:20:09', 900, 1, 1, '1', 2, 0, 4, 1, 0, 0, NULL, NULL, NULL, NULL, NULL, '100', 0, '北京'),
	(3, 1, 1, 'service_ 2016科技厅关于科技计划项目的申报通知', 56781, 1, 100, 100, '2016-06-19 17:19:57', '2017-09-19 17:19:55', 1000, 3, 1, '1', 3, 0, 5, 1, 0, 0, NULL, NULL, NULL, NULL, NULL, '100', 0, '北京');
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_class` (
  `gocl_id` int(11) NOT NULL,
  `gocl_code` int(11) NOT NULL,
  `gocl_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `gocl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gocl_sort` int(11) NOT NULL,
  `gocl_parent_id` int(11) NOT NULL,
  PRIMARY KEY (`gocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_class 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_goods_class`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_click 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gocl_id` int(11) NOT NULL,
  `gocl_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_click 的数据：~1 rows (大约)
DELETE FROM `zhengzihui_app_tb_goods_click`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_click` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods_click` (`id`, `goods_id`, `goods_name`, `gocl_id`, `gocl_num`) VALUES
	(1, 1, ' 2016科技厅关于科技计划项目的申报通知', 0, 11),
	(2, 2, 'service_ 2016科技厅关于科技计划项目的申报通知', 0, 5),
	(3, 3, 'service_ 2016科技厅关于科技计划项目的申报通知', 0, 2);
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_click` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_evaluation 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_evaluation` (
  `goev_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime NOT NULL,
  `goev_desccredit` int(11) NOT NULL,
  `goev_servicecredit` int(11) NOT NULL,
  `goev_content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `is_anonymous` int(11) NOT NULL,
  `goev_show` int(11) NOT NULL,
  `goev_status` int(11) NOT NULL,
  `reply_content` longtext COLLATE utf8_unicode_ci,
  `service_provider` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `star` int(11) DEFAULT NULL,
  `location` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`goev_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_evaluation 的数据：~3 rows (大约)
DELETE FROM `zhengzihui_app_tb_goods_evaluation`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_evaluation` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods_evaluation` (`goev_id`, `order_id`, `goods_id`, `goods_name`, `user_id`, `user_name`, `create_time`, `goev_desccredit`, `goev_servicecredit`, `goev_content`, `is_anonymous`, `goev_show`, `goev_status`, `reply_content`, `service_provider`, `star`, `location`) VALUES
	(2, 3, 3, '帮助徐成章找女朋友', 2, '徐成章', '2016-09-03 13:32:01', 1, 2, '这个项目非常好', 1, 2, 3, '啦啦啦', 'cyf', 5, '成都'),
	(3, 2, 2, '帮助徐成章找男朋友', 2, '徐成章', '2016-09-12 11:45:31', 1, 2, '这个项目更好', 1, 2, 3, '123', 'cyf', 5, '郫县'),
	(4, 1, 1, '帮基佬找徐成章', 3, 'GAY志', '2016-10-09 02:33:24', 1, 2, '这是一个号项目', 1, 2, 3, 'xixi', 'cyf', 5, '电子科大');
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_evaluation` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_wfc 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_wfc` (
  `goods_id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `item_id` int(11) NOT NULL,
  `sp_id` int(11) NOT NULL,
  `cont` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `steps` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `exa` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `goods_fanli` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `smod` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `goods_awardafter` int(11) DEFAULT NULL,
  `goods_payahead` int(11) NOT NULL,
  `goods_awardmid` int(11) DEFAULT NULL,
  `fea` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_wfc 的数据：~45 rows (大约)
DELETE FROM `zhengzihui_app_tb_goods_wfc`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_wfc` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods_wfc` (`goods_id`, `goods_name`, `item_id`, `sp_id`, `cont`, `steps`, `exa`, `goods_fanli`, `smod`, `goods_awardafter`, `goods_payahead`, `goods_awardmid`, `fea`) VALUES
	(1, 'hahaha', 1, 9, 'asdasd', 'asdasd', 'sdadss', '10%', '中期经费', 100, 100, NULL, ''),
	(2, 'hahaha', 1, 9, 'wqw ', 'wq ', 'sdasd', '10%', '启动经费中期经费成功赏金', 3333, 100000, 2222, ''),
	(3, 'hahaha', 1, 9, 'asss', 'asss', 'a', '10%', '启动经费中期经费成功赏金', 1233, 1000220, 0, ''),
	(4, 'woqu', 1, 9, 'asd', 'sc', 'e', '10%', '启动经费中期经费成功赏金', 333, 111, 222, ''),
	(5, '是水水水', 1, 9, '啊啊啊', '啊啊啊', '啊啊', '10%', '启动经费中期经费成功赏金', 1, 10000, 1, ''),
	(6, '111sadas', 1, 9, '', '', '', '10%', '启动经费', 0, 1111, 0, ''),
	(7, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '启动经费', 0, 10000, 0, ''),
	(8, 'aaa', 1, 9, '', '', '', '10%', '启动经费', 0, 123, 0, ''),
	(9, ' ', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(10, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(11, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(12, '', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(13, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '启动经费', 0, 10000, 0, ''),
	(14, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(15, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(16, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(17, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(18, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(19, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(20, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(21, '', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(22, '', 1, 9, 'None', 'None', 'None', '10%', '', 0, 1000, 0, ''),
	(23, '', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(24, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(25, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(26, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(27, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(28, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(29, '', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(30, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'None', 'None', 'None', '10%', '', 0, 1000, 0, ''),
	(31, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'None', 'None', 'None', '10%', '', 0, 100, 0, ''),
	(32, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(33, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(34, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'None', 'None', 'None', '10%', '', 0, 1000, 0, ''),
	(35, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(36, '', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(37, '', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(38, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(39, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(40, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(41, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'None', 'None', 'None', '10%', '', 0, 1000, 0, ''),
	(42, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(43, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(44, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, ''),
	(45, ' 2016科技厅关于科技计划项目的申报通知', 1, 9, 'a', 'a', 'a', '10%', '', 0, 10000, 0, '按时完成  保证修改  提供原版  后续服务  提供加急  ');
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_wfc` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item` (
  `item_id` int(11) NOT NULL,
  `item_code` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `item_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `itcl_id` int(11) NOT NULL,
  `item_level` int(11) NOT NULL,
  `item_ga` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `item_pa_id` int(11) NOT NULL,
  `item_publish` datetime NOT NULL,
  `item_deadtime` datetime NOT NULL,
  `item_about` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `item_url` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `item_key` longtext COLLATE utf8_unicode_ci NOT NULL,
  `item_status` int(11) NOT NULL,
  `is_hot` int(11) NOT NULL,
  `item_from` int(11) NOT NULL,
  `is_recommend` int(11) NOT NULL,
  `city` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `distr` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `privince` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `xianfen` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item 的数据：~18 rows (大约)
DELETE FROM `zhengzihui_app_tb_item`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item` (`item_id`, `item_code`, `item_name`, `itcl_id`, `item_level`, `item_ga`, `item_pa_id`, `item_publish`, `item_deadtime`, `item_about`, `item_url`, `item_key`, `item_status`, `is_hot`, `item_from`, `is_recommend`, `city`, `distr`, `privince`, `xianfen`) VALUES
	(1, '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, 1, '1', 1, '2016-04-03 04:35:19', '2017-10-01 00:00:00', '养殖/科技/互联网', '1', '科技项目', 1, 0, 0, 1, '成都市', NULL, '四川省', NULL),
	(2, '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, 4, '2', 2, '2016-05-01 04:35:42', '2016-06-18 04:35:43', '农林/住建/其他', '2', '互联网项目', 0, 0, 0, 1, '成都市', NULL, '四川省', NULL),
	(3, '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 3, 3, '3', 3, '2016-05-01 04:36:23', '2017-07-15 04:36:24', '农业/养殖/互联网+', '3', '科技项目', 1, 0, 0, 1, '成都市', NULL, '四川省', NULL),
	(4, '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 4, 3, '4', 4, '2016-05-01 04:36:47', '2016-05-28 04:36:48', '水产/养殖/其他', '4', '科技项目', 0, 0, 0, 0, NULL, NULL, NULL, NULL),
	(5, '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 5, 2, '5', 5, '2016-05-01 04:37:05', '2017-07-08 04:37:07', '水产/政务/管理/新产业', '5', '中央项目', 1, 0, 0, 0, NULL, NULL, NULL, NULL),
	(6, '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 6, 2, '5万-500万', 1, '2016-03-08 09:42:34', '2016-09-01 09:42:39', '农业/养殖/互联网+', '6', '水产/政务/管理/新产业', 0, 0, 1, 1, NULL, NULL, NULL, NULL),
	(7, '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 7, 1, '5万-500万', 2, '2016-03-23 09:44:34', '2016-06-11 09:44:38', '水产/政务/管理/新产业', '7', '科技项目', 0, 0, 0, 1, NULL, NULL, NULL, NULL),
	(8, '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 8, 1, '5万-500万', 3, '2015-12-03 09:45:32', '2016-10-30 09:45:40', '农林/住建/其他', '8', '互联网项目', 1, 0, 0, 1, NULL, NULL, NULL, NULL),
	(9, '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 9, 3, '5万-500万', 4, '2016-04-13 09:46:22', '2017-06-17 09:46:26', '农业/养殖/互联网+', '9', '中央项目', 1, 0, 0, 1, NULL, NULL, NULL, NULL),
	(10, '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 10, 4, '5万-500万', 5, '2016-05-01 09:47:25', '2016-05-31 09:47:28', '水产/政务/管理/新产业', '10', '科技项目', 0, 0, 0, 0, NULL, NULL, NULL, NULL),
	(11, '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 11, 4, '5万-500万', 1, '2016-04-03 09:48:13', '2017-05-04 09:48:23', '养殖/科技/互联网', '11', '互联网项目', 1, 0, 0, 1, NULL, NULL, NULL, NULL),
	(12, '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 12, 1, '5万-500万', 2, '2016-04-07 09:49:12', '2017-05-04 09:49:15', '养殖/科技/互联网', '12', '中央项目', 0, 0, 0, 0, NULL, NULL, NULL, NULL),
	(13, '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 13, 2, '5万-500万', 3, '2016-04-10 09:50:24', '2016-05-28 09:50:30', '水产/政务/管理/新产业', '13', '科技项目', 0, 0, 0, 1, NULL, NULL, NULL, NULL),
	(14, '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 14, 1, '5万-500万', 4, '2016-04-01 09:53:00', '2016-06-09 09:53:03', '水产/政务/管理/新产业', '14', '科技项目', 0, 0, 0, 1, NULL, NULL, NULL, NULL),
	(15, '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 15, 1, '5万-500万', 5, '2016-04-05 09:54:09', '2017-05-04 09:54:12', '养殖/科技/互联网', '15', '互联网项目', 1, 0, 0, 0, NULL, NULL, NULL, NULL),
	(16, '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 16, 1, '5万-500万', 1, '2016-04-03 09:55:05', '2016-06-24 09:55:08', '农林/住建/其他', '16', '中央项目', 0, 0, 0, 0, NULL, NULL, NULL, NULL),
	(17, '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 17, 1, '5万-500万', 2, '2016-04-20 09:56:04', '2016-11-08 09:56:08', '水产/政务/管理/新产业 ', '17', '科技项目', 0, 0, 0, 0, NULL, NULL, NULL, NULL),
	(18, '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 18, 1, '5万-500万', 3, '2016-03-31 09:56:50', '2016-05-26 09:56:53', '农业/养殖/互联网+', '18', '互联网项目', 0, 0, 0, 0, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `zhengzihui_app_tb_item` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item_class` (
  `itcl_id` int(11) NOT NULL,
  `itcl_code` int(11) NOT NULL,
  `itcl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `itcl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`itcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item_class 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_item_class`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item_click 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itcl_id` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `zheng_item_id_29097a73715f199e_fk_zhengzihui_app_tb_item_item_id` (`item_id`),
  CONSTRAINT `zheng_item_id_29097a73715f199e_fk_zhengzihui_app_tb_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `zhengzihui_app_tb_item` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item_click 的数据：~18 rows (大约)
DELETE FROM `zhengzihui_app_tb_item_click`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_click` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item_click` (`id`, `itcl_id`, `click_counter`, `item_id`) VALUES
	(2, 0, 31, 1),
	(3, 0, 25, 2),
	(4, 0, 14, 3),
	(5, 0, 5, 4),
	(6, 0, 5, 5),
	(7, 0, 2, 6),
	(8, 0, 1, 7),
	(9, 0, 0, 8),
	(10, 0, 1, 9),
	(11, 0, 2, 10),
	(12, 0, 2, 11),
	(13, 0, 0, 12),
	(14, 0, 0, 13),
	(15, 0, 0, 14),
	(16, 0, 0, 15),
	(17, 0, 0, 16),
	(18, 0, 0, 17),
	(19, 0, 0, 18);
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_click` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item_pa 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item_pa` (
  `ipa_id` int(11) NOT NULL,
  `ipa_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ipa_parent_id` int(11) NOT NULL,
  `ipa_sort` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `ipa_address` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`ipa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item_pa 的数据：~5 rows (大约)
DELETE FROM `zhengzihui_app_tb_item_pa`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_pa` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item_pa` (`ipa_id`, `ipa_name`, `ipa_parent_id`, `ipa_sort`, `area_id`, `ipa_address`) VALUES
	(1, '四川省科技厅', 1, 1, 1, '成都市天府广场'),
	(2, '四川农业局', 2, 2, 2, '成都市天府广场'),
	(3, '中央财政厅', 3, 3, 3, '成都市天府广场'),
	(4, '湖北教育局', 4, 4, 4, '成都市天府广场'),
	(5, '中央农业局', 5, 5, 5, '成都市天府广场');
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_pa` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_message 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_message` (
  `mess_id` int(11) NOT NULL,
  `send_id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL,
  `text_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`mess_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_message 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_message`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_message` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_messagetext 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_messagetext` (
  `text_id` int(11) NOT NULL,
  `mete_title` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `mete_content` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `mete_time` datetime NOT NULL,
  PRIMARY KEY (`text_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_messagetext 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_messagetext`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_messagetext` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_messagetext` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_news 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `news_time` datetime NOT NULL,
  `news_source` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `necl_id` int(11) NOT NULL,
  `news_sort` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  `has_album` int(11) NOT NULL,
  `news_hot` int(11) NOT NULL,
  `new_top` int(11) NOT NULL,
  `new_is_display` int(11) NOT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_news 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_news`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_news_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_news_class` (
  `necl_id` int(11) NOT NULL AUTO_INCREMENT,
  `necl_code` int(11) NOT NULL,
  `necl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`necl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_news_class 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_news_class`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_notice 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_notice` (
  `Notice_id` int(11) NOT NULL AUTO_INCREMENT,
  `Notice_title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Article_id` int(11) NOT NULL,
  `Notice_time` date NOT NULL,
  `Notice_source` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Nocl_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  `Notice_is_display` int(11) NOT NULL,
  `Notice_top` int(11) NOT NULL,
  `Notice_short_content` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Notice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_notice 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_notice`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_notice` (`Notice_id`, `Notice_title`, `Article_id`, `Notice_time`, `Notice_source`, `Nocl_id`, `Notice_sort`, `Notice_is_display`, `Notice_top`, `Notice_short_content`) VALUES
	(1, 'Test_notice', 1, '2016-07-19', '1', 0, 100, 1, 1, 'Test,,Comrnekskfksd');
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_notice_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_notice_class` (
  `Nocl_id` int(11) NOT NULL,
  `Nocl_code` int(11) NOT NULL,
  `Nocl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Nocl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Nocl_parent_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  PRIMARY KEY (`Nocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_notice_class 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_notice_class`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_order 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_order` (
  `order_id` int(11) NOT NULL,
  `order_no` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `pay_no` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  `sp_id` int(11) NOT NULL,
  `sp_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `buyer_id` int(11) NOT NULL,
  `buyer_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `buyer_email` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `add_time` datetime NOT NULL,
  `payment_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `payment_time` datetime DEFAULT NULL,
  `final_time` datetime DEFAULT NULL,
  `good_amount` int(11) NOT NULL,
  `order_amount` int(11) NOT NULL,
  `refund_amount` int(11) NOT NULL,
  `delay_time` datetime DEFAULT NULL,
  `order_from` int(11) NOT NULL,
  `express_id` int(11) NOT NULL,
  `express_no` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `eval_state` int(11) NOT NULL,
  `order_state` int(11) NOT NULL,
  `refund_state` int(11) NOT NULL,
  `lock_state` int(11) NOT NULL,
  `express_state` int(11) NOT NULL,
  `promise_finish_time` datetime DEFAULT NULL,
  `efile_send` int(11) NOT NULL,
  `paper_send` int(11) NOT NULL,
  `has_pay` int(11) NOT NULL,
  `finish_percentage` int(11) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_order 的数据：~5 rows (大约)
DELETE FROM `zhengzihui_app_tb_order`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_order` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_order` (`order_id`, `order_no`, `goods_id`, `pay_no`, `item_id`, `item_name`, `sp_id`, `sp_name`, `buyer_id`, `buyer_name`, `buyer_email`, `add_time`, `payment_code`, `payment_time`, `final_time`, `good_amount`, `order_amount`, `refund_amount`, `delay_time`, `order_from`, `express_id`, `express_no`, `eval_state`, `order_state`, `refund_state`, `lock_state`, `express_state`, `promise_finish_time`, `efile_send`, `paper_send`, `has_pay`, `finish_percentage`) VALUES
	(2, 105597, 3, 105597, 1, '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-03-02 07:15:16', '105597', NULL, NULL, 100, 200, 100, NULL, 1, 1, '1', 0, 1, 0, 0, 0, '2016-09-07 07:15:16', 0, 1, 0, 90),
	(10, 159020, 2, 159020, 3, '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-09-02 07:02:45', '159020', NULL, NULL, 1000, 2000, 1000, NULL, 1, 1, '1', 0, 2, 0, 0, 0, '2016-09-30 07:02:45', 0, 1, 1, 60),
	(11, 3551, 1, 3551, 1, '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-09-01 07:02:52', '3551', NULL, NULL, 10000, 20000, 10000, NULL, 1, 1, '1', 0, 3, 0, 0, 0, '2016-09-03 07:02:52', 0, 0, 2, 91),
	(12, 549961, 1, 549961, 1, '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-09-20 12:14:05', '549961', NULL, NULL, 10000, 20000, 10000, NULL, 1, 1, '1', 0, 3, 0, 0, 0, '2016-09-20 12:14:05', 0, 0, 0, 0),
	(13, 429111, 1, 429111, 1, '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-09-22 06:28:15', '429111', NULL, NULL, 10000, 20000, 10000, NULL, 1, 1, '1', 0, 3, 0, 0, 0, '2016-09-22 06:28:15', 0, 0, 0, 0),
	(14, 630037, 2, 630037, 3, '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-10-14 09:11:59', '630037', NULL, NULL, 1000, 2000, 1000, NULL, 1, 1, '1', 0, 3, 0, 0, 0, '2016-10-14 09:11:59', 0, 0, 0, 0),
	(15, 861226, 3, 861226, 1, '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, '', 9, 'orchard', 'changyifan123@qq.com', '2016-10-18 18:27:22', '861226', NULL, NULL, 100, 200, 100, NULL, 1, 1, '1', 0, 3, 0, 0, 0, '2016-10-18 18:27:22', 0, 0, 0, 0);
/*!40000 ALTER TABLE `zhengzihui_app_tb_order` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_pic 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_pic` (
  `pic_id` int(11) NOT NULL,
  `pic_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `pic_tag` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `album_id` int(11) NOT NULL,
  `pic_object` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pic_size` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  PRIMARY KEY (`pic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_pic 的数据：~22 rows (大约)
DELETE FROM `zhengzihui_app_tb_pic`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_pic` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_pic` (`pic_id`, `pic_name`, `pic_tag`, `album_id`, `pic_object`, `pic_size`, `upload_time`) VALUES
	(1, '1', '1', 1, 'img_for_items/2016/05/01/6aa33f80-a3c0-11e5-a70d-dc85def86878.png', 0, '2016-05-06 13:50:06'),
	(2, '2', '2', 2, 'img_for_items/2016/05/01/4adbe14f-a557-11e5-bd34-dc85def86878.png', 0, '2016-05-01 04:39:55'),
	(3, '3', '3', 3, 'img_for_items/2016/05/01/9a77684f-a558-11e5-91f7-dc85def86878.png', 0, '2016-05-01 04:40:07'),
	(4, '4', '4', 4, 'img_for_items/2016/05/01/34fd605a-a658-11e5-8df7-00163e0022d3.png', 0, '2016-05-01 04:40:19'),
	(5, '5', '5', 5, 'img_for_items/2016/05/01/39a46b8f-a558-11e5-949b-dc85def86878.png', 0, '2016-05-01 04:40:33'),
	(6, '6', '6', 6, 'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878.png', 0, '2016-05-04 09:30:26'),
	(7, '7', '7', 7, 'img_for_items/2016/05/04/6a12a4de-a558-11e5-b72c-dc85def86878.png', 0, '2016-05-04 09:30:41'),
	(8, '8', '8', 8, 'img_for_items/2016/05/04/34fd605a-a658-11e5-8df7-00163e0022d3.png', 0, '2016-05-04 09:30:53'),
	(9, '9', '9', 9, 'img_for_items/2016/05/04/6bd92fc0-a476-11e5-aaa1-dc85def86878.png', 0, '2016-05-04 09:31:05'),
	(10, '10', '10', 10, 'img_for_items/2016/05/04/76c0c68f-a265-11e5-80d4-3859f9fa9803.png', 0, '2016-05-04 09:31:25'),
	(11, '11', '11', 11, 'img_for_items/2016/05/04/56de86b0-a557-11e5-92af-dc85def86878.png', 0, '2016-05-04 09:32:58'),
	(12, '12', '12', 12, 'img_for_items/2016/05/04/2f9f86de-a277-11e5-a84a-3859f9fa9803.png', 0, '2016-05-04 09:33:09'),
	(13, '13', '13', 13, 'img_for_items/2016/05/04/9fdac0b0-a3c0-11e5-8a73-dc85def86878.png', 0, '2016-05-04 09:33:22'),
	(14, '14', '14', 14, 'img_for_items/2016/05/04/98c5db1e-a3c0-11e5-b491-dc85def86878.png', 0, '2016-05-04 09:33:34'),
	(15, '15', '15', 15, 'img_for_items/2016/05/04/2df0ed11-a557-11e5-8e43-dc85def86878.png', 0, '2016-05-04 09:33:51'),
	(16, '16', '16', 16, 'img_for_items/2016/05/04/17675c61-a263-11e5-a423-3859f9fa9803.png', 0, '2016-05-04 09:34:08'),
	(17, '17', '17', 17, 'img_for_items/2016/05/04/5be48e0f-a265-11e5-89c3-3859f9fa9803.png', 0, '2016-05-04 10:46:02'),
	(18, '18', '18', 18, 'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878_v0SFX5j.png', 0, '2016-05-04 09:34:23'),
	(19, '19', '19', 1, 'img_for_items/2016/05/06/a7.jpg', 0, '2016-05-06 13:54:33'),
	(20, '20', '20', 1, 'img_for_items/2016/05/06/a5.jpg', 0, '2016-05-06 13:51:08'),
	(21, '21', '21', 1, 'img_for_items/2016/05/06/a4.jpg', 0, '2016-05-06 13:51:23'),
	(22, '22', '22', 1, 'img_for_items/2016/05/06/a2.jpg', 0, '2016-05-06 13:51:33');
/*!40000 ALTER TABLE `zhengzihui_app_tb_pic` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_rongzi_fuwu_pic 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_rongzi_fuwu_pic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pic_name` varchar(40) NOT NULL,
  `pic_tag` varchar(40) NOT NULL,
  `pic_object` varchar(100) NOT NULL,
  `upload_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_rongzi_fuwu_pic 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_rongzi_fuwu_pic`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_fuwu_pic` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_fuwu_pic` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_rongzi_fuwu_service 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_rongzi_fuwu_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `privince` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `distr` varchar(100) DEFAULT NULL,
  `xianfen` varchar(100) DEFAULT NULL,
  `fuwu_service_code` int(11) NOT NULL,
  `fuwu_service_name` varchar(1000) NOT NULL,
  `fuwu_service_payahead` int(11) NOT NULL,
  `fuwu_service_award` int(11) NOT NULL,
  `fuwu_service_start_time` datetime NOT NULL,
  `fuwu_service_end_time` datetime NOT NULL,
  `fuwu_service_feature` varchar(100) DEFAULT NULL,
  `fuwu_service_short_intro` varchar(1000) DEFAULT NULL,
  `fuwu_service_liucheng` varchar(1000) DEFAULT NULL,
  `fuwu_click_counter` int(11) NOT NULL,
  `fuwu_service_provider_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `zhengzihui_app_tb_rongzi_fuwu_service_cbf4c405` (`fuwu_service_provider_id`),
  CONSTRAINT `ce75591b8fdd7e7b641e5fd885b3c634` FOREIGN KEY (`fuwu_service_provider_id`) REFERENCES `zhengzihui_app_tb_rongzi_fuwu_sp` (`sp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_rongzi_fuwu_service 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_rongzi_fuwu_service`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_fuwu_service` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_fuwu_service` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_rongzi_fuwu_sp 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_rongzi_fuwu_sp` (
  `privince` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `distr` varchar(100) DEFAULT NULL,
  `xianfen` varchar(100) DEFAULT NULL,
  `sp_id` int(11) NOT NULL AUTO_INCREMENT,
  `sp_name` varchar(100) NOT NULL,
  `sp_code` int(11) DEFAULT NULL,
  `sp_address` varchar(40) DEFAULT NULL,
  `psw` varchar(40) DEFAULT NULL,
  `tel` varchar(40) NOT NULL,
  `email` varchar(254) NOT NULL,
  `master` varchar(50) DEFAULT NULL,
  `sp_image1` varchar(100) DEFAULT NULL,
  `sp_image2` varchar(100) DEFAULT NULL,
  `sp_grade` int(11) DEFAULT NULL,
  `sp_sort` int(11) DEFAULT NULL,
  `area_id` varchar(10) DEFAULT NULL,
  `Register_cap` int(11) DEFAULT NULL,
  `staff_number` int(11) DEFAULT NULL,
  `Annual_totals` int(11) DEFAULT NULL,
  `organization_name` varchar(40) DEFAULT NULL,
  `organization_id` int(11) DEFAULT NULL,
  `organization_assets` int(11) DEFAULT NULL,
  `organization_profile` varchar(100) DEFAULT NULL,
  `sp_type` varchar(60) NOT NULL,
  `con_name` varchar(30) NOT NULL,
  `sp_auth` int(11) NOT NULL,
  `is_recommend` int(11) NOT NULL,
  PRIMARY KEY (`sp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_rongzi_fuwu_sp 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_rongzi_fuwu_sp`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_fuwu_sp` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_fuwu_sp` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_rongzi_item 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_rongzi_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `privince` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `distr` varchar(100) DEFAULT NULL,
  `xianfen` varchar(100) DEFAULT NULL,
  `fuwu_code` int(11) NOT NULL,
  `fuwu_name` varchar(1000) NOT NULL,
  `fuwu_provide_money` int(11) NOT NULL,
  `fuwu_start_time` datetime NOT NULL,
  `fuwu_end_time` datetime NOT NULL,
  `fuwu_Toptype` varchar(100) NOT NULL,
  `fuwu_Subtype` varchar(100) NOT NULL,
  `fuwu_short_intro` varchar(100) DEFAULT NULL,
  `fuwu_liucheng` longtext,
  `fuwu_click_counter` int(11) NOT NULL,
  `fuwu_type_Value` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_rongzi_item 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_tb_rongzi_item`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_item` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_rongzi_item` (`id`, `privince`, `city`, `distr`, `xianfen`, `fuwu_code`, `fuwu_name`, `fuwu_provide_money`, `fuwu_start_time`, `fuwu_end_time`, `fuwu_Toptype`, `fuwu_Subtype`, `fuwu_short_intro`, `fuwu_liucheng`, `fuwu_click_counter`, `fuwu_type_Value`) VALUES
	(1, '四川省', '成都市', '青羊区', '默认', 1, '测试1', 10000, '2016-10-13 17:40:31', '2016-10-23 17:40:33', '股权融资', '天使投资', '还没有简介', '无', 1, 11),
	(2, '四川省', '成都市', '青羊区', '默认', 2, '测试2', 1000000, '2016-10-13 17:40:31', '2016-10-23 17:40:33', '股权融资', '风险投资', '还没有简介', '无', 5, 12),
	(3, '四川省', '成都市', '青羊区', '默认', 3, '测试3', 100000, '2016-10-13 17:40:31', '2016-10-23 17:40:33', '股权融资', '政府引导资金', '还没有简介', '无', 3, 13);
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_item` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_rongzi_item_fuwu_pic_url 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_rongzi_item_fuwu_pic_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tb_rongzi_item_id` int(11) NOT NULL,
  `tb_rongzi_fuwu_pic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `zhengzihui_app_tb_rongzi_item_fu_tb_rongzi_item_id_96d14746_uniq` (`tb_rongzi_item_id`,`tb_rongzi_fuwu_pic_id`),
  KEY `D72c6d85a6ae8b4b77079a513421ab18` (`tb_rongzi_fuwu_pic_id`),
  CONSTRAINT `D72c6d85a6ae8b4b77079a513421ab18` FOREIGN KEY (`tb_rongzi_fuwu_pic_id`) REFERENCES `zhengzihui_app_tb_rongzi_fuwu_pic` (`id`),
  CONSTRAINT `z_tb_rongzi_item_id_0ddf66ad_fk_zhengzihui_app_tb_rongzi_item_id` FOREIGN KEY (`tb_rongzi_item_id`) REFERENCES `zhengzihui_app_tb_rongzi_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_rongzi_item_fuwu_pic_url 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_rongzi_item_fuwu_pic_url`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_item_fuwu_pic_url` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_item_fuwu_pic_url` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_rongzi_item_fuwu_service 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_rongzi_item_fuwu_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tb_rongzi_item_id` int(11) NOT NULL,
  `tb_rongzi_fuwu_service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `zhengzihui_app_tb_rongzi_item_fu_tb_rongzi_item_id_3fa85d7a_uniq` (`tb_rongzi_item_id`,`tb_rongzi_fuwu_service_id`),
  KEY `b5873205e6493b55934780a4b0a24b42` (`tb_rongzi_fuwu_service_id`),
  CONSTRAINT `b5873205e6493b55934780a4b0a24b42` FOREIGN KEY (`tb_rongzi_fuwu_service_id`) REFERENCES `zhengzihui_app_tb_rongzi_fuwu_service` (`id`),
  CONSTRAINT `z_tb_rongzi_item_id_efd59f1f_fk_zhengzihui_app_tb_rongzi_item_id` FOREIGN KEY (`tb_rongzi_item_id`) REFERENCES `zhengzihui_app_tb_rongzi_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_rongzi_item_fuwu_service 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_rongzi_item_fuwu_service`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_item_fuwu_service` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_rongzi_item_fuwu_service` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_service_provider 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_service_provider` (
  `sp_code` int(11) NOT NULL,
  `sp_id` int(11) NOT NULL,
  `sp_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `psw` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `master` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `sp_image1` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sp_image2` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sp_grade` int(11) NOT NULL,
  `sp_sort` int(11) NOT NULL,
  `area_id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `Register_cap` int(11) NOT NULL,
  `staff_number` int(11) NOT NULL,
  `Annual_totals` int(11) NOT NULL,
  `organization_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `organization_id` int(11) NOT NULL,
  `organization_assets` int(11) NOT NULL,
  `organization_profile` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sp_auth` int(11) NOT NULL,
  `is_recommend` int(11) NOT NULL,
  `sp_type` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `con_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `sp_address` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `chargeman_email` varchar(50) COLLATE utf8_unicode_ci,
  `chargeman_name` varchar(50) COLLATE utf8_unicode_ci,
  `chargeman_number` varchar(50) COLLATE utf8_unicode_ci,
  `con_email` varchar(50) COLLATE utf8_unicode_ci,
  `con_number` varchar(50) COLLATE utf8_unicode_ci,
  `short_intro` varchar(1000) COLLATE utf8_unicode_ci,
  `city` varchar(100) COLLATE utf8_unicode_ci,
  `distr` varchar(100) COLLATE utf8_unicode_ci,
  `privince` varchar(100) COLLATE utf8_unicode_ci,
  `xianfen` varchar(100) COLLATE utf8_unicode_ci,
  PRIMARY KEY (`sp_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_service_provider 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_tb_service_provider`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_service_provider` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_service_provider` (`sp_code`, `sp_id`, `sp_name`, `psw`, `tel`, `email`, `master`, `sp_image1`, `sp_image2`, `sp_grade`, `sp_sort`, `area_id`, `Register_cap`, `staff_number`, `Annual_totals`, `organization_name`, `organization_id`, `organization_assets`, `organization_profile`, `sp_auth`, `is_recommend`, `sp_type`, `con_name`, `sp_address`, `chargeman_email`, `chargeman_name`, `chargeman_number`, `con_email`, `con_number`, `short_intro`, `city`, `distr`, `privince`, `xianfen`) VALUES
	(231, 2, 'rongyida1', '123456', '2132', '32423', '213', '3423', '23', 324, 23, '42', 0, 0, 0, '00', 0, 0, '00', 1, 0, '1', 'rongyida', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(23423, 3, 'rongyida', '123456', '3214324', '324', '23', '34', '321', 432, 321, '434', 0, 0, 0, '00', 0, 0, '00', 1, 0, '3', 'rongyida', NULL, 'None问问', 'None而且气温', 'None去恶趣味', 'None惹我', 'None权威qw', '东方闪电', NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `zhengzihui_app_tb_service_provider` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_shoucang_goods 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_shoucang_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_shoucang_goods 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_shoucang_goods`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_goods` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_shoucang_goods` (`id`, `user_id`, `goods_id`) VALUES
	(1, 9, 1);
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_goods` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_shoucang_item 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_shoucang_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_shoucang_item 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_shoucang_item`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_item` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_sysmessage 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_sysmessage` (
  `sys_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `mess_id` int(11) NOT NULL,
  `sys_status` int(11) NOT NULL,
  PRIMARY KEY (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_sysmessage 的数据：~0 rows (大约)
DELETE FROM `zhengzihui_app_tb_sysmessage`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_sysmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_sysmessage` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_user 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_telephone` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `user_email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `user_auth` int(11) NOT NULL,
  `user_type` int(11) NOT NULL,
  `expand_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `zhengzihui_app_tb_user_5099c045` (`expand_id`),
  CONSTRAINT `zhen_expand_id_611cf3f8_fk_zhengzihui_app_tb_user_expand_user_id` FOREIGN KEY (`expand_id`) REFERENCES `zhengzihui_app_tb_user_expand` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_user 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_tb_user`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_user` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_user` (`user_id`, `user_name`, `user_password`, `user_telephone`, `user_email`, `user_auth`, `user_type`, `expand_id`) VALUES
	(1, 'testyz', '123456', '12312312', 'csdkfjsk@', 1, 1, 1),
	(9, 'orchard', '123456', '13688118677', 'changyifan123@qq.com', 1, 1, 9);
/*!40000 ALTER TABLE `zhengzihui_app_tb_user` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_user_expand 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_user_expand` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_tel` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `company_email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `company_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `company_district` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `company_address` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `company_registered_capital` int(11) NOT NULL,
  `company_industry` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `company_stuff_no` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `company_nature` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserContactName` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `companyUserPhone` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_user_expand 的数据：~2 rows (大约)
DELETE FROM `zhengzihui_app_tb_user_expand`;
/*!40000 ALTER TABLE `zhengzihui_app_tb_user_expand` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_user_expand` (`user_id`, `company_tel`, `company_email`, `company_name`, `company_district`, `company_address`, `company_registered_capital`, `company_industry`, `company_stuff_no`, `company_nature`, `companyUserContactName`, `companyUserPhone`) VALUES
	(1, '1231432', '2312312@2141', 'ueswtc', '四川省', '成都市', 2, '农业', '50-99', '国营', 'yz', '123242'),
	(9, '13688118677', 'changyifan123@qq.com', 'uestc', '四川省', '成都', 2, '科技', '50-99', '国营', '常益凡', '123455');
/*!40000 ALTER TABLE `zhengzihui_app_tb_user_expand` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
