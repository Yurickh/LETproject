PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE "Login_login" (
    "id" integer NOT NULL PRIMARY KEY,
    "user" integer NOT NULL,
    "field" varchar(4) NOT NULL,
    "value" text NOT NULL
);
INSERT INTO "Login_login" VALUES(1,1,'name','Yurick');
INSERT INTO "Login_login" VALUES(2,1,'password','a793812b');
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
INSERT INTO "django_session" VALUES('6au0ucrv5jth0h2x3en8nw7nhmonuest','M2ZkYjlkNjI0NWJkOGFkNTNkZWNkZDc2NTU0ZDEzZTgzMjE3N2FkZDqAAn1xAS4=','2013-12-13 20:02:07.051907');
INSERT INTO "django_session" VALUES('mf7gycnjohoonqtysxah6c0x4jycldc3','ZjUzZmFhOGQzYmY2ZjNiNDE3YjYyZGM4YmVlMTBmMDE5MDUwNDE2NjqAAn1xAVUEdXNlcnECY0VMTy5CYXNlVW5pdApOYW1lCnEDKYFxBH1xBVUGX3ZhbHVlcQZYBgAAAFl1cmlja3EHc2JzLg==','2014-01-01 16:47:13.807835');
INSERT INTO "django_session" VALUES('h3bynrb4bhvxfm1ssz88u2ra1sv0ilk2','ZjUzZmFhOGQzYmY2ZjNiNDE3YjYyZGM4YmVlMTBmMDE5MDUwNDE2NjqAAn1xAVUEdXNlcnECY0VMTy5CYXNlVW5pdApOYW1lCnEDKYFxBH1xBVUGX3ZhbHVlcQZYBgAAAFl1cmlja3EHc2JzLg==','2013-12-25 19:48:07.760919');
INSERT INTO "django_session" VALUES('l8voojc514pphbo331gurlb9q2nsyrpw','ZjUzZmFhOGQzYmY2ZjNiNDE3YjYyZGM4YmVlMTBmMDE5MDUwNDE2NjqAAn1xAVUEdXNlcnECY0VMTy5CYXNlVW5pdApOYW1lCnEDKYFxBH1xBVUGX3ZhbHVlcQZYBgAAAFl1cmlja3EHc2JzLg==','2014-03-05 20:31:42.783512');
INSERT INTO "django_session" VALUES('ys4i8cneysjq7kmatmxvufcln84v5qxe','ZTYyNWY3MDIyYmQwMGQxMTk4NWVlNTBmODE5NDdjMjRkNzk5ZmY2MTp7InVzZXIiOnsicGFzc3dvcmQiOiI4NGQxY2ZkNGExZTBhYTJkY2Q3YjY3NTRhMzYyNDc0NyIsInR5cGUiOiJTdHVkZW50IiwibmFtZSI6IkFuZHJlIn19','2014-04-09 18:19:27.979797');
INSERT INTO "django_session" VALUES('7j7hi8jemfg1je28yew6bcq8yydxrwx5','M2Y4MTkxYWFjNDg4NTg2NTAxY2ExYmEyNWQ0Nzg2N2Y5YzJkNDE5ZjqAAn1xAVUEdXNlcnECfXEDKFUIcGFzc3dvcmRxBFUgMmVhMmQwZjhkMzI1NTNjNWVlZGNkMTAyOTg3YzY4YjlVBHR5cGVxBVUJUHJvZmVzc29ycQZVBG5hbWVxB1gFAAAARGllZ29xCHVzLg==','2014-04-02 22:00:07.773083');
INSERT INTO "django_session" VALUES('rfzet0f3plg6ht5nkq1k9qjcwodn3wqa','M2Y4MTkxYWFjNDg4NTg2NTAxY2ExYmEyNWQ0Nzg2N2Y5YzJkNDE5ZjqAAn1xAVUEdXNlcnECfXEDKFUIcGFzc3dvcmRxBFUgMmVhMmQwZjhkMzI1NTNjNWVlZGNkMTAyOTg3YzY4YjlVBHR5cGVxBVUJUHJvZmVzc29ycQZVBG5hbWVxB1gFAAAARGllZ29xCHVzLg==','2014-04-02 22:06:30.985136');
INSERT INTO "django_session" VALUES('v4iokwkkgm8zxicm24tlqotdi53pjgc9','M2ZkYjlkNjI0NWJkOGFkNTNkZWNkZDc2NTU0ZDEzZTgzMjE3N2FkZDqAAn1xAS4=','2014-04-02 22:08:39.576422');
INSERT INTO "django_session" VALUES('d7ft4ko4aqck4rnzgwcttzc6dhnyhdhr','MTZlZmNiZDA1NzRkZjc1YjJkMDQ2MzcxYjUxNzg0NGFmNzE4MjJkZDp7InVzZXIiOnsiaW50ZXJlc3RzIjoiUG9ycmEgbG91Y2FzIiwibmFtZSI6IkFuZHJlIiwibGFuZ3VhZ2UiOiJwdC1iciIsImNvdXJzZXMiOlsiQWJhY2F0ZSIsInRpam9sbyJdLCJzZXgiOiIiLCJlbWFpbCI6IiIsImJpb3MiOiIiLCJncmFkZXMiOm51bGwsImF2YXRhciI6IiIsInBhc3N3b3JkIjoiODRkMWNmZDRhMWUwYWEyZGNkN2I2NzU0YTM2MjQ3NDciLCJ0eXBlIjoiU3R1ZGVudCIsImNhbXB1cyI6IjAiLCJtYXRyaWMiOiIwIn19','2014-05-08 14:40:56.589206');
INSERT INTO "django_session" VALUES('dxsb45gakntt34y6xe26adic6jsf37o2','YjU0NzlmMTMzOTY4ZGQ2NDU1YmU0MGI1MzBiNzc2NzU5NjM1YjY3ZTp7InVzZXIiOnsiaW50ZXJlc3RzIjoiUG9ycmEgbG91Y2FzIiwibmFtZSI6IkFuZHJlIiwibGFuZ3VhZ2UiOiJwdC1iciIsImNvdXJzZXMiOlsiQWJhY2F0ZSIsInRpam9sbyJdLCJzZXgiOiIiLCJlbWFpbCI6IiIsImJpb3MiOiIiLCJncmFkZXMiOm51bGwsImF2YXRhciI6IjAucG5nIiwicGFzc3dvcmQiOiI4NGQxY2ZkNGExZTBhYTJkY2Q3YjY3NTRhMzYyNDc0NyIsInR5cGUiOiJTdHVkZW50IiwiY2FtcHVzIjoiMCIsIm1hdHJpYyI6IjAifX0=','2014-06-05 19:36:39.141835');
INSERT INTO "django_session" VALUES('otelf9k7yuiqb2pzb116594n0nhbivdu','ZjE0ZmVkYWFkNWFiMmE4YTk3MjBjYzliYjgyMTk1M2Y3OWUwM2RmYjp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJpbnRlcmVzdHMiOiJQb3JyYSBsb3VjYXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6InB0LWJyIiwiY291cnNlcyI6WyJBYmFjYXRlIiwidGlqb2xvIl0sInNleCI6Ik0iLCJlbWFpbCI6IiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cclxuT3IganVzdCBmYW50YSBzZWE/IiwiZ3JhZGVzIjpudWxsLCJhdmF0YXIiOiIwLnBuZyIsInBhc3N3b3JkIjoiODRkMWNmZDRhMWUwYWEyZGNkN2I2NzU0YTM2MjQ3NDciLCJ0eXBlIjoiU3R1ZGVudCIsImNhbXB1cyI6IjAiLCJtYXRyaWMiOiIwIn19','2014-07-09 12:50:37.950700');
INSERT INTO "django_session" VALUES('n9jy44smyac0rgfpc603fxt1nn23svm9','ZjE0ZmVkYWFkNWFiMmE4YTk3MjBjYzliYjgyMTk1M2Y3OWUwM2RmYjp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJpbnRlcmVzdHMiOiJQb3JyYSBsb3VjYXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6InB0LWJyIiwiY291cnNlcyI6WyJBYmFjYXRlIiwidGlqb2xvIl0sInNleCI6Ik0iLCJlbWFpbCI6IiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cclxuT3IganVzdCBmYW50YSBzZWE/IiwiZ3JhZGVzIjpudWxsLCJhdmF0YXIiOiIwLnBuZyIsInBhc3N3b3JkIjoiODRkMWNmZDRhMWUwYWEyZGNkN2I2NzU0YTM2MjQ3NDciLCJ0eXBlIjoiU3R1ZGVudCIsImNhbXB1cyI6IjAiLCJtYXRyaWMiOiIwIn19','2014-07-09 12:51:01.904320');
INSERT INTO "django_session" VALUES('g1lzflnnkqyq68jrj0j4ofoamysahrn4','YTJlMDNkNmE4NjljZDdkOGU5ZmFkN2FmNDAyNmJmOTAxZWRhYTc2Mzp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIn0=','2014-07-09 12:51:39.077694');
INSERT INTO "django_session" VALUES('fgzepwed90lfzhcss4t5u2d7hw6uhxey','YTJlMDNkNmE4NjljZDdkOGU5ZmFkN2FmNDAyNmJmOTAxZWRhYTc2Mzp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIn0=','2014-07-09 12:53:46.894792');
INSERT INTO "django_session" VALUES('xhw85nheu6vx177aqac9xsoc8ampa9xi','ZWM1MDBmZjU2NTA4YmNjNWNjZmVjNjQ0YWVmZTEwNzk4NGY2ZmNjYzp7ImRqYW5nby1sYW5ndWFnZSI6InB0LWJyIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4ifQ==','2014-07-09 13:05:55.932230');
INSERT INTO "django_session" VALUES('0mxm1f5c2tp7lja4z1qpvt6ya7qqzf03','ZDFjMzg3YWRjOTAxYWE4ZTIwMWQzNjg4Y2JhZWNkNDVkMWQ5MGQ0Njp7ImRqYW5nby1sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoicHQtYnIifQ==','2014-07-09 13:06:21.691054');
INSERT INTO "django_session" VALUES('zl2j7ynto1ao9pbqspt9x6jafh6m50cl','Y2E5OGJkMTI0MTBlOWFlZTM4NTNhODAyODc5ZDk4MTZjYTI2MzBkNDp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIiwiZGphbmdvLWxhbmd1YWdlIjoicHQtYnIifQ==','2014-07-09 13:09:10.959869');
INSERT INTO "django_session" VALUES('1txogmqw5dvges9uslta39g6ajvvyil4','MGYwNzY2MTAyMGI4NjliMmQyY2RiZTc4ZmU4NGE3YzE3MTZhMTM0Mjp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIiwiZGphbmdvLWxhbmd1YWdlIjoiZW4ifQ==','2014-07-15 20:28:06.889169');
INSERT INTO "django_session" VALUES('7smom2i8bdievfh8r0da8gm9vld3b0ce','ODQzMDliYmI1MDdhNzQwN2YzOWE4NGFkNzk4MTJhOGVmMTYxMjQ5ZTp7ImRqYW5nby1sYW5ndWFnZSI6InB0LWJyIiwiZGphbmdvX2xhbmd1YWdlIjoicHQtYnIifQ==','2014-07-15 20:39:06.319516');
INSERT INTO "django_session" VALUES('5wimyteh9dcn8apu42ypqbi2n8awb75p','YTJlMDNkNmE4NjljZDdkOGU5ZmFkN2FmNDAyNmJmOTAxZWRhYTc2Mzp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIn0=','2014-07-15 20:48:46.050982');
INSERT INTO "django_session" VALUES('6lc9yginwe6t74lp6gvxdzlb6r03bq7c','OWNhMjI5YzFlMGZlY2M3ZDBiMzY0YzkwYzRhMTY3MDExN2M1ZDI2Yzp7ImRqYW5nb19sYW5ndWFnZSI6InB0LWJyIiwidXNlciI6eyJpbnRlcmVzdHMiOiJQb3JyYSBsb3VjYXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6InB0LWJyIiwiY291cnNlcyI6WyJBYmFjYXRlIiwidGlqb2xvIl0sInNleCI6Ik0iLCJiaW9zIjoiSXMgdGhpcyByZWFsIGxpZmU/XHJcbk9yIGp1c3QgZmFudGEgc2VhPyIsImdyYWRlcyI6bnVsbCwiZW1haWwiOiIiLCJhdmF0YXIiOiIwLnBuZyIsInBhc3N3b3JkIjoiODRkMWNmZDRhMWUwYWEyZGNkN2I2NzU0YTM2MjQ3NDciLCJ0eXBlIjoiU3R1ZGVudCIsImNhbXB1cyI6IjAiLCJtYXRyaWMiOiIwIn19','2014-07-24 19:13:48.878415');
INSERT INTO "django_session" VALUES('u2mkf6kbwrlgxn3b7ildlob3wbv0kd8a','MDkxZWUzOGI4Zjg0YzdhZDI3NTFiOGJiOTVjOTUxYjI1ZWY3MzdlOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIiwidXNlciI6eyJpbnRlcmVzdHMiOiJBYmFjYXRlcyxFdSxWb2NcdTAwZWEsWm9ib21hZm9vIiwibmFtZSI6IkFuZHJlIiwibGFuZ3VhZ2UiOiJlbiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cclxuT3IganVzdCBmYW50YSBzZWE/IEVzY3JldmF+IiwiY2FtcHVzIjoiMCIsInNleCI6Ik0iLCJjb3Vyc2VzIjpbIkFiYWNhdGUiLCJ0aWpvbG8iXSwiZ3JhZGVzIjpudWxsLCJhdmF0YXIiOiJhdmF0YXIvMS5wbmciLCJwYXNzd29yZCI6Ijg0ZDFjZmQ0YTFlMGFhMmRjZDdiNjc1NGEzNjI0NzQ3IiwidHlwZSI6IlN0dWRlbnQiLCJlbWFpbCI6IiIsIm1hdHJpYyI6IjAifX0=','2014-08-28 18:50:49.486293');
INSERT INTO "django_session" VALUES('02pthi3zvzfhdwtm2q0ayeiayb1yfwoc','MDhlMWZkNjA3MmYxNjQ0YWZkOWI2YWQyMGNjMzU2N2Y5OGRmZDVjODp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7ImludGVyZXN0cyI6Ill1cmljayx2b2NcdTAwZWEsQWJhY2F0ZXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6ImVuIiwiY291cnNlcyI6WyJBYmFjYXRlIiwidGlqb2xvIl0sInNleCI6Ik0iLCJlbWFpbCI6IiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cclxuT3IganVzdCBmYW50YSBzZWE/IEVzY3JldmF+IiwiZ3JhZGVzIjpudWxsLCJhdmF0YXIiOiJhdmF0YXIvMS5wbmciLCJwYXNzd29yZCI6Ijg0ZDFjZmQ0YTFlMGFhMmRjZDdiNjc1NGEzNjI0NzQ3IiwidHlwZSI6IlN0dWRlbnQiLCJjYW1wdXMiOiIwIiwibWF0cmljIjoiMCJ9fQ==','2014-10-31 02:16:19.158310');
INSERT INTO "django_session" VALUES('qx82gg8azdbbi8sb0ukb085y4tejjhvz','YzE2ZjQxZThmMTI4NzUzMTU2N2RjZDFiNjQ2NjBiNmY1M2MyZDg3Yzp7fQ==','2014-12-11 14:18:58.560515');
INSERT INTO "django_session" VALUES('fbu5iaihzuoswowsi0stxems3gwk2c0z','YTBiZjBmNzVmNGI1Mjk0MGZkZDZiY2IwMjdhZDlkMjU0N2Q0YzExYjp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7ImludGVyZXN0cyI6Ill1cmljayx2b2NcdTAwZWEsQWJhY2F0ZXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6ImVuIiwiY291cnNlcyI6W3siY29tcGxldGlvbiI6NTAuMCwibmFtZSI6InRlc3Rjb3Vyc2UiLCJpZCI6IjEifV0sInNleCI6Ik0iLCJlbWFpbCI6IiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cbk9yIGp1c3QgZmFudGEgc2VhPyBFc2NyZXZhfiIsImdyYWRlcyI6bnVsbCwiYXZhdGFyIjoiYXZhdGFyLzIucG5nIiwicGFzc3dvcmQiOiI4NGQxY2ZkNGExZTBhYTJkY2Q3YjY3NTRhMzYyNDc0NyIsInR5cGUiOiJTdHVkZW50IiwiY2FtcHVzIjoiMCIsIm1hdHJpYyI6IjAifX0=','2014-12-29 15:38:47.813036');
INSERT INTO "django_session" VALUES('meshnco32hqc9phwwhx55ytxcrs915ct','YTBiZjBmNzVmNGI1Mjk0MGZkZDZiY2IwMjdhZDlkMjU0N2Q0YzExYjp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7ImludGVyZXN0cyI6Ill1cmljayx2b2NcdTAwZWEsQWJhY2F0ZXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6ImVuIiwiY291cnNlcyI6W3siY29tcGxldGlvbiI6NTAuMCwibmFtZSI6InRlc3Rjb3Vyc2UiLCJpZCI6IjEifV0sInNleCI6Ik0iLCJlbWFpbCI6IiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cbk9yIGp1c3QgZmFudGEgc2VhPyBFc2NyZXZhfiIsImdyYWRlcyI6bnVsbCwiYXZhdGFyIjoiYXZhdGFyLzIucG5nIiwicGFzc3dvcmQiOiI4NGQxY2ZkNGExZTBhYTJkY2Q3YjY3NTRhMzYyNDc0NyIsInR5cGUiOiJTdHVkZW50IiwiY2FtcHVzIjoiMCIsIm1hdHJpYyI6IjAifX0=','2014-12-13 16:11:13.161669');
INSERT INTO "django_session" VALUES('vna5jaf7buzd3rski9h7alfjtp6zpjwk','YTBiZjBmNzVmNGI1Mjk0MGZkZDZiY2IwMjdhZDlkMjU0N2Q0YzExYjp7Il9sYW5ndWFnZSI6ImVuIiwiZGphbmdvX2xhbmd1YWdlIjoiZW4iLCJ1c2VyIjp7ImludGVyZXN0cyI6Ill1cmljayx2b2NcdTAwZWEsQWJhY2F0ZXMiLCJuYW1lIjoiQW5kcmUiLCJsYW5ndWFnZSI6ImVuIiwiY291cnNlcyI6W3siY29tcGxldGlvbiI6NTAuMCwibmFtZSI6InRlc3Rjb3Vyc2UiLCJpZCI6IjEifV0sInNleCI6Ik0iLCJlbWFpbCI6IiIsImJpb3MiOiJJcyB0aGlzIHJlYWwgbGlmZT9cbk9yIGp1c3QgZmFudGEgc2VhPyBFc2NyZXZhfiIsImdyYWRlcyI6bnVsbCwiYXZhdGFyIjoiYXZhdGFyLzIucG5nIiwicGFzc3dvcmQiOiI4NGQxY2ZkNGExZTBhYTJkY2Q3YjY3NTRhMzYyNDc0NyIsInR5cGUiOiJTdHVkZW50IiwiY2FtcHVzIjoiMCIsIm1hdHJpYyI6IjAifX0=','2014-12-31 17:25:30.256209');
INSERT INTO "django_session" VALUES('cjwbdlqiggfnojqd948kmi3k9ep1aln7','NDYzZDJlYzQyZDFiMDVhYTRhNDBmZWMwMmNmMGQxMjdhMzdkM2JjOTp7Il9sYW5ndWFnZSI6ImVuIiwidXNlciI6eyJuYW1lIjoiWXVyaWNrIiwibGFuZ3VhZ2UiOiJlbiIsImNvdXJzZXMiOm51bGwsInNleCI6bnVsbCwiZW1haWwiOm51bGwsImJpb3MiOm51bGwsImF2YXRhciI6bnVsbCwicGFzc3dvcmQiOiJiMGYxNjQ2MjUyZjQ0MzRiZTNlZjc0ZTdhYjZhYzE3NyIsInR5cGUiOiJQcm9mZXNzb3IiLCJjYW1wdXMiOm51bGwsIm1hdHJpYyI6bnVsbH0sImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=','2015-05-21 21:28:23.588632');
CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
INSERT INTO "auth_permission" VALUES(1,'Can add permission',1,'add_permission');
INSERT INTO "auth_permission" VALUES(2,'Can change permission',1,'change_permission');
INSERT INTO "auth_permission" VALUES(3,'Can delete permission',1,'delete_permission');
INSERT INTO "auth_permission" VALUES(4,'Can add group',2,'add_group');
INSERT INTO "auth_permission" VALUES(5,'Can change group',2,'change_group');
INSERT INTO "auth_permission" VALUES(6,'Can delete group',2,'delete_group');
INSERT INTO "auth_permission" VALUES(7,'Can add user',3,'add_user');
INSERT INTO "auth_permission" VALUES(8,'Can change user',3,'change_user');
INSERT INTO "auth_permission" VALUES(9,'Can delete user',3,'delete_user');
INSERT INTO "auth_permission" VALUES(10,'Can add content type',4,'add_contenttype');
INSERT INTO "auth_permission" VALUES(11,'Can change content type',4,'change_contenttype');
INSERT INTO "auth_permission" VALUES(12,'Can delete content type',4,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(13,'Can add session',5,'add_session');
INSERT INTO "auth_permission" VALUES(14,'Can change session',5,'change_session');
INSERT INTO "auth_permission" VALUES(15,'Can delete session',5,'delete_session');
INSERT INTO "auth_permission" VALUES(16,'Can add student',6,'add_student');
INSERT INTO "auth_permission" VALUES(17,'Can change student',6,'change_student');
INSERT INTO "auth_permission" VALUES(18,'Can delete student',6,'delete_student');
CREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
);
CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
CREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
);
CREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
);
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL
);
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

