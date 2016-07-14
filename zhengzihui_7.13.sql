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
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.auth_group 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_group_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.auth_group_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_permission 结构
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.auth_permission 的数据：~108 rows (大约)
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
	(28, 'Can add 用户', 10, 'add_tb_user'),
	(29, 'Can change 用户', 10, 'change_tb_user'),
	(30, 'Can delete 用户', 10, 'delete_tb_user'),
	(31, 'Can add 用户扩展信息', 11, 'add_tb_user_expand'),
	(32, 'Can change 用户扩展信息', 11, 'change_tb_user_expand'),
	(33, 'Can delete 用户扩展信息', 11, 'delete_tb_user_expand'),
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
	(64, 'Can add 地区表', 22, 'add_tb_area'),
	(65, 'Can change 地区表', 22, 'change_tb_area'),
	(66, 'Can delete 地区表', 22, 'delete_tb_area'),
	(67, 'Can add 项目分类', 23, 'add_tb_item_class'),
	(68, 'Can change 项目分类', 23, 'change_tb_item_class'),
	(69, 'Can delete 项目分类', 23, 'delete_tb_item_class'),
	(70, 'Can add 文章表', 24, 'add_tb_article'),
	(71, 'Can change 文章表', 24, 'change_tb_article'),
	(72, 'Can delete 文章表', 24, 'delete_tb_article'),
	(73, 'Can add 相册表', 25, 'add_tb_album'),
	(74, 'Can change 相册表', 25, 'change_tb_album'),
	(75, 'Can delete 相册表', 25, 'delete_tb_album'),
	(76, 'Can add 图片表', 26, 'add_tb_pic'),
	(77, 'Can change 图片表', 26, 'change_tb_pic'),
	(78, 'Can delete 图片表', 26, 'delete_tb_pic'),
	(79, 'Can add 其他附件表', 27, 'add_tb_accessory'),
	(80, 'Can change 其他附件表', 27, 'change_tb_accessory'),
	(81, 'Can delete 其他附件表', 27, 'delete_tb_accessory'),
	(82, 'Can add 人工申述表', 28, 'add_tb_artificial_representations'),
	(83, 'Can change 人工申述表', 28, 'change_tb_artificial_representations'),
	(84, 'Can delete 人工申述表', 28, 'delete_tb_artificial_representations'),
	(85, 'Can add 站内短信表', 29, 'add_tb_message'),
	(86, 'Can change 站内短信表', 29, 'change_tb_message'),
	(87, 'Can delete 站内短信表', 29, 'delete_tb_message'),
	(88, 'Can add 站内短信内容表', 30, 'add_tb_messagetext'),
	(89, 'Can change 站内短信内容表', 30, 'change_tb_messagetext'),
	(90, 'Can delete 站内短信内容表', 30, 'delete_tb_messagetext'),
	(91, 'Can add 系统信息表', 31, 'add_tb_sysmessage'),
	(92, 'Can change 系统信息表', 31, 'change_tb_sysmessage'),
	(93, 'Can delete 系统信息表', 31, 'delete_tb_sysmessage'),
	(94, 'Can add 服务商信息表', 32, 'add_tb_goods'),
	(95, 'Can change 服务商信息表', 32, 'change_tb_goods'),
	(96, 'Can delete 服务商信息表', 32, 'delete_tb_goods'),
	(97, 'Can add 服务商点击表', 33, 'add_tb_goods_click'),
	(98, 'Can change 服务商点击表', 33, 'change_tb_goods_click'),
	(99, 'Can delete 服务商点击表', 33, 'delete_tb_goods_click'),
	(100, 'Can add 服务商分类表', 34, 'add_tb_goods_class'),
	(101, 'Can change 服务商分类表', 34, 'change_tb_goods_class'),
	(102, 'Can delete 服务商分类表', 34, 'delete_tb_goods_class'),
	(103, 'Can add 服务商评价表', 35, 'add_tb_goods_evaluation'),
	(104, 'Can change 服务商评价表', 35, 'change_tb_goods_evaluation'),
	(105, 'Can delete 服务商评价表', 35, 'delete_tb_goods_evaluation'),
	(106, 'Can add 订单表', 36, 'add_tb_order'),
	(107, 'Can change 订单表', 36, 'change_tb_order'),
	(108, 'Can delete 订单表', 36, 'delete_tb_order');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_user 结构
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.auth_user 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_user_groups 结构
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.auth_user_groups 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.auth_user_user_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.auth_user_user_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_admin_log 结构
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.django_admin_log 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_content_type 结构
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.django_content_type 的数据：~36 rows (大约)
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
	(9, 'sessions', 'session'),
	(27, 'zhengzihui_app', 'tb_accessory'),
	(25, 'zhengzihui_app', 'tb_album'),
	(17, 'zhengzihui_app', 'tb_apage'),
	(18, 'zhengzihui_app', 'tb_apage_class'),
	(22, 'zhengzihui_app', 'tb_area'),
	(24, 'zhengzihui_app', 'tb_article'),
	(28, 'zhengzihui_app', 'tb_artificial_representations'),
	(32, 'zhengzihui_app', 'tb_goods'),
	(34, 'zhengzihui_app', 'tb_goods_class'),
	(33, 'zhengzihui_app', 'tb_goods_click'),
	(35, 'zhengzihui_app', 'tb_goods_evaluation'),
	(19, 'zhengzihui_app', 'tb_item'),
	(23, 'zhengzihui_app', 'tb_item_class'),
	(20, 'zhengzihui_app', 'tb_item_click'),
	(21, 'zhengzihui_app', 'tb_item_pa'),
	(29, 'zhengzihui_app', 'tb_message'),
	(30, 'zhengzihui_app', 'tb_messagetext'),
	(14, 'zhengzihui_app', 'tb_news'),
	(13, 'zhengzihui_app', 'tb_news_class'),
	(15, 'zhengzihui_app', 'tb_notice'),
	(16, 'zhengzihui_app', 'tb_notice_class'),
	(36, 'zhengzihui_app', 'tb_order'),
	(26, 'zhengzihui_app', 'tb_pic'),
	(12, 'zhengzihui_app', 'tb_service_provider'),
	(31, 'zhengzihui_app', 'tb_sysmessage'),
	(10, 'zhengzihui_app', 'tb_user'),
	(11, 'zhengzihui_app', 'tb_user_expand');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_migrations 结构
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.django_migrations 的数据：~15 rows (大约)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2016-07-13 01:08:40'),
	(2, 'auth', '0001_initial', '2016-07-13 01:08:40'),
	(3, 'admin', '0001_initial', '2016-07-13 01:08:40'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2016-07-13 01:08:40'),
	(5, 'contenttypes', '0002_remove_content_type_name', '2016-07-13 01:08:40'),
	(6, 'auth', '0002_alter_permission_name_max_length', '2016-07-13 01:08:40'),
	(7, 'auth', '0003_alter_user_email_max_length', '2016-07-13 01:08:40'),
	(8, 'auth', '0004_alter_user_username_opts', '2016-07-13 01:08:40'),
	(9, 'auth', '0005_alter_user_last_login_null', '2016-07-13 01:08:40'),
	(10, 'auth', '0006_require_contenttypes_0002', '2016-07-13 01:08:40'),
	(11, 'auth', '0007_alter_validators_add_error_messages', '2016-07-13 01:08:40'),
	(12, 'easy_thumbnails', '0001_initial', '2016-07-13 01:08:41'),
	(13, 'easy_thumbnails', '0002_thumbnaildimensions', '2016-07-13 01:08:41'),
	(14, 'sessions', '0001_initial', '2016-07-13 01:08:41'),
	(15, 'zhengzihui_app', '0001_initial', '2016-07-13 01:08:41');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.django_session 结构
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.django_session 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('0uqcozf92nhebgwo5y9hdtv9kbx7r76p', 'ZTZlMzhmZjA4MWEyZWIyYzc4YjljZTA1YjA2ZDQwYjQxMGI3Y2IzNjp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgiLCJzZWFyY2hfY29udGVudCI6Ilx1NzlkMVx1NjI4MCJ9', '2016-07-27 02:01:45');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.easy_thumbnails_source 结构
CREATE TABLE IF NOT EXISTS `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_storage_hash_481ce32d_uniq` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_source_b068931c` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.easy_thumbnails_source 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `easy_thumbnails_source` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_source` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.easy_thumbnails_thumbnail 结构
CREATE TABLE IF NOT EXISTS `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_thumbnail_storage_hash_fb375270_uniq` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thumbnails__source_id_5b57bc77_fk_easy_thumbnails_source_id` (`source_id`),
  KEY `easy_thumbnails_thumbnail_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_b068931c` (`name`),
  CONSTRAINT `easy_thumbnails__source_id_5b57bc77_fk_easy_thumbnails_source_id` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.easy_thumbnails_thumbnail 的数据：~0 rows (大约)
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
  CONSTRAINT `easy_thumb_thumbnail_id_c3a0c549_fk_easy_thumbnails_thumbnail_id` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.easy_thumbnails_thumbnaildimensions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_accessory 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_accessory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anne_id` int(11) NOT NULL,
  `comm_id` int(11) NOT NULL,
  `apubdate` int(11) NOT NULL,
  `apublisher` varchar(2) NOT NULL,
  `aposition` varchar(10) NOT NULL,
  `aaddtion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_accessory 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_accessory` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_accessory` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_album 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_album` (
  `album_id` int(11) NOT NULL,
  `album_name` varchar(40) NOT NULL,
  `album_type` int(11) NOT NULL,
  `affiliation_id` int(11) NOT NULL,
  `nacl_des` varchar(100) NOT NULL,
  `nacl_sort` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  `is_default` int(11) NOT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_album 的数据：~18 rows (大约)
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
  `Apage_source` varchar(100) NOT NULL,
  `Apcl_id` int(11) NOT NULL,
  `Apage_sort` int(11) NOT NULL,
  `Apage_is_display` int(11) NOT NULL,
  PRIMARY KEY (`Apage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_apage 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_apage_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_apage_class` (
  `Apcl_id` int(11) NOT NULL,
  `Apcl_code` int(11) NOT NULL,
  `Apcl_name` varchar(100) NOT NULL,
  `Apcl_parent_id` int(11) NOT NULL,
  `Apcl_sort` int(11) NOT NULL,
  PRIMARY KEY (`Apcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_apage_class 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_area 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_area` (
  `area_id` int(11) NOT NULL,
  `area_name` varchar(100) NOT NULL,
  `area_parent_id` int(11) NOT NULL,
  `area_sort` int(11) NOT NULL,
  `area_deep` int(11) NOT NULL,
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_area 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_area` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_article 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_article` (
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
  `article_click` int(11) NOT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_article 的数据：~3 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_article` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_article` (`article_id`, `article_code`, `article_name`, `author`, `author_email`, `article_type`, `affiliation_id`, `article_content`, `article_keywords`, `article_des`, `article_sort`, `upload_time`, `is_default`, `article_click`) VALUES
	(1, 1, '2016科技厅关于科技计划项目的申报通知	', '1', '1@qq.com', 0, 1, '     近日，四川省教育考试院来函批复，同意西华大学今年将22个本科专业调整到本科一批次录取。加上去年纳入本科一批次招生的21个专业，2016年西华大学共有43个专业纳入本科一批次在川招生，预计该校普通本科一本批次招生计划将占普通本科总计划数的60%。', '1', '1', 1, '2016-05-07 11:18:51', 1, 1),
	(2, 2, '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '1111@sina.com', 0, 1, '金正恩在讲话中高度肯定了朝鲜在今年1月份的核试验和2月份的火箭发射所取得的“前所未有”的伟大成就。\r\n　　朝鲜劳动党第七次全国代表大会6日在平壤开幕，朝中社当天曾发布一万多字的长篇报道称“开发小型核弹头是送给劳动党七大的礼物”。\r\n　　报道称，开发小型核弹头、弹道火箭重返大气层环境模拟试验取得成功、进行高功率固体火箭发动机地上点火及级间分离试验、进行新型洲际弹道火箭大功率发动机地上点火试验是朝鲜国防科技人员向劳动党七大献礼。\r\n　　此前，金正恩的西装照片几乎只出现在朝鲜对外公布的领导人官方照片中。\r\n　　韩国电视台对朝鲜电视台金正恩的讲话做了报道评论。韩国分析人士认为，朝鲜劳动党七大日程表一开始就未包含进行第五次核试验。而朝鲜是否举行第五次核试验，这也是韩国方面此前最担心的事情。', '111111111111111111111111111', '1', 1, '2016-05-07 11:20:34', 1, 1),
	(3, 3, '3', '3', '1111@sina.com', 0, 1, '从去年开始，川内不少老牌二本院校就将大批二本专业调整至一本招生，今年这一趋势仍在继续，再加上去年四川合并二、三本批次，各个批次的界限越来越模糊，这背后将会给考生们带来什么样的影响？考生们在志愿填报上应有哪些应对之策？记者采访了相关专家。', '3', '3', 3, '2016-05-07 11:19:51', 1, 3);
/*!40000 ALTER TABLE `zhengzihui_app_tb_article` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_artificial_representations 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_artificial_representations` (
  `arre_id` int(11) NOT NULL AUTO_INCREMENT,
  `arre_title` varchar(100) NOT NULL,
  `arre_content` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `arre_state` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`arre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_artificial_representations 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_artificial_representations` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_artificial_representations` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods` (
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
  `goods_status` int(11) NOT NULL,
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods 的数据：~3 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods` (`goods_id`, `item_id`, `sp_id`, `goods_name`, `goods_market_price`, `goods_price`, `goods_price_discouint`, `goods_pay`, `goods_guarantee`, `goods_sort`, `goods_commend`, `goods_evaluation_good_star`, `goods_evaluation_count`, `goods_show`, `goods_status`) VALUES
	(1, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 100000, 300, 1, 1, '1', 3, 0, 1, 1, 1, 0),
	(2, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 18888, 900, 1, 1, '1', 2, 0, 1, 1, 1, 0),
	(3, 1, 1, ' 2016科技厅关于科技计划项目的申报通知', 56781, 1000, 3, 1, '1', 1, 0, 1, 1, 1, 0);
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_class` (
  `gocl_id` int(11) NOT NULL,
  `gocl_code` int(11) NOT NULL,
  `gocl_name` varchar(40) NOT NULL,
  `gocl_des` varchar(100) NOT NULL,
  `gocl_sort` int(11) NOT NULL,
  `gocl_parent_id` int(11) NOT NULL,
  PRIMARY KEY (`gocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_class 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_click 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) NOT NULL,
  `gocl_id` int(11) NOT NULL,
  `gocl_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_click 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_click` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_click` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_goods_evaluation 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_goods_evaluation` (
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
  `goev_status` int(11) NOT NULL,
  PRIMARY KEY (`goev_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_goods_evaluation 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_evaluation` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_evaluation` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item` (
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
  `is_recommend` int(11) NOT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item 的数据：~18 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_item` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item` (`item_id`, `item_code`, `item_name`, `itcl_id`, `item_level`, `item_ga`, `item_pa_id`, `item_publish`, `item_deadtime`, `item_about`, `item_url`, `item_key`, `item_status`, `is_hot`, `item_from`, `is_recommend`) VALUES
	(1, '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', 1, 1, '1', 1, '2016-04-03 04:35:19', '2016-05-03 16:28:49', '养殖/科技/互联网', '1', '科技项目', 0, 0, 0, 1),
	(2, '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 2, 1, '2', 2, '2016-05-01 04:35:42', '2016-06-18 04:35:43', '农林/住建/其他', '2', '互联网项目', 0, 0, 0, 1),
	(3, '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 3, 1, '3', 3, '2016-05-01 04:36:23', '2016-07-15 04:36:24', '农业/养殖/互联网+', '3', '科技项目', 0, 0, 0, 1),
	(4, '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 4, 1, '4', 4, '2016-05-01 04:36:47', '2016-05-28 04:36:48', '水产/养殖/其他', '4', '科技项目', 0, 0, 0, 0),
	(5, '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 5, 1, '5', 5, '2016-05-01 04:37:05', '2016-07-08 04:37:07', '水产/政务/管理/新产业', '5', '中央项目', 0, 0, 0, 0),
	(6, '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 6, 1, '5万-500万', 1, '2016-03-08 09:42:34', '2016-09-01 09:42:39', '农业/养殖/互联网+', '6', '水产/政务/管理/新产业', 0, 0, 0, 1),
	(7, '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 7, 1, '5万-500万', 2, '2016-03-23 09:44:34', '2016-06-11 09:44:38', '水产/政务/管理/新产业', '7', '科技项目', 0, 0, 0, 1),
	(8, '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 8, 1, '5万-500万', 3, '2015-12-03 09:45:32', '2016-06-30 09:45:40', '农林/住建/其他', '8', '互联网项目', 0, 0, 0, 1),
	(9, '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 9, 1, '5万-500万', 4, '2016-04-13 09:46:22', '2016-06-17 09:46:26', '农业/养殖/互联网+', '9', '中央项目', 0, 0, 0, 1),
	(10, '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 10, 1, '5万-500万', 5, '2016-05-01 09:47:25', '2016-05-31 09:47:28', '水产/政务/管理/新产业', '10', '科技项目', 0, 0, 0, 0),
	(11, '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 11, 1, '5万-500万', 1, '2016-04-03 09:48:13', '2016-05-04 09:48:23', '养殖/科技/互联网', '11', '互联网项目', 0, 0, 0, 1),
	(12, '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 12, 1, '5万-500万', 2, '2016-04-07 09:49:12', '2016-05-04 09:49:15', '养殖/科技/互联网', '12', '中央项目', 0, 0, 0, 0),
	(13, '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 13, 1, '5万-500万', 3, '2016-04-10 09:50:24', '2016-05-28 09:50:30', '水产/政务/管理/新产业', '13', '科技项目', 0, 0, 0, 1),
	(14, '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 14, 1, '5万-500万', 4, '2016-04-01 09:53:00', '2016-06-09 09:53:03', '水产/政务/管理/新产业', '14', '科技项目', 0, 0, 0, 1),
	(15, '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 15, 1, '5万-500万', 5, '2016-04-05 09:54:09', '2016-05-04 09:54:12', '养殖/科技/互联网', '15', '互联网项目', 0, 0, 0, 0),
	(16, '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 16, 1, '5万-500万', 1, '2016-04-03 09:55:05', '2016-06-24 09:55:08', '农林/住建/其他', '16', '中央项目', 0, 0, 0, 0),
	(17, '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 17, 1, '5万-500万', 2, '2016-04-20 09:56:04', '2016-07-08 09:56:08', '水产/政务/管理/新产业 ', '17', '科技项目', 0, 0, 0, 0),
	(18, '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', 18, 1, '5万-500万', 3, '2016-03-31 09:56:50', '2016-05-26 09:56:53', '农业/养殖/互联网+', '18', '互联网项目', 0, 0, 0, 0);
/*!40000 ALTER TABLE `zhengzihui_app_tb_item` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item_class` (
  `itcl_id` int(11) NOT NULL,
  `itcl_code` int(11) NOT NULL,
  `itcl_name` varchar(100) NOT NULL,
  `itcl_des` varchar(100) NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`itcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item_class 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_item_click 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_item_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itcl_id` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `zhengzihui_ap_item_id_1e294869_fk_zhengzihui_app_tb_item_item_id` (`item_id`),
  CONSTRAINT `zhengzihui_ap_item_id_1e294869_fk_zhengzihui_app_tb_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `zhengzihui_app_tb_item` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item_click 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_click` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item_click` (`id`, `itcl_id`, `click_counter`, `item_id`) VALUES
	(2, 0, 7, 1),
	(3, 0, 11, 2),
	(4, 0, 1, 3),
	(5, 0, 1, 4),
	(6, 0, 0, 5),
	(7, 0, 2, 6),
	(8, 0, 0, 7),
	(9, 0, 0, 8),
	(10, 0, 0, 9),
	(11, 0, 0, 10),
	(12, 0, 0, 11),
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
  `ipa_name` varchar(100) NOT NULL,
  `ipa_parent_id` int(11) NOT NULL,
  `ipa_sort` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  PRIMARY KEY (`ipa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_item_pa 的数据：~5 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_pa` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item_pa` (`ipa_id`, `ipa_name`, `ipa_parent_id`, `ipa_sort`, `area_id`) VALUES
	(1, '四川省科技厅', 1, 1, 1),
	(2, '四川农业局', 2, 2, 2),
	(3, '中央财政厅', 3, 3, 3),
	(4, '湖北教育局', 4, 4, 4),
	(5, '中央农业局', 5, 5, 5);
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_pa` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_message 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_message` (
  `mess_id` int(11) NOT NULL,
  `send_id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL,
  `text_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`mess_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_message 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_message` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_messagetext 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_messagetext` (
  `text_id` int(11) NOT NULL,
  `mete_title` varchar(10) NOT NULL,
  `mete_content` varchar(300) NOT NULL,
  `mete_time` datetime NOT NULL,
  PRIMARY KEY (`text_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_messagetext 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_messagetext` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_messagetext` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_news 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `news_time` datetime NOT NULL,
  `news_source` varchar(100) NOT NULL,
  `necl_id` int(11) NOT NULL,
  `news_sort` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  `has_album` int(11) NOT NULL,
  `news_hot` int(11) NOT NULL,
  `new_top` int(11) NOT NULL,
  `new_is_display` int(11) NOT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_news 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_news_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_news_class` (
  `necl_id` int(11) NOT NULL AUTO_INCREMENT,
  `necl_code` int(11) NOT NULL,
  `necl_name` varchar(100) NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`necl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_news_class 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_news_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_notice 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_notice` (
  `Notice_id` int(11) NOT NULL AUTO_INCREMENT,
  `Notice_title` varchar(100) NOT NULL,
  `Article_id` int(11) NOT NULL,
  `Notice_time` date NOT NULL,
  `Notice_source` varchar(100) NOT NULL,
  `Nocl_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  `Notice_is_display` int(11) NOT NULL,
  `Notice_top` int(11) NOT NULL,
  PRIMARY KEY (`Notice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_notice 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_notice_class 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_notice_class` (
  `Nocl_id` int(11) NOT NULL,
  `Nocl_code` int(11) NOT NULL,
  `Nocl_name` varchar(100) NOT NULL,
  `Nocl_des` varchar(100) NOT NULL,
  `Nocl_parent_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  PRIMARY KEY (`Nocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_notice_class 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice_class` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_order 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_order` (
  `order_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
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
  `order_no` int(11) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_order 的数据：~6 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_order` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_order` (`order_id`, `goods_id`, `pay_no`, `item_id`, `item_name`, `sp_id`, `sp_name`, `buyer_id`, `buyer_name`, `buyer_email`, `add_time`, `payment_code`, `payment_time`, `final_time`, `good_amount`, `order_amount`, `refund_amount`, `delay_time`, `order_from`, `express_id`, `express_no`, `eval_state`, `order_state`, `refund_state`, `lock_state`, `express_state`, `order_no`) VALUES
	(1, 0, 1, 1, '的说法是尽快快快快快快快', 1, '1', 3, '3', '1@qq.com', '2016-05-21 03:39:54', '1', '2016-05-03 03:39:59', '2016-05-03 03:40:00', 1, 77777, 0, '2016-05-03 03:40:16', 1, 1, '1', 0, 0, 0, 0, 1, 1),
	(2, 0, 2, 2, '2016科技厅关于科技计划项目的申报通知', 1, '1', 3, '1', '1@qq.com', '2016-05-03 03:41:10', '1', '2016-05-03 03:41:11', '2016-05-03 03:41:14', 1, 8888, 1, '2016-05-03 03:41:23', 1, 1, '1', 0, 1, 0, 0, 1, 2),
	(3, 0, 3, 3, '2016科技厅关于科技计划项目的申报通知', 3, '3', 3, '3', '1@qq.com', '2016-05-02 03:42:03', '1', '2016-05-03 03:42:07', '2016-05-03 03:42:08', 1, 9999, 1, '2016-05-03 03:42:17', 1, 1, '1', 0, 2, 0, 0, 1, 3),
	(4, 0, 4, 4, '2016科技厅关于科技计划项目的申报通知', 4, '4', 3, '3', '1@qq.com', '2016-05-04 10:16:26', '1', '2016-05-04 10:16:29', '2016-05-04 10:16:30', 1, 0, 1, '2016-05-04 10:16:34', 1, 1, '1', 0, 3, 0, 0, 1, 4),
	(5, 0, 5, 5, '2016科技厅关于科技计划项目的申报通知', 5, '5', 3, '3', '1@qq.com', '2016-05-04 10:17:06', '1', '2016-05-04 10:17:09', '2016-05-04 10:17:11', 1, 0, 1, '2016-05-04 10:17:15', 1, 11, '1', 0, 4, 0, 0, 1, 5),
	(6, 0, 6, 6, '2016科技厅关于科技计划项目的申报通知', 6, '6', 3, '3', '1@qq.com', '2016-05-04 10:17:53', '1', '2016-05-04 10:17:58', '2016-05-04 10:17:59', 1, 0, 1, '2016-05-04 10:18:04', 1, 11, '1', 0, 0, 0, 0, 1, 6);
/*!40000 ALTER TABLE `zhengzihui_app_tb_order` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_pic 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_pic` (
  `pic_id` int(11) NOT NULL,
  `pic_name` varchar(40) NOT NULL,
  `pic_tag` varchar(40) NOT NULL,
  `album_id` int(11) NOT NULL,
  `pic_object` varchar(100) NOT NULL,
  `pic_size` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  PRIMARY KEY (`pic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_pic 的数据：~22 rows (大约)
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


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_service_provider 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_service_provider` (
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
  `is_recommend` int(11) NOT NULL,
  PRIMARY KEY (`sp_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_service_provider 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_service_provider` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_service_provider` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_sysmessage 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_sysmessage` (
  `sys_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `mess_id` int(11) NOT NULL,
  `sys_status` int(11) NOT NULL,
  PRIMARY KEY (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_sysmessage 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_sysmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_sysmessage` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_user 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_telephone` varchar(40) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_auth` int(11) NOT NULL,
  `user_type` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_user 的数据：~7 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_user` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_user` (`user_id`, `user_name`, `user_password`, `user_telephone`, `user_email`, `user_auth`, `user_type`) VALUES
	(1, '郭捷', '1', '1@qq', '1@qq.com', 0, 1),
	(2, '李泽华', '2', '2', '1@qq.com', 0, 1),
	(3, '张帅帅', '111', '3', '1@qq.com', 0, 1),
	(4, '袁志', '111', '111', '1@qq.com', 0, 0),
	(5, '常益凡', '111', '1111', '1@qq.com', 0, 0),
	(6, '徐成章', '1111', '11111', '1@qq.com', 0, 0),
	(7, '罗杰炜', '1111', '1111', '1@qq.com', 0, 0);
/*!40000 ALTER TABLE `zhengzihui_app_tb_user` ENABLE KEYS */;


-- 导出  表 zhengzihui_test_second.zhengzihui_app_tb_user_expand 结构
CREATE TABLE IF NOT EXISTS `zhengzihui_app_tb_user_expand` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_tel` varchar(30) NOT NULL,
  `company_email` varchar(254) NOT NULL,
  `company_name` varchar(30) NOT NULL,
  `company_district` varchar(50) NOT NULL,
  `company_address` varchar(50) NOT NULL,
  `company_registered_capital` int(11) NOT NULL,
  `company_industry` varchar(30) NOT NULL,
  `company_stuff_no` int(11) NOT NULL,
  `company_nature` varchar(30) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  zhengzihui_test_second.zhengzihui_app_tb_user_expand 的数据：~7 rows (大约)
/*!40000 ALTER TABLE `zhengzihui_app_tb_user_expand` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_user_expand` (`user_id`, `company_tel`, `company_email`, `company_name`, `company_district`, `company_address`, `company_registered_capital`, `company_industry`, `company_stuff_no`, `company_nature`) VALUES
	(1, '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', '四川成都市大慈寺', '四川成都市大慈寺', 100000000, '互联网科技服务', 100, '私营'),
	(2, ' 111111111111', '1@qq.com', '成都融亿达科技服务有限公司', '2 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, ' 私营'),
	(3, '1', '1@qq.com', '成都融亿达科技服务有限公司', '四川成都市大慈寺', '四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
	(4, '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
	(5, '111111111111', '1@qq.com', ' 四川成都市大慈寺', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
	(6, '111111111111', '1@qq.com', '成都融亿达科技服务有限公', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, ' 互联网科技服务', 100, '私营'),
	(7, '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', ' 四川成都市大慈寺', ' 四川成都市大慈寺', 10000000, '互联网科技服务', 100, ' 私营');
/*!40000 ALTER TABLE `zhengzihui_app_tb_user_expand` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
