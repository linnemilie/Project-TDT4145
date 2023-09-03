-- Gruppe 109 - Linn Emilie Kalleberg og Kirsten Gjester Nord

-- For å sette inn verdier gitt at du har fulgt instruksjonene i create-tables.sql: 

-- 1. .read insert-data.sql



-- BRUKERHISTORIE A:

insert into banestrekning values ("Nordlandsbanen", "diesel", "Trondheim", "Bodø");

insert into jernbanestasjon values ("Trondheim", 5.1);
insert into jernbanestasjon values ("Steinkjer", 3.6);
insert into jernbanestasjon values ("Mosjøen", 6.8);
insert into jernbanestasjon values ("Mo i rana", 3.5);
insert into jernbanestasjon values ("Fauske", 34.0);
insert into jernbanestasjon values ("Bodø", 4.1);

insert into delstrekning values ("Trondheim-Steinkjer", 120, "dobbel", "Nordlandsbanen", "Trondheim", "Steinkjer");
insert into delstrekning values ("Steinkjer-Mosjøen", 280, "enkel", "Nordlandsbanen", "Steinkjer", "Mosjøen");
insert into delstrekning values ("Mosjøen-Mo i Rana", 90, "enkel", "Nordlandsbanen", "Mosjøen", "Mo i rana");
insert into delstrekning values ("Mo i Rana-Fauske", 170, "enkel", "Nordlandsbanen", "Mo i rana", "Fauske");
insert into delstrekning values ("Fauske-Bodø", 60, "enkel", "Nordlandsbanen", "Fauske", "Bodø");

-- BRUKERHISTORIE B:

insert into togrute values ("Tro-Bod-dag", "Nordlandsbanen", "med", "Trondheim", "07:49:00", "Bodø", "17:34:00", 1);
insert into togrute values ("Tro-Bod-natt", "Nordlandsbanen", "med", "Trondheim", "23:05:00", "Bodø", "09:05:00", 1);
insert into togrute values ("Mo-Tro-morg", "Nordlandsbanen", "mot", "Mo i rana", "08:11:00", "Trondheim", "14:13:00", 1);

insert into mellomstasjon values ("Tro-Bod-dag", "Steinkjer", "09:51:00", "09:53:00");
insert into mellomstasjon values ("Tro-Bod-dag", "Mosjøen", "13:20:00", "13:22:00");
insert into mellomstasjon values ("Tro-Bod-dag", "Mo i rana", "14:31:00", "14:33:00");
insert into mellomstasjon values ("Tro-Bod-dag", "Fauske", "16:49:00", "16:51:00");

insert into mellomstasjon values ("Tro-Bod-natt", "Steinkjer", "00:57:00", "00:59:00");
insert into mellomstasjon values ("Tro-Bod-natt", "Mosjøen", "04:41:00", "04:43:00");
insert into mellomstasjon values ("Tro-Bod-natt", "Mo i rana", "05:55:00", "05:57:00");
insert into mellomstasjon values ("Tro-Bod-natt", "Fauske", "08:19:00", "08:21:00");

insert into mellomstasjon values ("Mo-Tro-morg", "Mosjøen", "09:14:00", "09:16:00");
insert into mellomstasjon values ("Mo-Tro-morg", "Steinkjer", "12:31:00", "12:33:00");

insert into operatør values (1, "SJ");

insert into togreise values ("Mandag", "Tro-Bod-dag", 1);
insert into togreise values ("Tirsdag", "Tro-Bod-dag", 1);
insert into togreise values ("Onsdag", "Tro-Bod-dag", 1);
insert into togreise values ("Torsdag", "Tro-Bod-dag", 1);
insert into togreise values ("Fredag", "Tro-Bod-dag", 1);

insert into togreise values ("Mandag", "Tro-Bod-natt", 2);
insert into togreise values ("Tirsdag", "Tro-Bod-natt", 2);
insert into togreise values ("Onsdag", "Tro-Bod-natt", 2);
insert into togreise values ("Torsdag", "Tro-Bod-natt", 2);
insert into togreise values ("Fredag", "Tro-Bod-natt", 2);
insert into togreise values ("Lørdag", "Tro-Bod-natt", 2);
insert into togreise values ("Søndag", "Tro-Bod-natt", 2);

