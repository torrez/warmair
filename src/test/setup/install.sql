CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `twitter_id` bigint(11) NOT NULL DEFAULT '0',
  `name` varchar(30) DEFAULT NULL,
  `screen_name` varchar(30) DEFAULT NULL,
  `description` text,
  `location` varchar(128) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `claimed` tinyint(1) NOT NULL DEFAULT '0',
  `profile_image_url` varchar(256) DEFAULT NULL,
  `time_zone` varchar(128) DEFAULT NULL,
  `access_token` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
