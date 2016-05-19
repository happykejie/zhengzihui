/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : zhengzihui_test_second

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-05-12 18:21:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add source', '1', 'add_source');
INSERT INTO `auth_permission` VALUES ('2', 'Can change source', '1', 'change_source');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete source', '1', 'delete_source');
INSERT INTO `auth_permission` VALUES ('4', 'Can add thumbnail', '2', 'add_thumbnail');
INSERT INTO `auth_permission` VALUES ('5', 'Can change thumbnail', '2', 'change_thumbnail');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete thumbnail', '2', 'delete_thumbnail');
INSERT INTO `auth_permission` VALUES ('7', 'Can add thumbnail dimensions', '3', 'add_thumbnaildimensions');
INSERT INTO `auth_permission` VALUES ('8', 'Can change thumbnail dimensions', '3', 'change_thumbnaildimensions');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete thumbnail dimensions', '3', 'delete_thumbnaildimensions');
INSERT INTO `auth_permission` VALUES ('10', 'Can add log entry', '4', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('11', 'Can change log entry', '4', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete log entry', '4', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('13', 'Can add permission', '5', 'add_permission');
INSERT INTO `auth_permission` VALUES ('14', 'Can change permission', '5', 'change_permission');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete permission', '5', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('16', 'Can add group', '6', 'add_group');
INSERT INTO `auth_permission` VALUES ('17', 'Can change group', '6', 'change_group');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete group', '6', 'delete_group');
INSERT INTO `auth_permission` VALUES ('19', 'Can add user', '7', 'add_user');
INSERT INTO `auth_permission` VALUES ('20', 'Can change user', '7', 'change_user');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete user', '7', 'delete_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can add content type', '8', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('23', 'Can change content type', '8', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete content type', '8', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('25', 'Can add session', '9', 'add_session');
INSERT INTO `auth_permission` VALUES ('26', 'Can change session', '9', 'change_session');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete session', '9', 'delete_session');
INSERT INTO `auth_permission` VALUES ('28', 'Can add tb_user', '10', 'add_tb_user');
INSERT INTO `auth_permission` VALUES ('29', 'Can change tb_user', '10', 'change_tb_user');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete tb_user', '10', 'delete_tb_user');
INSERT INTO `auth_permission` VALUES ('31', 'Can add tb_user_expand', '11', 'add_tb_user_expand');
INSERT INTO `auth_permission` VALUES ('32', 'Can change tb_user_expand', '11', 'change_tb_user_expand');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete tb_user_expand', '11', 'delete_tb_user_expand');
INSERT INTO `auth_permission` VALUES ('34', 'Can add tb_service_provider', '12', 'add_tb_service_provider');
INSERT INTO `auth_permission` VALUES ('35', 'Can change tb_service_provider', '12', 'change_tb_service_provider');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete tb_service_provider', '12', 'delete_tb_service_provider');
INSERT INTO `auth_permission` VALUES ('37', 'Can add tb_ news_ class', '13', 'add_tb_news_class');
INSERT INTO `auth_permission` VALUES ('38', 'Can change tb_ news_ class', '13', 'change_tb_news_class');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete tb_ news_ class', '13', 'delete_tb_news_class');
INSERT INTO `auth_permission` VALUES ('40', 'Can add tb_ news', '14', 'add_tb_news');
INSERT INTO `auth_permission` VALUES ('41', 'Can change tb_ news', '14', 'change_tb_news');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete tb_ news', '14', 'delete_tb_news');
INSERT INTO `auth_permission` VALUES ('43', 'Can add tb_ notice', '15', 'add_tb_notice');
INSERT INTO `auth_permission` VALUES ('44', 'Can change tb_ notice', '15', 'change_tb_notice');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete tb_ notice', '15', 'delete_tb_notice');
INSERT INTO `auth_permission` VALUES ('46', 'Can add tb_ notice_ class', '16', 'add_tb_notice_class');
INSERT INTO `auth_permission` VALUES ('47', 'Can change tb_ notice_ class', '16', 'change_tb_notice_class');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete tb_ notice_ class', '16', 'delete_tb_notice_class');
INSERT INTO `auth_permission` VALUES ('49', 'Can add tb_ apage', '17', 'add_tb_apage');
INSERT INTO `auth_permission` VALUES ('50', 'Can change tb_ apage', '17', 'change_tb_apage');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete tb_ apage', '17', 'delete_tb_apage');
INSERT INTO `auth_permission` VALUES ('52', 'Can add tb_ apage_ class', '18', 'add_tb_apage_class');
INSERT INTO `auth_permission` VALUES ('53', 'Can change tb_ apage_ class', '18', 'change_tb_apage_class');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete tb_ apage_ class', '18', 'delete_tb_apage_class');
INSERT INTO `auth_permission` VALUES ('55', 'Can add tb_item', '19', 'add_tb_item');
INSERT INTO `auth_permission` VALUES ('56', 'Can change tb_item', '19', 'change_tb_item');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete tb_item', '19', 'delete_tb_item');
INSERT INTO `auth_permission` VALUES ('58', 'Can add tb_item_click', '20', 'add_tb_item_click');
INSERT INTO `auth_permission` VALUES ('59', 'Can change tb_item_click', '20', 'change_tb_item_click');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete tb_item_click', '20', 'delete_tb_item_click');
INSERT INTO `auth_permission` VALUES ('61', 'Can add tb_item_class', '21', 'add_tb_item_class');
INSERT INTO `auth_permission` VALUES ('62', 'Can change tb_item_class', '21', 'change_tb_item_class');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete tb_item_class', '21', 'delete_tb_item_class');
INSERT INTO `auth_permission` VALUES ('64', 'Can add tb_item_pa', '22', 'add_tb_item_pa');
INSERT INTO `auth_permission` VALUES ('65', 'Can change tb_item_pa', '22', 'change_tb_item_pa');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete tb_item_pa', '22', 'delete_tb_item_pa');
INSERT INTO `auth_permission` VALUES ('67', 'Can add tb_article', '23', 'add_tb_article');
INSERT INTO `auth_permission` VALUES ('68', 'Can change tb_article', '23', 'change_tb_article');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete tb_article', '23', 'delete_tb_article');
INSERT INTO `auth_permission` VALUES ('70', 'Can add tb_album', '24', 'add_tb_album');
INSERT INTO `auth_permission` VALUES ('71', 'Can change tb_album', '24', 'change_tb_album');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete tb_album', '24', 'delete_tb_album');
INSERT INTO `auth_permission` VALUES ('73', 'Can add tb_pic', '25', 'add_tb_pic');
INSERT INTO `auth_permission` VALUES ('74', 'Can change tb_pic', '25', 'change_tb_pic');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete tb_pic', '25', 'delete_tb_pic');
INSERT INTO `auth_permission` VALUES ('76', 'Can add tb_accessory', '26', 'add_tb_accessory');
INSERT INTO `auth_permission` VALUES ('77', 'Can change tb_accessory', '26', 'change_tb_accessory');
INSERT INTO `auth_permission` VALUES ('78', 'Can delete tb_accessory', '26', 'delete_tb_accessory');
INSERT INTO `auth_permission` VALUES ('79', 'Can add tb_ artificial_ representations', '27', 'add_tb_artificial_representations');
INSERT INTO `auth_permission` VALUES ('80', 'Can change tb_ artificial_ representations', '27', 'change_tb_artificial_representations');
INSERT INTO `auth_permission` VALUES ('81', 'Can delete tb_ artificial_ representations', '27', 'delete_tb_artificial_representations');
INSERT INTO `auth_permission` VALUES ('82', 'Can add tb_ message', '28', 'add_tb_message');
INSERT INTO `auth_permission` VALUES ('83', 'Can change tb_ message', '28', 'change_tb_message');
INSERT INTO `auth_permission` VALUES ('84', 'Can delete tb_ message', '28', 'delete_tb_message');
INSERT INTO `auth_permission` VALUES ('85', 'Can add tb_ message text', '29', 'add_tb_messagetext');
INSERT INTO `auth_permission` VALUES ('86', 'Can change tb_ message text', '29', 'change_tb_messagetext');
INSERT INTO `auth_permission` VALUES ('87', 'Can delete tb_ message text', '29', 'delete_tb_messagetext');
INSERT INTO `auth_permission` VALUES ('88', 'Can add tb_ sys message', '30', 'add_tb_sysmessage');
INSERT INTO `auth_permission` VALUES ('89', 'Can change tb_ sys message', '30', 'change_tb_sysmessage');
INSERT INTO `auth_permission` VALUES ('90', 'Can delete tb_ sys message', '30', 'delete_tb_sysmessage');
INSERT INTO `auth_permission` VALUES ('91', 'Can add tb_goods', '31', 'add_tb_goods');
INSERT INTO `auth_permission` VALUES ('92', 'Can change tb_goods', '31', 'change_tb_goods');
INSERT INTO `auth_permission` VALUES ('93', 'Can delete tb_goods', '31', 'delete_tb_goods');
INSERT INTO `auth_permission` VALUES ('94', 'Can add tb_goods_click', '32', 'add_tb_goods_click');
INSERT INTO `auth_permission` VALUES ('95', 'Can change tb_goods_click', '32', 'change_tb_goods_click');
INSERT INTO `auth_permission` VALUES ('96', 'Can delete tb_goods_click', '32', 'delete_tb_goods_click');
INSERT INTO `auth_permission` VALUES ('97', 'Can add tb_goods_class', '33', 'add_tb_goods_class');
INSERT INTO `auth_permission` VALUES ('98', 'Can change tb_goods_class', '33', 'change_tb_goods_class');
INSERT INTO `auth_permission` VALUES ('99', 'Can delete tb_goods_class', '33', 'delete_tb_goods_class');
INSERT INTO `auth_permission` VALUES ('100', 'Can add tb_goods_evaluation', '34', 'add_tb_goods_evaluation');
INSERT INTO `auth_permission` VALUES ('101', 'Can change tb_goods_evaluation', '34', 'change_tb_goods_evaluation');
INSERT INTO `auth_permission` VALUES ('102', 'Can delete tb_goods_evaluation', '34', 'delete_tb_goods_evaluation');
INSERT INTO `auth_permission` VALUES ('103', 'Can add tb_order', '35', 'add_tb_order');
INSERT INTO `auth_permission` VALUES ('104', 'Can change tb_order', '35', 'change_tb_order');
INSERT INTO `auth_permission` VALUES ('105', 'Can delete tb_order', '35', 'delete_tb_order');
INSERT INTO `auth_permission` VALUES ('106', 'Can add tb_area', '36', 'add_tb_area');
INSERT INTO `auth_permission` VALUES ('107', 'Can change tb_area', '36', 'change_tb_area');
INSERT INTO `auth_permission` VALUES ('108', 'Can delete tb_area', '36', 'delete_tb_area');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$20000$gfG4zfThkngp$zh2ENS/JoUtJqeZ/ejvU0iosw9WGbTt9Y4RuhDuhpPg=', '2016-05-06 12:31:33', '1', 'zhangshuaishuai', '', '', '2468435837@qq.com', '1', '1', '2016-05-01 04:29:36');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=155 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2016-05-01 04:31:41', '1', '1@qq', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2016-05-01 04:31:59', '2', '2', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2016-05-01 04:32:25', '3', '3', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2016-05-01 04:34:16', '1', '1', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2016-05-01 04:34:36', '2', '2', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2016-05-01 04:34:58', '3', '3', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2016-05-01 04:35:31', '1', '1', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2016-05-01 04:35:50', '2', '2', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2016-05-01 04:36:33', '3', '3', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2016-05-01 04:36:53', '4', '4', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2016-05-01 04:37:15', '5', '5', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2016-05-01 04:37:31', '1', '1', '1', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2016-05-01 04:37:40', '2', '2', '1', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2016-05-01 04:37:48', '3', '3', '1', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2016-05-01 04:37:57', '4', '4', '1', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2016-05-01 04:38:07', '5', '5', '1', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2016-05-01 04:38:30', '1', '1', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2016-05-01 04:38:39', '2', '2', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2016-05-01 04:38:50', '3', '3', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2016-05-01 04:38:58', '4', '4', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2016-05-01 04:39:06', '5', '5', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2016-05-01 04:39:45', '1', '1', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2016-05-01 04:39:55', '2', '2', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2016-05-01 04:40:07', '3', '3', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2016-05-01 04:40:19', '4', '4', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2016-05-01 04:40:33', '5', '5', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2016-05-03 03:40:34', '1', '的说法是尽快快快快快快快', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2016-05-03 03:41:41', '2', '2016科技厅关于科技计划项目的申报通知', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2016-05-03 03:42:26', '3', '3', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2016-05-03 07:41:28', '1', '四川省科技厅', '1', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2016-05-03 07:41:53', '2', '四川农业局', '1', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2016-05-03 07:42:08', '3', '中央财政厅', '1', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2016-05-03 07:42:38', '4', '湖北教育局', '1', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2016-05-03 07:43:03', '5', '中央农业局', '1', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2016-05-03 12:27:11', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_name 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2016-05-03 13:11:04', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_publish 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2016-05-03 15:45:55', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2016-05-03 15:46:08', '2', '2', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2016-05-03 15:46:12', '3', '3', '2', '没有字段被修改。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2016-05-03 15:46:23', '3', '3', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2016-05-03 15:46:32', '4', '4', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2016-05-03 15:46:41', '5', '5', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2016-05-03 15:48:52', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2016-05-03 16:28:51', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_deadtime 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2016-05-03 16:42:07', '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_name 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2016-05-03 16:42:14', '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_name 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('47', '2016-05-03 16:42:21', '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_name 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2016-05-03 16:42:27', '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_name 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2016-05-03 16:44:59', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_about 和 item_key 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2016-05-03 16:46:10', '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_about 和 item_key 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('51', '2016-05-03 16:46:26', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '2', '已修改 item_about 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('52', '2016-05-03 16:47:09', '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_about 和 item_key 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('53', '2016-05-03 16:48:04', '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_about 和 item_key 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('54', '2016-05-03 16:48:50', '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_about 和 item_key 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('55', '2016-05-04 00:59:05', '1', '1', '1', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('56', '2016-05-04 02:08:20', '1', '1', '1', '', '31', '1');
INSERT INTO `django_admin_log` VALUES ('57', '2016-05-04 02:13:19', '2', '1', '1', '', '31', '1');
INSERT INTO `django_admin_log` VALUES ('58', '2016-05-04 02:25:14', '2', '1', '3', '', '31', '1');
INSERT INTO `django_admin_log` VALUES ('59', '2016-05-04 09:30:26', '6', '6', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('60', '2016-05-04 09:30:41', '7', '7', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('61', '2016-05-04 09:30:53', '8', '8', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('62', '2016-05-04 09:31:05', '9', '9', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('63', '2016-05-04 09:31:26', '10', '10', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('64', '2016-05-04 09:32:58', '11', '11', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('65', '2016-05-04 09:33:09', '12', '12', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('66', '2016-05-04 09:33:22', '13', '13', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('67', '2016-05-04 09:33:34', '14', '14', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('68', '2016-05-04 09:33:51', '15', '15', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('69', '2016-05-04 09:34:08', '16', '16', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('70', '2016-05-04 09:34:23', '18', '18', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('71', '2016-05-04 09:34:52', '6', '6', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('72', '2016-05-04 09:35:00', '7', '7', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('73', '2016-05-04 09:35:08', '8', '8', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('74', '2016-05-04 09:35:14', '9', '9', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('75', '2016-05-04 09:35:32', '10', '10', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('76', '2016-05-04 09:35:56', '11', '11', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('77', '2016-05-04 09:36:08', '12', '12', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('78', '2016-05-04 09:36:23', '13', '13', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('79', '2016-05-04 09:36:38', '14', '14', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('80', '2016-05-04 09:36:58', '15', '15', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('81', '2016-05-04 09:37:08', '16', '16', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('82', '2016-05-04 09:37:19', '17', '17', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('83', '2016-05-04 09:37:34', '18', '18', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('84', '2016-05-04 09:43:58', '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('85', '2016-05-04 09:45:00', '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('86', '2016-05-04 09:45:57', '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('87', '2016-05-04 09:46:52', '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('88', '2016-05-04 09:47:48', '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('89', '2016-05-04 09:48:46', '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('90', '2016-05-04 09:49:43', '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('91', '2016-05-04 09:50:50', '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('92', '2016-05-04 09:53:32', '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('93', '2016-05-04 09:54:32', '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('94', '2016-05-04 09:55:34', '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('95', '2016-05-04 09:56:25', '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('96', '2016-05-04 09:57:11', '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '1', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('97', '2016-05-04 09:58:36', '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('98', '2016-05-04 09:58:45', '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('99', '2016-05-04 09:58:53', '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('100', '2016-05-04 09:59:04', '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('101', '2016-05-04 09:59:14', '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('102', '2016-05-04 09:59:22', '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('103', '2016-05-04 09:59:28', '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('104', '2016-05-04 09:59:35', '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('105', '2016-05-04 09:59:41', '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('106', '2016-05-04 09:59:48', '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('107', '2016-05-04 09:59:54', '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('108', '2016-05-04 10:00:00', '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('109', '2016-05-04 10:00:04', '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '已修改 item_pa_id 。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('110', '2016-05-04 10:00:39', '3', '3', '2', '已修改 user_name 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('111', '2016-05-04 10:00:51', '2', '2', '2', '已修改 user_name 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('112', '2016-05-04 10:01:01', '1', '1@qq', '2', '已修改 user_name 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('113', '2016-05-04 10:01:21', '4', '111', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('114', '2016-05-04 10:01:56', '5', '1111', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('115', '2016-05-04 10:02:12', '6', '11111', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('116', '2016-05-04 10:03:01', '7', '1111', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('117', '2016-05-04 10:08:55', '1', '成都融亿达科技服务有限公司', '2', '已修改 company_tel，company_name，company_district，company_address，company_registered_capital，company_industry，company_stuff_no 和 company_nature 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('118', '2016-05-04 10:09:45', '1', '111111111111', '2', '已修改 company_tel 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('119', '2016-05-04 10:10:34', '3', '111111111111', '2', '已修改 company_tel，company_name，company_district，company_address，company_registered_capital，company_industry，company_stuff_no 和 company_nature 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('120', '2016-05-04 10:11:08', '2', ' 111111111111', '2', '已修改 company_tel，company_name，company_district，company_address，company_registered_capital，company_industry，company_stuff_no 和 company_nature 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('121', '2016-05-04 10:11:44', '4', '111111111111', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('122', '2016-05-04 10:12:23', '5', '111111111111', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('123', '2016-05-04 10:12:58', '6', '111111111111', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('124', '2016-05-04 10:13:27', '7', '111111111111', '1', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('125', '2016-05-04 10:15:44', '3', '2016科技厅关于科技计划项目的申报通知', '2', '已修改 item_name 。', '35', '1');
INSERT INTO `django_admin_log` VALUES ('126', '2016-05-04 10:16:45', '4', '2016科技厅关于科技计划项目的申报通知', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('127', '2016-05-04 10:17:23', '5', '2016科技厅关于科技计划项目的申报通知', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('128', '2016-05-04 10:18:14', '6', '2016科技厅关于科技计划项目的申报通知', '1', '', '35', '1');
INSERT INTO `django_admin_log` VALUES ('129', '2016-05-04 10:19:43', '1', '1', '2', '没有字段被修改。', '31', '1');
INSERT INTO `django_admin_log` VALUES ('130', '2016-05-04 10:22:13', '1', ' 2016科技厅关于科技计划项目的申报通知', '2', '已修改 goods_name 和 goods_market_price 。', '31', '1');
INSERT INTO `django_admin_log` VALUES ('131', '2016-05-04 10:23:18', '2', ' 2016科技厅关于科技计划项目的申报通知', '1', '', '31', '1');
INSERT INTO `django_admin_log` VALUES ('132', '2016-05-04 10:24:24', '3', ' 2016科技厅关于科技计划项目的申报通知', '1', '', '31', '1');
INSERT INTO `django_admin_log` VALUES ('133', '2016-05-04 10:28:19', '1', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 article_name 和 article_content 。', '23', '1');
INSERT INTO `django_admin_log` VALUES ('134', '2016-05-04 10:46:02', '17', '17', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('135', '2016-05-04 10:49:37', '1', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 item_name 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('136', '2016-05-04 10:49:45', '2', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 item_name 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('137', '2016-05-04 10:49:53', '3', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 item_name 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('138', '2016-05-04 10:49:58', '4', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 item_name 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('139', '2016-05-04 10:50:03', '5', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 item_name 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('140', '2016-05-06 13:50:06', '1', '1', '2', '没有字段被修改。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('141', '2016-05-06 13:50:31', '19', '19', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('142', '2016-05-06 13:51:08', '20', '20', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('143', '2016-05-06 13:51:23', '21', '21', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('144', '2016-05-06 13:51:33', '22', '22', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('145', '2016-05-06 13:54:33', '19', '19', '2', '已修改 pic_object 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('146', '2016-05-07 10:44:16', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '1', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('147', '2016-05-07 10:48:54', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '3', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('148', '2016-05-07 11:09:22', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '1', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('149', '2016-05-07 11:16:48', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '2', '已修改 article_content 。', '23', '1');
INSERT INTO `django_admin_log` VALUES ('150', '2016-05-07 11:17:59', '1', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 article_content 。', '23', '1');
INSERT INTO `django_admin_log` VALUES ('151', '2016-05-07 11:18:40', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '2', '已修改 article_content 。', '23', '1');
INSERT INTO `django_admin_log` VALUES ('152', '2016-05-07 11:18:51', '1', '2016科技厅关于科技计划项目的申报通知	', '2', '已修改 article_content 。', '23', '1');
INSERT INTO `django_admin_log` VALUES ('153', '2016-05-07 11:19:51', '3', '3', '1', '', '23', '1');
INSERT INTO `django_admin_log` VALUES ('154', '2016-05-07 11:20:34', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '2', '已修改 article_content 。', '23', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('4', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('6', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('5', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('7', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('8', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('1', 'easy_thumbnails', 'source');
INSERT INTO `django_content_type` VALUES ('2', 'easy_thumbnails', 'thumbnail');
INSERT INTO `django_content_type` VALUES ('3', 'easy_thumbnails', 'thumbnaildimensions');
INSERT INTO `django_content_type` VALUES ('9', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('26', 'zhengzihui_app', 'tb_accessory');
INSERT INTO `django_content_type` VALUES ('24', 'zhengzihui_app', 'tb_album');
INSERT INTO `django_content_type` VALUES ('17', 'zhengzihui_app', 'tb_apage');
INSERT INTO `django_content_type` VALUES ('18', 'zhengzihui_app', 'tb_apage_class');
INSERT INTO `django_content_type` VALUES ('36', 'zhengzihui_app', 'tb_area');
INSERT INTO `django_content_type` VALUES ('23', 'zhengzihui_app', 'tb_article');
INSERT INTO `django_content_type` VALUES ('27', 'zhengzihui_app', 'tb_artificial_representations');
INSERT INTO `django_content_type` VALUES ('31', 'zhengzihui_app', 'tb_goods');
INSERT INTO `django_content_type` VALUES ('33', 'zhengzihui_app', 'tb_goods_class');
INSERT INTO `django_content_type` VALUES ('32', 'zhengzihui_app', 'tb_goods_click');
INSERT INTO `django_content_type` VALUES ('34', 'zhengzihui_app', 'tb_goods_evaluation');
INSERT INTO `django_content_type` VALUES ('19', 'zhengzihui_app', 'tb_item');
INSERT INTO `django_content_type` VALUES ('21', 'zhengzihui_app', 'tb_item_class');
INSERT INTO `django_content_type` VALUES ('20', 'zhengzihui_app', 'tb_item_click');
INSERT INTO `django_content_type` VALUES ('22', 'zhengzihui_app', 'tb_item_pa');
INSERT INTO `django_content_type` VALUES ('28', 'zhengzihui_app', 'tb_message');
INSERT INTO `django_content_type` VALUES ('29', 'zhengzihui_app', 'tb_messagetext');
INSERT INTO `django_content_type` VALUES ('14', 'zhengzihui_app', 'tb_news');
INSERT INTO `django_content_type` VALUES ('13', 'zhengzihui_app', 'tb_news_class');
INSERT INTO `django_content_type` VALUES ('15', 'zhengzihui_app', 'tb_notice');
INSERT INTO `django_content_type` VALUES ('16', 'zhengzihui_app', 'tb_notice_class');
INSERT INTO `django_content_type` VALUES ('35', 'zhengzihui_app', 'tb_order');
INSERT INTO `django_content_type` VALUES ('25', 'zhengzihui_app', 'tb_pic');
INSERT INTO `django_content_type` VALUES ('12', 'zhengzihui_app', 'tb_service_provider');
INSERT INTO `django_content_type` VALUES ('30', 'zhengzihui_app', 'tb_sysmessage');
INSERT INTO `django_content_type` VALUES ('10', 'zhengzihui_app', 'tb_user');
INSERT INTO `django_content_type` VALUES ('11', 'zhengzihui_app', 'tb_user_expand');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-05-01 04:25:04');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-05-01 04:25:11');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-05-01 04:25:12');
INSERT INTO `django_migrations` VALUES ('4', 'contenttypes', '0002_remove_content_type_name', '2016-05-01 04:25:14');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0002_alter_permission_name_max_length', '2016-05-01 04:25:15');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0003_alter_user_email_max_length', '2016-05-01 04:25:15');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0004_alter_user_username_opts', '2016-05-01 04:25:15');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0005_alter_user_last_login_null', '2016-05-01 04:25:15');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0006_require_contenttypes_0002', '2016-05-01 04:25:15');
INSERT INTO `django_migrations` VALUES ('10', 'easy_thumbnails', '0001_initial', '2016-05-01 04:25:18');
INSERT INTO `django_migrations` VALUES ('11', 'easy_thumbnails', '0002_thumbnaildimensions', '2016-05-01 04:25:19');
INSERT INTO `django_migrations` VALUES ('12', 'sessions', '0001_initial', '2016-05-01 04:25:19');
INSERT INTO `django_migrations` VALUES ('13', 'zhengzihui_app', '0001_initial', '2016-05-01 04:25:27');
INSERT INTO `django_migrations` VALUES ('14', 'zhengzihui_app', '0002_auto_20160503_1519', '2016-05-03 07:19:34');
INSERT INTO `django_migrations` VALUES ('15', 'zhengzihui_app', '0003_auto_20160504_1910', '2016-05-04 11:10:08');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('qy3xpzcvw28iujvct0uq8ymjtqzr0chm', 'ZWI2MjQwY2Y4MWQxOWRlNmNkZmIwZDZiYzU2YzE5NzMzOWUxN2QxNjp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiX2F1dGhfdXNlcl9oYXNoIjoiODJiYzViZWFiZmQ0NTU0NzA2NGQ1ZTg4N2Q4MmQ1ODY1N2Y3MDU5YiIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-05-20 12:31:53');
INSERT INTO `django_session` VALUES ('vd5p3bqq84jqssxzp4wf85j7oxpsc2vb', 'MTRkYjJkODc5M2JiMTc3ZmZlNTM0YTBkNTAyY2NlM2ZlNTViYjg1MDp7ImJ1bWVuIjoiXHU4MGZkXHU2ZTkwIiwidXNlcl9pZCI6MywiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYmM1YmVhYmZkNDU1NDcwNjRkNWU4ODdkODJkNTg2NTdmNzA1OWIiLCJ6aHVhbmd0YWkiOiJcdTZiNjNcdTU3MjhcdTc1MzNcdTYyYTUsXHU2MjJhXHU2YjYyXHU3NTMzXHU2MmE1In0=', '2016-05-18 11:16:56');

-- ----------------------------
-- Table structure for easy_thumbnails_source
-- ----------------------------
DROP TABLE IF EXISTS `easy_thumbnails_source`;
CREATE TABLE `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_storage_hash_3e1b0d13_uniq` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_source_b068931c` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of easy_thumbnails_source
-- ----------------------------

-- ----------------------------
-- Table structure for easy_thumbnails_thumbnail
-- ----------------------------
DROP TABLE IF EXISTS `easy_thumbnails_thumbnail`;
CREATE TABLE `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_thumbnail_storage_hash_7ef9fce_uniq` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thumbnails__source_id_7106e1b7_fk_easy_thumbnails_source_id` (`source_id`),
  KEY `easy_thumbnails_thumbnail_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_b068931c` (`name`),
  CONSTRAINT `easy_thumbnails__source_id_7106e1b7_fk_easy_thumbnails_source_id` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of easy_thumbnails_thumbnail
-- ----------------------------

-- ----------------------------
-- Table structure for easy_thumbnails_thumbnaildimensions
-- ----------------------------
DROP TABLE IF EXISTS `easy_thumbnails_thumbnaildimensions`;
CREATE TABLE `easy_thumbnails_thumbnaildimensions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thumbnail_id` int(11) NOT NULL,
  `width` int(10) unsigned DEFAULT NULL,
  `height` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thumbnail_id` (`thumbnail_id`),
  CONSTRAINT `easy_thumb_thumbnail_id_314c3e84_fk_easy_thumbnails_thumbnail_id` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of easy_thumbnails_thumbnaildimensions
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_accessory
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_accessory`;
CREATE TABLE `zhengzihui_app_tb_accessory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anne_id` int(11) NOT NULL,
  `comm_id` int(11) NOT NULL,
  `apubdate` int(11) NOT NULL,
  `apublisher` varchar(2) NOT NULL,
  `aposition` varchar(10) NOT NULL,
  `aaddtion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_accessory
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_album
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_album`;
CREATE TABLE `zhengzihui_app_tb_album` (
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

-- ----------------------------
-- Records of zhengzihui_app_tb_album
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_album` VALUES ('1', '1', '0', '1', '1', '1', '2016-05-01 04:38:30', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('2', '2', '0', '2', '2', '2', '2016-05-01 04:38:39', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('3', '3', '0', '3', '3', '3', '2016-05-01 04:38:50', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('4', '4', '0', '4', '4', '4', '2016-05-01 04:38:58', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('5', '5', '0', '5', '5', '5', '2016-05-01 04:39:06', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('6', '6', '0', '6', '6', '6', '2016-05-04 09:34:52', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('7', '7', '0', '7', '7', '7', '2016-05-04 09:35:00', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('8', '8', '0', '8', '8', '8', '2016-05-04 09:35:08', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('9', '9', '0', '9', '9', '9', '2016-05-04 09:35:14', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('10', '10', '0', '10', '10', '10', '2016-05-04 09:35:32', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('11', '11', '0', '11', '11', '11', '2016-05-04 09:35:56', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('12', '12', '0', '12', '12', '12', '2016-05-04 09:36:08', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('13', '13', '0', '13', '13', '13', '2016-05-04 09:36:23', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('14', '14', '0', '14', '14', '14', '2016-05-04 09:36:38', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('15', '15', '0', '15', '15', '15', '2016-05-04 09:36:58', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('16', '16', '0', '16', '16', '16', '2016-05-04 09:37:08', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('17', '17', '0', '17', '17', '17', '2016-05-04 09:37:19', '1');
INSERT INTO `zhengzihui_app_tb_album` VALUES ('18', '18', '0', '18', '18', '18', '2016-05-04 09:37:34', '1');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_apage
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_apage`;
CREATE TABLE `zhengzihui_app_tb_apage` (
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

-- ----------------------------
-- Records of zhengzihui_app_tb_apage
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_apage_class
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_apage_class`;
CREATE TABLE `zhengzihui_app_tb_apage_class` (
  `Apcl_id` int(11) NOT NULL,
  `Apcl_code` int(11) NOT NULL,
  `Apcl_name` varchar(100) NOT NULL,
  `Apcl_parent_id` int(11) NOT NULL,
  `Apcl_sort` int(11) NOT NULL,
  PRIMARY KEY (`Apcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_apage_class
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_area
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_area`;
CREATE TABLE `zhengzihui_app_tb_area` (
  `area_id` int(11) NOT NULL,
  `area_name` varchar(100) NOT NULL,
  `area_parent_id` int(11) NOT NULL,
  `area_sort` int(11) NOT NULL,
  `area_deep` int(11) NOT NULL,
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_area
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_article
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_article`;
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
  `article_click` int(11) NOT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_article
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_article` VALUES ('1', '1', '2016科技厅关于科技计划项目的申报通知	', '1', '1@qq.com', '0', '1', '     近日，四川省教育考试院来函批复，同意西华大学今年将22个本科专业调整到本科一批次录取。加上去年纳入本科一批次招生的21个专业，2016年西华大学共有43个专业纳入本科一批次在川招生，预计该校普通本科一本批次招生计划将占普通本科总计划数的60%。', '1', '1', '1', '2016-05-07 11:18:51', '1', '1');
INSERT INTO `zhengzihui_app_tb_article` VALUES ('2', '2', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '项目负责人、申报单位登录“四川省科技计划项目管理中心”', '1111@sina.com', '0', '1', '金正恩在讲话中高度肯定了朝鲜在今年1月份的核试验和2月份的火箭发射所取得的“前所未有”的伟大成就。\r\n　　朝鲜劳动党第七次全国代表大会6日在平壤开幕，朝中社当天曾发布一万多字的长篇报道称“开发小型核弹头是送给劳动党七大的礼物”。\r\n　　报道称，开发小型核弹头、弹道火箭重返大气层环境模拟试验取得成功、进行高功率固体火箭发动机地上点火及级间分离试验、进行新型洲际弹道火箭大功率发动机地上点火试验是朝鲜国防科技人员向劳动党七大献礼。\r\n　　此前，金正恩的西装照片几乎只出现在朝鲜对外公布的领导人官方照片中。\r\n　　韩国电视台对朝鲜电视台金正恩的讲话做了报道评论。韩国分析人士认为，朝鲜劳动党七大日程表一开始就未包含进行第五次核试验。而朝鲜是否举行第五次核试验，这也是韩国方面此前最担心的事情。', '111111111111111111111111111', '1', '1', '2016-05-07 11:20:34', '1', '1');
INSERT INTO `zhengzihui_app_tb_article` VALUES ('3', '3', '3', '3', '1111@sina.com', '0', '1', '从去年开始，川内不少老牌二本院校就将大批二本专业调整至一本招生，今年这一趋势仍在继续，再加上去年四川合并二、三本批次，各个批次的界限越来越模糊，这背后将会给考生们带来什么样的影响？考生们在志愿填报上应有哪些应对之策？记者采访了相关专家。', '3', '3', '3', '2016-05-07 11:19:51', '1', '3');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_artificial_representations
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_artificial_representations`;
CREATE TABLE `zhengzihui_app_tb_artificial_representations` (
  `arre_id` int(11) NOT NULL AUTO_INCREMENT,
  `arre_title` varchar(100) NOT NULL,
  `arre_content` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `arre_state` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`arre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_artificial_representations
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_goods
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_goods`;
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
  `goods_status` int(11) NOT NULL,
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_goods
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_goods` VALUES ('1', '1', '1', ' 2016科技厅关于科技计划项目的申报通知', '100000', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0');
INSERT INTO `zhengzihui_app_tb_goods` VALUES ('2', '1', '1', ' 2016科技厅关于科技计划项目的申报通知', '18888', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0');
INSERT INTO `zhengzihui_app_tb_goods` VALUES ('3', '1', '1', ' 2016科技厅关于科技计划项目的申报通知', '56781', '1', '3', '1', '1', '1', '0', '1', '1', '1', '0');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_goods_class
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_class`;
CREATE TABLE `zhengzihui_app_tb_goods_class` (
  `gocl_id` int(11) NOT NULL,
  `gocl_code` int(11) NOT NULL,
  `gocl_name` varchar(40) NOT NULL,
  `gocl_des` varchar(100) NOT NULL,
  `gocl_sort` int(11) NOT NULL,
  `gocl_parent_id` int(11) NOT NULL,
  PRIMARY KEY (`gocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_goods_class
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_goods_click
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_click`;
CREATE TABLE `zhengzihui_app_tb_goods_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) NOT NULL,
  `gocl_id` int(11) NOT NULL,
  `gocl_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_goods_click
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_goods_evaluation
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_evaluation`;
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
  `goev_status` int(11) NOT NULL,
  PRIMARY KEY (`goev_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_goods_evaluation
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_item
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_item`;
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
  `is_recommend` int(11) NOT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_item
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_item` VALUES ('1', '1', '四川省科技厅计划项目招标通知2016之特别假话找白哦', '1', '1', '1', '1', '2016-04-03 04:35:19', '2016-05-03 16:28:49', '养殖/科技/互联网', '1', '科技项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('2', '2', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '2', '1', '2', '2', '2016-05-01 04:35:42', '2016-06-18 04:35:43', '农林/住建/其他', '2', '互联网项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('3', '3', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '3', '1', '3', '3', '2016-05-01 04:36:23', '2016-07-15 04:36:24', '农业/养殖/互联网+', '3', '科技项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('4', '4', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '4', '1', '4', '4', '2016-05-01 04:36:47', '2016-05-28 04:36:48', '水产/养殖/其他', '4', '科技项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('5', '5', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '5', '1', '5', '5', '2016-05-01 04:37:05', '2016-07-08 04:37:07', '水产/政务/管理/新产业', '5', '中央项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('6', '6', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '6', '1', '5万-500万', '1', '2016-03-08 09:42:34', '2016-09-01 09:42:39', '农业/养殖/互联网+', '6', '水产/政务/管理/新产业', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('7', '7', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '7', '1', '5万-500万', '2', '2016-03-23 09:44:34', '2016-06-11 09:44:38', '水产/政务/管理/新产业', '7', '科技项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('8', '8', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '8', '1', '5万-500万', '3', '2015-12-03 09:45:32', '2016-06-30 09:45:40', '农林/住建/其他', '8', '互联网项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('9', '9', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '9', '1', '5万-500万', '4', '2016-04-13 09:46:22', '2016-06-17 09:46:26', '农业/养殖/互联网+', '9', '中央项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('10', '10', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '10', '1', '5万-500万', '5', '2016-05-01 09:47:25', '2016-05-31 09:47:28', '水产/政务/管理/新产业', '10', '科技项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('11', '11', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '11', '1', '5万-500万', '1', '2016-04-03 09:48:13', '2016-05-04 09:48:23', '养殖/科技/互联网', '11', '互联网项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('12', '12', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '12', '1', '5万-500万', '2', '2016-04-07 09:49:12', '2016-05-04 09:49:15', '养殖/科技/互联网', '12', '中央项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('13', '13', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '13', '1', '5万-500万', '3', '2016-04-10 09:50:24', '2016-05-28 09:50:30', '水产/政务/管理/新产业', '13', '科技项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('14', '14', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '14', '1', '5万-500万', '4', '2016-04-01 09:53:00', '2016-06-09 09:53:03', '水产/政务/管理/新产业', '14', '科技项目', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('15', '15', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '15', '1', '5万-500万', '5', '2016-04-05 09:54:09', '2016-05-04 09:54:12', '养殖/科技/互联网', '15', '互联网项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('16', '16', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '16', '1', '5万-500万', '1', '2016-04-03 09:55:05', '2016-06-24 09:55:08', '农林/住建/其他', '16', '中央项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('17', '17', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '17', '1', '5万-500万', '2', '2016-04-20 09:56:04', '2016-07-08 09:56:08', '水产/政务/管理/新产业 ', '17', '科技项目', '0', '0', '0', '0');
INSERT INTO `zhengzihui_app_tb_item` VALUES ('18', '18', '四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦', '18', '1', '5万-500万', '3', '2016-03-31 09:56:50', '2016-05-26 09:56:53', '农业/养殖/互联网+', '18', '互联网项目', '0', '0', '0', '0');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_item_class
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_item_class`;
CREATE TABLE `zhengzihui_app_tb_item_class` (
  `itcl_id` int(11) NOT NULL,
  `itcl_code` int(11) NOT NULL,
  `itcl_name` varchar(100) NOT NULL,
  `itcl_des` varchar(100) NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`itcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_item_class
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_item_click
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_item_click`;
CREATE TABLE `zhengzihui_app_tb_item_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `itcl_id` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_item_click
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_item_click` VALUES ('1', '1', '2016科技厅关于科技计划项目的申报通知	', '1', '1');
INSERT INTO `zhengzihui_app_tb_item_click` VALUES ('2', '2', '2016科技厅关于科技计划项目的申报通知	', '2', '2');
INSERT INTO `zhengzihui_app_tb_item_click` VALUES ('3', '3', '2016科技厅关于科技计划项目的申报通知	', '3', '3');
INSERT INTO `zhengzihui_app_tb_item_click` VALUES ('4', '4', '2016科技厅关于科技计划项目的申报通知	', '4', '4');
INSERT INTO `zhengzihui_app_tb_item_click` VALUES ('5', '5', '2016科技厅关于科技计划项目的申报通知	', '5', '5');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_item_pa
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_item_pa`;
CREATE TABLE `zhengzihui_app_tb_item_pa` (
  `ipa_id` int(11) NOT NULL,
  `ipa_name` varchar(100) NOT NULL,
  `ipa_parent_id` int(11) NOT NULL,
  `ipa_sort` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  PRIMARY KEY (`ipa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_item_pa
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_item_pa` VALUES ('1', '四川省科技厅', '1', '1', '1');
INSERT INTO `zhengzihui_app_tb_item_pa` VALUES ('2', '四川农业局', '2', '2', '2');
INSERT INTO `zhengzihui_app_tb_item_pa` VALUES ('3', '中央财政厅', '3', '3', '3');
INSERT INTO `zhengzihui_app_tb_item_pa` VALUES ('4', '湖北教育局', '4', '4', '4');
INSERT INTO `zhengzihui_app_tb_item_pa` VALUES ('5', '中央农业局', '5', '5', '5');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_message
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_message`;
CREATE TABLE `zhengzihui_app_tb_message` (
  `mess_id` int(11) NOT NULL,
  `send_id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL,
  `text_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`mess_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_message
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_messagetext
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_messagetext`;
CREATE TABLE `zhengzihui_app_tb_messagetext` (
  `text_id` int(11) NOT NULL,
  `mete_title` varchar(10) NOT NULL,
  `mete_content` varchar(300) NOT NULL,
  `mete_time` datetime NOT NULL,
  PRIMARY KEY (`text_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_messagetext
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_news
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_news`;
CREATE TABLE `zhengzihui_app_tb_news` (
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

-- ----------------------------
-- Records of zhengzihui_app_tb_news
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_news_class
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_news_class`;
CREATE TABLE `zhengzihui_app_tb_news_class` (
  `necl_id` int(11) NOT NULL AUTO_INCREMENT,
  `necl_code` int(11) NOT NULL,
  `necl_name` varchar(100) NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`necl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_news_class
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_notice
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_notice`;
CREATE TABLE `zhengzihui_app_tb_notice` (
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

-- ----------------------------
-- Records of zhengzihui_app_tb_notice
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_notice_class
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_notice_class`;
CREATE TABLE `zhengzihui_app_tb_notice_class` (
  `Nocl_id` int(11) NOT NULL,
  `Nocl_code` int(11) NOT NULL,
  `Nocl_name` varchar(100) NOT NULL,
  `Nocl_des` varchar(100) NOT NULL,
  `Nocl_parent_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  PRIMARY KEY (`Nocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_notice_class
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_order
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_order`;
CREATE TABLE `zhengzihui_app_tb_order` (
  `order_id` int(11) NOT NULL,
  `order_no` int(11) NOT NULL,
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
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_order
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_order` VALUES ('1', '1', '1', '1', '的说法是尽快快快快快快快', '1', '1', '3', '3', '1@qq.com', '2016-05-21 03:39:54', '1', '2016-05-03 03:39:59', '2016-05-03 03:40:00', '1', '77777', '0', '2016-05-03 03:40:16', '1', '1', '1', '0', '0', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_order` VALUES ('2', '2', '2', '2', '2016科技厅关于科技计划项目的申报通知', '1', '1', '3', '1', '1@qq.com', '2016-05-03 03:41:10', '1', '2016-05-03 03:41:11', '2016-05-03 03:41:14', '1', '8888', '1', '2016-05-03 03:41:23', '1', '1', '1', '0', '1', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_order` VALUES ('3', '3', '3', '3', '2016科技厅关于科技计划项目的申报通知', '3', '3', '3', '3', '1@qq.com', '2016-05-02 03:42:03', '1', '2016-05-03 03:42:07', '2016-05-03 03:42:08', '1', '9999', '1', '2016-05-03 03:42:17', '1', '1', '1', '0', '2', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_order` VALUES ('4', '4', '4', '4', '2016科技厅关于科技计划项目的申报通知', '4', '4', '3', '3', '1@qq.com', '2016-05-04 10:16:26', '1', '2016-05-04 10:16:29', '2016-05-04 10:16:30', '1', '0', '1', '2016-05-04 10:16:34', '1', '1', '1', '0', '3', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_order` VALUES ('5', '5', '5', '5', '2016科技厅关于科技计划项目的申报通知', '5', '5', '3', '3', '1@qq.com', '2016-05-04 10:17:06', '1', '2016-05-04 10:17:09', '2016-05-04 10:17:11', '1', '0', '1', '2016-05-04 10:17:15', '1', '11', '1', '0', '4', '0', '0', '1');
INSERT INTO `zhengzihui_app_tb_order` VALUES ('6', '6', '6', '6', '2016科技厅关于科技计划项目的申报通知', '6', '6', '3', '3', '1@qq.com', '2016-05-04 10:17:53', '1', '2016-05-04 10:17:58', '2016-05-04 10:17:59', '1', '0', '1', '2016-05-04 10:18:04', '1', '11', '1', '0', '0', '0', '0', '1');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_pic
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_pic`;
CREATE TABLE `zhengzihui_app_tb_pic` (
  `pic_id` int(11) NOT NULL,
  `pic_name` varchar(40) NOT NULL,
  `pic_tag` varchar(40) NOT NULL,
  `album_id` int(11) NOT NULL,
  `pic_object` varchar(100) NOT NULL,
  `pic_size` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  PRIMARY KEY (`pic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_pic
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('1', '1', '1', '1', 'img_for_items/2016/05/01/6aa33f80-a3c0-11e5-a70d-dc85def86878.png', '0', '2016-05-06 13:50:06');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('2', '2', '2', '2', 'img_for_items/2016/05/01/4adbe14f-a557-11e5-bd34-dc85def86878.png', '0', '2016-05-01 04:39:55');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('3', '3', '3', '3', 'img_for_items/2016/05/01/9a77684f-a558-11e5-91f7-dc85def86878.png', '0', '2016-05-01 04:40:07');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('4', '4', '4', '4', 'img_for_items/2016/05/01/34fd605a-a658-11e5-8df7-00163e0022d3.png', '0', '2016-05-01 04:40:19');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('5', '5', '5', '5', 'img_for_items/2016/05/01/39a46b8f-a558-11e5-949b-dc85def86878.png', '0', '2016-05-01 04:40:33');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('6', '6', '6', '6', 'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878.png', '0', '2016-05-04 09:30:26');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('7', '7', '7', '7', 'img_for_items/2016/05/04/6a12a4de-a558-11e5-b72c-dc85def86878.png', '0', '2016-05-04 09:30:41');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('8', '8', '8', '8', 'img_for_items/2016/05/04/34fd605a-a658-11e5-8df7-00163e0022d3.png', '0', '2016-05-04 09:30:53');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('9', '9', '9', '9', 'img_for_items/2016/05/04/6bd92fc0-a476-11e5-aaa1-dc85def86878.png', '0', '2016-05-04 09:31:05');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('10', '10', '10', '10', 'img_for_items/2016/05/04/76c0c68f-a265-11e5-80d4-3859f9fa9803.png', '0', '2016-05-04 09:31:25');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('11', '11', '11', '11', 'img_for_items/2016/05/04/56de86b0-a557-11e5-92af-dc85def86878.png', '0', '2016-05-04 09:32:58');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('12', '12', '12', '12', 'img_for_items/2016/05/04/2f9f86de-a277-11e5-a84a-3859f9fa9803.png', '0', '2016-05-04 09:33:09');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('13', '13', '13', '13', 'img_for_items/2016/05/04/9fdac0b0-a3c0-11e5-8a73-dc85def86878.png', '0', '2016-05-04 09:33:22');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('14', '14', '14', '14', 'img_for_items/2016/05/04/98c5db1e-a3c0-11e5-b491-dc85def86878.png', '0', '2016-05-04 09:33:34');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('15', '15', '15', '15', 'img_for_items/2016/05/04/2df0ed11-a557-11e5-8e43-dc85def86878.png', '0', '2016-05-04 09:33:51');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('16', '16', '16', '16', 'img_for_items/2016/05/04/17675c61-a263-11e5-a423-3859f9fa9803.png', '0', '2016-05-04 09:34:08');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('17', '17', '17', '17', 'img_for_items/2016/05/04/5be48e0f-a265-11e5-89c3-3859f9fa9803.png', '0', '2016-05-04 10:46:02');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('18', '18', '18', '18', 'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878_v0SFX5j.png', '0', '2016-05-04 09:34:23');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('19', '19', '19', '1', 'img_for_items/2016/05/06/a7.jpg', '0', '2016-05-06 13:54:33');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('20', '20', '20', '1', 'img_for_items/2016/05/06/a5.jpg', '0', '2016-05-06 13:51:08');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('21', '21', '21', '1', 'img_for_items/2016/05/06/a4.jpg', '0', '2016-05-06 13:51:23');
INSERT INTO `zhengzihui_app_tb_pic` VALUES ('22', '22', '22', '1', 'img_for_items/2016/05/06/a2.jpg', '0', '2016-05-06 13:51:33');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_service_provider
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_service_provider`;
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
  `is_recommend` int(11) NOT NULL,
  PRIMARY KEY (`sp_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_service_provider
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_sysmessage
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_sysmessage`;
CREATE TABLE `zhengzihui_app_tb_sysmessage` (
  `sys_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `mess_id` int(11) NOT NULL,
  `sys_status` int(11) NOT NULL,
  PRIMARY KEY (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_sysmessage
-- ----------------------------

-- ----------------------------
-- Table structure for zhengzihui_app_tb_user
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_user`;
CREATE TABLE `zhengzihui_app_tb_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_telephone` varchar(40) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_auth` int(11) NOT NULL,
  `user_type` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of zhengzihui_app_tb_user
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_user` VALUES ('1', '郭捷', '1', '1@qq', '1@qq.com', '0', '1');
INSERT INTO `zhengzihui_app_tb_user` VALUES ('2', '李泽华', '2', '2', '1@qq.com', '0', '1');
INSERT INTO `zhengzihui_app_tb_user` VALUES ('3', '张帅帅', '111', '3', '1@qq.com', '0', '1');
INSERT INTO `zhengzihui_app_tb_user` VALUES ('4', '袁志', '111', '111', '1@qq.com', '0', '0');
INSERT INTO `zhengzihui_app_tb_user` VALUES ('5', '常益凡', '111', '1111', '1@qq.com', '0', '0');
INSERT INTO `zhengzihui_app_tb_user` VALUES ('6', '徐成章', '1111', '11111', '1@qq.com', '0', '0');
INSERT INTO `zhengzihui_app_tb_user` VALUES ('7', '罗杰炜', '1111', '1111', '1@qq.com', '0', '0');

-- ----------------------------
-- Table structure for zhengzihui_app_tb_user_expand
-- ----------------------------
DROP TABLE IF EXISTS `zhengzihui_app_tb_user_expand`;
CREATE TABLE `zhengzihui_app_tb_user_expand` (
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

-- ----------------------------
-- Records of zhengzihui_app_tb_user_expand
-- ----------------------------
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('1', '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', '四川成都市大慈寺', '四川成都市大慈寺', '100000000', '互联网科技服务', '100', '私营');
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('2', ' 111111111111', '1@qq.com', '成都融亿达科技服务有限公司', '2 四川成都市大慈寺', ' 四川成都市大慈寺', '10000000', ' 互联网科技服务', '100', ' 私营');
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('3', '1', '1@qq.com', '成都融亿达科技服务有限公司', '四川成都市大慈寺', '四川成都市大慈寺', '10000000', ' 互联网科技服务', '100', '私营');
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('4', '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', ' 四川成都市大慈寺', ' 四川成都市大慈寺', '10000000', ' 互联网科技服务', '100', '私营');
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('5', '111111111111', '1@qq.com', ' 四川成都市大慈寺', ' 四川成都市大慈寺', ' 四川成都市大慈寺', '10000000', ' 互联网科技服务', '100', '私营');
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('6', '111111111111', '1@qq.com', '成都融亿达科技服务有限公', ' 四川成都市大慈寺', ' 四川成都市大慈寺', '10000000', ' 互联网科技服务', '100', '私营');
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES ('7', '111111111111', '1@qq.com', '成都融亿达科技服务有限公司', ' 四川成都市大慈寺', ' 四川成都市大慈寺', '10000000', '互联网科技服务', '100', ' 私营');