INSERT INTO "ELO_student" VALUES(1,1,'NAME','Andre');
INSERT INTO "ELO_student" VALUES(2,1,'PASSWORD','84d1cfd4a1e0aa2dcd7b6754a3624747');
INSERT INTO "ELO_student" VALUES(3,1,'BIOS','Is this real life?
Or just fanta sea? Escreva~');
INSERT INTO "ELO_student" VALUES(4,1,'MATRIC','0');
INSERT INTO "ELO_student" VALUES(5,1,'CAMPUS','0');
INSERT INTO "ELO_student" VALUES(6,1,'AVATAR','avatar/2.png');
INSERT INTO "ELO_student" VALUES(7,1,'EMAIL','');
INSERT INTO "ELO_student" VALUES(8,1,'SEX','M');
INSERT INTO "ELO_student" VALUES(9,1,'INTEREST','Yurick,você,Abacates');
INSERT INTO "ELO_student" VALUES(10,1,'LANGUAGE','en');
INSERT INTO "ELO_student" VALUES(11,1,'COURSE','1');

INSERT INTO "ELO_student" VALUES(12,1,'MODULE_COMPLETED','2');
INSERT INTO "ELO_student" VALUES(13,1,'LOCK_COMPLETED','4');
INSERT INTO "ELO_student" VALUES(14,1,'LESSON_COMPLETED','1');
INSERT INTO "ELO_student" VALUES(15,1,'LOCK_COMPLETED','2');

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

INSERT INTO "ELO_professor" VALUES(3,1,'NAME','Yurick');
INSERT INTO "ELO_professor" VALUES(4,1,'PASSWORD','b0f1646252f4434be3ef74e7ab6ac177');
INSERT INTO "ELO_professor" VALUES(5,1,'LANGUAGE','en');

CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2014-10-03 21:10:53.126238');
INSERT INTO "django_migrations" VALUES(2,'sessions','0001_initial','2014-10-03 21:10:53.222176');

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

INSERT INTO "ELO_courses" VALUES(1,1,'STUDENT','1');
INSERT INTO "ELO_courses" VALUES(2,1,'MODULE','2');
INSERT INTO "ELO_courses" VALUES(3,1,'MODULE','1');
INSERT INTO "ELO_courses" VALUES(4,1,'NAME','testcourse');
INSERT INTO "ELO_courses" VALUES(5,1,'EXERCISE','1');

CREATE TABLE "ELO_module" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);

