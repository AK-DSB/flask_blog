-- MySQL dump 10.13  Distrib 5.7.30, for Win64 (x86_64)
--
-- Host: localhost    Database: flask_blog
-- ------------------------------------------------------
-- Server version	5.7.30-log

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
-- Table structure for table `about_me`
--

DROP TABLE IF EXISTS `about_me`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `about_me` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` blob NOT NULL,
  `pdatetime` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `about_me_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about_me`
--

LOCK TABLES `about_me` WRITE;
/*!40000 ALTER TABLE `about_me` DISABLE KEYS */;
INSERT INTO `about_me` VALUES (1,_binary '<h3>基本信息:</h3>\r\n<h3>姓名:AK</h3>\r\n<h3>性别:男</h3>\r\n<h3>职业:职业选手</h3>\r\n<h2><strong>爱好:敲代码，运动，打游戏</strong></h2>\r\n<p><strong>自我介绍:熟悉python，Java，C语言等多门语言的hello world的程序编写</strong></p>\r\n<p><strong>联系方式:18573778821</strong></p>\r\n<p><strong>微信:w2497744746</strong></p>\r\n<p><strong>QQ:2497744746</strong></p>\r\n<p>&nbsp;</p>\r\n<h3>&nbsp;</h3>','2021-01-14 16:13:49',4),(8,_binary '<h3>基本信息</h3>\r\n<h3>姓名:AK-DSB</h3>\r\n<p>&nbsp;</p>','2021-01-14 19:17:29',1);
/*!40000 ALTER TABLE `about_me` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('7b31933bfd98');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` blob NOT NULL,
  `publish_date` datetime DEFAULT NULL,
  `click_num` int(11) DEFAULT NULL,
  `save_num` int(11) DEFAULT NULL,
  `love_num` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `article_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `article_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'东斌的健身梦',_binary '非堵塞九分裤水电费返回环境返回几号法国红酒合法','2020-12-19 21:34:08',0,0,0,2,1),(2,'东斌的健身梦',_binary '脚后跟圣诞节黄金分割李开复和积分换积分是经历过空集合金发科技老客户可好看','2020-12-19 21:35:47',0,0,0,1,1),(3,'太白的诱惑',_binary '福建师大焚枯食淡符合恢复施工发广告和豆腐干对方的 个东方古柯个 给对方鬼地方个打个卡结果看科技馆个个刚开个看看','2020-12-20 10:25:52',0,0,0,3,2),(4,'得港的内心独白',_binary '房间看到萨福克斯的回复华发商都华发商都何妨吮短毫水电费回复粉红色的的双方各红烧冬瓜就何妨吮短毫发光时代氨基酸的股份结束递归见多识广发光时代坚实的刚十多个手打个','2020-12-20 10:26:26',0,0,0,3,3),(5,'金瓶梅',_binary '分解了打发时间是打分的省份发动机更好的房价快速更好合格咖啡店空格看刚开框架就kg好看和可靠花港饭店好','2020-12-20 21:26:35',0,0,0,2,4),(6,'AKW_CHARATER',_binary '<p>附近的刷卡会更好款到发货浮动口诀电话费环境积分的宽和高电话费就觉得</p>','2021-01-09 21:48:55',0,0,0,1,2),(7,'社会民的KPL梦',_binary '<p>2001年的某月某日一王者社会民横空出世，震惊整个王者峡谷😇😉</p>','2021-01-09 22:10:09',0,5,5,1,3),(8,'社会人的内心独白',_binary '<p>范德萨发第三个梵蒂冈好干活高合金钢 😝😛</p>','2021-01-14 15:15:09',0,1,1,4,2),(10,'社会斌健身之旅',_binary '<p>社会斌衡阳人，不会做人乃其口头禅</p>','2021-01-15 12:13:46',0,0,0,4,4);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article_type`
--

DROP TABLE IF EXISTS `article_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article_type`
--

LOCK TABLES `article_type` WRITE;
/*!40000 ALTER TABLE `article_type` DISABLE KEYS */;
INSERT INTO `article_type` VALUES (1,'科技'),(2,'随笔'),(3,'慢生活'),(4,'程序人生');
/*!40000 ALTER TABLE `article_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  `comment_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `article_id` (`article_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'阿民666',1,7,'2021-01-14 12:07:00'),(2,'阿民牛逼',2,7,'2021-01-14 12:07:00'),(3,'社会民6666',3,7,'2021-01-14 12:09:33'),(4,'民哥带带我',1,7,'2021-01-14 14:27:11'),(5,'斌哥666',1,2,'2021-01-14 14:27:59'),(6,'阿民',4,7,'2021-01-14 14:36:32'),(7,'社会民太牛了',4,7,'2021-01-14 14:44:47'),(8,'哈哈哈',4,7,'2021-01-14 14:44:57'),(9,'666666666',4,7,'2021-01-14 14:45:05'),(10,'民哥带带我',2,7,'2021-01-14 14:45:58'),(11,'社会人6666',4,8,'2021-01-14 15:15:21');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(100) NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message_board`
--

DROP TABLE IF EXISTS `message_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message_board` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `mdatetime` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `message_board_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message_board`
--

LOCK TABLES `message_board` WRITE;
/*!40000 ALTER TABLE `message_board` DISABLE KEYS */;
INSERT INTO `message_board` VALUES (1,'写下你想说的，开始我们的对话\r\n                    ','2021-01-14 22:02:24',1),(2,'哈哈哈哈','2021-01-14 22:13:31',1),(3,'66666\r\n','2021-01-14 22:17:18',NULL),(5,'呜呜呜呜','2021-01-14 22:28:10',4),(6,'耶耶耶耶耶耶','2021-01-14 22:28:16',4),(7,'法第三方士大夫','2021-01-14 22:28:26',4);
/*!40000 ALTER TABLE `message_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_name` varchar(32) NOT NULL,
  `photo_datetime` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `photo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo`
--

LOCK TABLES `photo` WRITE;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo` VALUES (1,'3_478.jpg','2021-01-11 22:18:06',1),(2,'胖丁_978.jpg','2021-01-13 20:16:27',1),(3,'Erha_624.jpg','2021-01-13 20:17:06',1),(4,'Erha_567.jpg','2021-01-13 20:58:04',1),(5,'胖丁_724.jpg','2021-01-13 20:58:20',1),(6,'Erha_619.jpg','2021-01-13 21:58:14',1),(8,'bg_459.jpg','2021-01-13 21:58:45',1),(9,'3_682.jpg','2021-01-14 14:35:51',4),(10,'3_585.jpg','2021-01-14 15:00:18',2);
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(101) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'AK','bbb927e2274a2541c2ba9d07bddaef22','18573778821','2497744746@qq.com','upload/icon/Erha.jpg',0,NULL),(2,'AKW','bbb927e2274a2541c2ba9d07bddaef22','18670905392','2497744746@qq.com','upload/icon/jpg',0,NULL),(3,'AKM','bbb927e2274a2541c2ba9d07bddaef22','15573778821','2497744746@qq.com',NULL,0,NULL),(4,'AK-DSB','bbb927e2274a2541c2ba9d07bddaef22','18677887522','2497744746@qq.com','upload/icon/3.jpg',0,'2020-12-23 16:23:43');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_goods`
--

DROP TABLE IF EXISTS `user_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `goods_id` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_id` (`goods_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_goods_ibfk_1` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `user_goods_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_goods`
--

LOCK TABLES `user_goods` WRITE;
/*!40000 ALTER TABLE `user_goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_goods` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-16 11:29:59
