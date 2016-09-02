-- MySQL dump 10.13  Distrib 5.7.13, for Linux (x86_64)
--
-- Host: localhost    Database: zhengzihui_test_second
-- ------------------------------------------------------
-- Server version	5.7.13-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add source',1,'add_source'),(2,'Can change source',1,'change_source'),(3,'Can delete source',1,'delete_source'),(4,'Can add thumbnail',2,'add_thumbnail'),(5,'Can change thumbnail',2,'change_thumbnail'),(6,'Can delete thumbnail',2,'delete_thumbnail'),(7,'Can add thumbnail dimensions',3,'add_thumbnaildimensions'),(8,'Can change thumbnail dimensions',3,'change_thumbnaildimensions'),(9,'Can delete thumbnail dimensions',3,'delete_thumbnaildimensions'),(10,'Can add log entry',4,'add_logentry'),(11,'Can change log entry',4,'change_logentry'),(12,'Can delete log entry',4,'delete_logentry'),(13,'Can add permission',5,'add_permission'),(14,'Can change permission',5,'change_permission'),(15,'Can delete permission',5,'delete_permission'),(16,'Can add group',6,'add_group'),(17,'Can change group',6,'change_group'),(18,'Can delete group',6,'delete_group'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add content type',8,'add_contenttype'),(23,'Can change content type',8,'change_contenttype'),(24,'Can delete content type',8,'delete_contenttype'),(25,'Can add session',9,'add_session'),(26,'Can change session',9,'change_session'),(27,'Can delete session',9,'delete_session'),(28,'Can add 用户扩展信息',10,'add_tb_user_expand'),(29,'Can change 用户扩展信息',10,'change_tb_user_expand'),(30,'Can delete 用户扩展信息',10,'delete_tb_user_expand'),(31,'Can add 用户',11,'add_tb_user'),(32,'Can change 用户',11,'change_tb_user'),(33,'Can delete 用户',11,'delete_tb_user'),(34,'Can add 服务提供商',12,'add_tb_service_provider'),(35,'Can change 服务提供商',12,'change_tb_service_provider'),(36,'Can delete 服务提供商',12,'delete_tb_service_provider'),(37,'Can add 新闻类别',13,'add_tb_news_class'),(38,'Can change 新闻类别',13,'change_tb_news_class'),(39,'Can delete 新闻类别',13,'delete_tb_news_class'),(40,'Can add 新闻',14,'add_tb_news'),(41,'Can change 新闻',14,'change_tb_news'),(42,'Can delete 新闻',14,'delete_tb_news'),(43,'Can add 公告 ',15,'add_tb_notice'),(44,'Can change 公告 ',15,'change_tb_notice'),(45,'Can delete 公告 ',15,'delete_tb_notice'),(46,'Can add 公告类别',16,'add_tb_notice_class'),(47,'Can change 公告类别',16,'change_tb_notice_class'),(48,'Can delete 公告类别',16,'delete_tb_notice_class'),(49,'Can add 单页表',17,'add_tb_apage'),(50,'Can change 单页表',17,'change_tb_apage'),(51,'Can delete 单页表',17,'delete_tb_apage'),(52,'Can add 单页分类表',18,'add_tb_apage_class'),(53,'Can change 单页分类表',18,'change_tb_apage_class'),(54,'Can delete 单页分类表',18,'delete_tb_apage_class'),(55,'Can add 项目详情表',19,'add_tb_item'),(56,'Can change 项目详情表',19,'change_tb_item'),(57,'Can delete 项目详情表',19,'delete_tb_item'),(58,'Can add 项目点击表',20,'add_tb_item_click'),(59,'Can change 项目点击表',20,'change_tb_item_click'),(60,'Can delete 项目点击表',20,'delete_tb_item_click'),(61,'Can add 项目发布机构表',21,'add_tb_item_pa'),(62,'Can change 项目发布机构表',21,'change_tb_item_pa'),(63,'Can delete 项目发布机构表',21,'delete_tb_item_pa'),(64,'Can add tb_shoucang_item',22,'add_tb_shoucang_item'),(65,'Can change tb_shoucang_item',22,'change_tb_shoucang_item'),(66,'Can delete tb_shoucang_item',22,'delete_tb_shoucang_item'),(67,'Can add tb_shoucang_goods',23,'add_tb_shoucang_goods'),(68,'Can change tb_shoucang_goods',23,'change_tb_shoucang_goods'),(69,'Can delete tb_shoucang_goods',23,'delete_tb_shoucang_goods'),(70,'Can add 地区表',24,'add_tb_area'),(71,'Can change 地区表',24,'change_tb_area'),(72,'Can delete 地区表',24,'delete_tb_area'),(73,'Can add 项目分类',25,'add_tb_item_class'),(74,'Can change 项目分类',25,'change_tb_item_class'),(75,'Can delete 项目分类',25,'delete_tb_item_class'),(76,'Can add 文章表',26,'add_tb_article'),(77,'Can change 文章表',26,'change_tb_article'),(78,'Can delete 文章表',26,'delete_tb_article'),(79,'Can add 相册表',27,'add_tb_album'),(80,'Can change 相册表',27,'change_tb_album'),(81,'Can delete 相册表',27,'delete_tb_album'),(82,'Can add 图片表',28,'add_tb_pic'),(83,'Can change 图片表',28,'change_tb_pic'),(84,'Can delete 图片表',28,'delete_tb_pic'),(85,'Can add 其他附件表',29,'add_tb_accessory'),(86,'Can change 其他附件表',29,'change_tb_accessory'),(87,'Can delete 其他附件表',29,'delete_tb_accessory'),(88,'Can add 人工申述表',30,'add_tb_artificial_representations'),(89,'Can change 人工申述表',30,'change_tb_artificial_representations'),(90,'Can delete 人工申述表',30,'delete_tb_artificial_representations'),(91,'Can add 站内短信表',31,'add_tb_message'),(92,'Can change 站内短信表',31,'change_tb_message'),(93,'Can delete 站内短信表',31,'delete_tb_message'),(94,'Can add 站内短信内容表',32,'add_tb_messagetext'),(95,'Can change 站内短信内容表',32,'change_tb_messagetext'),(96,'Can delete 站内短信内容表',32,'delete_tb_messagetext'),(97,'Can add 系统信息表',33,'add_tb_sysmessage'),(98,'Can change 系统信息表',33,'change_tb_sysmessage'),(99,'Can delete 系统信息表',33,'delete_tb_sysmessage'),(100,'Can add 服务商信息表',34,'add_tb_goods'),(101,'Can change 服务商信息表',34,'change_tb_goods'),(102,'Can delete 服务商信息表',34,'delete_tb_goods'),(103,'Can add 服务商点击表',35,'add_tb_goods_click'),(104,'Can change 服务商点击表',35,'change_tb_goods_click'),(105,'Can delete 服务商点击表',35,'delete_tb_goods_click'),(106,'Can add 服务商分类表',36,'add_tb_goods_class'),(107,'Can change 服务商分类表',36,'change_tb_goods_class'),(108,'Can delete 服务商分类表',36,'delete_tb_goods_class'),(109,'Can add 服务商评价表',37,'add_tb_goods_evaluation'),(110,'Can change 服务商评价表',37,'change_tb_goods_evaluation'),(111,'Can delete 服务商评价表',37,'delete_tb_goods_evaluation'),(112,'Can add 订单表',38,'add_tb_order'),(113,'Can change 订单表',38,'change_tb_order'),(114,'Can delete 订单表',38,'delete_tb_order'),(115,'Can add tb_companyuser',39,'add_tb_companyuser'),(116,'Can change tb_companyuser',39,'change_tb_companyuser'),(117,'Can delete tb_companyuser',39,'delete_tb_companyuser'),(118,'Can add tb_customcompany',40,'add_tb_customcompany'),(119,'Can change tb_customcompany',40,'change_tb_customcompany'),(120,'Can delete tb_customcompany',40,'delete_tb_customcompany'),(121,'Can add 待测服务信息表',41,'add_tb_goods_wfc'),(122,'Can change 待测服务信息表',41,'change_tb_goods_wfc'),(123,'Can delete 待测服务信息表',41,'delete_tb_goods_wfc');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$vrePNmsfkowk$6tslXw/PW6FIHwaJdhn4t6OnDNvnyOVyTDv4FD0tInI=','2016-07-19 08:42:44',1,'admin','','','oeiro@qq.com',1,1,'2016-07-19 08:42:36');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (4,'admin','logentry'),(6,'auth','group'),(5,'auth','permission'),(7,'auth','user'),(8,'contenttypes','contenttype'),(1,'easy_thumbnails','source'),(2,'easy_thumbnails','thumbnail'),(3,'easy_thumbnails','thumbnaildimensions'),(9,'sessions','session'),(29,'zhengzihui_app','tb_accessory'),(27,'zhengzihui_app','tb_album'),(17,'zhengzihui_app','tb_apage'),(18,'zhengzihui_app','tb_apage_class'),(24,'zhengzihui_app','tb_area'),(26,'zhengzihui_app','tb_article'),(30,'zhengzihui_app','tb_artificial_representations'),(39,'zhengzihui_app','tb_companyuser'),(40,'zhengzihui_app','tb_customcompany'),(34,'zhengzihui_app','tb_goods'),(36,'zhengzihui_app','tb_goods_class'),(35,'zhengzihui_app','tb_goods_click'),(37,'zhengzihui_app','tb_goods_evaluation'),(41,'zhengzihui_app','tb_goods_wfc'),(19,'zhengzihui_app','tb_item'),(25,'zhengzihui_app','tb_item_class'),(20,'zhengzihui_app','tb_item_click'),(21,'zhengzihui_app','tb_item_pa'),(31,'zhengzihui_app','tb_message'),(32,'zhengzihui_app','tb_messagetext'),(14,'zhengzihui_app','tb_news'),(13,'zhengzihui_app','tb_news_class'),(15,'zhengzihui_app','tb_notice'),(16,'zhengzihui_app','tb_notice_class'),(38,'zhengzihui_app','tb_order'),(28,'zhengzihui_app','tb_pic'),(12,'zhengzihui_app','tb_service_provider'),(23,'zhengzihui_app','tb_shoucang_goods'),(22,'zhengzihui_app','tb_shoucang_item'),(33,'zhengzihui_app','tb_sysmessage'),(11,'zhengzihui_app','tb_user'),(10,'zhengzihui_app','tb_user_expand');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-07-27 07:15:40'),(2,'auth','0001_initial','2016-07-27 07:15:40'),(3,'admin','0001_initial','2016-07-27 07:15:41'),(4,'contenttypes','0002_remove_content_type_name','2016-07-27 07:15:41'),(5,'auth','0002_alter_permission_name_max_length','2016-07-27 07:15:41'),(6,'auth','0003_alter_user_email_max_length','2016-07-27 07:15:41'),(7,'auth','0004_alter_user_username_opts','2016-07-27 07:15:41'),(8,'auth','0005_alter_user_last_login_null','2016-07-27 07:15:41'),(9,'auth','0006_require_contenttypes_0002','2016-07-27 07:15:41'),(10,'easy_thumbnails','0001_initial','2016-07-27 07:15:41'),(11,'easy_thumbnails','0002_thumbnaildimensions','2016-07-27 07:15:41'),(12,'sessions','0001_initial','2016-07-27 07:15:41'),(13,'zhengzihui_app','0001_initial','2016-07-27 07:15:42'),(14,'zhengzihui_app','0002_auto_20160901_0132','2016-09-01 01:33:10'),(15,'zhengzihui_app','0003_auto_20160901_0136','2016-09-01 01:36:07'),(16,'zhengzihui_app','0004_auto_20160901_0933','2016-09-01 09:35:07'),(17,'zhengzihui_app','0005_auto_20160901_0933','2016-09-01 09:35:07'),(18,'zhengzihui_app','0006_tb_goods_goods_fanli','2016-09-01 09:35:08'),(19,'zhengzihui_app','0007_auto_20160901_0950','2016-09-01 09:50:26'),(20,'zhengzihui_app','0008_auto_20160901_1129','2016-09-01 11:29:54'),(21,'zhengzihui_app','0009_auto_20160901_1131','2016-09-01 11:31:05'),(22,'zhengzihui_app','0010_auto_20160901_1141','2016-09-01 11:41:56'),(23,'zhengzihui_app','0011_auto_20160901_1144','2016-09-01 11:44:54'),(24,'admin','0002_logentry_remove_auto_add','2016-09-02 05:03:39'),(25,'auth','0007_alter_validators_add_error_messages','2016-09-02 05:03:40'),(26,'zhengzihui_app','0002_tb_order_has_pay','2016-09-02 05:59:51'),(27,'zhengzihui_app','0003_tb_order_finish_percentage','2016-09-02 08:08:40');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4f5mpio9ula0pskfpo7emo11w7uor5i6','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-08 02:34:08'),('4wmm56o2l1o07zqc77tokrcv1u36kh4h','YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-09-05 08:43:26'),('7meh46fget24szd6zl1y0x2ewcfacgr9','ODIwZWEwMjg3NWFmODVlZmVlNTdmODlhNDk1NTVmZDI3NWE1NTBhMTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJmb3Jfc29ydF9pdGVtaWQiOjEsInpodWFuZ3RhaSI6Ilx1NTE2OFx1OTBlOCJ9','2016-08-08 02:32:09'),('7qganljyjdteufpclr2zgya0lweb31dr','NDRiOWVjMmJjZTUwYTYyYjIxNWUyOTk1NGVjYjFjMzRlYjZlODJjNzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImppYmllIjoiXHU1MTY4XHU5MGU4IiwiZm9yX3NvcnRfaXRlbWlkIjoxLCJfYXV0aF91c2VyX2hhc2giOiIwMGVjMmNjMmNlOTIzMWNmOTM0YTk1NmJmMDUzNTU3NTcyYjI5ZDgxIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4In0=','2016-08-02 13:47:25'),('7wtcpe5m2w9gocwire5pfn16baqg191g','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-08 02:36:12'),('8mqzg7nc4l4qbws0a0z7nn02ou3879ny','MmMyYWRiMmY0MTgxYzRjMTZlNTM5ZWM2ZTU5ZDgxOTk5ZjU5ZGE3ODp7ImZvcl9zb3J0X2l0ZW1pZCI6MX0=','2016-09-15 11:09:32'),('9dp6w2jpzdshzbwazoipe3bfvnxohly2','MmMyYWRiMmY0MTgxYzRjMTZlNTM5ZWM2ZTU5ZDgxOTk5ZjU5ZGE3ODp7ImZvcl9zb3J0X2l0ZW1pZCI6MX0=','2016-09-14 02:03:29'),('9rooe4o0xd1zgrvg2gcx7w2i4cz31zj0','ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-10 07:54:27'),('ayfwmhi2pyb2amamddqfx0hzrfe5iu2x','ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==','2016-09-12 01:50:29'),('fb32vczafm3s4un0vm6tt7hgrk41rdfw','ZWViNTEyZGQ5MzFlMjc4YTI3ZjIyZjg4MGI0M2MzYTc5NTFhYWRhNTp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==','2016-09-14 01:51:07'),('g74t7umm0bkaxfi5i4jawotb2946jwbd','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-09-13 10:53:09'),('gd580dkz0eyrrr11wafgqjbsyftxgmbg','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-10 07:36:30'),('jyh3e3h927q7oog3vywep3l99g2zwnl7','MzIyZTE2NjhmMTNmNGM4Njk2MTdjMmZlZWQ0OThiYmI1Yjk2NWQ5Mzp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiZm9yX3NvcnRfaXRlbWlkIjoxLCJqaWJpZSI6Ilx1NTE2OFx1OTBlOCJ9','2016-08-08 09:09:32'),('l9nn59s7a5ap3mzjjhvru9bmkdnz2zww','ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-05 02:44:08'),('qy5mld7xggy4og300tz0xrr1soi20f1d','ZGUzYWVlNjg0NjhkMGFhYmY1YmNjZTFjY2ZjNDFjMDVmMjZhMzQ1OTp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgiLCJ6aHVhbmd0YWkiOiJcdTUxNjhcdTkwZTgifQ==','2016-09-12 01:51:11'),('rx2skr0pks0psj8zcg2n95gmgj3l9t1n','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-10 07:35:13'),('t55odyzfjrf4oewehidfei9l3idpcxbq','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-10 07:21:35'),('v8x6esqk69i3vzixb23qh9pl1pz9iep0','ZGQ0MDU5NjZkY2ZiYWU3ZjcwYzFhMGRjNzU4Mzg5MjE3ZmZlMzVhZDp7ImJ1bWVuIjoiXHU1MTY4XHU5MGU4Iiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-08-10 08:08:11'),('wx2peycobkerdqro2ir6nwdag0hlrr27','YjY2Yjk2NDkyZDRiNzYwMWJjYmI0YmU3Y2ZlNWIwYjBmMjZjZmNjNzp7ImJ1bWVuIjoiXHU4ZDIyXHU2NTNmIiwiemh1YW5ndGFpIjoiXHU1MTY4XHU5MGU4IiwiamliaWUiOiJcdTUxNjhcdTkwZTgifQ==','2016-09-13 11:44:16');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_source`
--