INSERT INTO "ELO_module" VALUES(1,1,'NAME','first module');
INSERT INTO "ELO_module" VALUES(2,1,'LESSON','1');
INSERT INTO "ELO_module" VALUES(3,1,'LESSON','2');
INSERT INTO "ELO_module" VALUES(5,1,'EXERCISE','2');
INSERT INTO "ELO_module" VALUES(6,2,'NAME','second funny module');
INSERT INTO "ELO_module" VALUES(7,1,'LESSON','3');
INSERT INTO "ELO_module" VALUES(8,2,'LESSON','4');
INSERT INTO "ELO_module" VALUES(9,2,'EXERCISE','3');
CREATE TABLE "ELO_lesson" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "identity" integer NOT NULL,
    "field" varchar(32) NOT NULL,
    "value" text NOT NULL
);
INSERT INTO "ELO_lesson" VALUES(1,1,'NAME','About Avocados');
INSERT INTO "ELO_lesson" VALUES(2,1,'LINK','less1_about_avocados');
INSERT INTO "ELO_lesson" VALUES(3,1,'EXERCISE','4');
INSERT INTO "ELO_lesson" VALUES(4,2,'NAME','About Bricks');
INSERT INTO "ELO_lesson" VALUES(5,2,'LINK','less2_about_bricks');
INSERT INTO "ELO_lesson" VALUES(6,2,'EXERCISE','5');
INSERT INTO "ELO_lesson" VALUES(7,2,'EXERCISE','6');
INSERT INTO "ELO_lesson" VALUES(8,3,'NAME','About Onions');
INSERT INTO "ELO_lesson" VALUES(9,3,'LINK','less3_about_onions');
INSERT INTO "ELO_lesson" VALUES(10,4,'NAME','About Bears');
INSERT INTO "ELO_lesson" VALUES(11,4,'LINK','less4_about_bears');
INSERT INTO "ELO_lesson" VALUES(12,1,'SLIDES','4');
INSERT INTO "ELO_lesson" VALUES(13,2,'SLIDES','3');
INSERT INTO "ELO_lesson" VALUES(14,3,'SLIDES','0');
INSERT INTO "ELO_lesson" VALUES(15,4,'SLIDES','0');
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

