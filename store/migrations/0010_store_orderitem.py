# Generated by Django 5.0.6 on 2024-07-07 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_store_order'),
    ]

    operations = [
        migrations.RunSQL("""
insert into store_orderitem (id, quantity, unit_price, order_id, product_id)
values  (1, 3, 81.61, 357, 751),
        (2, 4, 18.06, 903, 920),
        (3, 4, 38.24, 420, 62),
        (4, 3, 61.53, 767, 863),
        (5, 5, 78.22, 944, 944),
        (6, 1, 4.95, 913, 977),
        (7, 1, 9.07, 105, 890),
        (8, 2, 88.70, 928, 556),
        (9, 5, 26.82, 758, 413),
        (10, 1, 80.23, 712, 262),
        (11, 3, 30.10, 199, 816),
        (12, 3, 41.42, 706, 427),
        (13, 2, 90.25, 78, 183),
        (14, 1, 52.33, 406, 605),
        (15, 1, 12.11, 252, 227),
        (16, 5, 18.34, 330, 695),
        (17, 4, 53.03, 881, 71),
        (18, 1, 54.43, 134, 174),
        (19, 2, 80.03, 331, 923),
        (20, 4, 75.02, 855, 785),
        (21, 4, 74.85, 693, 528),
        (22, 3, 98.50, 720, 80),
        (23, 2, 4.94, 357, 690),
        (24, 4, 62.72, 346, 38),
        (25, 1, 37.66, 475, 52),
        (26, 2, 69.56, 248, 505),
        (27, 4, 54.21, 843, 766),
        (28, 1, 40.84, 726, 451),
        (29, 3, 94.71, 534, 5),
        (30, 3, 49.54, 466, 245),
        (31, 1, 28.70, 864, 701),
        (32, 2, 42.30, 609, 604),
        (33, 1, 70.34, 676, 514),
        (34, 2, 86.21, 104, 259),
        (35, 1, 77.65, 372, 821),
        (36, 4, 71.03, 577, 81),
        (37, 2, 12.65, 288, 676),
        (38, 4, 68.73, 689, 343),
        (39, 4, 36.71, 940, 222),
        (40, 2, 39.89, 240, 1),
        (41, 5, 42.05, 804, 967),
        (42, 1, 18.54, 458, 616),
        (43, 1, 64.43, 170, 747),
        (44, 2, 94.47, 910, 654),
        (45, 2, 99.97, 864, 791),
        (46, 1, 42.21, 541, 893),
        (47, 5, 13.57, 937, 683),
        (48, 1, 3.75, 247, 114),
        (49, 3, 3.68, 56, 626),
        (50, 5, 24.44, 131, 952),
        (51, 5, 5.09, 72, 683),
        (52, 1, 58.95, 937, 621),
        (53, 1, 3.42, 507, 610),
        (54, 5, 29.53, 203, 58),
        (55, 5, 91.98, 858, 26),
        (56, 5, 7.48, 117, 136),
        (57, 1, 67.92, 870, 517),
        (58, 1, 76.86, 884, 295),
        (59, 1, 11.29, 119, 187),
        (60, 5, 18.04, 436, 946),
        (61, 3, 19.07, 322, 234),
        (62, 1, 1.46, 841, 574),
        (63, 3, 55.85, 597, 647),
        (64, 5, 46.73, 450, 150),
        (65, 2, 2.67, 623, 238),
        (66, 1, 53.93, 182, 825),
        (67, 5, 83.39, 49, 660),
        (68, 5, 79.71, 263, 743),
        (69, 5, 48.05, 678, 548),
        (70, 1, 23.57, 790, 216),
        (71, 4, 12.40, 185, 5),
        (72, 3, 96.27, 304, 981),
        (73, 2, 45.85, 661, 852),
        (74, 4, 94.06, 999, 941),
        (75, 1, 43.44, 846, 216),
        (76, 4, 48.03, 496, 183),
        (77, 1, 81.57, 32, 142),
        (78, 5, 74.47, 740, 398),
        (79, 5, 2.17, 515, 905),
        (80, 5, 58.37, 623, 911),
        (81, 2, 16.10, 997, 866),
        (82, 2, 55.28, 67, 818),
        (83, 2, 81.11, 893, 592),
        (84, 4, 38.32, 94, 558),
        (85, 5, 18.97, 773, 724),
        (86, 3, 99.51, 940, 136),
        (87, 5, 39.48, 164, 810),
        (88, 2, 3.07, 36, 845),
        (89, 1, 16.89, 728, 767),
        (90, 1, 54.62, 439, 689),
        (91, 3, 65.71, 969, 792),
        (92, 4, 5.08, 524, 329),
        (93, 2, 98.76, 1000, 381),
        (94, 1, 59.74, 542, 900),
        (95, 1, 7.28, 191, 992),
        (96, 5, 78.97, 333, 847),
        (97, 4, 22.85, 966, 609),
        (98, 1, 8.47, 584, 21),
        (99, 3, 38.23, 997, 106),
        (100, 4, 73.69, 609, 186),
        (101, 2, 79.76, 527, 771),
        (102, 4, 92.63, 912, 357),
        (103, 4, 2.31, 813, 840),
        (104, 1, 6.84, 278, 44),
        (105, 3, 98.89, 986, 236),
        (106, 5, 3.43, 272, 275),
        (107, 3, 75.65, 303, 973),
        (108, 2, 7.52, 731, 315),
        (109, 3, 3.09, 517, 221),
        (110, 3, 75.04, 972, 146),
        (111, 2, 27.63, 850, 938),
        (112, 1, 80.11, 61, 346),
        (113, 1, 29.23, 877, 116),
        (114, 4, 32.59, 492, 561),
        (115, 1, 16.08, 981, 508),
        (116, 5, 8.36, 670, 539),
        (117, 1, 60.05, 471, 155),
        (118, 2, 74.59, 381, 985),
        (119, 5, 90.90, 569, 374),
        (120, 5, 38.82, 565, 420),
        (121, 1, 97.92, 915, 267),
        (122, 3, 18.91, 676, 940),
        (123, 5, 20.94, 21, 444),
        (124, 1, 39.96, 917, 529),
        (125, 3, 19.68, 514, 31),
        (126, 4, 43.69, 683, 865),
        (127, 3, 25.34, 495, 320),
        (128, 4, 31.25, 602, 294),
        (129, 1, 84.29, 62, 775),
        (130, 1, 39.26, 341, 29),
        (131, 5, 98.77, 473, 564),
        (132, 1, 16.39, 386, 329),
        (133, 3, 8.51, 855, 203),
        (134, 5, 63.51, 274, 439),
        (135, 5, 82.54, 145, 368),
        (136, 5, 7.71, 434, 738),
        (137, 5, 52.62, 237, 834),
        (138, 1, 34.87, 900, 979),
        (139, 1, 52.83, 678, 696),
        (140, 3, 52.20, 954, 821),
        (141, 4, 11.89, 543, 328),
        (142, 1, 33.57, 199, 283),
        (143, 2, 42.31, 606, 877),
        (144, 4, 33.54, 398, 92),
        (145, 5, 49.20, 97, 261),
        (146, 2, 5.74, 978, 570),
        (147, 1, 30.45, 674, 659),
        (148, 2, 79.30, 268, 422),
        (149, 1, 36.63, 873, 492),
        (150, 1, 4.87, 322, 970),
        (151, 5, 49.31, 614, 960),
        (152, 3, 66.83, 938, 810),
        (153, 3, 26.86, 942, 927),
        (154, 2, 88.94, 692, 591),
        (155, 1, 17.93, 599, 349),
        (156, 5, 80.49, 227, 184),
        (157, 2, 12.08, 510, 530),
        (158, 2, 98.73, 46, 79),
        (159, 4, 70.85, 522, 736),
        (160, 3, 27.06, 68, 247),
        (161, 2, 10.46, 692, 103),
        (162, 1, 32.74, 963, 397),
        (163, 5, 80.50, 410, 267),
        (164, 3, 72.57, 293, 307),
        (165, 2, 10.51, 889, 241),
        (166, 2, 34.34, 383, 753),
        (167, 2, 39.90, 931, 632),
        (168, 1, 76.16, 184, 212),
        (169, 2, 68.11, 285, 284),
        (170, 4, 16.67, 119, 133),
        (171, 4, 42.18, 901, 191),
        (172, 4, 87.60, 53, 450),
        (173, 1, 97.04, 521, 197),
        (174, 1, 9.05, 704, 717),
        (175, 1, 74.86, 871, 328),
        (176, 1, 53.50, 549, 799),
        (177, 3, 64.32, 21, 829),
        (178, 4, 90.48, 725, 333),
        (179, 5, 40.80, 254, 705),
        (180, 1, 42.83, 600, 643),
        (181, 1, 91.38, 637, 616),
        (182, 4, 7.59, 858, 951),
        (183, 2, 63.97, 209, 268),
        (184, 3, 43.60, 672, 677),
        (185, 5, 11.46, 884, 216),
        (186, 1, 75.44, 967, 918),
        (187, 1, 95.04, 157, 209),
        (188, 2, 43.35, 953, 877),
        (189, 5, 81.68, 40, 782),
        (190, 5, 23.02, 206, 347),
        (191, 5, 71.84, 164, 803),
        (192, 4, 34.41, 691, 867),
        (193, 4, 55.12, 667, 582),
        (194, 1, 21.05, 161, 152),
        (195, 3, 45.02, 757, 755),
        (196, 3, 88.13, 493, 640),
        (197, 4, 68.24, 826, 103),
        (198, 5, 11.22, 697, 298),
        (199, 4, 60.50, 512, 13),
        (200, 5, 48.42, 223, 609),
        (201, 5, 89.50, 128, 969),
        (202, 3, 26.30, 807, 191),
        (203, 3, 36.08, 443, 88),
        (204, 3, 76.13, 485, 754),
        (205, 4, 60.21, 765, 704),
        (206, 5, 90.87, 367, 309),
        (207, 1, 89.24, 149, 628),
        (208, 2, 19.51, 466, 309),
        (209, 2, 69.50, 863, 600),
        (210, 1, 5.52, 923, 875),
        (211, 3, 54.81, 451, 858),
        (212, 3, 67.38, 106, 654),
        (213, 1, 86.85, 698, 561),
        (214, 3, 84.56, 645, 53),
        (215, 3, 28.06, 69, 870),
        (216, 2, 10.27, 261, 135),
        (217, 5, 32.34, 683, 596),
        (218, 5, 7.72, 709, 530),
        (219, 4, 45.34, 469, 179),
        (220, 3, 66.43, 186, 81),
        (221, 5, 2.16, 300, 317),
        (222, 3, 58.41, 402, 398),
        (223, 2, 82.79, 108, 165),
        (224, 1, 43.63, 230, 41),
        (225, 3, 9.68, 759, 907),
        (226, 5, 50.32, 964, 44),
        (227, 1, 91.02, 951, 61),
        (228, 1, 39.43, 124, 353),
        (229, 1, 37.10, 704, 904),
        (230, 1, 62.78, 332, 187),
        (231, 1, 9.65, 576, 277),
        (232, 5, 1.31, 180, 328),
        (233, 4, 93.97, 472, 737),
        (234, 4, 41.07, 271, 669),
        (235, 3, 95.46, 414, 932),
        (236, 5, 58.67, 194, 941),
        (237, 3, 13.94, 70, 695),
        (238, 2, 78.96, 562, 44),
        (239, 4, 52.99, 376, 402),
        (240, 1, 93.57, 539, 127),
        (241, 2, 49.65, 295, 444),
        (242, 5, 48.01, 636, 534),
        (243, 2, 15.44, 710, 106),
        (244, 3, 85.77, 802, 217),
        (245, 3, 20.62, 178, 238),
        (246, 2, 67.19, 611, 188),
        (247, 5, 20.13, 43, 466),
        (248, 5, 67.66, 591, 947),
        (249, 3, 54.81, 669, 86),
        (250, 3, 55.20, 535, 85),
        (251, 4, 69.05, 751, 317),
        (252, 3, 98.78, 200, 485),
        (253, 5, 4.88, 72, 228),
        (254, 2, 65.19, 964, 782),
        (255, 4, 56.62, 135, 314),
        (256, 3, 95.98, 775, 403),
        (257, 4, 9.70, 810, 33),
        (258, 1, 32.10, 404, 972),
        (259, 5, 91.47, 949, 627),
        (260, 3, 12.10, 702, 888),
        (261, 3, 22.48, 912, 616),
        (262, 3, 81.24, 832, 475),
        (263, 2, 78.31, 861, 957),
        (264, 3, 58.66, 590, 379),
        (265, 5, 22.52, 408, 976),
        (266, 2, 89.43, 745, 272),
        (267, 3, 1.66, 877, 102),
        (268, 3, 53.77, 332, 409),
        (269, 4, 86.00, 669, 873),
        (270, 2, 29.37, 634, 217),
        (271, 5, 41.92, 662, 4),
        (272, 4, 44.75, 453, 85),
        (273, 3, 78.20, 891, 408),
        (274, 2, 32.42, 654, 573),
        (275, 4, 46.92, 283, 574),
        (276, 1, 93.22, 119, 633),
        (277, 1, 91.16, 205, 314),
        (278, 2, 13.07, 594, 293),
        (279, 5, 44.57, 506, 160),
        (280, 1, 75.22, 998, 272),
        (281, 3, 37.26, 377, 208),
        (282, 3, 79.95, 382, 675),
        (283, 1, 14.42, 494, 758),
        (284, 1, 2.56, 995, 135),
        (285, 2, 85.77, 612, 269),
        (286, 1, 32.89, 585, 887),
        (287, 5, 92.87, 539, 641),
        (288, 1, 51.78, 20, 859),
        (289, 5, 21.63, 402, 90),
        (290, 2, 85.29, 99, 330),
        (291, 3, 54.96, 847, 707),
        (292, 2, 97.91, 138, 535),
        (293, 3, 59.74, 929, 26),
        (294, 5, 79.94, 280, 774),
        (295, 5, 92.39, 317, 790),
        (296, 4, 24.48, 157, 265),
        (297, 5, 12.57, 565, 744),
        (298, 3, 46.65, 41, 832),
        (299, 3, 42.10, 117, 233),
        (300, 1, 67.61, 411, 343),
        (301, 3, 67.80, 954, 617),
        (302, 1, 56.45, 784, 483),
        (303, 5, 94.66, 637, 172),
        (304, 2, 66.67, 705, 511),
        (305, 1, 13.14, 392, 630),
        (306, 1, 20.78, 7, 382),
        (307, 1, 14.35, 104, 361),
        (308, 2, 17.44, 988, 485),
        (309, 2, 37.76, 949, 830),
        (310, 3, 3.66, 523, 735),
        (311, 5, 55.01, 687, 631),
        (312, 4, 29.60, 304, 437),
        (313, 4, 72.83, 100, 858),
        (314, 1, 73.91, 504, 609),
        (315, 1, 69.94, 418, 112),
        (316, 4, 1.17, 610, 617),
        (317, 4, 14.49, 977, 571),
        (318, 1, 89.92, 618, 762),
        (319, 3, 60.81, 205, 105),
        (320, 2, 41.65, 237, 701),
        (321, 1, 98.77, 792, 323),
        (322, 3, 10.62, 884, 864),
        (323, 2, 14.15, 391, 32),
        (324, 4, 19.66, 110, 860),
        (325, 3, 53.61, 251, 262),
        (326, 2, 25.96, 457, 254),
        (327, 3, 52.80, 160, 370),
        (328, 4, 10.37, 878, 264),
        (329, 3, 11.51, 228, 871),
        (330, 4, 98.41, 757, 336),
        (331, 1, 85.17, 1, 784),
        (332, 5, 24.72, 698, 796),
        (333, 3, 31.66, 951, 999),
        (334, 3, 61.80, 292, 22),
        (335, 4, 44.05, 711, 166),
        (336, 3, 60.34, 6, 148),
        (337, 1, 20.35, 845, 488),
        (338, 2, 8.22, 761, 952),
        (339, 2, 45.12, 960, 738),
        (340, 1, 13.19, 27, 257),
        (341, 2, 69.29, 379, 439),
        (342, 3, 70.86, 174, 737),
        (343, 3, 16.15, 66, 319),
        (344, 4, 10.17, 320, 972),
        (345, 4, 76.48, 24, 95),
        (346, 5, 71.74, 18, 440),
        (347, 5, 25.49, 724, 677),
        (348, 1, 98.80, 654, 560),
        (349, 5, 67.89, 20, 179),
        (350, 4, 52.49, 686, 563),
        (351, 3, 24.18, 983, 633),
        (352, 1, 46.92, 948, 672),
        (353, 1, 82.13, 426, 810),
        (354, 2, 57.08, 860, 688),
        (355, 2, 89.13, 104, 365),
        (356, 4, 77.59, 54, 488),
        (357, 5, 74.99, 240, 433),
        (358, 3, 29.31, 458, 811),
        (359, 2, 56.30, 97, 513),
        (360, 4, 47.82, 951, 738),
        (361, 1, 74.91, 143, 745),
        (362, 1, 58.78, 579, 790),
        (363, 3, 19.14, 634, 6),
        (364, 1, 22.71, 429, 717),
        (365, 3, 43.41, 314, 321),
        (366, 1, 62.43, 635, 252),
        (367, 5, 87.20, 805, 33),
        (368, 2, 17.84, 672, 854),
        (369, 3, 19.53, 132, 211),
        (370, 1, 4.09, 325, 128),
        (371, 4, 50.36, 702, 366),
        (372, 4, 11.97, 407, 349),
        (373, 2, 4.57, 748, 845),
        (374, 2, 49.40, 461, 74),
        (375, 4, 84.20, 60, 264),
        (376, 1, 60.03, 66, 703),
        (377, 5, 55.87, 133, 711),
        (378, 3, 51.08, 945, 348),
        (379, 3, 21.50, 526, 186),
        (380, 2, 30.38, 792, 772),
        (381, 1, 41.55, 620, 363),
        (382, 4, 13.60, 546, 512),
        (383, 1, 21.66, 663, 773),
        (384, 4, 10.91, 709, 661),
        (385, 3, 38.65, 922, 500),
        (386, 5, 42.43, 685, 438),
        (387, 2, 78.61, 889, 616),
        (388, 4, 32.73, 973, 139),
        (389, 1, 10.72, 47, 345),
        (390, 2, 66.12, 187, 113),
        (391, 2, 26.23, 65, 318),
        (392, 2, 15.46, 497, 393),
        (393, 4, 12.35, 579, 925),
        (394, 1, 17.72, 892, 750),
        (395, 4, 5.22, 11, 852),
        (396, 4, 97.47, 989, 481),
        (397, 3, 66.97, 993, 927),
        (398, 1, 37.79, 907, 209),
        (399, 1, 98.32, 252, 238),
        (400, 4, 99.20, 324, 507),
        (401, 4, 65.18, 233, 109),
        (402, 3, 71.99, 253, 108),
        (403, 5, 12.87, 511, 196),
        (404, 5, 44.37, 607, 738),
        (405, 2, 77.66, 201, 390),
        (406, 1, 49.41, 54, 599),
        (407, 3, 21.81, 921, 192),
        (408, 1, 80.35, 525, 34),
        (409, 1, 68.71, 871, 508),
        (410, 5, 95.71, 771, 685),
        (411, 3, 62.15, 113, 902),
        (412, 4, 19.79, 839, 25),
        (413, 2, 67.95, 84, 116),
        (414, 4, 12.44, 895, 305),
        (415, 1, 30.41, 999, 11),
        (416, 3, 3.55, 274, 673),
        (417, 1, 43.03, 173, 958),
        (418, 1, 54.39, 813, 601),
        (419, 2, 53.00, 745, 810),
        (420, 2, 99.68, 903, 638),
        (421, 5, 68.36, 607, 927),
        (422, 2, 68.20, 536, 751),
        (423, 4, 12.22, 305, 448),
        (424, 2, 30.14, 820, 111),
        (425, 3, 57.51, 985, 830),
        (426, 4, 40.13, 708, 138),
        (427, 1, 34.49, 961, 401),
        (428, 2, 18.18, 276, 250),
        (429, 5, 16.53, 791, 515),
        (430, 2, 35.98, 594, 802),
        (431, 2, 22.94, 426, 962),
        (432, 4, 26.80, 976, 78),
        (433, 4, 72.68, 480, 199),
        (434, 3, 30.56, 538, 252),
        (435, 2, 36.02, 547, 774),
        (436, 3, 79.20, 738, 306),
        (437, 3, 3.42, 382, 507),
        (438, 5, 70.30, 234, 354),
        (439, 3, 60.68, 140, 237),
        (440, 4, 3.15, 489, 405),
        (441, 2, 70.44, 593, 579),
        (442, 2, 98.35, 288, 133),
        (443, 5, 60.11, 739, 584),
        (444, 3, 35.18, 528, 4),
        (445, 3, 76.59, 584, 208),
        (446, 4, 29.60, 949, 442),
        (447, 2, 9.20, 479, 527),
        (448, 5, 6.95, 655, 513),
        (449, 1, 63.82, 533, 968),
        (450, 4, 97.78, 182, 109),
        (451, 3, 75.12, 960, 484),
        (452, 4, 92.30, 177, 884),
        (453, 1, 1.70, 919, 471),
        (454, 2, 33.47, 781, 782),
        (455, 4, 90.16, 952, 446),
        (456, 3, 59.26, 87, 306),
        (457, 1, 67.52, 99, 575),
        (458, 1, 83.32, 947, 210),
        (459, 5, 40.09, 59, 222),
        (460, 5, 88.73, 382, 603),
        (461, 3, 34.74, 764, 209),
        (462, 2, 23.10, 726, 827),
        (463, 2, 58.05, 621, 143),
        (464, 2, 13.72, 331, 829),
        (465, 3, 45.98, 379, 216),
        (466, 1, 86.74, 264, 310),
        (467, 5, 12.95, 347, 943),
        (468, 2, 18.13, 858, 652),
        (469, 1, 47.92, 75, 316),
        (470, 4, 48.67, 83, 658),
        (471, 4, 43.27, 750, 677),
        (472, 1, 99.58, 982, 648),
        (473, 4, 65.15, 930, 648),
        (474, 3, 66.92, 469, 462),
        (475, 5, 23.74, 316, 983),
        (476, 5, 30.61, 241, 810),
        (477, 2, 28.28, 330, 565),
        (478, 2, 6.23, 399, 182),
        (479, 2, 84.14, 14, 303),
        (480, 1, 81.17, 98, 591),
        (481, 3, 37.08, 357, 194),
        (482, 1, 78.14, 705, 925),
        (483, 3, 46.40, 910, 471),
        (484, 3, 85.31, 634, 499),
        (485, 2, 38.81, 599, 921),
        (486, 5, 40.17, 217, 705),
        (487, 1, 75.90, 645, 874),
        (488, 1, 3.81, 305, 587),
        (489, 2, 89.26, 399, 244),
        (490, 4, 73.51, 414, 578),
        (491, 2, 44.23, 153, 310),
        (492, 5, 96.24, 159, 459),
        (493, 5, 18.04, 726, 202),
        (494, 3, 90.81, 412, 492),
        (495, 1, 53.37, 528, 739),
        (496, 1, 2.85, 197, 830),
        (497, 4, 45.92, 261, 17),
        (498, 4, 24.69, 853, 102),
        (499, 4, 33.30, 993, 82),
        (500, 5, 70.07, 243, 766),
        (501, 1, 2.78, 533, 876),
        (502, 1, 48.30, 889, 66),
        (503, 5, 15.18, 884, 673),
        (504, 2, 36.28, 317, 767),
        (505, 5, 36.59, 211, 12),
        (506, 2, 80.85, 851, 983),
        (507, 1, 1.73, 728, 751),
        (508, 2, 81.26, 900, 657),
        (509, 5, 7.27, 661, 346),
        (510, 2, 43.93, 883, 151),
        (511, 4, 32.10, 598, 12),
        (512, 2, 54.29, 963, 951),
        (513, 1, 84.60, 629, 944),
        (514, 4, 12.52, 623, 698),
        (515, 3, 64.25, 643, 316),
        (516, 2, 89.33, 91, 280),
        (517, 3, 28.85, 338, 602),
        (518, 2, 91.76, 849, 282),
        (519, 2, 52.84, 53, 334),
        (520, 2, 30.54, 382, 231),
        (521, 4, 52.63, 83, 633),
        (522, 1, 82.26, 238, 109),
        (523, 1, 21.81, 877, 532),
        (524, 4, 38.74, 836, 622),
        (525, 5, 42.23, 168, 227),
        (526, 2, 5.30, 743, 185),
        (527, 5, 74.74, 135, 426),
        (528, 1, 72.23, 111, 183),
        (529, 4, 90.11, 756, 880),
        (530, 4, 19.35, 917, 885),
        (531, 3, 82.49, 176, 28),
        (532, 4, 47.45, 141, 913),
        (533, 1, 52.74, 656, 254),
        (534, 3, 92.82, 768, 302),
        (535, 5, 33.34, 558, 203),
        (536, 1, 25.47, 147, 224),
        (537, 2, 53.18, 922, 664),
        (538, 3, 10.20, 269, 756),
        (539, 3, 5.37, 388, 746),
        (540, 2, 94.41, 185, 249),
        (541, 2, 50.94, 898, 329),
        (542, 1, 29.91, 599, 363),
        (543, 1, 92.78, 223, 776),
        (544, 3, 34.98, 414, 361),
        (545, 4, 59.73, 911, 700),
        (546, 4, 23.96, 238, 701),
        (547, 2, 79.67, 140, 813),
        (548, 1, 4.25, 530, 208),
        (549, 4, 22.76, 773, 682),
        (550, 1, 22.18, 78, 869),
        (551, 4, 48.75, 466, 415),
        (552, 5, 27.99, 428, 219),
        (553, 1, 66.00, 566, 362),
        (554, 3, 77.35, 6, 37),
        (555, 1, 6.76, 517, 404),
        (556, 4, 48.83, 464, 673),
        (557, 3, 23.62, 357, 345),
        (558, 3, 81.26, 269, 423),
        (559, 3, 99.46, 120, 729),
        (560, 4, 80.46, 312, 572),
        (561, 1, 29.84, 921, 219),
        (562, 5, 4.27, 977, 271),
        (563, 2, 59.70, 380, 563),
        (564, 4, 25.40, 801, 79),
        (565, 1, 95.58, 728, 809),
        (566, 4, 61.84, 229, 871),
        (567, 3, 7.80, 172, 216),
        (568, 2, 87.48, 805, 226),
        (569, 5, 32.48, 916, 983),
        (570, 2, 27.80, 833, 397),
        (571, 1, 57.11, 318, 893),
        (572, 1, 50.13, 793, 909),
        (573, 3, 34.72, 129, 558),
        (574, 4, 80.30, 701, 461),
        (575, 1, 59.11, 153, 477),
        (576, 3, 2.72, 697, 225),
        (577, 3, 75.12, 656, 398),
        (578, 2, 16.01, 789, 147),
        (579, 3, 37.90, 714, 122),
        (580, 5, 59.93, 159, 982),
        (581, 2, 67.47, 408, 219),
        (582, 1, 45.25, 259, 251),
        (583, 3, 65.64, 137, 915),
        (584, 4, 73.87, 607, 721),
        (585, 2, 66.17, 769, 949),
        (586, 1, 91.47, 526, 643),
        (587, 4, 54.89, 187, 975),
        (588, 4, 72.03, 651, 800),
        (589, 2, 38.84, 871, 914),
        (590, 2, 15.42, 42, 168),
        (591, 2, 77.95, 765, 840),
        (592, 1, 65.33, 817, 573),
        (593, 5, 22.88, 671, 141),
        (594, 2, 90.59, 926, 665),
        (595, 5, 48.60, 29, 984),
        (596, 5, 52.62, 642, 997),
        (597, 2, 60.12, 747, 697),
        (598, 5, 73.14, 184, 136),
        (599, 2, 96.35, 377, 776),
        (600, 2, 77.30, 407, 765),
        (601, 4, 43.92, 234, 560),
        (602, 5, 4.34, 337, 668),
        (603, 5, 61.66, 473, 234),
        (604, 1, 16.02, 766, 475),
        (605, 1, 34.52, 369, 541),
        (606, 2, 64.25, 811, 242),
        (607, 4, 47.63, 623, 206),
        (608, 2, 46.96, 516, 260),
        (609, 3, 23.45, 748, 999),
        (610, 2, 3.99, 589, 797),
        (611, 1, 69.15, 853, 739),
        (612, 4, 60.94, 265, 155),
        (613, 2, 48.23, 822, 611),
        (614, 4, 52.69, 910, 661),
        (615, 5, 73.37, 949, 533),
        (616, 4, 17.86, 953, 20),
        (617, 3, 89.33, 402, 618),
        (618, 1, 59.32, 957, 55),
        (619, 5, 24.28, 15, 685),
        (620, 1, 93.22, 678, 973),
        (621, 4, 74.83, 843, 284),
        (622, 2, 81.84, 361, 720),
        (623, 5, 49.11, 155, 509),
        (624, 3, 94.35, 380, 610),
        (625, 2, 52.55, 975, 608),
        (626, 5, 44.62, 22, 483),
        (627, 3, 69.16, 767, 532),
        (628, 4, 1.13, 972, 958),
        (629, 1, 70.54, 852, 576),
        (630, 5, 82.89, 230, 364),
        (631, 5, 21.79, 644, 54),
        (632, 5, 99.46, 474, 90),
        (633, 1, 33.59, 652, 880),
        (634, 5, 86.95, 602, 860),
        (635, 4, 59.10, 389, 666),
        (636, 2, 80.21, 222, 209),
        (637, 1, 77.79, 483, 305),
        (638, 1, 99.34, 466, 685),
        (639, 4, 73.29, 520, 838),
        (640, 5, 5.78, 867, 929),
        (641, 3, 2.38, 42, 303),
        (642, 5, 93.23, 518, 453),
        (643, 1, 71.21, 513, 780),
        (644, 2, 45.74, 564, 944),
        (645, 5, 10.87, 714, 832),
        (646, 3, 65.85, 629, 717),
        (647, 2, 56.31, 940, 854),
        (648, 2, 48.40, 911, 125),
        (649, 2, 8.50, 817, 636),
        (650, 2, 30.68, 850, 906),
        (651, 2, 61.42, 454, 275),
        (652, 5, 43.10, 525, 634),
        (653, 1, 72.96, 201, 826),
        (654, 1, 91.96, 258, 506),
        (655, 3, 41.48, 515, 865),
        (656, 1, 94.72, 970, 231),
        (657, 3, 30.36, 444, 219),
        (658, 5, 55.64, 706, 517),
        (659, 1, 33.74, 167, 34),
        (660, 4, 20.72, 879, 327),
        (661, 4, 23.19, 6, 673),
        (662, 3, 33.13, 273, 836),
        (663, 1, 50.22, 683, 57),
        (664, 2, 50.27, 689, 607),
        (665, 1, 91.52, 749, 684),
        (666, 3, 58.67, 811, 725),
        (667, 3, 16.64, 876, 155),
        (668, 4, 50.42, 115, 717),
        (669, 1, 14.03, 742, 578),
        (670, 5, 28.88, 171, 376),
        (671, 2, 45.59, 389, 904),
        (672, 4, 73.59, 498, 154),
        (673, 4, 21.88, 632, 205),
        (674, 2, 61.49, 940, 956),
        (675, 1, 60.77, 109, 740),
        (676, 1, 95.00, 40, 21),
        (677, 3, 30.57, 48, 487),
        (678, 1, 62.60, 637, 883),
        (679, 3, 90.81, 845, 773),
        (680, 5, 65.14, 322, 147),
        (681, 2, 14.78, 567, 734),
        (682, 4, 11.01, 193, 968),
        (683, 4, 32.43, 364, 527),
        (684, 5, 91.93, 787, 10),
        (685, 5, 32.72, 456, 997),
        (686, 3, 75.69, 267, 229),
        (687, 5, 16.83, 228, 743),
        (688, 4, 33.70, 201, 548),
        (689, 3, 46.25, 827, 296),
        (690, 2, 27.78, 942, 223),
        (691, 5, 55.98, 953, 367),
        (692, 1, 84.63, 777, 14),
        (693, 2, 11.61, 490, 862),
        (694, 3, 80.25, 378, 176),
        (695, 4, 56.10, 904, 97),
        (696, 3, 76.66, 629, 828),
        (697, 3, 71.20, 308, 498),
        (698, 3, 59.87, 565, 226),
        (699, 2, 7.55, 411, 722),
        (700, 5, 95.88, 555, 585),
        (701, 3, 61.66, 585, 135),
        (702, 1, 99.52, 627, 789),
        (703, 1, 62.86, 153, 46),
        (704, 2, 52.49, 593, 418),
        (705, 3, 48.88, 310, 963),
        (706, 3, 91.47, 42, 161),
        (707, 4, 42.05, 561, 761),
        (708, 2, 32.71, 138, 423),
        (709, 5, 94.70, 515, 900),
        (710, 1, 75.69, 840, 214),
        (711, 4, 4.77, 453, 644),
        (712, 3, 26.40, 385, 881),
        (713, 5, 19.64, 293, 180),
        (714, 4, 6.03, 285, 874),
        (715, 3, 3.24, 773, 805),
        (716, 3, 93.86, 849, 133),
        (717, 2, 34.68, 855, 338),
        (718, 2, 65.56, 403, 578),
        (719, 1, 36.67, 67, 332),
        (720, 5, 79.43, 92, 683),
        (721, 5, 72.94, 189, 128),
        (722, 1, 8.21, 587, 478),
        (723, 2, 25.67, 788, 394),
        (724, 3, 35.74, 897, 628),
        (725, 2, 64.83, 150, 973),
        (726, 2, 96.80, 574, 213),
        (727, 4, 43.77, 817, 91),
        (728, 2, 9.58, 815, 572),
        (729, 5, 29.56, 923, 673),
        (730, 4, 44.85, 725, 649),
        (731, 2, 1.94, 465, 108),
        (732, 4, 88.62, 637, 795),
        (733, 2, 46.74, 159, 491),
        (734, 5, 22.55, 828, 429),
        (735, 2, 61.22, 425, 839),
        (736, 4, 80.13, 784, 326),
        (737, 3, 40.60, 451, 491),
        (738, 2, 93.53, 850, 507),
        (739, 5, 40.20, 723, 781),
        (740, 3, 4.97, 514, 909),
        (741, 1, 79.83, 66, 883),
        (742, 3, 18.86, 911, 906),
        (743, 5, 23.74, 963, 476),
        (744, 2, 88.81, 984, 740),
        (745, 1, 1.27, 282, 685),
        (746, 3, 6.41, 227, 846),
        (747, 3, 87.89, 35, 413),
        (748, 4, 74.50, 307, 971),
        (749, 5, 66.06, 703, 693),
        (750, 4, 5.38, 180, 248),
        (751, 3, 51.37, 508, 270),
        (752, 1, 93.93, 891, 352),
        (753, 4, 69.75, 5, 117),
        (754, 3, 29.93, 619, 5),
        (755, 3, 66.94, 192, 305),
        (756, 2, 24.96, 102, 409),
        (757, 4, 10.73, 35, 181),
        (758, 3, 42.13, 95, 976),
        (759, 3, 96.64, 456, 301),
        (760, 5, 18.69, 18, 696),
        (761, 1, 58.57, 367, 770),
        (762, 2, 94.58, 502, 762),
        (763, 1, 90.78, 311, 359),
        (764, 4, 61.56, 586, 532),
        (765, 2, 46.87, 507, 1),
        (766, 2, 95.54, 222, 931),
        (767, 4, 17.23, 110, 777),
        (768, 5, 64.21, 702, 40),
        (769, 3, 56.89, 205, 626),
        (770, 2, 48.71, 551, 956),
        (771, 1, 55.20, 768, 621),
        (772, 2, 83.19, 70, 35),
        (773, 4, 64.33, 22, 894),
        (774, 4, 3.27, 984, 360),
        (775, 3, 1.98, 343, 642),
        (776, 5, 30.64, 557, 269),
        (777, 2, 68.27, 813, 169),
        (778, 3, 55.78, 187, 964),
        (779, 2, 62.43, 712, 769),
        (780, 5, 26.09, 610, 997),
        (781, 4, 27.58, 707, 553),
        (782, 4, 59.89, 170, 467),
        (783, 5, 78.19, 189, 503),
        (784, 5, 89.60, 374, 994),
        (785, 3, 86.92, 260, 432),
        (786, 4, 85.12, 596, 688),
        (787, 5, 84.21, 672, 673),
        (788, 4, 37.15, 772, 678),
        (789, 2, 95.11, 241, 86),
        (790, 2, 59.69, 951, 467),
        (791, 2, 34.36, 47, 98),
        (792, 4, 31.12, 150, 713),
        (793, 5, 65.94, 434, 341),
        (794, 5, 97.54, 369, 224),
        (795, 1, 33.21, 427, 858),
        (796, 3, 62.24, 779, 235),
        (797, 3, 86.85, 592, 373),
        (798, 2, 31.12, 773, 711),
        (799, 5, 80.33, 376, 241),
        (800, 1, 31.14, 509, 472),
        (801, 4, 74.07, 209, 758),
        (802, 2, 79.86, 814, 913),
        (803, 4, 91.86, 884, 19),
        (804, 1, 98.80, 685, 723),
        (805, 2, 24.08, 225, 624),
        (806, 5, 69.41, 846, 34),
        (807, 3, 11.78, 141, 555),
        (808, 3, 24.35, 674, 137),
        (809, 5, 59.01, 652, 309),
        (810, 1, 11.14, 573, 701),
        (811, 5, 63.82, 769, 577),
        (812, 5, 38.68, 528, 850),
        (813, 2, 61.60, 29, 306),
        (814, 3, 33.75, 122, 814),
        (815, 4, 59.84, 814, 181),
        (816, 1, 26.19, 249, 31),
        (817, 5, 26.10, 976, 144),
        (818, 4, 66.48, 669, 74),
        (819, 1, 76.74, 9, 286),
        (820, 5, 19.22, 880, 173),
        (821, 3, 71.37, 423, 534),
        (822, 2, 12.91, 343, 446),
        (823, 4, 42.58, 121, 769),
        (824, 5, 6.18, 603, 668),
        (825, 1, 83.75, 294, 127),
        (826, 3, 48.65, 810, 489),
        (827, 1, 7.48, 210, 256),
        (828, 3, 79.41, 505, 52),
        (829, 3, 26.25, 866, 990),
        (830, 5, 75.12, 183, 883),
        (831, 2, 38.81, 429, 452),
        (832, 1, 57.39, 335, 139),
        (833, 5, 70.75, 512, 638),
        (834, 3, 63.14, 202, 33),
        (835, 3, 53.58, 322, 355),
        (836, 2, 65.74, 990, 81),
        (837, 5, 1.73, 104, 723),
        (838, 4, 25.36, 742, 196),
        (839, 5, 18.30, 342, 818),
        (840, 1, 60.44, 632, 578),
        (841, 3, 67.78, 539, 625),
        (842, 4, 64.43, 589, 541),
        (843, 4, 70.21, 358, 523),
        (844, 1, 92.91, 739, 829),
        (845, 2, 51.87, 512, 721),
        (846, 2, 29.24, 547, 13),
        (847, 4, 45.85, 401, 201),
        (848, 3, 12.29, 297, 34),
        (849, 4, 86.42, 1, 458),
        (850, 5, 52.21, 312, 483),
        (851, 2, 50.23, 91, 461),
        (852, 4, 47.38, 719, 251),
        (853, 5, 41.76, 997, 864),
        (854, 3, 30.80, 498, 898),
        (855, 3, 38.66, 710, 78),
        (856, 2, 27.21, 705, 518),
        (857, 5, 65.06, 345, 909),
        (858, 4, 46.93, 31, 678),
        (859, 2, 61.24, 297, 119),
        (860, 3, 19.84, 792, 420),
        (861, 5, 90.37, 418, 956),
        (862, 5, 32.91, 68, 286),
        (863, 4, 28.63, 5, 91),
        (864, 3, 92.32, 561, 397),
        (865, 2, 57.77, 124, 141),
        (866, 1, 18.36, 581, 361),
        (867, 1, 44.81, 675, 261),
        (868, 3, 3.53, 403, 633),
        (869, 4, 70.50, 847, 359),
        (870, 4, 50.10, 1000, 444),
        (871, 2, 69.20, 281, 149),
        (872, 2, 55.65, 574, 628),
        (873, 2, 23.80, 125, 665),
        (874, 3, 43.83, 656, 220),
        (875, 1, 60.28, 622, 184),
        (876, 2, 91.71, 735, 622),
        (877, 2, 79.95, 905, 257),
        (878, 4, 91.10, 312, 365),
        (879, 5, 71.48, 158, 428),
        (880, 3, 36.39, 838, 251),
        (881, 1, 76.92, 273, 373),
        (882, 2, 94.04, 332, 845),
        (883, 5, 54.42, 449, 391),
        (884, 3, 48.40, 854, 212),
        (885, 4, 78.06, 554, 565),
        (886, 1, 6.97, 511, 77),
        (887, 2, 82.69, 148, 349),
        (888, 1, 5.13, 871, 166),
        (889, 2, 59.00, 367, 958),
        (890, 5, 36.10, 219, 250),
        (891, 5, 10.75, 750, 942),
        (892, 2, 65.79, 829, 388),
        (893, 4, 71.46, 839, 201),
        (894, 5, 12.54, 426, 396),
        (895, 2, 53.78, 466, 451),
        (896, 5, 75.67, 824, 515),
        (897, 1, 76.85, 426, 470),
        (898, 2, 73.88, 134, 877),
        (899, 1, 11.59, 959, 375),
        (900, 4, 41.19, 560, 350),
        (901, 5, 74.72, 98, 508),
        (902, 3, 82.55, 911, 34),
        (903, 2, 74.48, 660, 419),
        (904, 3, 29.60, 816, 793),
        (905, 2, 54.50, 346, 233),
        (906, 5, 23.00, 45, 391),
        (907, 1, 31.00, 274, 799),
        (908, 1, 79.85, 134, 725),
        (909, 4, 31.08, 987, 705),
        (910, 1, 13.14, 285, 280),
        (911, 3, 37.07, 575, 657),
        (912, 4, 88.56, 899, 824),
        (913, 1, 89.26, 587, 548),
        (914, 1, 69.21, 585, 179),
        (915, 1, 97.31, 144, 398),
        (916, 4, 28.56, 805, 838),
        (917, 3, 33.91, 976, 497),
        (918, 1, 55.28, 309, 44),
        (919, 4, 48.52, 828, 760),
        (920, 1, 38.28, 415, 762),
        (921, 1, 19.11, 747, 479),
        (922, 3, 85.39, 271, 117),
        (923, 1, 26.44, 379, 978),
        (924, 2, 5.40, 964, 126),
        (925, 2, 67.20, 261, 49),
        (926, 3, 37.31, 235, 918),
        (927, 5, 90.75, 563, 616),
        (928, 1, 44.57, 32, 587),
        (929, 3, 11.96, 475, 622),
        (930, 4, 27.86, 336, 559),
        (931, 4, 13.49, 208, 726),
        (932, 3, 99.60, 750, 779),
        (933, 4, 96.27, 931, 464),
        (934, 4, 17.62, 413, 669),
        (935, 3, 20.75, 7, 348),
        (936, 2, 74.03, 104, 97),
        (937, 4, 45.25, 202, 501),
        (938, 3, 23.45, 283, 333),
        (939, 3, 65.77, 709, 884),
        (940, 1, 58.70, 342, 424),
        (941, 3, 17.79, 337, 964),
        (942, 2, 62.48, 323, 624),
        (943, 4, 55.22, 171, 874),
        (944, 1, 83.97, 198, 651),
        (945, 4, 47.03, 723, 604),
        (946, 2, 59.71, 542, 964),
        (947, 5, 43.68, 14, 139),
        (948, 2, 48.13, 939, 251),
        (949, 3, 89.79, 392, 149),
        (950, 1, 68.68, 560, 59),
        (951, 2, 72.70, 466, 808),
        (952, 5, 69.60, 617, 520),
        (953, 2, 5.82, 640, 124),
        (954, 5, 83.05, 51, 371),
        (955, 2, 29.78, 256, 868),
        (956, 3, 51.14, 342, 370),
        (957, 2, 15.53, 186, 550),
        (958, 5, 57.78, 226, 374),
        (959, 5, 33.31, 121, 126),
        (960, 1, 83.93, 71, 971),
        (961, 3, 5.54, 625, 196),
        (962, 5, 90.46, 453, 140),
        (963, 5, 7.33, 526, 664),
        (964, 3, 19.62, 601, 486),
        (965, 4, 5.57, 541, 282),
        (966, 2, 9.29, 692, 68),
        (967, 4, 77.58, 218, 799),
        (968, 3, 49.38, 352, 623),
        (969, 1, 83.33, 574, 947),
        (970, 3, 38.20, 470, 687),
        (971, 2, 85.19, 150, 425),
        (972, 4, 57.68, 296, 762),
        (973, 1, 31.40, 151, 839),
        (974, 3, 26.19, 424, 815),
        (975, 3, 68.24, 926, 315),
        (976, 1, 95.18, 28, 152),
        (977, 5, 14.53, 546, 616),
        (978, 3, 90.20, 144, 288),
        (979, 1, 44.87, 945, 56),
        (980, 4, 67.84, 665, 480),
        (981, 3, 53.60, 365, 72),
        (982, 4, 15.69, 328, 718),
        (983, 2, 76.83, 264, 384),
        (984, 2, 80.10, 624, 642),
        (985, 4, 35.11, 505, 943),
        (986, 2, 97.23, 661, 179),
        (987, 4, 23.62, 852, 144),
        (988, 2, 15.25, 660, 111),
        (989, 5, 49.74, 509, 578),
        (990, 2, 10.72, 438, 994),
        (991, 5, 15.92, 543, 389),
        (992, 4, 97.33, 994, 718),
        (993, 5, 74.56, 437, 327),
        (994, 1, 69.70, 864, 529),
        (995, 3, 37.04, 930, 179),
        (996, 3, 44.45, 929, 57),
        (997, 4, 29.10, 589, 867),
        (998, 4, 80.82, 725, 25),
        (999, 5, 99.80, 573, 834),
        (1000, 4, 93.80, 380, 188);                  
""", """
delete from store_orderitem
"""
                          )
    ]
