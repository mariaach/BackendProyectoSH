-- ProyectoFundacionSH.mascotas_mascota definition

CREATE TABLE `mascotas_mascota` (
  `id_masc` int NOT NULL AUTO_INCREMENT,
  `nombre_masc` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `especie` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `raza` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `edad_masc` int unsigned NOT NULL,
  `estado` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  `foto_masc` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_masc`),
  CONSTRAINT `mascotas_mascota_chk_1` CHECK ((`edad_masc` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