INSERT INTO "ELO_exercise" VALUES(1,1,'LINK','ex1_module1');
INSERT INTO "ELO_exercise" VALUES(2,1,'TYPE','1');
INSERT INTO "ELO_exercise" VALUES(3,1,'ITEM_1','Happy');
INSERT INTO "ELO_exercise" VALUES(4,1,'ITEM_2','Bored');
INSERT INTO "ELO_exercise" VALUES(5,1,'ITEM_3','ULTRA DUPPER HAPPY OMG THIS SHIT IS AWSM');
INSERT INTO "ELO_exercise" VALUES(6,2,'LINK','ex2_module1');
INSERT INTO "ELO_exercise" VALUES(7,2,'TYPE','1');
INSERT INTO "ELO_exercise" VALUES(9,2,'ITEM_1','Obviously, 0');
INSERT INTO "ELO_exercise" VALUES(10,2,'ITEM_2','TLDR;');
INSERT INTO "ELO_exercise" VALUES(11,2,'ITEM_3','Don''t really know');
INSERT INTO "ELO_exercise" VALUES(12,1,'CORRECT','3');
INSERT INTO "ELO_exercise" VALUES(13,2,'CORRECT','2');
INSERT INTO "ELO_exercise" VALUES(14,3,'LINK','ex3_module2');
INSERT INTO "ELO_exercise" VALUES(15,3,'TYPE','2');
INSERT INTO "ELO_exercise" VALUES(16,3,'CORECT','shuffling');
INSERT INTO "ELO_exercise" VALUES(18,4,'LINK','ex4_avocados');
INSERT INTO "ELO_exercise" VALUES(19,4,'TYPE','1');
INSERT INTO "ELO_exercise" VALUES(20,4,'ITEM_1','Great!');
INSERT INTO "ELO_exercise" VALUES(21,4,'ITEM_2','Healthy');
INSERT INTO "ELO_exercise" VALUES(22,4,'ITEM_3','AWSM!!!1!');
INSERT INTO "ELO_exercise" VALUES(23,4,'ITEM_4','Bad');
INSERT INTO "ELO_exercise" VALUES(24,4,'CORRECT','3');
INSERT INTO "ELO_exercise" VALUES(25,5,'LINK','ex5_bricks');
INSERT INTO "ELO_exercise" VALUES(26,5,'TYPE','2');
INSERT INTO "ELO_exercise" VALUES(28,5,'CORRECT','Brazil');
INSERT INTO "ELO_exercise" VALUES(29,5,'CORRECT','Russia');
INSERT INTO "ELO_exercise" VALUES(30,5,'CORRECT','India');
INSERT INTO "ELO_exercise" VALUES(31,5,'CORRECT','China');
INSERT INTO "ELO_exercise" VALUES(32,5,'CORRECT','South Africa');
INSERT INTO "ELO_exercise" VALUES(33,6,'LINK','ex6_bricks');
INSERT INTO "ELO_exercise" VALUES(34,6,'TYPE','1');
INSERT INTO "ELO_exercise" VALUES(35,6,'ITEM_1','Good for throwing at people');
INSERT INTO "ELO_exercise" VALUES(36,6,'ITEM_2','Hard as rock');
INSERT INTO "ELO_exercise" VALUES(37,6,'ITEM_3','AWSM!!!1!!!11');
INSERT INTO "ELO_exercise" VALUES(38,6,'CORRECT','3');

DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('django_migrations',2);
INSERT INTO "sqlite_sequence" VALUES('ELO_courses',5);
INSERT INTO "sqlite_sequence" VALUES('ELO_module',9);
INSERT INTO "sqlite_sequence" VALUES('ELO_lesson',15);
INSERT INTO "sqlite_sequence" VALUES('ELO_exercise',38);
CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date");
COMMIT;
