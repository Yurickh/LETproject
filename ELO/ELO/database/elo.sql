PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
INSERT INTO "django_content_type" VALUES(1,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(2,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(3,'professor','ELO','professor');
INSERT INTO "django_content_type" VALUES(4,'adm','ELO','adm');
INSERT INTO "django_content_type" VALUES(5,'student','ELO','student');
INSERT INTO "django_content_type" VALUES(6,'god','ELO','god');
INSERT INTO "django_content_type" VALUES(7,'module','ELO','module');
INSERT INTO "django_content_type" VALUES(8,'courses','ELO','courses');
INSERT INTO "django_content_type" VALUES(9,'lesson','ELO','lesson');
INSERT INTO "django_content_type" VALUES(10,'exercise','ELO','exercise');
INSERT INTO "django_content_type" VALUES(11,'identities','ELO','identities');
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
INSERT INTO "django_session" VALUES('3ewvot5bp7vm4om0zon1hxe1pnfebtzc','ZWRhZDI4NzAxMjUwMDkwZDY2NTczZmI4YWMxYjI0MjVhNDQzYjkxNzp7InVzZXIiOnsicGFzc3dvcmQiOiJkYWZiN2JiNjhhZjM3OWM2YzM5MWZmOWU0ZjJkMWJiZSIsInR5cGUiOiJBZG0iLCJuYW1lIjoiRGF5YW5uZSIsImxhbmd1YWdlIjoicHQtYnIifX0=','2014-10-17 18:11:23.278731');
INSERT INTO "django_session" VALUES('tzqiuiajf3agum8ffobip264rkkqndb9','MWY4ZjA0NDYwMmU0MWQxOWM1ODg3YzFiZGRkOTkyOGIwYTU4MzZjMTp7Il9sYW5ndWFnZSI6ImVuIn0=','2014-10-17 21:15:22.493487');
INSERT INTO "django_session" VALUES('qv3f743pm7yv2y40ni3cxkdtwzdj35qt','NDI1MzQxM2VkZGFiMGQzZGNiZDY4OWY4NDcyOGI3ZWRhYzJiNjhlNTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImIwZjE2NDYyNTJmNDQzNGJlM2VmNzRlN2FiNmFjMTc3IiwidHlwZSI6IkFkbSIsIm5hbWUiOiJZdXJpY2siLCJsYW5ndWFnZSI6InB0LWJyIn19','2014-10-17 21:16:15.356578');
INSERT INTO "django_session" VALUES('y9ejmdvi4lvf3egwvx6giakw3wee6f9k','ZWRhZDI4NzAxMjUwMDkwZDY2NTczZmI4YWMxYjI0MjVhNDQzYjkxNzp7InVzZXIiOnsicGFzc3dvcmQiOiJkYWZiN2JiNjhhZjM3OWM2YzM5MWZmOWU0ZjJkMWJiZSIsInR5cGUiOiJBZG0iLCJuYW1lIjoiRGF5YW5uZSIsImxhbmd1YWdlIjoicHQtYnIifX0=','2014-10-20 14:54:06.895188');
INSERT INTO "django_session" VALUES('nhcq2vey6yvqxsvx68ba9ulo9pkkknfu','ZWRhZDI4NzAxMjUwMDkwZDY2NTczZmI4YWMxYjI0MjVhNDQzYjkxNzp7InVzZXIiOnsicGFzc3dvcmQiOiJkYWZiN2JiNjhhZjM3OWM2YzM5MWZmOWU0ZjJkMWJiZSIsInR5cGUiOiJBZG0iLCJuYW1lIjoiRGF5YW5uZSIsImxhbmd1YWdlIjoicHQtYnIifX0=','2014-10-21 23:31:08.870743');
INSERT INTO "django_session" VALUES('9lc0fa8zbpd6libhoyya950336tn3jfs','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-10-23 18:31:17.510749');
INSERT INTO "django_session" VALUES('hsi55cup5c23pwa6o60nfbkzd91yixch','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-10-24 17:45:19.477189');
INSERT INTO "django_session" VALUES('3hnxbs7r1btobg53m6torpa5lin82x2m','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-10-28 19:45:38.417432');
INSERT INTO "django_session" VALUES('pi21efywgiikt76b7oxubvb58epecpg8','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-10-29 16:37:59.759592');
INSERT INTO "django_session" VALUES('qevsmpzizr2pcjgvj8qe0047rfv5ppm2','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-10-30 20:31:32.213229');
INSERT INTO "django_session" VALUES('h9cawya7gzzzy6gtbripa9y2eal2c6y1','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-10-31 17:50:52.971224');
INSERT INTO "django_session" VALUES('bkel26j213mcsp14vgz20hty5j0a1ku7','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-04 16:33:04.139698');
INSERT INTO "django_session" VALUES('hwzxzn4bukrmfke93mln46rr2g13xhdo','ODY5NmNhODZjY2RkY2NlMDIwMzYzZjI3NTQ2MTA3MTYyYTU4OTM0NTp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7InBhc3N3b3JkIjoiZGFmYjdiYjY4YWYzNzljNmMzOTFmZjllNGYyZDFiYmUiLCJ0eXBlIjoiQWRtIiwibmFtZSI6IkRheWFubmUiLCJsYW5ndWFnZSI6ImVuIn19','2014-11-05 16:18:13.273154');
INSERT INTO "django_session" VALUES('pks2yfs60yzq8l671ubna76s1rtm1kyw','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-10 17:18:42.560322');
INSERT INTO "django_session" VALUES('py78dshfbn4fpfpd5k93afq4c8jpyfb3','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-12 11:14:18.569774');
INSERT INTO "django_session" VALUES('wzceik97sfj7sroigti6vm0f0jni4zhb','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-13 16:44:38.845277');
INSERT INTO "django_session" VALUES('aj69onltsx7613b0hlwxb97lrgjvb3fh','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-18 15:15:57.153754');
INSERT INTO "django_session" VALUES('27jwu6n8i32be84bvpar8jy96rhpn9nm','ODY5NmNhODZjY2RkY2NlMDIwMzYzZjI3NTQ2MTA3MTYyYTU4OTM0NTp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7InBhc3N3b3JkIjoiZGFmYjdiYjY4YWYzNzljNmMzOTFmZjllNGYyZDFiYmUiLCJ0eXBlIjoiQWRtIiwibmFtZSI6IkRheWFubmUiLCJsYW5ndWFnZSI6ImVuIn19','2014-11-19 15:14:07.520942');
INSERT INTO "django_session" VALUES('25ph8qc8veissh7n0fcva8rqvxpuo9hq','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-24 16:46:17.253274');
INSERT INTO "django_session" VALUES('975v56uz074cb7vf0l69jgcp9gksioop','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-25 15:14:28.242360');
INSERT INTO "django_session" VALUES('18uaers2sqc7igopgf70wnas9rfgrl2i','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-11-27 16:58:14.608530');
INSERT INTO "django_session" VALUES('1mw9r4vs6uo9feigyiwy1r27n6oji0rp','MDM3Yjk0OTdlMDRiMTY3NzRhNTlmNWU3YzA5ODE3NzNlMDg2Yjc1Yjp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7ImludGVyZXN0cyI6Im9pLHNvbWV0aGluZyxvdGhlciIsIm5hbWUiOiJEYXkiLCJsYW5ndWFnZSI6ImVuIiwiY291cnNlcyI6bnVsbCwic2V4IjpudWxsLCJiaW9zIjpudWxsLCJncmFkZXMiOm51bGwsImVtYWlsIjpudWxsLCJhdmF0YXIiOm51bGwsInBhc3N3b3JkIjoiZGFmYjdiYjY4YWYzNzljNmMzOTFmZjllNGYyZDFiYmUiLCJ0eXBlIjoiU3R1ZGVudCIsImNhbXB1cyI6bnVsbCwibWF0cmljIjpudWxsfX0=','2014-12-01 16:00:48.936293');
INSERT INTO "django_session" VALUES('xxrsw2i1bb7m2ct6zc4zvifyp3sgf1s3','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-12-03 17:41:37.119090');
INSERT INTO "django_session" VALUES('hbajvnar6zfaenv9qkcu6d8g3zlx414j','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-12-09 15:59:50.660599');
INSERT INTO "django_session" VALUES('agr17m2uk5t18mywouknylu9d5lsazie','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-12-10 18:05:05.869811');
INSERT INTO "django_session" VALUES('82sbmb1fofdc6puq1xrown1zbshqzdc6','NTBiMGQ2Zjc4YTIyZGNjOTkxYmY4N2E0MTllMjgxOTA1NTY4YTdlMTp7Il9sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJwYXNzd29yZCI6ImRhZmI3YmI2OGFmMzc5YzZjMzkxZmY5ZTRmMmQxYmJlIiwidHlwZSI6IkFkbSIsIm5hbWUiOiJEYXlhbm5lIiwibGFuZ3VhZ2UiOiJwdC1iciJ9fQ==','2014-12-11 17:51:36.913330');
CREATE TABLE "ELO_student" (
    "id" integer NOT NULL PRIMARY KEY,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
INSERT INTO "ELO_student" VALUES(1,1,'PASSWORD','dafb7bb68af379c6c391ff9e4f2d1bbe');
INSERT INTO "ELO_student" VALUES(2,1,'NAME','Day');
INSERT INTO "ELO_student" VALUES(3,1,'LANGUAGE','en');
INSERT INTO "ELO_student" VALUES(46,1,'INTEREST','oi,something,other');
INSERT INTO "ELO_student" VALUES(47,2,'NAME','Dayof');
INSERT INTO "ELO_student" VALUES(48,2,'LANGUAGE','pt-br');
INSERT INTO "ELO_student" VALUES(49,2,'SEX','F');
INSERT INTO "ELO_student" VALUES(50,2,'EMAIL','dayof@gmail.com');
INSERT INTO "ELO_student" VALUES(51,2,'CAMPUS','15987532');
INSERT INTO "ELO_student" VALUES(52,2,'MATRIC','123456789');
INSERT INTO "ELO_student" VALUES(53,3,'NAME','Outrapessoa');
INSERT INTO "ELO_student" VALUES(54,3,'LANGUAGE','pt-br');
INSERT INTO "ELO_student" VALUES(55,3,'SEX','F');
INSERT INTO "ELO_student" VALUES(56,3,'EMAIL','another@hotmail.com');
INSERT INTO "ELO_student" VALUES(57,3,'CAMPUS','3543434');
INSERT INTO "ELO_student" VALUES(58,3,'MATRIC','54634');
INSERT INTO "ELO_student" VALUES(59,4,'NAME','Outrapessoa');
INSERT INTO "ELO_student" VALUES(60,4,'LANGUAGE','pt-br');
INSERT INTO "ELO_student" VALUES(61,4,'SEX','F');
INSERT INTO "ELO_student" VALUES(62,4,'EMAIL','another@hotmail.com');
INSERT INTO "ELO_student" VALUES(63,4,'CAMPUS','3543434');
INSERT INTO "ELO_student" VALUES(64,4,'MATRIC','54634');
INSERT INTO "ELO_student" VALUES(71,6,'NAME','Hikari');
INSERT INTO "ELO_student" VALUES(72,6,'LANGUAGE','pt-br');
INSERT INTO "ELO_student" VALUES(73,6,'SEX','F');
INSERT INTO "ELO_student" VALUES(74,6,'EMAIL','nope@gmail.com');
INSERT INTO "ELO_student" VALUES(75,6,'CAMPUS','363543');
INSERT INTO "ELO_student" VALUES(76,6,'MATRIC','54544');
INSERT INTO "ELO_student" VALUES(77,7,'NAME','Whatfuck');
INSERT INTO "ELO_student" VALUES(78,7,'LANGUAGE','pt-br');
INSERT INTO "ELO_student" VALUES(79,7,'SEX','M');
INSERT INTO "ELO_student" VALUES(80,7,'EMAIL','whats@nope.com');
INSERT INTO "ELO_student" VALUES(81,7,'CAMPUS','544465');
INSERT INTO "ELO_student" VALUES(82,7,'MATRIC','54546');
INSERT INTO "ELO_student" VALUES(83,8,'NAME','Whooo');
INSERT INTO "ELO_student" VALUES(84,8,'LANGUAGE','pt-br');
INSERT INTO "ELO_student" VALUES(85,8,'SEX','F');
INSERT INTO "ELO_student" VALUES(86,8,'EMAIL','whoooo@ahhh.com');
INSERT INTO "ELO_student" VALUES(87,8,'CAMPUS','35435454');
INSERT INTO "ELO_student" VALUES(88,8,'MATRIC','3135454');
CREATE TABLE "ELO_adm" (
    "id" integer NOT NULL PRIMARY KEY,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
INSERT INTO "ELO_adm" VALUES(1,1,'NAME','Dayanne');
INSERT INTO "ELO_adm" VALUES(2,1,'PASSWORD','dafb7bb68af379c6c391ff9e4f2d1bbe');
INSERT INTO "ELO_adm" VALUES(3,1,'LANGUAGE','en');
INSERT INTO "ELO_adm" VALUES(4,2,'NAME','Yurick');
INSERT INTO "ELO_adm" VALUES(5,2,'PASSWORD','b0f1646252f4434be3ef74e7ab6ac177');
CREATE TABLE "ELO_professor" (
    "id" integer NOT NULL PRIMARY KEY,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
INSERT INTO "ELO_professor" VALUES(1,1,'NAME','Dayof');
INSERT INTO "ELO_professor" VALUES(2,1,'PASSWORD','dafb7bb68af379c6c391ff9e4f2d1bbe');
INSERT INTO "ELO_professor" VALUES(3,1,'LANGUAGE','en');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2014-10-03 21:10:53.126238');
INSERT INTO "django_migrations" VALUES(2,'sessions','0001_initial','2014-10-03 21:10:53.222176');
CREATE TABLE "ELO_god" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(32) NOT NULL,
    "password" text NOT NULL
);
CREATE TABLE "ELO_courses" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
INSERT INTO "ELO_courses" VALUES(11,4,'PROFESSOR','Vidal');
INSERT INTO "ELO_courses" VALUES(12,4,'NAME','Computação');
INSERT INTO "ELO_courses" VALUES(13,4,'MATRIC','123456789');
INSERT INTO "ELO_courses" VALUES(14,4,'STUDENTS','[130107191, 1234567]');
CREATE TABLE "ELO_module" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
CREATE TABLE "ELO_lesson" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
CREATE TABLE "ELO_exercise" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
CREATE TABLE "ELO_identities" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "model" text NOT NULL
);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('django_migrations',2);
INSERT INTO "sqlite_sequence" VALUES('ELO_courses',14);
INSERT INTO "sqlite_sequence" VALUES('ELO_identities',2);
CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date");
COMMIT;