DROP TABLE IF EXISTS `easy_thumbnails_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_storage_hash_40116450c1e4f2ed_uniq` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_source_b068931c` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_source`
--

LOCK TABLES `easy_thumbnails_source` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_source` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

DROP TABLE IF EXISTS `easy_thumbnails_thumbnail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_thumbnail` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_thumbnail`
--

LOCK TABLES `easy_thumbnails_thumbnail` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_thumbnaildimensions`
--

DROP TABLE IF EXISTS `easy_thumbnails_thumbnaildimensions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_thumbnaildimensions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thumbnail_id` int(11) NOT NULL,
  `width` int(10) unsigned DEFAULT NULL,
  `height` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thumbnail_id` (`thumbnail_id`),
  CONSTRAINT `ea_thumbnail_id_29ad34faceb3c17c_fk_easy_thumbnails_thumbnail_id` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_thumbnaildimensions`
--

LOCK TABLES `easy_thumbnails_thumbnaildimensions` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` DISABLE KEYS */;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnaildimensions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_accessory`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_accessory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_accessory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anne_id` int(11) NOT NULL,
  `comm_id` int(11) NOT NULL,
  `apubdate` int(11) NOT NULL,
  `apublisher` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `aposition` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `aaddtion` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_accessory`
--

LOCK TABLES `zhengzihui_app_tb_accessory` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_accessory` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_accessory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_album`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_album` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_album`
--

LOCK TABLES `zhengzihui_app_tb_album` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_album` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_album` VALUES (1,'1',0,1,'1',1,'2016-05-01 04:38:30',1),(2,'2',0,2,'2',2,'2016-05-01 04:38:39',1),(3,'3',0,3,'3',3,'2016-05-01 04:38:50',1),(4,'4',0,4,'4',4,'2016-05-01 04:38:58',1),(5,'5',0,5,'5',5,'2016-05-01 04:39:06',1),(6,'6',0,6,'6',6,'2016-05-04 09:34:52',1),(7,'7',0,7,'7',7,'2016-05-04 09:35:00',1),(8,'8',0,8,'8',8,'2016-05-04 09:35:08',1),(9,'9',0,9,'9',9,'2016-05-04 09:35:14',1),(10,'10',0,10,'10',10,'2016-05-04 09:35:32',1),(11,'11',0,11,'11',11,'2016-05-04 09:35:56',1),(12,'12',0,12,'12',12,'2016-05-04 09:36:08',1),(13,'13',0,13,'13',13,'2016-05-04 09:36:23',1),(14,'14',0,14,'14',14,'2016-05-04 09:36:38',1),(15,'15',0,15,'15',15,'2016-05-04 09:36:58',1),(16,'16',0,16,'16',16,'2016-05-04 09:37:08',1),(17,'17',0,17,'17',17,'2016-05-04 09:37:19',1),(18,'18',0,18,'18',18,'2016-05-04 09:37:34',1);
/*!40000 ALTER TABLE `zhengzihui_app_tb_album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_apage`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_apage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_apage` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_apage`
--

LOCK TABLES `zhengzihui_app_tb_apage` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_apage_class`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_apage_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_apage_class` (
  `Apcl_id` int(11) NOT NULL,
  `Apcl_code` int(11) NOT NULL,
  `Apcl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Apcl_parent_id` int(11) NOT NULL,
  `Apcl_sort` int(11) NOT NULL,
  PRIMARY KEY (`Apcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_apage_class`
--

LOCK TABLES `zhengzihui_app_tb_apage_class` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_apage_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_area`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_area` (
  `area_id` int(11) NOT NULL,
  `area_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `area_parent_id` int(11) NOT NULL,
  `area_sort` int(11) NOT NULL,
  `area_deep` int(11) NOT NULL,
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_area`
--

LOCK TABLES `zhengzihui_app_tb_area` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_article`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_article` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_article`
--