insert into togreise values ("Mandag", "Mo-Tro-morg", 3);
insert into togreise values ("Tirsdag", "Mo-Tro-morg", 3);
insert into togreise values ("Onsdag", "Mo-Tro-morg", 3);
insert into togreise values ("Torsdag", "Mo-Tro-morg", 3);
insert into togreise values ("Fredag", "Mo-Tro-morg", 3);

insert into vognoppsett values (1);
insert into vognoppsett values (2);
insert into vognoppsett values (3);

insert into vognIOppsett values (1, "1", 1);
insert into vognIOppsett values (1, "2", 2);
insert into vognIOppsett values (2, "4", 1);
insert into vognIOppsett values (2, "S1", 2);
insert into vognIOppsett values (3, "3", 1);


insert into vogn values ("1", 12);
insert into vogn values ("2", 12);
insert into vogn values ("S1", 8);
insert into vogn values ("3", 12);
insert into vogn values ("4", 12);


-- BRUKERHISTORIE F:

insert into billett values (1, 1, 1, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (2, 1, 2, 'Mandag', 'Tro-Bod-dag', '2023-04-03' ); 
insert into billett values (3, 1, 3, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (4, 1, 4, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (5, 1, 5, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (6, 1, 6, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (7, 1, 7, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (8, 1, 8, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (9, 1, 9, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (10, 1, 10, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (11, 1, 11, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (12, 1, 12, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (13, 2, 1, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (14, 2, 2, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (15, 2, 3, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (16, 2, 4, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (17, 2, 5, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (18, 2, 6, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (19, 2, 7, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (20, 2, 8, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (21, 2, 9, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (22, 2, 10, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (23, 2, 11, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );
insert into billett values (24, 2, 12, 'Mandag', 'Tro-Bod-dag', '2023-04-03' );

insert into billett values (25, 1, 1, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (26, 1, 2, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (27, 1, 3, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (28, 1, 4, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (29, 1, 5, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (30, 1, 6, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (31, 1, 7, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (32, 1, 8, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (33, 1, 9, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (34, 1, 10, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (35, 1, 11, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (36, 1, 12, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (37, 2, 1, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (38, 2, 2, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (39, 2, 3, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (40, 2, 4, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (41, 2, 5, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (42, 2, 6, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (43, 2, 7, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );
insert into billett values (44, 2, 8, 'Mandag', 'Tro-Bod-natt', '2023-04-03' );

insert into billett values (45, 1, 1, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (46, 1, 2, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (47, 1, 3, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (48, 1, 4, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (49, 1, 5, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (50, 1, 6, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (51, 1, 7, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (52, 1, 8, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (53, 1, 9, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (54, 1, 10, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (55, 1, 11, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );
insert into billett values (56, 1, 12, 'Mandag', 'Mo-Tro-morg', '2023-04-03' );


-- billetter neste dag (4 april)

insert into billett values (57, 1, 1, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (58, 1, 2, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (59, 1, 3, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (60, 1, 4, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (61, 1, 5, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (62, 1, 6, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (63, 1, 7, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (64, 1, 8, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (65, 1, 9, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (66, 1, 10, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (67, 1, 11, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (68, 1, 12, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (69, 2, 1, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (70, 2, 2, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (71, 2, 3, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (72, 2, 4, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (73, 2, 5, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (74, 2, 6, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (75, 2, 7, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (76, 2, 8, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (77, 2, 9, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (78, 2, 10, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (79, 2, 11, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );
insert into billett values (80, 2, 12, 'Tirsdag', 'Tro-Bod-dag', '2023-04-04' );

insert into billett values (81, 1, 1, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (82, 1, 2, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (83, 1, 3, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (84, 1, 4, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (85, 1, 5, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (86, 1, 6, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (87, 1, 7, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (88, 1, 8, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (89, 1, 9, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (90, 1, 10, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (91, 1, 11, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (92, 1, 12, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (93, 2, 1, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (94, 2, 2, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (95, 2, 3, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (96, 2, 4, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (97, 2, 5, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (98, 2, 6, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (99, 2, 7, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );
insert into billett values (100, 2, 8, 'Tirsdag', 'Tro-Bod-natt', '2023-04-04' );

insert into billett values (101, 1, 1, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (102, 1, 2, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (103, 1, 3, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (104, 1, 4, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (105, 1, 5, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (106, 1, 6, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (107, 1, 7, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (108, 1, 8, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (109, 1, 9, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (110, 1, 10, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (111, 1, 11, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );
insert into billett values (112, 1, 12, 'Tirsdag', 'Mo-Tro-morg', '2023-04-04' );