LOCK TABLES `zhengzihui_app_tb_article` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_article` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_article` VALUES (1,1,'2016科技厅关于科技计划项目的申报通知	','1','1@qq.com',0,1,'     近日，四川省教育考试院来函批复，同意西华大学今年将22个本科专业调整到本科一批次录取。加上去年纳入本科一批次招生的21个专业，2016年西华大学共有43个专业纳入本科一批次在川招生，预计该校普通本科一本批次招生计划将占普通本科总计划数的60%。','1','1',1,'2016-05-07 11:18:51',1,1),(2,2,'项目负责人、申报单位登录“四川省科技计划项目管理中心”','项目负责人、申报单位登录“四川省科技计划项目管理中心”','1111@sina.com',0,2,'金正恩在讲话中高度肯定了朝鲜在今年1月份的核试验和2月份的火箭发射所取得的“前所未有”的伟大成就。\r\n　　朝鲜劳动党第七次全国代表大会6日在平壤开幕，朝中社当天曾发布一万多字的长篇报道称“开发小型核弹头是送给劳动党七大的礼物”。\r\n　　报道称，开发小型核弹头、弹道火箭重返大气层环境模拟试验取得成功、进行高功率固体火箭发动机地上点火及级间分离试验、进行新型洲际弹道火箭大功率发动机地上点火试验是朝鲜国防科技人员向劳动党七大献礼。\r\n　　此前，金正恩的西装照片几乎只出现在朝鲜对外公布的领导人官方照片中。\r\n　　韩国电视台对朝鲜电视台金正恩的讲话做了报道评论。韩国分析人士认为，朝鲜劳动党七大日程表一开始就未包含进行第五次核试验。而朝鲜是否举行第五次核试验，这也是韩国方面此前最担心的事情。','111111111111111111111111111','1',1,'2016-05-07 11:20:34',1,1),(3,3,'3','3','1111@sina.com',0,3,'从去年开始，川内不少老牌二本院校就将大批二本专业调整至一本招生，今年这一趋势仍在继续，再加上去年四川合并二、三本批次，各个批次的界限越来越模糊，这背后将会给考生们带来什么样的影响？考生们在志愿填报上应有哪些应对之策？记者采访了相关专家。','3','3',3,'2016-05-07 11:19:51',1,3);
/*!40000 ALTER TABLE `zhengzihui_app_tb_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_artificial_representations`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_artificial_representations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_artificial_representations` (
  `arre_id` int(11) NOT NULL AUTO_INCREMENT,
  `arre_title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `arre_content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `arre_state` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`arre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_artificial_representations`
--

LOCK TABLES `zhengzihui_app_tb_artificial_representations` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_artificial_representations` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_artificial_representations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_companyuser`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_companyuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_companyuser` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_companyuser`
--

LOCK TABLES `zhengzihui_app_tb_companyuser` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_companyuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_companyuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_customcompany`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_customcompany`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_customcompany` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_customcompany`
--

LOCK TABLES `zhengzihui_app_tb_customcompany` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_customcompany` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_customcompany` VALUES ('2016','建筑业','监管汇：人民银行／银监／质监／保监／证监／药监／安监／统计／更多','中央','风险投资','银行','创业板','niaho ','nihao ','','','水产'),('9','采矿业','政府机关／直属事业单位','市级','天使投资','全部','全部','','','','','水产');
/*!40000 ALTER TABLE `zhengzihui_app_tb_customcompany` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_goods`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_goods` (
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
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_goods`
--

LOCK TABLES `zhengzihui_app_tb_goods` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods` VALUES (1,1,1,' 2016科技厅关于科技计划项目的申报通知',100000,3,10000,10000,'2016-07-19 17:20:16','2016-09-19 17:20:14',300,1,1,'1',1,0,1,1,0,0,'a','a','a','','','100',0),(2,3,1,' 2016科技厅关于科技计划项目的申报通知',18888,2,1000,1000,'2016-07-19 17:20:10','2016-09-19 17:20:09',900,1,1,'1',2,0,4,1,0,0,NULL,NULL,NULL,NULL,NULL,'100',NULL),(3,1,1,' 2016科技厅关于科技计划项目的申报通知',56781,1,100,100,'2016-06-19 17:19:57','2016-09-19 17:19:55',1000,3,1,'1',3,0,5,1,0,0,NULL,NULL,NULL,NULL,NULL,'100',NULL);
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_goods_class`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_goods_class` (
  `gocl_id` int(11) NOT NULL,
  `gocl_code` int(11) NOT NULL,
  `gocl_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `gocl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gocl_sort` int(11) NOT NULL,
  `gocl_parent_id` int(11) NOT NULL,
  PRIMARY KEY (`gocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_goods_class`
--

LOCK TABLES `zhengzihui_app_tb_goods_class` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_goods_click`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_click`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_goods_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `goods_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gocl_id` int(11) NOT NULL,
  `gocl_num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_goods_click`
--

LOCK TABLES `zhengzihui_app_tb_goods_click` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_click` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods_click` VALUES (1,1,' 2016科技厅关于科技计划项目的申报通知',0,1);
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_click` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_goods_evaluation`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_evaluation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_goods_evaluation` (
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
  PRIMARY KEY (`goev_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_goods_evaluation`
--

LOCK TABLES `zhengzihui_app_tb_goods_evaluation` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_evaluation` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_evaluation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_goods_wfc`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_goods_wfc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_goods_wfc` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_goods_wfc`
--

LOCK TABLES `zhengzihui_app_tb_goods_wfc` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_wfc` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_goods_wfc` VALUES (1,'hahaha',1,9,'asdasd','asdasd','sdadss','10%','中期经费',100,100,NULL,''),(2,'hahaha',1,9,'wqw ','wq ','sdasd','10%','启动经费中期经费成功赏金',3333,100000,2222,''),(3,'hahaha',1,9,'asss','asss','a','10%','启动经费中期经费成功赏金',1233,1000220,0,''),(4,'woqu',1,9,'asd','sc','e','10%','启动经费中期经费成功赏金',333,111,222,''),(5,'是水水水',1,9,'啊啊啊','啊啊啊','啊啊','10%','启动经费中期经费成功赏金',1,10000,1,''),(6,'111sadas',1,9,'','','','10%','启动经费',0,1111,0,''),(7,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','启动经费',0,10000,0,''),(8,'aaa',1,9,'','','','10%','启动经费',0,123,0,''),(9,' ',1,9,'a','a','a','10%','',0,10000,0,''),(10,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(11,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(12,'',1,9,'a','a','a','10%','',0,10000,0,''),(13,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','启动经费',0,10000,0,''),(14,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(15,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(16,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(17,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(18,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(19,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(20,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(21,'',1,9,'a','a','a','10%','',0,10000,0,''),(22,'',1,9,'None','None','None','10%','',0,1000,0,''),(23,'',1,9,'a','a','a','10%','',0,10000,0,''),(24,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(25,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(26,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(27,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(28,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(29,'',1,9,'a','a','a','10%','',0,10000,0,''),(30,' 2016科技厅关于科技计划项目的申报通知',1,9,'None','None','None','10%','',0,1000,0,''),(31,' 2016科技厅关于科技计划项目的申报通知',1,9,'None','None','None','10%','',0,100,0,''),(32,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(33,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(34,' 2016科技厅关于科技计划项目的申报通知',1,9,'None','None','None','10%','',0,1000,0,''),(35,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(36,'',1,9,'a','a','a','10%','',0,10000,0,''),(37,'',1,9,'a','a','a','10%','',0,10000,0,''),(38,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(39,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(40,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(41,' 2016科技厅关于科技计划项目的申报通知',1,9,'None','None','None','10%','',0,1000,0,''),(42,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(43,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(44,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,''),(45,' 2016科技厅关于科技计划项目的申报通知',1,9,'a','a','a','10%','',0,10000,0,'按时完成  保证修改  提供原版  后续服务  提供加急  ');
/*!40000 ALTER TABLE `zhengzihui_app_tb_goods_wfc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_item`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_item` (
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
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_item`
--

LOCK TABLES `zhengzihui_app_tb_item` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item` VALUES (1,'1','四川省科技厅计划项目招标通知2016之特别假话找白哦',1,1,'1',1,'2016-04-03 04:35:19','2016-10-01 00:00:00','养殖/科技/互联网','1','科技项目',0,0,0,1),(2,'2','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',2,4,'2',2,'2016-05-01 04:35:42','2016-06-18 04:35:43','农林/住建/其他','2','互联网项目',0,0,0,1),(3,'3','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',3,3,'3',3,'2016-05-01 04:36:23','2016-07-15 04:36:24','农业/养殖/互联网+','3','科技项目',0,0,0,1),(4,'4','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',4,3,'4',4,'2016-05-01 04:36:47','2016-05-28 04:36:48','水产/养殖/其他','4','科技项目',0,0,0,0),(5,'5','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',5,2,'5',5,'2016-05-01 04:37:05','2016-07-08 04:37:07','水产/政务/管理/新产业','5','中央项目',0,0,0,0),(6,'6','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',6,2,'5万-500万',1,'2016-03-08 09:42:34','2016-09-01 09:42:39','农业/养殖/互联网+','6','水产/政务/管理/新产业',0,0,1,1),(7,'7','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',7,1,'5万-500万',2,'2016-03-23 09:44:34','2016-06-11 09:44:38','水产/政务/管理/新产业','7','科技项目',0,0,0,1),(8,'8','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',8,1,'5万-500万',3,'2015-12-03 09:45:32','2016-06-30 09:45:40','农林/住建/其他','8','互联网项目',0,0,0,1),(9,'9','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',9,3,'5万-500万',4,'2016-04-13 09:46:22','2016-06-17 09:46:26','农业/养殖/互联网+','9','中央项目',0,0,0,1),(10,'10','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',10,4,'5万-500万',5,'2016-05-01 09:47:25','2016-05-31 09:47:28','水产/政务/管理/新产业','10','科技项目',0,0,0,0),(11,'11','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',11,4,'5万-500万',1,'2016-04-03 09:48:13','2016-05-04 09:48:23','养殖/科技/互联网','11','互联网项目',0,0,0,1),(12,'12','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',12,1,'5万-500万',2,'2016-04-07 09:49:12','2016-05-04 09:49:15','养殖/科技/互联网','12','中央项目',0,0,0,0),(13,'13','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',13,2,'5万-500万',3,'2016-04-10 09:50:24','2016-05-28 09:50:30','水产/政务/管理/新产业','13','科技项目',0,0,0,1),(14,'14','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',14,1,'5万-500万',4,'2016-04-01 09:53:00','2016-06-09 09:53:03','水产/政务/管理/新产业','14','科技项目',0,0,0,1),(15,'15','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',15,1,'5万-500万',5,'2016-04-05 09:54:09','2016-05-04 09:54:12','养殖/科技/互联网','15','互联网项目',0,0,0,0),(16,'16','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',16,1,'5万-500万',1,'2016-04-03 09:55:05','2016-06-24 09:55:08','农林/住建/其他','16','中央项目',0,0,0,0),(17,'17','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',17,1,'5万-500万',2,'2016-04-20 09:56:04','2016-07-08 09:56:08','水产/政务/管理/新产业 ','17','科技项目',0,0,0,0),(18,'18','四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',18,1,'5万-500万',3,'2016-03-31 09:56:50','2016-05-26 09:56:53','农业/养殖/互联网+','18','互联网项目',0,0,0,0);
/*!40000 ALTER TABLE `zhengzihui_app_tb_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_item_class`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_item_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_item_class` (
  `itcl_id` int(11) NOT NULL,
  `itcl_code` int(11) NOT NULL,
  `itcl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `itcl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`itcl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_item_class`
--

LOCK TABLES `zhengzihui_app_tb_item_class` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_item_click`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_item_click`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_item_click` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itcl_id` int(11) NOT NULL,
  `click_counter` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `zheng_item_id_29097a73715f199e_fk_zhengzihui_app_tb_item_item_id` (`item_id`),
  CONSTRAINT `zheng_item_id_29097a73715f199e_fk_zhengzihui_app_tb_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `zhengzihui_app_tb_item` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_item_click`
--

LOCK TABLES `zhengzihui_app_tb_item_click` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_click` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item_click` VALUES (2,0,12,1),(3,0,19,2),(4,0,1,3),(5,0,5,4),(6,0,4,5),(7,0,2,6),(8,0,1,7),(9,0,0,8),(10,0,0,9),(11,0,2,10),(12,0,0,11),(13,0,0,12),(14,0,0,13),(15,0,0,14),(16,0,0,15),(17,0,0,16),(18,0,0,17),(19,0,0,18);
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_click` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_item_pa`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_item_pa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_item_pa` (
  `ipa_id` int(11) NOT NULL,
  `ipa_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ipa_parent_id` int(11) NOT NULL,
  `ipa_sort` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  `ipa_address` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`ipa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_item_pa`
--

LOCK TABLES `zhengzihui_app_tb_item_pa` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_pa` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_item_pa` VALUES (1,'四川省科技厅',1,1,1,'成都市天府广场'),(2,'四川农业局',2,2,2,'成都市天府广场'),(3,'中央财政厅',3,3,3,'成都市天府广场'),(4,'湖北教育局',4,4,4,'成都市天府广场'),(5,'中央农业局',5,5,5,'成都市天府广场');
/*!40000 ALTER TABLE `zhengzihui_app_tb_item_pa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_message`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_message` (
  `mess_id` int(11) NOT NULL,
  `send_id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL,
  `text_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`mess_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_message`
--

LOCK TABLES `zhengzihui_app_tb_message` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_messagetext`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_messagetext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_messagetext` (
  `text_id` int(11) NOT NULL,
  `mete_title` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `mete_content` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `mete_time` datetime NOT NULL,
  PRIMARY KEY (`text_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_messagetext`
--

LOCK TABLES `zhengzihui_app_tb_messagetext` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_messagetext` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_messagetext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_news`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_news` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_news`
--

LOCK TABLES `zhengzihui_app_tb_news` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_news_class`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_news_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_news_class` (
  `necl_id` int(11) NOT NULL AUTO_INCREMENT,
  `necl_code` int(11) NOT NULL,
  `necl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `necl_parent_id` int(11) NOT NULL,
  `necl_sort` int(11) NOT NULL,
  PRIMARY KEY (`necl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_news_class`
--

LOCK TABLES `zhengzihui_app_tb_news_class` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_news_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_notice`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_notice` (
  `Notice_id` int(11) NOT NULL AUTO_INCREMENT,
  `Notice_title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Article_id` int(11) NOT NULL,
  `Notice_time` date NOT NULL,
  `Notice_source` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Nocl_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  `Notice_is_display` int(11) NOT NULL,
  `Notice_top` int(11) NOT NULL,
  PRIMARY KEY (`Notice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_notice`
--

LOCK TABLES `zhengzihui_app_tb_notice` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_notice_class`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_notice_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_notice_class` (
  `Nocl_id` int(11) NOT NULL,
  `Nocl_code` int(11) NOT NULL,
  `Nocl_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Nocl_des` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Nocl_parent_id` int(11) NOT NULL,
  `Notice_sort` int(11) NOT NULL,
  PRIMARY KEY (`Nocl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_notice_class`
--

LOCK TABLES `zhengzihui_app_tb_notice_class` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_notice_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_order`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_order` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_order`
--

LOCK TABLES `zhengzihui_app_tb_order` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_order` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_order` VALUES (2,105597,3,105597,1,'四川省科技厅计划项目招标通知2016之特别假话找白哦',1,'',9,'orchard','changyifan123@qq.com','2016-03-02 07:15:16','105597',NULL,NULL,100,200,100,NULL,1,1,'1',0,3,0,0,0,'2016-09-07 07:15:16',0,1,0,90),(10,159020,2,159020,3,'四川省科技厅计划项目招标通知201顶顶顶顶顶顶顶顶6之特别假话找白哦',1,'',9,'orchard','changyifan123@qq.com','2016-09-02 07:02:45','159020',NULL,NULL,1000,2000,1000,NULL,1,1,'1',0,3,0,0,0,'2016-09-30 07:02:45',0,1,1,60),(11,3551,1,3551,1,'四川省科技厅计划项目招标通知2016之特别假话找白哦',1,'',9,'orchard','changyifan123@qq.com','2016-09-01 07:02:52','3551',NULL,NULL,10000,20000,10000,NULL,1,1,'1',0,3,0,0,0,'2016-09-02 07:02:52',0,0,2,91);
/*!40000 ALTER TABLE `zhengzihui_app_tb_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_pic`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_pic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_pic` (
  `pic_id` int(11) NOT NULL,
  `pic_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `pic_tag` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `album_id` int(11) NOT NULL,
  `pic_object` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pic_size` int(11) NOT NULL,
  `upload_time` datetime NOT NULL,
  PRIMARY KEY (`pic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_pic`
--

LOCK TABLES `zhengzihui_app_tb_pic` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_pic` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_pic` VALUES (1,'1','1',1,'img_for_items/2016/05/01/6aa33f80-a3c0-11e5-a70d-dc85def86878.png',0,'2016-05-06 13:50:06'),(2,'2','2',2,'img_for_items/2016/05/01/4adbe14f-a557-11e5-bd34-dc85def86878.png',0,'2016-05-01 04:39:55'),(3,'3','3',3,'img_for_items/2016/05/01/9a77684f-a558-11e5-91f7-dc85def86878.png',0,'2016-05-01 04:40:07'),(4,'4','4',4,'img_for_items/2016/05/01/34fd605a-a658-11e5-8df7-00163e0022d3.png',0,'2016-05-01 04:40:19'),(5,'5','5',5,'img_for_items/2016/05/01/39a46b8f-a558-11e5-949b-dc85def86878.png',0,'2016-05-01 04:40:33'),(6,'6','6',6,'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878.png',0,'2016-05-04 09:30:26'),(7,'7','7',7,'img_for_items/2016/05/04/6a12a4de-a558-11e5-b72c-dc85def86878.png',0,'2016-05-04 09:30:41'),(8,'8','8',8,'img_for_items/2016/05/04/34fd605a-a658-11e5-8df7-00163e0022d3.png',0,'2016-05-04 09:30:53'),(9,'9','9',9,'img_for_items/2016/05/04/6bd92fc0-a476-11e5-aaa1-dc85def86878.png',0,'2016-05-04 09:31:05'),(10,'10','10',10,'img_for_items/2016/05/04/76c0c68f-a265-11e5-80d4-3859f9fa9803.png',0,'2016-05-04 09:31:25'),(11,'11','11',11,'img_for_items/2016/05/04/56de86b0-a557-11e5-92af-dc85def86878.png',0,'2016-05-04 09:32:58'),(12,'12','12',12,'img_for_items/2016/05/04/2f9f86de-a277-11e5-a84a-3859f9fa9803.png',0,'2016-05-04 09:33:09'),(13,'13','13',13,'img_for_items/2016/05/04/9fdac0b0-a3c0-11e5-8a73-dc85def86878.png',0,'2016-05-04 09:33:22'),(14,'14','14',14,'img_for_items/2016/05/04/98c5db1e-a3c0-11e5-b491-dc85def86878.png',0,'2016-05-04 09:33:34'),(15,'15','15',15,'img_for_items/2016/05/04/2df0ed11-a557-11e5-8e43-dc85def86878.png',0,'2016-05-04 09:33:51'),(16,'16','16',16,'img_for_items/2016/05/04/17675c61-a263-11e5-a423-3859f9fa9803.png',0,'2016-05-04 09:34:08'),(17,'17','17',17,'img_for_items/2016/05/04/5be48e0f-a265-11e5-89c3-3859f9fa9803.png',0,'2016-05-04 10:46:02'),(18,'18','18',18,'img_for_items/2016/05/04/7c0867cf-a476-11e5-9797-dc85def86878_v0SFX5j.png',0,'2016-05-04 09:34:23'),(19,'19','19',1,'img_for_items/2016/05/06/a7.jpg',0,'2016-05-06 13:54:33'),(20,'20','20',1,'img_for_items/2016/05/06/a5.jpg',0,'2016-05-06 13:51:08'),(21,'21','21',1,'img_for_items/2016/05/06/a4.jpg',0,'2016-05-06 13:51:23'),(22,'22','22',1,'img_for_items/2016/05/06/a2.jpg',0,'2016-05-06 13:51:33');
/*!40000 ALTER TABLE `zhengzihui_app_tb_pic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_service_provider`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_service_provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_service_provider` (
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
  PRIMARY KEY (`sp_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_service_provider`
--

LOCK TABLES `zhengzihui_app_tb_service_provider` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_service_provider` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_service_provider` VALUES (1,1,'rongyida','123456','12312','12@1213','1','24','2232',1,21,'100',339999,12,1231,'rongyida',2,112321312,'3422skdfjkd',1,1);
/*!40000 ALTER TABLE `zhengzihui_app_tb_service_provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_shoucang_goods`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_shoucang_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_shoucang_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_shoucang_goods`
--

LOCK TABLES `zhengzihui_app_tb_shoucang_goods` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_shoucang_item`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_shoucang_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_shoucang_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_shoucang_item`
--

LOCK TABLES `zhengzihui_app_tb_shoucang_item` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_shoucang_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_sysmessage`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_sysmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_sysmessage` (
  `sys_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `mess_id` int(11) NOT NULL,
  `sys_status` int(11) NOT NULL,
  PRIMARY KEY (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_sysmessage`
--

LOCK TABLES `zhengzihui_app_tb_sysmessage` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_sysmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhengzihui_app_tb_sysmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_user`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_telephone` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `user_email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `user_auth` int(11) NOT NULL,
  `user_type` int(11) NOT NULL,
  `expand_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `zhengzihui_app_tb_user_5099c045` (`expand_id`),
  CONSTRAINT `D488b378309e1fcb47188b2b261691cb` FOREIGN KEY (`expand_id`) REFERENCES `zhengzihui_app_tb_user_expand` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2017 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_user`
--

LOCK TABLES `zhengzihui_app_tb_user` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_user` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_user` VALUES (9,'orchard','123456','13688118677','changyifan123@qq.com',1,1,9),(2016,'testxcz','123456','2234234234','21312@123',1,1,9);
/*!40000 ALTER TABLE `zhengzihui_app_tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhengzihui_app_tb_user_expand`
--

DROP TABLE IF EXISTS `zhengzihui_app_tb_user_expand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhengzihui_app_tb_user_expand` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhengzihui_app_tb_user_expand`
--

LOCK TABLES `zhengzihui_app_tb_user_expand` WRITE;
/*!40000 ALTER TABLE `zhengzihui_app_tb_user_expand` DISABLE KEYS */;
INSERT INTO `zhengzihui_app_tb_user_expand` VALUES (9,'13688118677','changyifan123@qq.com','uestc','四川','成都',2,'金融','50-99','国营','常益凡','123455');
/*!40000 ALTER TABLE `zhengzihui_app_tb_user_expand` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-02 16:15:50
