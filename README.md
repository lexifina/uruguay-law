# Uruguay: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Uruguay's national law, which global-law reads at `uruguay/national/acts/`.

The law of Uruguay as a git history: one file per provision, one commit per law (or plebiscite) on the day it took effect, and the law that made each change as the commit's author. `git blame` names the reform behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `uy/`.

*En español: [más abajo](#en-español).*

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución de la República Oriental del Uruguay (1967) | 5 | From its entry into force (15 February 1967) through the reforms approved by plebiscite in 1989, 1994, 1996 and 2004, to today |
| `codigo-civil/` | Código Civil, as approved by Ley Nº 16.603 (1994) | 19 | From the re-edition approved by Ley 16.603 (in force 1 December 1994) through 20 amending laws (Leyes 16.719 to 20.446), to today. The code of 1868 and its changes before 1994 are not included |
| `codigo-penal/` | Código Penal (Ley Nº 9.155 of 1933) | 36 | As enacted (in force 1 August 1934, Ley 9.414 art. 2), then 47 amending laws from Ley 13.737 (1969) to Ley 20.353 (2024), to today. IMPO records no amendment between 1934 and 1969 (see below) |
| `ley-18331/` | Ley Nº 18.331 de Protección de Datos Personales (2008) | 7 | As enacted (in force 28 August 2008), then every amending law IMPO names: Leyes 18.719, 18.996, 19.355, 19.670, 19.924 and 20.075, to today |
| `codigo-general-proceso/` | Código General del Proceso (Ley Nº 15.982 of 1988) | 29 | From its entry into force (20 November 1989, art. 547), with Ley 16.053's earlier changes, through 36 amending laws to today; on the `futuro` branch, Ley 20.531's new arts. 64 and 64 BIS from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `codigo-comercio/` | Código de Comercio (1865) | 14 | The 1865 code as IMPO gives it, dated 24 January 1866 (Ley 841), through 15 amending laws and decree-laws to today; Libro IV (quiebras) reads a placeholder from 1879, as no source gives its 1878 and 1900 texts |
| `codigo-proceso-penal/` | Código del Proceso Penal (Ley Nº 19.293 of 2014) | 12 | From its entry into force (1 November 2017, art. 403), with the laws that changed it before that day, through 12 amending laws to today |
| `codigo-tributario/` | Código Tributario (Decreto-Ley Nº 14.306 of 1974) | 10 | As enacted (in force 16 December 1974), then 13 amending decree-laws and laws from Decreto-Ley 14.416 (1975) to Ley 20.446 (2025), to today |
| `ley-16060/` | Ley Nº 16.060 de Sociedades Comerciales (1989) | 21 | As enacted (in force 31 December 1989, art. 511), then 21 amending laws from Ley 16.296 (1992) to Ley 19.924 (2020), to today |
| `ley-17250/` | Ley Nº 17.250 de Relaciones de Consumo (2000) | 8 | As enacted (in force 27 August 2000), then Leyes 18.046, 18.362, 19.149, 19.355, 19.924 and 20.212, to today; on the `futuro` branch, Ley 20.531's new art. 16 and its changes to art. 42 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `codigo-ninez-adolescencia/` | Código de la Niñez y la Adolescencia (Ley Nº 17.823 of 2004) | 22 | As enacted (in force 24 September 2004), then 24 amending laws from Ley 17.930 (2005) to Ley 20.266 (2024), to today. Articles added inside a chapter are `art-132-1.md` (Artículo 132.1) |
| `codigo-aduanero/` | Código Aduanero (CAROU, Ley Nº 19.276 of 2014) | 9 | As enacted (in force 18 March 2015, art. 276), then 6 amending laws to today, and two wording-unchanged commits for Leyes 19.322 and 19.394, which suspended arts. 224 to 257 and 269 until 16 July 2017 |
| `ley-18381/` | Ley Nº 18.381 de Acceso a la Información Pública (2008) | 4 | As enacted (in force 17 November 2008), then Leyes 18.719, 19.178 and 19.996, to today |
| `ley-17514/` | Ley Nº 17.514 de Violencia Doméstica (2002) | 3 | As enacted (in force 19 July 2002), then Leyes 19.580 and 19.670, to today |
| `ley-19580/` | Ley Nº 19.580 de Violencia hacia las Mujeres Basada en Género (2017) | 7 | As enacted (in force 19 January 2018), then 5 amending laws from Ley 19.670 (2018) to Ley 20.446 (2025), to today |
| `ley-19574/` | Ley Nº 19.574 Integral contra el Lavado de Activos (2017) | 8 | As enacted (in force 20 January 2018), then 8 amending laws from Ley 19.670 (2018) to Ley 20.469 (2026), to today |
| `codigo-mineria/` | Código de Minería (Decreto-Ley Nº 15.242 of 1982) | 13 | As enacted (in force 1 April 1982, art. 135), then 13 amending decree-laws and laws from Decreto-Ley 15.516 (1984) to Ley 20.446 (2025), to today |
| `codigo-rural/` | Código Rural (Ley Nº 10.024 of 1941) | 13 | As enacted (in force 14 June 1942, art. 291), then 13 amending decree-laws and laws from Decreto-Ley 10.386 (1943) to Ley 20.212 (2023), to today |
| `ley-18159/` | Ley de Defensa de la Libre Competencia en el Comercio (Ley Nº 18.159 of 2007) | 6 | As enacted (in force 9 August 2007), then 6 amending laws from Ley 19.355 (2015) to Ley 20.446 (2025), to today |
| `ley-17011/` | Ley de Marcas (Ley Nº 17.011 of 1998) | 9 | As enacted (in force 17 October 1998), then 8 amending laws from Ley 17.930 (2005) to Ley 20.212 (2023), to today |
| `ley-17164/` | Ley de Patentes (Ley Nº 17.164 of 1999) | 6 | As enacted (in force 18 January 2000), then 5 amending laws from Ley 18.172 (2007) to Ley 20.446 (2025), to today |
| `ley-18600/` | Ley de Documento Electrónico y Firma Electrónica (Ley Nº 18.600 of 2009) | 4 | As enacted (in force 15 November 2009), then Ley 18.996, Ley 19.355, Ley 19.535, to today |
| `ley-18250/` | Ley de Migraciones (Ley Nº 18.250 of 2008) | 10 | As enacted (in force 27 January 2008), then 8 amending laws from Ley 18.996 (2012) to Ley 20.446 (2025), to today |
| `ley-18246/` | Ley de Unión Concubinaria (Ley Nº 18.246 of 2007) | 3 | As enacted (in force 20 January 2008), then Ley 20.130, Ley 20.212, to today |
| `ley-18987/` | Ley de Interrupción Voluntaria del Embarazo (Ley Nº 18.987 of 2012) | 1 | As enacted (in force 9 November 2012), with no amendment recorded by IMPO, to today |
| `ley-19172/` | Ley de Regulación y Control del Cannabis (Ley Nº 19.172 of 2013) | 4 | As enacted (in force 17 January 2014), then Ley 19.355, Ley 19.845, Ley 19.924, to today |
| `ley-18211/` | Ley de Creación del Sistema Nacional Integrado de Salud (Ley Nº 18.211 of 2007) | 9 | As enacted (in force 1 January 2008), then 8 amending laws from Ley 18.731 (2011) to Ley 20.446 (2025), to today |
| `ley-18437/` | Ley General de Educación (Ley Nº 18.437 of 2008) | 13 | As enacted (in force 26 January 2009), then 12 amending laws from Ley 18.869 (2011) to Ley 20.446 (2025), to today |
| `ley-18308/` | Ley de Ordenamiento Territorial y Desarrollo Sostenible (Ley Nº 18.308 of 2008) | 8 | As enacted (in force 10 July 2008), then 8 amending laws from Ley 18.719 (2010) to Ley 20.446 (2025), to today |
| `ley-17283/` | Ley de Protección del Medio Ambiente (Ley Nº 17.283 of 2000) | 4 | As enacted (in force 22 December 2000), then 4 amending laws from Ley 19.355 (2015) to Ley 19.996 (2021), to today |
| `ley-18651/` | Ley de Protección Integral de Personas con Discapacidad (Ley Nº 18.651 of 2010) | 7 | As enacted (in force 19 March 2010), then 7 amending laws from Ley 18.719 (2010) to Ley 20.454 (2025), to today |
| `ley-18566/` | Ley de Negociación Colectiva (Ley Nº 18.566 of 2009) | 3 | As enacted (in force 10 October 2009), then Ley 19.027, Ley 20.145, to today |
| `ley-18387/` | Ley de Declaración Judicial del Concurso y Reorganización Empresarial (Ley Nº 18.387 of 2008) | 6 | As enacted (in force 13 November 2008, ten days after publication; its own clause gives 2 November 2008, before its publication), then 6 amending laws from Ley 18.411 (2008) to Ley 20.404 (2025), to today |
| `ley-17703/` | Ley de Fideicomiso (Ley Nº 17.703 of 2003) | 3 | As enacted (in force 26 November 2003), then Ley 18.673, Ley 20.446, to today |
| `ley-16871/` | Ley de Registros Públicos (Ley Nº 16.871 of 1997) | 11 | As enacted (in force 20 October 1997), then 12 amending laws from Ley 17.296 (2001) to Ley 20.446 (2025), to today |
| `ley-18627/` | Ley de Mercado de Valores (Ley Nº 18.627 of 2009) | 6 | As enacted (in force 26 December 2009), then 5 amending laws from Ley 18.719 (2010) to Ley 20.345 (2024), to today |
| `ley-19210/` | Ley de Inclusión Financiera (Ley Nº 19.210 of 2014) | 13 | As enacted (in force 19 May 2014), then 13 amending laws from Ley 19.228 (2014) to Ley 20.469 (2026), to today |
| `ley-18212/` | Ley de Tasas de Interés y Usura (Ley Nº 18.212 of 2007) | 4 | As enacted (in force 29 December 2007), then Ley 19.210, Ley 19.732, Ley 20.446, to today |
| `ley-18099/` | Ley de Responsabilidad Solidaria y Seguros por Accidentes de Trabajo (Ley Nº 18.099 of 2007) | 2 | As enacted (in force 17 February 2007), then Ley 18.251, to today |
| `ley-18065/` | Ley de Trabajo Doméstico (Ley Nº 18.065 of 2006) | 1 | As enacted (in force 15 December 2006), with no amendment recorded by IMPO, to today |
| `ley-16074/` | Ley de Seguros sobre Accidentes de Trabajo y Enfermedades Profesionales (Ley Nº 16.074 of 1989) | 7 | As enacted (in force 17 April 1990), then 6 amending laws from Ley 16.134 (1990) to Ley 20.396 (2025), to today |
| `ley-19121/` | Estatuto del Funcionario Público de la Administración Central (Ley Nº 19.121 of 2013) | 9 | As enacted (in force 7 September 2013), then 8 amending laws from Ley 19.355 (2015) to Ley 20.312 (2024), to today |
| `ley-17060/` | Ley Cristal: Funcionarios Públicos (Ley Nº 17.060 of 1998) | 8 | As enacted (in force 18 January 1999), then 10 amending laws from Ley 17.296 (2001) to Ley 20.292 (2024), to today |
| `ley-18335/` | Ley de Derechos y Obligaciones de Pacientes y Usuarios de los Servicios de Salud (Ley Nº 18.335 of 2008) | 4 | As enacted (in force 5 September 2008), then 4 amending laws from Ley 18.362 (2008) to Ley 20.431 (2025), to today |
| `ley-19684/` | Ley Integral para Personas Trans (Ley Nº 19.684 of 2018) | 2 | As enacted (in force 17 November 2018), then Ley 20.212, to today |
| `ley-19161/` | Ley de Subsidios por Maternidad, Paternidad y Cuidado del Recién Nacido (Ley Nº 19.161 of 2013) | 4 | As enacted (in force 25 November 2013), then Ley 20.000, Ley 20.312, Ley 20.364, to today |
| `ley-18384/` | Estatuto del Artista y Oficios Conexos (Ley Nº 18.384 of 2008) | 2 | As enacted (in force 10 November 2008), then Ley 20.212, to today |
| `ley-17940/` | Ley de Libertad Sindical (Ley Nº 17.940 of 2006) | 1 | As enacted (in force 20 January 2006, ten days after publication; its own clause gives 2 January 2006, before its publication), with no amendment recorded by IMPO, to today |
| `ley-18561/` | Ley de Acoso Sexual (Ley Nº 18.561 of 2009) | 1 | As enacted (in force 1 October 2009), with no amendment recorded by IMPO, to today |
| `ley-18345/` | Ley de Licencias Especiales (Ley Nº 18.345 of 2008) | 4 | As enacted (in force 3 October 2008), then Ley 18.458, Ley 19.729, Ley 19.924, to today |
| `ley-18441/` | Ley de Jornada Laboral y Régimen de Descansos en el Sector Rural (Ley Nº 18.441 of 2008) | 1 | As enacted (in force 2 February 2009), with no amendment recorded by IMPO, to today |
| `ley-16045/` | Ley de Igualdad de Trato y Oportunidades en la Actividad Laboral (Ley Nº 16.045 of 1989) | 1 | As enacted (in force 25 June 1989), with no amendment recorded by IMPO, to today |
| `ley-19307/` | Ley de Servicios de Comunicación Audiovisual (Ley Nº 19.307 of 2014) | 4 | As enacted (in force 24 January 2015), then Ley 19.670, Ley 19.834, Ley 20.075, to today |
| `ley-17234/` | Ley del Sistema Nacional de Áreas Naturales Protegidas (Ley Nº 17.234 of 2000) | 7 | As enacted (in force 19 March 2000), then 6 amending laws from Ley 17.930 (2005) to Ley 20.446 (2025), to today |
| `ley-18610/` | Ley de Política Nacional de Aguas (Ley Nº 18.610 of 2009) | 2 | As enacted (in force 7 November 2009), then Ley 20.075, to today |
| `ley-19829/` | Ley de Gestión Integral de Residuos (Ley Nº 19.829 of 2019) | 1 | As enacted (in force 10 October 2019), with no amendment recorded by IMPO, to today |
| `ley-18315/` | Ley de Procedimiento Policial (Ley Nº 18.315 of 2008) | 2 | As enacted (in force 1 August 2008), then Ley 19.889, to today |
| `ley-19315/` | Ley Orgánica Policial (Ley Nº 19.315 of 2015) | 11 | From its entry into force (1 January 2016), with the changes Ley 19.355 made by that day, then 9 amending laws from Ley 19.438 (2016) to Ley 20.446 (2025), to today |
| `ley-17897/` | Ley de Humanización y Modernización del Sistema Carcelario (Ley Nº 17.897 of 2005) | 5 | As enacted (in force 29 September 2005, ten days after publication; its own clause gives 14 September 2005, before its publication), then 4 amending laws from Ley 18.172 (2007) to Ley 20.446 (2025), to today |
| `ley-15750/` | Ley Orgánica de la Judicatura y de Organización de los Tribunales (Ley Nº 15.750 of 1985) | 15 | As enacted (in force 18 July 1985, ten days after publication; its own clause gives 24 June 1985, before its publication), then 15 amending laws from Ley 15.860 (1987) to Ley 19.996 (2021), to today |
| `ley-18508/` | Ley de Negociación Colectiva en el Marco de las Relaciones Laborales en el Sector Público (Ley Nº 18.508 of 2009) | 1 | As enacted (in force 26 July 2009), with no amendment recorded by IMPO, to today |
| `ley-18596/` | Ley de Reparación a las Víctimas de la Actuación Ilegítima del Estado (Ley Nº 18.596 of 2009) | 2 | As enacted (in force 29 October 2009), then Ley 18.996, to today |
| `ley-18026/` | Ley de Cooperación con la Corte Penal Internacional (Ley Nº 18.026 of 2006) | 2 | As enacted (in force 14 October 2006), then Ley 18.494, to today |
| `ley-19643/` | Ley de Prevención y Combate de la Trata de Personas (Ley Nº 19.643 of 2018) | 1 | As enacted (in force 24 August 2018), with no amendment recorded by IMPO, to today |
| `ley-17815/` | Ley de Violencia Sexual contra Niños, Adolescentes o Incapaces (Ley Nº 17.815 of 2004) | 3 | As enacted (in force 24 September 2004), then Ley 18.914, Ley 19.643, to today |
| `ley-18407/` | Ley General de Cooperativas (Ley Nº 18.407 of 2008) | 14 | As enacted (in force 24 November 2008), then 15 amending laws from Ley 18.719 (2010) to Ley 20.212 (2023), to today |
| `ley-19353/` | Ley del Sistema Nacional Integrado de Cuidados (Ley Nº 19.353 of 2015) | 4 | As enacted (in force 18 December 2015), then 4 amending laws from Ley 19.535 (2017) to Ley 20.446 (2025), to today |
| `ley-18471/` | Ley de Protección, Bienestar y Tenencia de Animales (Ley Nº 18.471 of 2009) | 7 | As enacted (in force 1 May 2009), then 7 amending laws from Ley 19.355 (2015) to Ley 20.212 (2023), to today |
| `ley-16906/` | Ley de Promoción y Protección de Inversiones (Ley Nº 16.906 of 1998) | 9 | As enacted (in force 30 January 1998), then 8 amending laws from Ley 17.243 (2000) to Ley 20.446 (2025), to today |
| `ley-19529/` | Ley de Salud Mental (Ley Nº 19.529 of 2017) | 2 | As enacted (in force 29 September 2017), then Ley 20.446, to today |
| `ley-18412/` | Ley del Seguro Obligatorio de Automotores (Ley Nº 18.412 of 2008) | 4 | As enacted (in force 16 May 2009), then Ley 19.678, Ley 19.924, Ley 19.996, to today |
| `ley-18191/` | Ley de Tránsito y Seguridad Vial (Ley Nº 18.191 of 2007) | 4 | As enacted (in force 8 December 2007), then 4 amending laws from Ley 19.360 (2015) to Ley 20.212 (2023), to today |
| `ley-19691/` | Ley de Promoción del Trabajo para Personas con Discapacidad (Ley Nº 19.691 of 2018) | 2 | As enacted (in force 18 November 2018), then Ley 19.924, to today |
| `ley-16713/` | Ley de Seguridad Social (Ley Nº 16.713 of 1995) | 21 | As enacted (in force 1 April 1996), then 25 amending laws from Ley 16.759 (1996) to Ley 20.130 (2023), to today |
| `ley-18446/` | Ley de la Institución Nacional de Derechos Humanos y Defensoría del Pueblo (Ley Nº 18.446 of 2008) | 4 | As enacted (in force 6 February 2009), then Ley 18.806, Ley 19.763, Ley 20.212, to today |
| `ley-18795/` | Ley de Acceso a la Vivienda de Interés Social (Ley Nº 18.795 of 2011) | 8 | As enacted (in force 22 September 2011), then 8 amending laws from Ley 18.996 (2012) to Ley 20.446 (2025), to today |
| `ley-17957/` | Ley del Registro Nacional de Deudores Alimentarios (Ley Nº 17.957 of 2006) | 3 | As enacted (in force 28 April 2006), then Ley 18.244, Ley 20.212, to today |
| `ley-18076/` | Ley sobre el Derecho al Refugio y a los Refugiados (Ley Nº 18.076 of 2006) | 2 | As enacted (in force 15 January 2007), then Ley 19.996, to today |
| `ley-19167/` | Ley de Técnicas de Reproducción Humana Asistida (Ley Nº 19.167 of 2013) | 2 | As enacted (in force 20 February 2014), then Ley 20.062, to today |
| `ley-18473/` | Ley de Voluntad Anticipada (Ley Nº 18.473 of 2009) | 1 | As enacted (in force 1 May 2009), with no amendment recorded by IMPO, to today |
| `ley-16832/` | Ley de Actualización del Sistema Eléctrico Nacional (Ley Nº 16.832 of 1997) | 1 | As enacted (in force 7 July 1997), with no amendment recorded by IMPO, to today |
| `ley-9515/` | Ley Orgánica Municipal (Ley Nº 9.515 of 1935) | 8 | As enacted (in force 11 November 1935), then 12 amending laws from Ley 13.835 (1970) to Ley 19.829 (2019), to today |
| `ley-17163/` | Ley de Fundaciones (Ley Nº 17.163 of 1999) | 1 | As enacted (in force 20 September 1999), with no amendment recorded by IMPO, to today |
| `ley-18256/` | Ley de Control del Tabaquismo (Ley Nº 18.256 of 2008) | 5 | As enacted (in force 20 March 2008), then 4 amending laws from Ley 18.362 (2008) to Ley 19.723 (2018), to today |
| `ley-18091/` | Ley de Prescripción de Acciones y Créditos Laborales (Ley Nº 18.091 of 2007) | 1 | As enacted (in force 29 January 2007), with no amendment recorded by IMPO, to today |
| `ley-18251/` | Ley de Tercerizaciones Laborales (Ley Nº 18.251 of 2008) | 1 | As enacted (in force 27 January 2008), with no amendment recorded by IMPO, to today |
| `ley-12590/` | Ley de Licencia Anual (Ley Nº 12.590 of 1958) | 2 | As enacted (in force 15 January 1959), then Ley 13.556, to today |
| `ley-15996/` | Ley de Horas Extras (Ley Nº 15.996 of 1988) | 1 | As enacted (in force 5 December 1988), with no amendment recorded by IMPO, to today |
| `ley-18572/` | Ley de Abreviación de los Juicios Laborales (Ley Nº 18.572 of 2009) | 2 | As enacted (in force 18 October 2009), then Ley 18.847, to today |
| `ley-19690/` | Ley del Fondo de Garantía de Créditos Laborales (Ley Nº 19.690 of 2018) | 1 | As enacted (in force 1 December 2018), with no amendment recorded by IMPO, to today |
| `ley-18227/` | Ley de Asignaciones Familiares (Ley Nº 18.227 of 2007) | 2 | As enacted (in force 19 January 2008), then Ley 19.924, to today |
| `ley-19313/` | Ley de Trabajo Nocturno (Ley Nº 19.313 of 2015) | 1 | As enacted (in force 7 March 2015), with no amendment recorded by IMPO, to today |
| `ley-17215/` | Ley de Trabajadoras en Estado de Gravidez o en Período de Lactancia (Ley Nº 17.215 of 1999) | 1 | As enacted (in force 17 October 1999), with no amendment recorded by IMPO, to today |
| `ley-16774/` | Ley de Fondos de Inversión (Ley Nº 16.774 of 1996) | 6 | As enacted (in force 17 October 1996), then 5 amending laws from Ley 17.202 (1999) to Ley 20.075 (2022), to today |
| `ley-17613/` | Ley de Bancos (Ley Nº 17.613 of 2002) | 6 | As enacted (in force 31 December 2002), then 5 amending laws from Ley 17.740 (2004) to Ley 20.446 (2025), to today |
| `codigo-aeronautico/` | Código Aeronáutico (Decreto-Ley Nº 14.305 of 1974) | 6 | As enacted (in force 4 January 1975), then 5 amending laws from Decreto-Ley 14.653 (1977) to Ley 18.619 (2009), to today |
| `codigo-aguas/` | Código de Aguas (Decreto-Ley Nº 14.859 of 1978) | 7 | As enacted (in force 21 January 1979), then 7 amending laws from Decreto-Ley 15.576 (1984) to Ley 19.670 (2018), to today |
| `ley-19920/` | Ley General de Derecho Internacional Privado (Ley Nº 19.920 of 2020) | 1 | As enacted (in force 16 March 2021), with no amendment recorded by IMPO, to today |
| `ley-7812/` | Ley de Elecciones (Ley Nº 7.812 of 1925) | 14 | As enacted (in force 29 January 1925), then 16 amending laws from Ley 7.912 (1925) to Ley 19.790 (2019), to today |
| `ley-18485/` | Ley de Partidos Políticos (Ley Nº 18.485 of 2009) | 2 | As enacted (in force 30 May 2009), then Ley 20.292, to today |
| `ley-15848/` | Ley de Caducidad de la Pretensión Punitiva del Estado (Ley Nº 15.848 of 1986) | 1 | As enacted (in force 10 January 1987, ten days after publication; its own clause gives 22 December 1986, before its publication), with no amendment recorded by IMPO, to today |
| `ley-18831/` | Ley de Restablecimiento de la Pretensión Punitiva del Estado (Ley Nº 18.831 of 2011) | 1 | As enacted (in force 11 November 2011, ten days after publication; its own clause gives 27 October 2011, before its publication), with no amendment recorded by IMPO, to today |
| `ley-16099/` | Ley de Prensa (Ley Nº 16.099 of 1989) | 2 | As enacted (in force 14 December 1989), then Ley 18.515, to today |
| `ley-18232/` | Ley de Radiodifusión Comunitaria (Ley Nº 18.232 of 2007) | 5 | As enacted (in force 19 January 2008), then 4 amending laws from Ley 18.996 (2012) to Ley 20.446 (2025), to today |
| `ley-19043/` | Ley de Creación de la Universidad Tecnológica (Ley Nº 19.043 of 2012) | 3 | As enacted (in force 18 January 2013), then Ley 19.889, Ley 20.096, Ley 20.125, to today |
| `ley-12549/` | Ley Orgánica de la Universidad de la República (Ley Nº 12.549 of 1958) | 3 | As enacted (in force 8 November 1958), then Decreto-Ley 15.524, Ley 19.889, to today |
| `ley-19122/` | Ley de Afrodescendientes: Normas para Favorecer su Participación (Ley Nº 19.122 of 2013) | 2 | As enacted (in force 19 September 2013), then Ley 20.075, to today |
| `ley-19846/` | Ley de Igualdad y No Discriminación entre Mujeres y Varones (Ley Nº 19.846 of 2019) | 1 | As enacted (in force 18 January 2020), with no amendment recorded by IMPO, to today |
| `ley-17817/` | Ley de Lucha contra el Racismo, la Xenofobia y la Discriminación (Ley Nº 17.817 of 2004) | 2 | As enacted (in force 24 September 2004), then Ley 19.122, Ley 20.212, to today |
| `ley-19828/` | Ley de Fomento y Protección del Sistema Deportivo (Ley Nº 19.828 of 2019) | 4 | As enacted (in force 6 October 2019), then Ley 19.924, Ley 20.075, Ley 20.212, to today |
| `ley-15921/` | Ley de Zonas Francas (Ley Nº 15.921 of 1987) | 9 | As enacted (in force 5 February 1988), then 10 amending laws from Ley 17.292 (2001) to Ley 20.446 (2025), to today |
| `ley-16246/` | Ley de Puertos (Ley Nº 16.246 of 1992) | 3 | As enacted (in force 3 May 1992), then Ley 19.670, Ley 19.996, to today |
| `ley-16466/` | Ley de Evaluación del Impacto Ambiental (Ley Nº 16.466 of 1994) | 3 | As enacted (in force 5 February 1994), then Ley 19.670, Ley 19.924, to today |
| `ley-17849/` | Ley de Uso de Envases no Retornables (Ley Nº 17.849 of 2004) | 2 | As enacted (in force 8 January 2005), then Ley 18.996, to today |
| `ley-19175/` | Ley de Pesca Responsable y Fomento de la Acuicultura (Ley Nº 19.175 of 2013) | 6 | As enacted (in force 17 January 2014), then 5 amending laws from Ley 19.355 (2015) to Ley 20.212 (2023), to today |
| `ley-15939/` | Ley Forestal (Ley Nº 15.939 of 1987) | 9 | As enacted (in force 19 February 1988), then 8 amending laws from Ley 16.002 (1988) to Ley 20.446 (2025), to today |
| `ley-16858/` | Ley de Riego con Destino Agrario (Ley Nº 16.858 of 1997) | 2 | As enacted (in force 21 September 1997), then Ley 19.553, to today |
| `ley-18161/` | Ley de Creación de la Administración de los Servicios de Salud del Estado (Ley Nº 18.161 of 2007) | 3 | As enacted (in force 18 August 2007), then 4 amending laws from Ley 18.362 (2008) to Ley 19.308 (2015), to today |
| `decreto-ley-15322/` | Ley de Intermediación Financiera (Decreto-Ley Nº 15.322 of 1982) | 9 | As enacted (in force 3 October 1982), then 8 amending laws from Ley 15.768 (1985) to Ley 20.075 (2022), to today |
| `decreto-ley-14219/` | Ley de Arrendamientos Urbanos y Suburbanos (Decreto-Ley Nº 14.219 of 1974) | 13 | From its entry into force (1 August 1974), with the changes Decreto-Ley 14.220 made by that day, then 15 amending laws from Decreto-Ley 14.266 (1974) to Ley 20.352 (2024), to today |
| `ley-19820/` | Ley de Fomento del Emprendedurismo (Ley Nº 19.820 of 2019) | 2 | As enacted (in force 7 October 2019), then Ley 19.924, to today |
| `ley-18930/` | Ley sobre Información de Participaciones Patrimoniales al Portador (Ley Nº 18.930 of 2012) | 7 | As enacted (in force 1 August 2012), then 6 amending laws from Ley 19.288 (2014) to Ley 20.446 (2025), to today |
| `ley-18786/` | Ley de Participación Público-Privada (Ley Nº 18.786 of 2011) | 3 | As enacted (in force 29 August 2011, ten days after publication; its own clause gives 18 August 2011, before its publication), then Ley 19.553, Ley 19.924, to today |
| `ley-19253/` | Ley de Turismo (Ley Nº 19.253 of 2014) | 2 | As enacted (in force 19 September 2014), then Ley 19.996, to today |
| `ley-19272/` | Ley de Descentralización y Participación Ciudadana (Ley Nº 19.272 of 2014) | 3 | As enacted (in force 5 October 2014), then Ley 19.355, Ley 19.924, to today |
| `ley-18597/` | Ley de Uso Eficiente de la Energía (Ley Nº 18.597 of 2009) | 4 | As enacted (in force 26 October 2009), then Ley 18.719, Ley 19.355, Ley 19.924, to today |
| `decreto-ley-14701/` | Ley de Títulos Valores (Decreto-Ley Nº 14.701 of 1977) | 5 | As enacted (in force 1 November 1977), then 4 amending laws from Decreto-Ley 15.226 (1981) to Ley 16.906 (1998), to today |
| `ley-19678/` | Ley del Mercado de Seguros (Ley Nº 19.678 of 2018) | 1 | As enacted (in force 18 November 2018), with no amendment recorded by IMPO, to today |
| `ley-10751/` | Ley de Propiedad Horizontal (Ley Nº 10.751 of 1946) | 5 | As enacted (in force 29 September 1946), then 4 amending laws from Ley 12.358 (1957) to Ley 20.446 (2025), to today |
| `ley-10449/` | Ley de Consejos de Salarios (Ley Nº 10.449 of 1943) | 7 | As enacted (in force 30 November 1943), then 7 amending laws from Ley 11.618 (1950) to Ley 18.566 (2009), to today |
| `ley-18840/` | Ley de Conexión a las Redes Públicas de Saneamiento (Ley Nº 18.840 of 2011) | 4 | As enacted (in force 18 December 2011), then Ley 18.996, Ley 19.149, Ley 19.535, to today |
| `ley-18244/` | Ley de Deudores Alimentarios Morosos (Ley Nº 18.244 of 2007) | 2 | As enacted (in force 18 January 2008), then Ley 20.446, to today |
| `ley-16021/` | Ley de Nacionalidad y Ciudadanía (Ley Nº 16.021 of 1989) | 3 | As enacted (in force 7 May 1989), then Ley 18.858, Ley 19.362, to today |
| `ley-19140/` | Ley de Alimentación Saludable en los Centros de Enseñanza (Ley Nº 19.140 of 2013) | 3 | As enacted (in force 7 November 2013), then Ley 20.075, to today |
| `ley-19978/` | Ley de Teletrabajo (Ley Nº 19.978 of 2021) | 1 | As enacted (in force 9 September 2021), with no amendment recorded by IMPO, to today |
| `ley-17228/` | Ley de Prenda sin Desplazamiento (Ley Nº 17.228 of 2000) | 3 | As enacted (in force 3 February 2000), then Ley 17.296, Ley 19.090, to today |
| `ley-17684/` | Ley del Comisionado Parlamentario para el Sistema Carcelario (Ley Nº 17.684 of 2003) | 5 | As enacted (in force 28 September 2003), then 4 amending laws from Ley 17.919 (2005) to Ley 20.446 (2025), to today |
| `ley-18125/` | Carta Orgánica del Banco Hipotecario del Uruguay (Ley Nº 18.125 of 2007) | 6 | As enacted (in force 21 May 2007), then 5 amending laws from Ley 18.574 (2009) to Ley 20.212 (2023), to today |
| `ley-18131/` | Ley de Creación del Fondo Nacional de Salud (Ley Nº 18.131 of 2007) | 2 | As enacted (in force 10 June 2007), then Ley 20.446, to today |
| `ley-19286/` | Código de Ética Médica (Ley Nº 19.286 of 2014) | 2 | As enacted (in force 27 October 2014), then Ley 20.431, to today |
| `ley-18426/` | Ley de Salud Sexual y Reproductiva (Ley Nº 18.426 of 2008) | 1 | As enacted (in force 20 December 2008), with no amendment recorded by IMPO, to today |
| `ley-19823/` | Código de Ética en la Función Pública (Ley Nº 19.823 of 2019) | 1 | As enacted (in force 5 October 2019), with no amendment recorded by IMPO, to today |
| `ley-17866/` | Ley de Creación del Ministerio de Desarrollo Social (Ley Nº 17.866 of 2005) | 3 | As enacted (in force 10 April 2005), then Ley 19.353, Ley 19.670, to today |
| `ley-19869/` | Ley de Telemedicina (Ley Nº 19.869 of 2020) | 3 | As enacted (in force 25 April 2020), then Ley 19.924, Ley 19.984, to today |
| `ley-15977/` | Ley de Creación del Instituto Nacional del Menor (Ley Nº 15.977 of 1988) | 5 | As enacted (in force 27 October 1988), then 4 amending laws from Ley 16.736 (1996) to Ley 20.075 (2022), to today |
| `ley-19530/` | Ley de Salas de Lactancia Materna (Ley Nº 19.530 of 2017) | 1 | As enacted (in force 21 September 2017), with no amendment recorded by IMPO, to today |
| `ley-18405/` | Ley del Servicio de Retiros y Pensiones Policiales (Ley Nº 18.405 of 2008) | 3 | As enacted (in force 1 January 2009), then Ley 19.924, Ley 20.130, to today |
| `ley-18396/` | Ley Orgánica de la Caja de Jubilaciones y Pensiones Bancarias (Ley Nº 18.396 of 2008) | 4 | As enacted (in force 1 January 2009), then Ley 19.996, Ley 20.130, Ley 20.208, to today |
| `ley-17738/` | Ley Orgánica de la Caja de Jubilaciones y Pensiones de Profesionales Universitarios (Ley Nº 17.738 of 2004) | 6 | As enacted (in force 1 August 2004), then 5 amending laws from Ley 17.993 (2006) to Ley 20.410 (2025), to today |
| `codigo-contencioso-administrativo/` | Código de lo Contencioso Administrativo (Ley Nº 20.333 of 2024) | 2 | As enacted (in force 24 December 2024), with no amendment in force recorded by IMPO, to today; on the `futuro` branch, Ley 20.531's changes from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `decreto-ley-14412/` | Ley de Cheques (Decreto-Ley Nº 14.412 of 1975) | 5 | As enacted (in force 1 October 1975), then 5 amending laws from Decreto-Ley 14.701 (1977) to Ley 20.038 (2022), to today |
| `ley-19483/` | Ley Orgánica de la Fiscalía General de la Nación (Ley Nº 19.483 of 2017) | 13 | As enacted (in force 9 February 2017), then 11 amending laws from Ley 19.535 (2017) to Ley 20.446 (2025), to today |
| `ley-19636/` | Ley de Arbitraje Comercial Internacional (Ley Nº 19.636 of 2018) | 1 | As enacted (in force 5 August 2018), with no amendment recorded by IMPO, to today |
| `ley-19775/` | Ley Orgánica Militar (Ley Nº 19.775 of 2019) | 3 | As enacted (in force 15 August 2019), then Ley 19.889, Ley 19.924, to today |
| `ley-18650/` | Ley Marco de Defensa Nacional (Ley Nº 18.650 of 2010) | 3 | As enacted (in force 18 March 2010), then Ley 18.896, Ley 19.889, to today |
| `ley-11029/` | Ley de Creación del Instituto Nacional de Colonización (Ley Nº 11.029 of 1948) | 7 | As enacted (in force 15 February 1948), then 6 amending laws from Ley 18.187 (2007) to Ley 19.996 (2021), to today |
| `ley-10723/` | Ley de Centros Poblados (Ley Nº 10.723 of 1946) | 6 | As enacted (in force 26 May 1946), then 8 amending laws from Ley 10.866 (1946) to Ley 20.212 (2023), to today |
| `ley-14040/` | Ley de la Comisión del Patrimonio Histórico, Artístico y Cultural de la Nación (Ley Nº 14.040 of 1971) | 4 | As enacted (in force 6 November 1971), then 4 amending laws from Ley 15.851 (1986) to Ley 19.355 (2015), to today |
| `decreto-ley-15239/` | Ley de Uso y Conservación de los Suelos y de las Aguas (Decreto-Ley Nº 15.239 of 1981) | 4 | As enacted (in force 17 January 1982), then Ley 18.564, Ley 19.355, Ley 20.075, to today |
| `ley-18621/` | Ley del Sistema Nacional de Emergencias (Ley Nº 18.621 of 2009) | 6 | As enacted (in force 27 November 2009), then 5 amending laws from Ley 18.719 (2010) to Ley 20.212 (2023), to today |
| `ley-19696/` | Ley del Sistema Nacional de Inteligencia de Estado (Ley Nº 19.696 of 2018) | 3 | As enacted (in force 17 November 2018), then Ley 19.889, Ley 20.469, to today |
| `decreto-ley-15180/` | Ley de Seguro de Desempleo (Decreto-Ley Nº 15.180 of 1981) | 2 | As enacted (in force 17 September 1981), then Ley 18.399, to today |
| `ley-12840/` | Ley de Aguinaldo (Ley Nº 12.840 of 1960) | 1 | As enacted (in force 9 January 1961, ten days after publication; its own clause gives 23 December 1960, before its publication), with no amendment recorded by IMPO, to today |
| `ley-16811/` | Ley de Semillas (Ley Nº 16.811 of 1997) | 4 | As enacted (in force 10 March 1997), then Ley 18.467, Ley 20.212, Ley 20.446, to today |
| `ley-17598/` | Ley de la Unidad Reguladora de Servicios de Energía y Agua (Ley Nº 17.598 of 2002) | 10 | As enacted (in force 3 January 2003), then 11 amending laws from Ley 17.930 (2005) to Ley 20.212 (2023), to today |
| `ley-7318/` | Ley de Descanso Semanal (Ley Nº 7.318 of 1920) | 2 | As enacted (in force 20 December 1920), then Decreto-Ley 10.321, to today |
| `ley-17230/` | Ley de Pasantías Laborales (Ley Nº 17.230 of 2000) | 2 | As enacted (in force 3 February 2000), then Ley 19.670, to today |
| `ley-9202/` | Ley Orgánica de Salud Pública (Ley Nº 9.202 of 1934) | 5 | As enacted (in force 1 February 1934), then 4 amending laws from Ley 9.892 (1939) to Ley 17.930 (2005), to today |
| `ley-18476/` | Ley de Participación Equitativa de Ambos Sexos en los Órganos Electivos (Ley Nº 18.476 of 2009) | 2 | As enacted (in force 1 May 2009), then Ley 19.555, to today |
| `ley-16072/` | Ley de Crédito de Uso (Ley Nº 16.072 of 1989) | 4 | As enacted (in force 20 November 1989), then Ley 16.205, Ley 16.320, Ley 16.906, to today |
| `ley-17066/` | Ley de Establecimientos Privados para Adultos Mayores (Ley Nº 17.066 of 1998) | 1 | As enacted (in force 18 January 1999), with no amendment recorded by IMPO, to today |
| `decreto-ley-15084/` | Ley de Asignaciones Familiares (Decreto-Ley Nº 15.084 of 1980) | 3 | As enacted (in force 1 January 1981), then Ley 19.161, Ley 20.446, to today |
| `decreto-ley-14178/` | Ley de Promoción Industrial (Decreto-Ley Nº 14.178 of 1974) | 4 | As enacted (in force 28 April 1974), then Decreto-Ley 14.335, Ley 15.851, Ley 15.903, to today |
| `ley-7690/` | Ley de Registro Cívico Nacional (Ley Nº 7.690 of 1924) | 26 | As enacted (in force 21 January 1924), then 27 amending laws from Ley 7.782 (1924) to Ley 17.690 (2003), to today |
| `ley-19855/` | Ley de Regulación del Consumo Problemático de Alcohol (Ley Nº 19.855 of 2019) | 2 | As enacted (in force 18 January 2020), then Ley 19.866, to today |
| `ley-19784/` | Ley de Parques Industriales y Parques Científico-Tecnológicos (Ley Nº 19.784 of 2019) | 2 | As enacted (in force 21 September 2019), then Ley 19.924, to today |
| `ley-18240/` | Ley de Creación del Programa Uruguay Trabaja (Ley Nº 18.240 of 2007) | 3 | As enacted (in force 19 January 2008), then Ley 19.149, Ley 19.670, to today |
| `ley-9481/` | Ley de Protección de la Fauna Indígena (Ley Nº 9.481 of 1935) | 2 | As enacted (in force 20 July 1935), then Ley 20.212, to today |
| `ley-18033/` | Ley de Recuperación de Derechos Jubilatorios y Pensionarios (Ley Nº 18.033 of 2006) | 3 | As enacted (in force 29 October 2006), then Ley 18.235, Ley 18.596, to today |
| `ley-19534/` | Ley de Derecho de Admisión en Espectáculos Públicos (Ley Nº 19.534 of 2017) | 2 | As enacted (in force 28 October 2017), then Ley 19.889, to today |
| `decreto-ley-14470/` | Ley de Reclusión Carcelaria y Personal Penitenciario (Decreto-Ley Nº 14.470 of 1975) | 12 | As enacted (in force 21 December 1975), then 10 amending laws from Decreto-Ley 15.536 (1984) to Ley 20.212 (2023), to today; on the `futuro` branch, Ley 20.531's new art. 54 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `ley-18716/` | Carta Orgánica del Banco de la República Oriental del Uruguay (Ley Nº 18.716 of 2010) | 4 | As enacted (in force 10 January 2011), then Ley 19.889, Ley 20.075, to today; on the `futuro` branch, Ley 20.531's new inciso 2 of art. 11 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `decreto-ley-15031/` | Ley Orgánica de UTE (Decreto-Ley Nº 15.031 of 1980) | 2 | As enacted (in force 22 August 1980), then Ley 16.211, Ley 16.462, Ley 16.832, to today |
| `ley-11907/` | Ley Orgánica de la Administración de las Obras Sanitarias del Estado (Ley Nº 11.907 of 1952) | 3 | As enacted (in force 19 January 1953), then 4 amending laws from Ley 13.737 (1969) to Ley 18.046 (2006), to today |
| `ley-8764/` | Ley de Creación de la Administración Nacional de Combustibles, Alcohol y Portland (Ley Nº 8.764 of 1931) | 5 | As enacted (in force 2 November 1931), then 5 amending laws from Decreto-Ley 9.024 (1933) to Ley 20.075 (2022), to today |
| `decreto-ley-15181/` | Ley de Instituciones de Asistencia Médica Colectiva (Decreto-Ley Nº 15.181 of 1981) | 3 | As enacted (in force 12 September 1981), then Ley 17.296, Ley 18.440, to today |
| `decreto-ley-15605/` | Ley de Creación del Instituto Nacional de Carnes (Decreto-Ley Nº 15.605 of 1984) | 8 | As enacted (in force 13 August 1984), then 9 amending laws from Ley 16.170 (1990) to Ley 20.212 (2023), to today |
| `decreto-ley-15703/` | Ley de Farmacias (Decreto-Ley Nº 15.703 of 1985) | 4 | As enacted (in force 26 April 1985), then Ley 17.296, Ley 17.715, Ley 20.075, to today |
| `ley-16065/` | Ley de Creación del Instituto Nacional de Investigación Agropecuaria (Ley Nº 16.065 of 1989) | 6 | As enacted (in force 10 November 1989), then 5 amending laws from Ley 16.226 (1991) to Ley 20.075 (2022), to today; on the `futuro` branch, Ley 20.531's new art. 32 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `ley-15785/` | Ley de Creación de la Corporación Nacional para el Desarrollo (Ley Nº 15.785 of 1985) | 8 | As enacted (in force 2 January 1986), then 8 amending laws from Ley 15.903 (1987) to Ley 20.075 (2022), to today |
| `ley-18406/` | Ley de Creación del Instituto Nacional de Empleo y Formación Profesional (Ley Nº 18.406 of 2008) | 6 | As enacted (in force 20 November 2008), then 7 amending laws from Ley 18.996 (2012) to Ley 20.446 (2025), to today |
| `ley-18084/` | Ley de la Agencia Nacional de Investigación e Innovación (Ley Nº 18.084 of 2006) | 6 | As enacted (in force 19 January 2007), then 4 amending laws from Ley 19.472 (2016) to Ley 20.446 (2025), to today; on the `futuro` branch, Ley 20.531's new literal B) of art. 6 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `ley-19367/` | Ley de Creación del Instituto Nacional de Inclusión Social Adolescente (Ley Nº 19.367 of 2015) | 4 | As enacted (in force 6 February 2016), then Ley 19.535, to today; on the `futuro` branch, Ley 20.531's new literal H) of art. 3 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `ley-18242/` | Ley de Regulación, Fomento y Desarrollo de la Producción Láctea (Ley Nº 18.242 of 2007) | 5 | As enacted (in force 20 January 2008), then Ley 19.355, Ley 19.924, Ley 20.446, to today; on the `futuro` branch, Ley 20.531's new arts. 8 and 11 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `ley-16616/` | Ley de Estadística Nacional (Ley Nº 16.616 of 1994) | 2 | As enacted (in force 10 November 1994), then Ley 20.446, to today |
| `ley-16524/` | Ley de Creación del Fondo de Solidaridad (Ley Nº 16.524 of 1994) | 11 | As enacted (in force 14 August 1994), then 11 amending laws from Ley 17.296 (2001) to Ley 20.446 (2025), to today; on the `futuro` branch, Ley 20.531's new numeral 3) of art. 1 from 1 January 2027, built from that law's own text (not yet consolidated by IMPO) |
| `ley-19158/` | Ley de Creación del Instituto Uruguayo de Meteorología (Ley Nº 19.158 of 2013) | 3 | As enacted (in force 25 November 2013), then Ley 19.670, Ley 19.889, Ley 20.446, to today |
| `ley-18640/` | Ley de Creación del Centro Ceibal para el Apoyo a la Educación de la Niñez y la Adolescencia (Ley Nº 18.640 of 2010) | 6 | As enacted (in force 5 February 2010), then 5 amending laws from Ley 18.719 (2010) to Ley 20.212 (2023), to today |
| `ley-18697/` | Ley de Creación del Instituto Nacional de Logística (Ley Nº 18.697 of 2010) | 1 | As enacted (in force 13 December 2010), with no amendment recorded by IMPO, to today |
| `ley-18602/` | Ley de Creación de la Agencia Nacional de Desarrollo (Ley Nº 18.602 of 2009) | 4 | As enacted (in force 15 November 2009), then Ley 19.472, Ley 19.670, Ley 19.924, to today |
| `ley-14005/` | Ley de Donación de Órganos y Tejidos (Ley Nº 14.005 of 1971) | 4 | As enacted (in force 30 August 1971), then Ley 17.668, Ley 18.968, Ley 20.212, to today |
| `ley-18591/` | Ley de Creación del Colegio Médico del Uruguay (Ley Nº 18.591 of 2009) | 1 | As enacted (in force 26 October 2009), with no amendment recorded by IMPO, to today |
| `ley-18113/` | Ley de Creación de la Unidad Nacional de Seguridad Vial (Ley Nº 18.113 of 2007) | 3 | As enacted (in force 17 May 2007), then Ley 19.355, Ley 19.924, to today |
| `ley-19334/` | Ley de Creación de la Fiscalía General de la Nación como Servicio Descentralizado (Ley Nº 19.334 of 2015) | 1 | As enacted (in force 3 September 2015), with no amendment recorded by IMPO, to today |
| `ley-18195/` | Ley de Agrocombustibles (Ley Nº 18.195 of 2007) | 2 | As enacted (in force 8 December 2007), then Ley 19.996, to today |
| `ley-18284/` | Ley de Creación del Instituto del Cine y el Audiovisual del Uruguay (Ley Nº 18.284 of 2008) | 3 | As enacted (in force 12 June 2008), then Ley 20.075, Ley 20.212, to today |
| `ley-19525/` | Ley de Directrices Nacionales de Ordenamiento Territorial y Desarrollo Sostenible (Ley Nº 19.525 of 2017) | 2 | As enacted (in force 29 September 2017), then Ley 20.212, to today |
| `ley-19655/` | Ley de Prevención y Reducción del Impacto Ambiental de las Bolsas Plásticas (Ley Nº 19.655 of 2018) | 1 | As enacted (in force 13 September 2018), with no amendment recorded by IMPO, to today |
| `decreto-ley-15661/` | Ley de Títulos Profesionales de las Universidades Privadas (Decreto-Ley Nº 15.661 of 1984) | 2 | As enacted (in force 30 November 1984), then Ley 20.075, to today |
| `ley-18516/` | Ley de Distribución del Trabajo de Peones Prácticos y Obreros No Especializados en Obras del Estado (Ley Nº 18.516 of 2009) | 2 | As enacted (in force 26 July 2009, ten days after publication; its own clause gives 26 June 2009, before its publication), then Ley 20.212, to today |
| `ley-19641/` | Ley de Sitios de Memoria Histórica del Pasado Reciente (Ley Nº 19.641 of 2018) | 1 | As enacted (in force 24 August 2018), with no amendment recorded by IMPO, to today |
| `ley-19039/` | Ley de Pensión a las Víctimas de Delitos Violentos (Ley Nº 19.039 of 2012) | 3 | As enacted (in force 17 January 2013), then Ley 19.889, Ley 20.446, to today |
| `ley-17220/` | Ley de Prohibición de la Introducción de Desechos Peligrosos (Ley Nº 17.220 of 1999) | 3 | As enacted (in force 27 November 1999), then Ley 17.930, Ley 19.829, to today |
| `ley-15737/` | Ley de Amnistía, Aprobación del Pacto de San José de Costa Rica y Comisión Nacional de Repatriación (Ley Nº 15.737 of 1985) | 3 | As enacted (in force 1 April 1985, ten days after publication; its own clause gives 8 March 1985, before its publication), then Ley 16.349, Ley 17.272, to today |
| `ley-18829/` | Ley del Plan Nacional de Integración Socio-Habitacional Juntos (Ley Nº 18.829 of 2011) | 4 | As enacted (in force 14 November 2011, ten days after publication; its own clause gives 24 October 2011, before its publication), then Ley 19.355, Ley 19.924, Ley 20.212, to today |
| `ley-17781/` | Ley de Certificados de Depósito y Warrants (Ley Nº 17.781 of 2004) | 1 | As enacted (in force 19 June 2004), with no amendment recorded by IMPO, to today |
| `ley-20431/` | Ley de Muerte Digna (Ley Nº 20.431 of 2025) | 1 | As enacted (in force 15 November 2025), with no amendment recorded by IMPO, to today |
| `ley-19337/` | Ley de Creación del Fondo para el Desarrollo (FONDES) (Ley Nº 19.337 of 2015) | 5 | As enacted (in force 11 October 2015), then 4 amending laws from Ley 19.829 (2019) to Ley 20.075 (2022), to today |
| `ley-20419/` | Ley del Régimen Especial de Comercio de Frontera (Ley Nº 20.419 of 2025) | 1 | As enacted (in force 13 September 2025), with no amendment recorded by IMPO, to today |
| `ley-19246/` | Ley de Derecho Comercial Marítimo (Ley Nº 19.246 of 2014) | 1 | As enacted (in force 19 September 2014), with no amendment recorded by IMPO, to today |
| `ley-20519/` | Ley de Creación del Programa Piloto de Justicia Terapéutica (Ley Nº 20.519 of 2026) | 1 | As enacted (in force 24 September 2026), with no amendment recorded by IMPO, to today |
| `ley-20352/` | Ley de Alojamiento Turístico en Inmuebles (Ley Nº 20.352 of 2024) | 1 | As enacted (in force 7 October 2024), with no amendment recorded by IMPO, to today |
| `ley-20396/` | Ley de Niveles Mínimos de Protección para Trabajadores de Plataformas Digitales (Ley Nº 20.396 of 2025) | 1 | As enacted (in force 14 May 2025), with no amendment recorded by IMPO, to today |
| `ley-20141/` | Ley de Corresponsabilidad en la Crianza (Ley Nº 20.141 of 2023) | 1 | As enacted (in force 8 June 2023), with no amendment recorded by IMPO, to today |
| `ley-20360/` | Ley de la Acción de Repetición (Ley Nº 20.360 of 2024) | 1 | As enacted (in force 12 October 2024), with no amendment recorded by IMPO, to today |
| `ley-18619/` | Ley de Seguridad Operacional de la Aeronáutica Civil (Ley Nº 18.619 of 2009) | 2 | As enacted (in force 27 November 2009), then Ley 20.158, to today |
| `ley-19288/` | Ley de Depuración de Sociedades Inactivas e Identificación de Titulares de Participaciones al Portador (Ley Nº 19.288 of 2014) | 1 | As enacted (in force 1 November 2014), with no amendment recorded by IMPO, to today |
| `ley-19845/` | Ley de Investigación sobre el Cannabis y sus Aplicaciones (Ley Nº 19.845 of 2019) | 1 | As enacted (in force 17 January 2020), with no amendment recorded by IMPO, to today |
| `ley-18187/` | Ley de Regulación de la Colonización de Tierras (Ley Nº 18.187 of 2007) | 1 | As enacted (in force 22 November 2007), with no amendment recorded by IMPO, to today |
| `ley-17951/` | Ley de Erradicación de la Violencia en el Deporte (Ley Nº 17.951 of 2006) | 3 | As enacted (in force 23 January 2006), then Ley 18.362, Ley 19.331, to today |
| `ley-19661/` | Ley de Desalojos Colectivos (Ley Nº 19.661 of 2018) | 1 | As enacted (in force 26 October 2018), with no amendment recorded by IMPO, to today |
| `ley-19791/` | Ley de Medidas Preventivas para Instituciones con Trato Directo con Niños, Personas con Discapacidad y Personas Mayores Dependientes (Ley Nº 19.791 of 2019) | 1 | As enacted (in force 4 October 2019), with no amendment recorded by IMPO, to today |
| `ley-19790/` | Ley de Garantía del Derecho al Voto de las Personas con Discapacidad Motriz (Ley Nº 19.790 of 2019) | 1 | As enacted (in force 4 October 2019), with no amendment recorded by IMPO, to today |
| `ley-10783/` | Ley de Derechos Civiles de la Mujer (Ley Nº 10.783 of 1946) | 1 | As enacted (in force 12 October 1946), with no amendment recorded by IMPO, to today |
| `ley-18895/` | Ley de Restitución de Personas Menores de Dieciséis Años Trasladadas o Retenidas Ilícitamente (Ley Nº 18.895 of 2012) | 2 | As enacted (in force 1 June 2012), then Ley 19.580, to today |
| `ley-19628/` | Ley de Expedición de Certificados de Defunción (Ley Nº 19.628 of 2018) | 2 | As enacted (in force 14 July 2018), then Ley 20.431, to today |
| `ley-19317/` | Ley de Promoción de la Biotecnología (Ley Nº 19.317 of 2015) | 2 | As enacted (in force 12 March 2015), then Ley 19.820, to today |
| `ley-15800/` | Ley de Reinstitucionalización del Banco de Previsión Social (Ley Nº 15.800 of 1986) | 5 | As enacted (in force 13 March 1986), then 4 amending laws from Ley 16.170 (1990) to Ley 20.130 (2023), to today |
| `ley-19310/` | Ley de Remuneraciones de Magistrados, Fiscales y Funcionarios del Poder Judicial (Ley Nº 19.310 of 2015) | 2 | As enacted (in force 5 February 2015), then Ley 20.360, to today |
| `ley-17547/` | Ley de Parques Industriales (Ley Nº 17.547 of 2002) | 3 | As enacted (in force 6 September 2002), then Ley 19.784, Ley 19.924, to today |
| `ley-18456/` | Ley de Empadronamiento de Vehículos Automotores (Ley Nº 18.456 of 2008) | 2 | As enacted (in force 5 February 2009), then Ley 18.860, to today |
| `ley-13493/` | Ley de Fraccionamientos de Suelo Urbano sin Servicios de Agua Potable y Energía Eléctrica (Ley Nº 13.493 of 1966) | 3 | As enacted (in force 7 October 1966), then Decreto-Ley 15.452, Ley 18.308, to today |
| `ley-18637/` | Ley de Elección de Miembros de los Consejos Directivo Central y de Educación de la ANEP (Ley Nº 18.637 of 2009) | 1 | As enacted (in force 22 January 2010), with no amendment recorded by IMPO, to today |
| `ley-9318/` | Ley de Elecciones Nacionales y Plebiscito Constitucional de 1934 (Ley Nº 9.318 of 1934) | 2 | As enacted (in force 31 March 1934), then Ley 10.789, to today |
| `ley-9038/` | Ley de Elección de la Convención Nacional Constituyente de 1933 (Ley Nº 9.038 of 1933) | 2 | As enacted (in force 6 June 1933), then Ley 9.051, to today |
| `ley-15852/` | Ley de Aportaciones Tributarias de las Empresas Rurales (Ley Nº 15.852 of 1986) | 8 | As enacted (in force 26 January 1987), then 7 amending laws from Ley 15.953 (1988) to Ley 19.924 (2020), to today |
| `ley-5495/` | Ley de Creación de la Administración Nacional del Puerto de Montevideo (Ley Nº 5.495 of 1916) | 4 | As enacted (in force 4 August 1916), then Ley 6.861, Ley 9.602, Ley 16.246, to today |
| `ley-16112/` | Ley de Creación del Ministerio de Vivienda, Ordenamiento Territorial y Medio Ambiente (Ley Nº 16.112 of 1990) | 6 | As enacted (in force 18 June 1990), then 5 amending laws from Ley 17.283 (2000) to Ley 19.535 (2017), to today |
| `ley-19300/` | Ley del Seguro para el Control de Enfermedades (Ley Nº 19.300 of 2014) | 6 | As enacted (in force 18 January 2015), then 5 amending laws from Ley 19.438 (2016) to Ley 20.446 (2025), to today |
| `ley-16104/` | Ley de Licencias de los Funcionarios Públicos (Ley Nº 16.104 of 1990) | 8 | As enacted (in force 12 February 1990), then 7 amending laws from Ley 16.736 (1996) to Ley 19.996 (2021), to today |
| `decreto-ley-14261/` | Ley de Incorporación al Régimen de Propiedad Horizontal (Decreto-Ley Nº 14.261 of 1974) | 7 | As enacted (in force 19 September 1974), then 6 amending laws from Decreto-Ley 14.560 (1976) to Ley 19.924 (2020), to today |
| `decreto-ley-15298/` | Ley del Sistema Obligatorio de Unidades de Medida (Decreto-Ley Nº 15.298 of 1982) | 5 | As enacted (in force 1 January 1983), then 4 amending laws from Ley 15.903 (1987) to Ley 19.149 (2013), to today |
| `decreto-ley-15716/` | Ley del Monopolio del Juego de Quinielas y su Gravamen (Decreto-Ley Nº 15.716 of 1985) | 4 | As enacted (in force 21 April 1985), then Ley 15.903, Ley 18.362, Ley 19.535, to today |
| `ley-12091/` | Ley de Navegación y Comercio de Cabotaje Nacional (Ley Nº 12.091 of 1954) | 9 | As enacted (in force 5 February 1954), then 8 amending laws from Ley 12.613 (1959) to Ley 19.535 (2017), to today |
| `ley-13921/` | Ley de Habilitación de Salas de Juegos de Azar (Ley Nº 13.921 of 1970) | 3 | As enacted (in force 14 December 1970), then Decreto-Ley 14.189, Ley 16.226, to today |
| `ley-13793/` | Ley de Retiro de los Funcionarios Policiales y Pensiones a sus Causahabientes (Ley Nº 13.793 of 1969) | 3 | As enacted (in force 7 December 1969), then Decreto-Ley 14.610, Ley 16.911, to today |
| `ley-13833/` | Ley de Pesca (Ley Nº 13.833 of 1969) | 5 | As enacted (in force 15 January 1970), then 4 amending laws from Decreto-Ley 15.590 (1984) to Ley 19.996 (2021), to today |
| `ley-19037/` | Ley del Marco Legal de los Museos (Ley Nº 19.037 of 2012) | 4 | As enacted (in force 17 January 2013), then Ley 19.670, Ley 19.924, Ley 20.446, to today |
| `ley-19009/` | Ley del Régimen General de las Actividades Postales (Ley Nº 19.009 of 2012) | 4 | As enacted (in force 10 December 2012), then Ley 19.355, Ley 19.594, Ley 19.670, to today |
| `ley-13641/` | Ley de Aportaciones de Seguridad Social de las Empresas Periodísticas (Ley Nº 13.641 of 1968) | 7 | As enacted (in force 18 January 1968), then 6 amending laws from Ley 13.892 (1970) to Ley 16.275 (1992), to today |
| `ley-18874/` | Ley del Monotributo Social MIDES (Ley Nº 18.874 of 2011) | 4 | As enacted (in force 21 January 2012), then Ley 19.355, Ley 19.417, Ley 19.670, to today |
| `ley-11021/` | Ley de Jubilación de los Docentes de Enseñanza Primaria y Normal (Ley Nº 11.021 of 1948) | 4 | As enacted (in force 24 January 1948), then Ley 11.923, Ley 12.087, Ley 12.802, to today |
| `ley-20506/` | Ley de Promoción del Trabajo Digno y Decente de las Personas que Enfrentan Mayores Obstáculos para Acceder al Mercado Laboral (Ley Nº 20.506 of 2026) | 1 | As enacted (in force 27 July 2026), with no amendment recorded by IMPO, to today |
| `ley-17885/` | Ley del Voluntariado Social (Ley Nº 17.885 of 2005) | 3 | As enacted (in force 29 August 2005), then Ley 18.172, Ley 18.719, to today |
| `ley-18241/` | Ley del Subsidio a la Vejez para Personas en Situación de Indigencia o Extrema Pobreza (Ley Nº 18.241 of 2007) | 3 | As enacted (in force 18 January 2008), then Ley 19.996, Ley 20.130, to today |
| `ley-17968/` | Ley de la Comisión Permanente de Pensiones Graciables (Ley Nº 17.968 of 2006) | 3 | As enacted (in force 15 June 2006), then Ley 18.046, Ley 20.446, to today |
| `ley-19480/` | Ley del Registro de Personas Obligadas al Pago de Pensiones Alimenticias (Ley Nº 19.480 of 2017) | 3 | As enacted (in force 27 January 2017), then Ley 19.924, Ley 19.996, to today |
| `ley-19061/` | Ley de Tránsito y Seguridad Vial (Ley Nº 19.061 of 2013) | 3 | As enacted (in force 1 February 2013), then Ley 19.824, Ley 19.996, to today |
| `ley-18126/` | Ley del Consejo Agropecuario (Ley Nº 18.126 of 2007) | 3 | As enacted (in force 1 June 2007), then Ley 20.212, Ley 20.446, to today |
| `ley-10062/` | LEY ORGANICA DE LA CAJA NOTARIAL DE JUBILACIONES Y PENSIONES (Ley Nº 10.062 of 1941) | 1 | Current text only (IMPO's text, last changed 21 February 2001), to today |
| `ley-10446/` | LEY DE REGISTRO CIVICO NACIONAL. MODIFICACION (Ley Nº 10.446 of 1943) | 1 | Current text only (IMPO's text, last changed 20 October 1943), to today |
| `ley-10489/` | COMERCIO. REGIMEN HORARIO. FIJACION (Ley Nº 10.489 of 1944) | 1 | Current text only (IMPO's text, last changed 17 December 1974), to today |
| `ley-10597/` | FIJACION DE IMPUESTO. GANANCIAS ELEVADAS (Ley Nº 10.597 of 1944) | 1 | Current text only (IMPO's text, last changed 30 November 1960), to today |
| `ley-10709/` | COMISION HONORARIA PARA LA LUCHA ANTITUBERCULOSA. FONDO NACIONAL PERMANENTE PARA LA LUCHA ANTITUBERCULOSA. CREACION (Ley Nº 10.709 of 1946) | 1 | Current text only (IMPO's text, last changed 24 October 2013), to today |
| `ley-10757/` | LEY ORGANICA MILITAR. MODIFICACION (Ley Nº 10.757 of 1946) | 1 | Current text only (IMPO's text, last changed 14 May 1981), to today |
| `ley-10789/` | ELECCIONES NACIONALES. REGULACION (Ley Nº 10.789 of 1946) | 1 | Current text only (IMPO's text, last changed 23 September 1946), to today |
| `ley-10793/` | LEY DE REGISTROS PUBLICOS (Ley Nº 10.793 of 1946) | 1 | Current text only (IMPO's text, last changed 11 January 1994), to today |
| `ley-10808/` | LEY ORGANICA DE LA MARINA (Ley Nº 10.808 of 1946) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-10853/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 10.853 of 1946) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-10866/` | LEY DE CENTROS POBLADOS. MODIFICACION (Ley Nº 10.866 of 1946) | 1 | Current text only (IMPO's text, last changed 25 October 1946), to today |
| `ley-10940/` | CONSEJO NACIONAL DE SUBSISTENCIAS Y CONTRALOR DE PRECIOS. CREACION (Ley Nº 10.940 of 1947) | 1 | Current text only (IMPO's text, last changed 14 March 1973), to today |
| `ley-10976/` | BANCO HIPOTECARIO DEL URUGUAY (BHU). PRESTAMOS. VIVIENDA (Ley Nº 10.976 of 1947) | 1 | Current text only (IMPO's text, last changed 27 November 1975), to today |
| `ley-11182/` | CAJA DE JUBILACIONES Y PENSIONES ESCOLARES. MODIFICACION (Ley Nº 11.182 of 1948) | 1 | Current text only (IMPO's text, last changed 28 December 1964), to today |
| `ley-11285/` | ENSEÑANZA. PRESUPUESTO. MODIFICACION (Ley Nº 11.285 of 1949) | 1 | Current text only (IMPO's text, last changed 16 April 1968), to today |
| `ley-11326/` | EJERCITO. MARINA. FUNCIONARIOS MILITARES. REMUNERACIONES. FIJACION DE IMPUESTO (Ley Nº 11.326 of 1949) | 1 | Current text only (IMPO's text, last changed 7 September 1949), to today |
| `ley-11460/` | JUZGADOS. CREACION. DENOMINACION (Ley Nº 11.460 of 1950) | 1 | Current text only (IMPO's text, last changed 4 November 2011), to today |
| `ley-11474/` | DIRECCION GENERAL DE CORREOS. PRESUPUESTO (Ley Nº 11.474 of 1950) | 1 | Current text only (IMPO's text, last changed 21 February 2001), to today |
| `ley-11490/` | BANCO HIPOTECARIO DEL URUGUAY (BHU). AUTORIZACION. PRESTAMOS. FUNCIONARIOS. REMUNERACIONES (Ley Nº 11.490 of 1950) | 1 | Current text only (IMPO's text, last changed 20 April 1977), to today |
| `ley-11549/` | SERVICIO OFICIAL DE DIFUSION RADIO ELECTRICA (SODRE). PRESUPUESTO (Ley Nº 11.549 of 1950) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-11577/` | INDUSTRIAS INSALUBRES. CREACION DE LA COMISION HONORARIA DE TRABAJOS INSALUBRES (Ley Nº 11.577 of 1950) | 1 | Current text only (IMPO's text, last changed 14 October 1950), to today |
| `ley-11618/` | NEGOCIACION COLECTIVA. CONSEJOS DE SALARIOS. MODIFICACION (Ley Nº 11.618 of 1950) | 1 | Current text only (IMPO's text, last changed 7 November 1958), to today |
| `ley-11637/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS. BENEFICIO ESPECIAL DE RETIRO (Ley Nº 11.637 of 1951) | 1 | Current text only (IMPO's text, last changed 13 February 1967), to today |
| `ley-11638/` | DIRECCION GENERAL DE INMIGRACION. PRESUPUESTO (Ley Nº 11.638 of 1951) | 1 | Current text only (IMPO's text, last changed 29 December 1972), to today |
| `ley-11727/` | ELECCIONES NACIONALES. PLEBISCITO. REGLAMENTACION (Ley Nº 11.727 of 1951) | 1 | Current text only (IMPO's text, last changed 5 April 1962), to today |
| `ley-11759/` | JUZGADOS. REGISTROS PUBLICOS. MODIFICACION (Ley Nº 11.759 of 1951) | 1 | Current text only (IMPO's text, last changed 19 November 1951), to today |
| `ley-11908/` | NEGOCIACION COLECTIVA. CONSEJOS DE SALARIOS. TRABAJADORES. REMUNERACIONES. FISCALIZACION (Ley Nº 11.908 of 1952) | 1 | Current text only (IMPO's text, last changed 19 December 1952), to today |
| `ley-11923/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1953 (Ley Nº 11.923 of 1953) | 1 | Current text only (IMPO's text, last changed 8 October 1981), to today |
| `ley-11924/` | PRESUPUESTO (Ley Nº 11.924 of 1953) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-11925/` | CONTADURIA GENERAL DE LA NACION. NORMAS DE ORDENAMIENTO FINANCIERO. AMPLIACION (Ley Nº 11.925 of 1953) | 1 | Current text only (IMPO's text, last changed 10 November 1987), to today |
| `ley-11937/` | PODER EJECUTIVO. AUTORIZACION. DEUDA PUBLICA. EMISION (Ley Nº 11.937 of 1953) | 1 | Current text only (IMPO's text, last changed 15 May 1953), to today |
| `ley-12070/` | FUERZA AEREA MILITAR. CREACION (Ley Nº 12.070 of 1953) | 1 | Current text only (IMPO's text, last changed 20 December 1976), to today |
| `ley-12079/` | PRESUPUESTO. MODIFICACION (Ley Nº 12.079 of 1953) | 1 | Current text only (IMPO's text, last changed 30 November 1960), to today |
| `ley-12185/` | MODIFICACION DE LA LEY 10.757 RELATIVO AL REGIMEN DE ASCENSOS DE FUNCIONARIOS MILITARES (Ley Nº 12.185 of 1955) | 1 | Current text only (IMPO's text, last changed 15 February 1955), to today |
| `ley-12276/` | AUTORIZACION PARA LA EMISION DE DEUDA PUBLICA (Ley Nº 12.276 of 1956) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-12358/` | OTORGAMIENTO DE EXONERACIONES TRIBUTARIAS Y AMPLIACION DE LOS PRESTAMOS PARA VIVIENDA DEL BHU (Ley Nº 12.358 of 1957) | 1 | Current text only (IMPO's text, last changed 26 January 1957), to today |
| `ley-12376/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1957 (Ley Nº 12.376 of 1957) | 1 | Current text only (IMPO's text, last changed 20 October 2022), to today |
| `ley-12464/` | INCREMENTO DE LAS JUBILACIONES Y PENSIONES. ENERO 1958 (Ley Nº 12.464 of 1957) | 1 | Current text only (IMPO's text, last changed 22 November 1968), to today |
| `ley-12482/` | ASIGNACION DE RECURSOS PRESUPUESTALES (Ley Nº 12.482 of 1957) | 1 | Current text only (IMPO's text, last changed 30 November 1960), to today |
| `ley-12485/` | SE INSTITUYEN LAS CAJAS DE COMPENSACIONES Y ASIGNACIONES FAMILIARES (Ley Nº 12.485 of 1957) | 1 | Current text only (IMPO's text, last changed 26 December 1957), to today |
| `ley-12543/` | SEGURIDAD SOCIAL. ASIGNACIONES FAMILIARES. APORTES PATRONALES (Ley Nº 12.543 of 1958) | 1 | Current text only (IMPO's text, last changed 16 October 1958), to today |
| `ley-12613/` | MODIFICACIONES A LA REGLAMENTACION DE LA NAVEGACION Y COMERCIO DE CABOTAJE (Ley Nº 12.613 of 1959) | 1 | Current text only (IMPO's text, last changed 7 July 1959), to today |
| `ley-12691/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1959 (Ley Nº 12.691 of 1959) | 1 | Current text only (IMPO's text, last changed 31 March 1960), to today |
| `ley-12700/` | CREACION DEL IMPUESTO A LOS REMATES DE BIENES MUEBLES, INMUEBLES Y SEMOVIENTES (Ley Nº 12.700 of 1960) | 1 | Current text only (IMPO's text, last changed 19 October 1970), to today |
| `ley-12745/` | FUNCIONARIOS CONTRATADOS. SERVICIO DE COBRANZAS DOMICILIARIAS DE LA CAJA DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO (Ley Nº 12.745 of 1960) | 1 | Current text only (IMPO's text, last changed 16 August 1966), to today |
| `ley-12761/` | SEGURIDAD SOCIAL. JUBILACIONES Y PENSIONES (Ley Nº 12.761 of 1960) | 1 | Current text only (IMPO's text, last changed 10 June 1977), to today |
| `ley-12801/` | REESTRUCTURACION DEL PRESUPUESTO GENERAL DE SUELDOS Y GASTOS (Ley Nº 12.801 of 1960) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-12802/` | APROBACION DE NORMAS DE ORDENAMIENTO FINANCIERO (Ley Nº 12.802 of 1960) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-12803/` | PRESUPUESTO GENERAL DE SUELDOS Y GASTOS (Ley Nº 12.803 of 1960) | 1 | Current text only (IMPO's text, last changed 10 November 1987), to today |
| `ley-12938/` | LEY DE CONTROL Y ERRADICACION DE LA FIEBRE AFTOSA (Ley Nº 12.938 of 1961) | 1 | Current text only (IMPO's text, last changed 29 October 2002), to today |
| `ley-12950/` | TESORO DE OBRAS PUBLICAS. TRIBUTOS A LOS COMBUSTIBLES GRASAS Y LUBRICANTES. IMPUESTO ADICIONAL A LA CONTRIBUCION INMOBILIARIA. IMPUESTO A LA VENTA DE LAS CAMARAS Y CUBIERTAS DE VEHICULOS AUTOMOTORES. IMPUESTO A LOS EJES. IMPUESTO A LOS INGRESOS BRUTOS DE LAS EMPRESAS DE TRANSPORTE DE PASAJEROS (Ley Nº 12.950 of 1961) | 1 | Current text only (IMPO's text, last changed 4 June 2003), to today |
| `ley-12990/` | MODIFICACIONES A LA LEY ORGANICA DE LA MARINA (Ley Nº 12.990 of 1961) | 1 | Current text only (IMPO's text, last changed 26 November 1961), to today |
| `ley-12996/` | SEGURIDAD SOCIAL. JUBILACIONES Y PENSIONES CIVILES Y ESCOLARES, RURALES Y DOMESTICOS, INDUSTRIA Y COMERCIO (Ley Nº 12.996 of 1961) | 1 | Current text only (IMPO's text, last changed 24 December 1986), to today |
| `ley-13032/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1960 (Ley Nº 13.032 of 1961) | 1 | Current text only (IMPO's text, last changed 10 November 1987), to today |
| `ley-13041/` | DECLARACION DE VALIDEZ DE LAS INSCRIPCIONES Y REINSCRIPCIONES INCORPORADAS AL REGISTRO CIVICO NACIONAL (Ley Nº 13.041 of 1962) | 1 | Current text only (IMPO's text, last changed 5 April 1962), to today |
| `ley-13102/` | REGIMEN DE IMPORTACION DE VEHICULOS AUTOMOTORES PARA PERSONAS CON DISCAPACIDAD (Ley Nº 13.102 of 1962) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-13145/` | MODIFICACIONES A LAS LEYES ORGANICAS DE LAS FUERZAS ARMADAS Y DE LA ARMADA NACIONAL. FUNCIONARIOS MILITARES (Ley Nº 13.145 of 1963) | 1 | Current text only (IMPO's text, last changed 9 July 1963), to today |
| `ley-13241/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1962 (Ley Nº 13.241 of 1964) | 1 | Current text only (IMPO's text, last changed 5 January 1978), to today |
| `ley-13292/` | ARRENDAMIENTOS URBANOS. SUSPENSION DE DESALOJOS Y LANZAMIENTOS (Ley Nº 13.292 of 1964) | 1 | Current text only (IMPO's text, last changed 2 December 1965), to today |
| `ley-13296/` | REGIMEN DE REAJUSTE DE JUBILACIONES Y PENSIONES. OCTUBRE 1964 (Ley Nº 13.296 of 1964) | 1 | Current text only (IMPO's text, last changed 13 February 1967), to today |
| `ley-13315/` | SEGURIDAD SOCIAL. AJUSTE DE TOPES JUBILATORIOS Y FIJACION DE SUELDOS FICTOS DE DIRECTORES DE S.A. (Ley Nº 13.315 of 1964) | 1 | Current text only (IMPO's text, last changed 2 December 1965), to today |
| `ley-13317/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES - MODIFICACIONES A LA LEY 12801 (Ley Nº 13.317 of 1964) | 1 | Current text only (IMPO's text, last changed 8 April 1986), to today |
| `ley-13318/` | APROBACION DE NORMAS DE ORDENAMIENTO FINANCIERO. INFRACCIONES Y PROCEDIMIENTOS ADUANEROS. INGRESO A LA ADMINISTRACION PUBLICA (Ley Nº 13.318 of 1964) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-13319/` | RECURSOS PARA EL PRESUPUESTO GENERAL DE SUELDOS Y GASTOS (Ley Nº 13.319 of 1964) | 1 | Current text only (IMPO's text, last changed 5 January 1996), to today |
| `ley-13320/` | PRESUPUESTO GENERAL DE SUELDOS Y GASTOS (Ley Nº 13.320 of 1964) | 1 | Current text only (IMPO's text, last changed 9 May 1980), to today |
| `ley-13349/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1963 (Ley Nº 13.349 of 1965) | 1 | Current text only (IMPO's text, last changed 28 August 1975), to today |
| `ley-13355/` | LEY DE ABREVIACION DE JUICIOS. MODIFICACIONES AL CODIGO DE PROCEDIMIENTO CIVIL (Ley Nº 13.355 of 1965) | 1 | Current text only (IMPO's text, last changed 19 September 1983), to today |
| `ley-13420/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1964 (Ley Nº 13.420 of 1965) | 1 | Current text only (IMPO's text, last changed 28 September 1997), to today |
| `ley-13426/` | FIJACION DE AUMENTO EN PASIVIDADES (Ley Nº 13.426 of 1965) | 1 | Current text only (IMPO's text, last changed 14 October 2016), to today |
| `ley-13453/` | EXTENSION DE LA EXPLOTACION OTORGADA AL PODER EJECUTIVO DE CASINOS. PUNTA DEL ESTE. SAN RAFAEL. ATLANTIDA. PIRIAPOLIS. RIVERA. CARMELO (Ley Nº 13.453 of 1965) | 1 | Current text only (IMPO's text, last changed 5 January 1996), to today |
| `ley-13556/` | LICENCIAS ANUALES DE LOS EMPLEADOS PRIVADOS. CONVENIOS COLECTIVOS DE TRABAJO (Ley Nº 13.556 of 1966) | 1 | Current text only (IMPO's text, last changed 19 December 1974), to today |
| `ley-13581/` | PRESTAMOS PARA LA ADQUISICION DE VIVIENDAS PARA FUNCIONARIOS (Ley Nº 13.581 of 1966) | 1 | Current text only (IMPO's text, last changed 15 December 1978), to today |
| `ley-13586/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1965 (Ley Nº 13.586 of 1967) | 1 | Current text only (IMPO's text, last changed 27 November 1987), to today |
| `ley-13596/` | TRIBUTOS. REGIMEN DE FACILIDADES DE PAGO (Ley Nº 13.596 of 1967) | 1 | Current text only (IMPO's text, last changed 28 December 1979), to today |
| `ley-13608/` | LEY DE EMERGENCIA. SE ESTABLECEN NORMAS SOBRE POLITICA TRIBUTARIA, BANCARIA, COMERCIO EXTERIOR Y FOMENTO INDUSTRIAL, PRECIOS, INGRESOS, SEGURIDAD SOCIAL Y OBRAS PUBLICAS (Ley Nº 13.608 of 1967) | 1 | Current text only (IMPO's text, last changed 25 June 1999), to today |
| `ley-13637/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES (Ley Nº 13.637 of 1967) | 1 | Current text only (IMPO's text, last changed 15 October 2018), to today |
| `ley-13640/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1968 1972 (Ley Nº 13.640 of 1967) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-13659/` | ARRENDAMIENTOS. REGIMEN DE ALQUILERES, DESALOJOS Y LANZAMIENTOS (Ley Nº 13.659 of 1968) | 1 | Current text only (IMPO's text, last changed 14 March 1973), to today |
| `ley-13665/` | REGISTROS DE LA OFICINA DE IMPUESTOS INTERNOS Y DE LA DIRECCION DE CONTRALOR LEGAL. DIRECCION GENERAL IMPOSITIVA Y MINISTERIO DE GANADERIA Y AGRICULTURA (Ley Nº 13.665 of 1968) | 1 | Current text only (IMPO's text, last changed 17 June 1968), to today |
| `ley-13695/` | APROBACION DEL TEXTO ORDENADO 1968 (Ley Nº 13.695 of 1968) | 1 | Current text only (IMPO's text, last changed 23 December 1993), to today |
| `ley-13728/` | PLAN NACIONAL DE VIVIENDAS (Ley Nº 13.728 of 1968) | 1 | Current text only (IMPO's text, last changed 3 November 2021), to today |
| `ley-13737/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIOS 1966 Y 1967 (Ley Nº 13.737 of 1969) | 1 | Current text only (IMPO's text, last changed 14 September 2012), to today |
| `ley-13782/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. RENTA NETA (Ley Nº 13.782 of 1969) | 1 | Current text only (IMPO's text, last changed 19 September 2014), to today |
| `ley-13797/` | PRORROGA DE AUTORIZACION PARA EXPLOTACION DE CASINOS. PUNTA DEL ESTE. SAN RAFAEL. ATLANTIDA. PIRIAPOLIS. RIVERA. CARMELO (Ley Nº 13.797 of 1969) | 1 | Current text only (IMPO's text, last changed 30 November 1970), to today |
| `ley-13835/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1968 (Ley Nº 13.835 of 1970) | 1 | Current text only (IMPO's text, last changed 15 October 2018), to today |
| `ley-13870/` | ARRENDAMIENTOS RURALES. SUSPENSION DE LANZAMIENTOS CONTRA ARRENDATARIOS Y SUBARRENDATARIOS BUENOS PAGADORES Y SUS EXCEPCIONES (Ley Nº 13.870 of 1970) | 1 | Current text only (IMPO's text, last changed 3 September 1974), to today |
| `ley-13892/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1969 (Ley Nº 13.892 of 1970) | 1 | Current text only (IMPO's text, last changed 31 August 2007), to today |
| `ley-13899/` | EXPROPIACIONES PARA OBRAS EN RUTAS NACIONALES (Ley Nº 13.899 of 1970) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-13958/` | ESTABLECIMIENTO DE SERVIDUMBRE PARA OBRAS DE APROVECHAMIENTO HIDROELECTRICO DEL RIO URUGUAY - CREACION DEL FONDO ENERGETICO NACIONAL - EMISION DE BONOS ENERGETICOS REAJUSTABLES (Ley Nº 13.958 of 1971) | 1 | Current text only (IMPO's text, last changed 30 April 1974), to today |
| `ley-14057/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1970 (Ley Nº 14.057 of 1972) | 1 | Current text only (IMPO's text, last changed 28 August 2014), to today |
| `ley-14095/` | TIPIFICACION DE DELITOS ECONOMICOS DEL BANCO CENTRAL DEL URUGUAY Y CREACION DE UN CUERPO ESPECIAL DE PREVENCION Y REPRESION DE DELITOS ECONOMICOS (Ley Nº 14.095 of 1972) | 1 | Current text only (IMPO's text, last changed 5 December 2007), to today |
| `ley-14100/` | LEY DE PRESUPUESTO NACIONAL DE RECURSOS. IRPF. IRIC (Ley Nº 14.100 of 1972) | 1 | Current text only (IMPO's text, last changed 29 October 1991), to today |
| `ley-14106/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1973 1976 (Ley Nº 14.106 of 1973) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-14127/` | ASIGNACION DE RECURSOS. CORTE ELECTORAL. INSCRIPCION EN EL REGISTRO CIVICO NACIONAL (Ley Nº 14.127 of 1973) | 1 | Current text only (IMPO's text, last changed 17 May 1973), to today |
| `ley-15757/` | LEY DE CREACION DE LA OFICINA NACIONAL DEL SERVICIO CIVIL (Ley Nº 15.757 of 1985) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-15767/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL - EJERCICIO 1984 (Ley Nº 15.767 of 1985) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-15768/` | MODIFICACION DEL TEXTO ORDENADO DGI, RELATIVO AL IMPUESTO AL PATRIMONIO E IMPUESTO A LAS RENTAS AGROPECUARIAS (Ley Nº 15.768 of 1985) | 1 | Current text only (IMPO's text, last changed 13 September 1985), to today |
| `ley-15770/` | COMPETENCIAS DE JUZGADOS LETRADOS DE PRIMERA INSTANCIA EN LO CIVIL - LOT (Ley Nº 15.770 of 1985) | 1 | Current text only (IMPO's text, last changed 16 September 1985), to today |
| `ley-15783/` | LEY DE FUNCIONARIOS DESTITUIDOS (Ley Nº 15.783 of 1985) | 1 | Current text only (IMPO's text, last changed 12 July 1991), to today |
| `ley-15799/` | LEY DE ARRENDAMIENTOS URBANOS Y SUBURBANOS - LEY DE EMERGENCIA (Ley Nº 15.799 of 1985) | 1 | Current text only (IMPO's text, last changed 19 December 2005), to today |
| `ley-15808/` | FUNCIONARIOS MILITARES (Ley Nº 15.808 of 1986) | 1 | Current text only (IMPO's text, last changed 7 April 1986), to today |
| `ley-15809/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1985 1990 (Ley Nº 15.809 of 1986) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-15851/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1985 (Ley Nº 15.851 of 1986) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-15863/` | PASIVIDADES - INCOMPATIBILIDADES (Ley Nº 15.863 of 1987) | 1 | Current text only (IMPO's text, last changed 22 May 1987), to today |
| `ley-15881/` | PROCESOS JUDICIALES - ORGANIZACION DE LOS TRIBUNALES (Ley Nº 15.881 of 1987) | 1 | Current text only (IMPO's text, last changed 20 September 2024), to today |
| `ley-15896/` | REGULACION DE LAS HABILITACIONES QUE OTORGA LA DIRECCION NACIONAL DE BOMBEROS (Ley Nº 15.896 of 1987) | 1 | Current text only (IMPO's text, last changed 20 September 2024), to today |
| `ley-15903/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1986 (Ley Nº 15.903 of 1987) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-15913/` | LEY DEL LIBRO. DECLARACION DE INTERES NACIONAL (Ley Nº 15.913 of 1987) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-16002/` | MODIFICACION DEL PLAN DE INVERSIONES. EJERCICIO 1988 - 1989 (Ley Nº 16.002 of 1988) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-16011/` | REGULACION DE DISPOSICIONES RELATIVA A LA ACCION DE AMPARO (Ley Nº 16.011 of 1988) | 1 | Current text only (IMPO's text, last changed 19 December 1988), to today |
| `ley-16017/` | MODIFICACION DE LA LEY DE ELECCIONES (Ley Nº 16.017 of 1989) | 1 | Current text only (IMPO's text, last changed 19 April 2019), to today |
| `ley-16053/` | MODIFICACION AL CODIGO GENERAL DEL PROCESO - VIGENCIA (Ley Nº 16.053 of 1989) | 1 | Current text only (IMPO's text, last changed 20 July 1989), to today |
| `ley-16082/` | DECLARACION DE INTERES NACIONAL - FIEBRE AFTOSA (Ley Nº 16.082 of 1989) | 1 | Current text only (IMPO's text, last changed 7 November 2012), to today |
| `ley-16097/` | COMISION HONORARIA DE LUCHA CONTRA EL CANCER. CREACION. COMETIDOS (Ley Nº 16.097 of 1989) | 1 | Current text only (IMPO's text, last changed 29 October 1991), to today |
| `ley-16101/` | TURISMO - REGISTRO DE EMPRESAS DE TURISMO SOCIAL - SALARIO VACACIONAL (Ley Nº 16.101 of 1989) | 1 | Current text only (IMPO's text, last changed 10 November 1989), to today |
| `ley-16105/` | APROBACION DE LA RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1988 (Ley Nº 16.105 of 1990) | 1 | Current text only (IMPO's text, last changed 20 October 2022), to today |
| `ley-16107/` | FIJACION DE AJUSTE FISCAL TRIBUTARIO Y APORTACION AL BPS (Ley Nº 16.107 of 1990) | 1 | Current text only (IMPO's text, last changed 21 February 2001), to today |
| `ley-16127/` | DESIGNACION, ASCENSOS E INCENTIVOS PARA FUNCIONARIOS PUBLICOS (Ley Nº 16.127 of 1990) | 1 | Current text only (IMPO's text, last changed 25 September 2017), to today |
| `ley-16134/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1989 (Ley Nº 16.134 of 1990) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16170/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1990 - 1994 (Ley Nº 16.170 of 1990) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16211/` | LEY DE EMPRESAS PUBLICAS (Ley Nº 16.211 of 1991) | 1 | Current text only (IMPO's text, last changed 3 November 2021), to today |
| `ley-16226/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1990 (Ley Nº 16.226 of 1991) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16244/` | REGIMEN DE REFINANCIACION DE DEUDAS POR OBLIGACIONES TRIBUTARIAS CON EL BANCO DE PREVISION SOCIAL (Ley Nº 16.244 of 1992) | 1 | Current text only (IMPO's text, last changed 20 October 2022), to today |
| `ley-16298/` | REGULACION DE LOS CERTIFICADOS EXPEDIDOS POR EL BPS POR ENAJENACIONES QUE SE LLEVAN A CABO POR EXPROPIACION (Ley Nº 16.298 of 1992) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-16320/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1991 (Ley Nº 16.320 of 1992) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-16333/` | MODIFICACION DEL DECRETO LEY 14.157, REFERENTE AL PERSONAL MILITAR Y POLICIAL EN ACTIVIDAD Y EN RETIRO (Ley Nº 16.333 of 1992) | 1 | Current text only (IMPO's text, last changed 7 November 2012), to today |
| `ley-16343/` | INSTALACION Y FUNCIONAMIENTO DE LOS INSTITUTOS DE MEDICINA ALTAMENTE ESPECIALIZADA (Ley Nº 16.343 of 1992) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16387/` | MARINA MERCANTE (Ley Nº 16.387 of 1993) | 1 | Current text only (IMPO's text, last changed 6 October 2008), to today |
| `ley-16389/` | MODIFICACION AL CODIGO RURAL (Ley Nº 16.389 of 1993) | 1 | Current text only (IMPO's text, last changed 6 July 1993), to today |
| `ley-16426/` | SEGUROS (Ley Nº 16.426 of 1993) | 1 | Current text only (IMPO's text, last changed 26 October 2018), to today |
| `ley-16462/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 1992 (Ley Nº 16.462 of 1994) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16568/` | CASINOS DEL ESTADO - FUNCIONARIOS (Ley Nº 16.568 of 1994) | 1 | Current text only (IMPO's text, last changed 27 December 2010), to today |
| `ley-16685/` | ADMINISTRACION DE JUSTICIA - MENORES ABANDONADOS (Ley Nº 16.685 of 1994) | 1 | Current text only (IMPO's text, last changed 21 December 1994), to today |
| `ley-16694/` | IMPUESTO A LOS REMATES DE BIENES MUEBLES INMUEBLES Y SEMOVIENTES (Ley Nº 16.694 of 1995) | 1 | Current text only (IMPO's text, last changed 27 March 1996), to today |
| `ley-16696/` | CARTA ORGANICA DEL BANCO CENTRAL DEL URUGUAY (Ley Nº 16.696 of 1995) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16697/` | LEY DE AJUSTE FISCAL. NUEVO REGIMEN FISCAL Y DE MEJORA DE LA COMPETITIVIDAD DEL SECTOR PRODUCTIVO (Ley Nº 16.697 of 1995) | 1 | Current text only (IMPO's text, last changed 19 December 2005), to today |
| `ley-16720/` | SANIDAD MILITAR. DIRECCION NACIONAL DE SANIDAD DE LAS FUERZAS ARMADAS (Ley Nº 16.720 of 1995) | 1 | Current text only (IMPO's text, last changed 4 November 2011), to today |
| `ley-16736/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 1995 1999 (Ley Nº 16.736 of 1996) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-16737/` | APROBACION DE LAS ENMIENDAS A LOS ARTS. 24 Y 25 DE LA CONSTITUCION DE LA ORGANIZACION MUNDIAL DE LA SALUD (OMS) (Ley Nº 16.737 of 1996) | 1 | Current text only (IMPO's text, last changed 9 January 1996), to today |
| `ley-16747/` | DECLARACION DE PLAGA NACIONAL. PIOJERA OVINA (Ley Nº 16.747 of 1996) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-16812/` | EMISION BONOS DEL TESORO Y LETRAS DE TESORERIA (Ley Nº 16.812 of 1997) | 1 | Current text only (IMPO's text, last changed 14 March 1997), to today |
| `ley-16838/` | SOCIEDADES COMERCIALES (Ley Nº 16.838 of 1997) | 1 | Current text only (IMPO's text, last changed 1 July 1997), to today |
| `ley-16851/` | SEGUROS (Ley Nº 16.851 of 1997) | 1 | Current text only (IMPO's text, last changed 15 July 1997), to today |
| `ley-16883/` | TRABAJADORES RURALES. SEGURIDAD SOCIAL. APORTES (Ley Nº 16.883 of 1997) | 1 | Current text only (IMPO's text, last changed 10 November 1997), to today |
| `ley-16901/` | LEY DE REGISTROS PUBLICOS - VIGENCIA (Ley Nº 16.901 of 1997) | 1 | Current text only (IMPO's text, last changed 26 December 1997), to today |
| `ley-16911/` | FUNCIONARIOS POLICIALES (Ley Nº 16.911 of 1998) | 1 | Current text only (IMPO's text, last changed 13 February 1998), to today |
| `ley-16995/` | CODIGO GENERAL DEL PROCESO - LEY PROCESAL CIVIL (Ley Nº 16.995 of 1998) | 1 | Current text only (IMPO's text, last changed 26 August 1998), to today |
| `ley-17036/` | SEGURIDAD SOCIAL - FUNCIONARIOS MILITARES (Ley Nº 17.036 of 1998) | 1 | Current text only (IMPO's text, last changed 20 November 1998), to today |
| `ley-17243/` | LEY DE URGENCIA. SERVICIOS PUBLICOS Y PRIVADOS. FOMENTO DEL EMPLEO Y LA INVERSION (Ley Nº 17.243 of 2000) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-17292/` | LEY DE URGENCIA. ADMINISTRACION PUBLICA. FOMENTO Y MEJORAS DEL EMPLEO (Ley Nº 17.292 of 2001) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-17296/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 2000 2004 (Ley Nº 17.296 of 2001) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-17309/` | CREACION DEL IMPUESTO ESPECIFICO A LOS SERVICIOS DE SALUD (Ley Nº 17.309 of 2001) | 2 | Current text only (IMPO's text, last changed 30 March 2001), then repealed by Ley 18.083 (in force 1 July 2007) |
| `ley-17437/` | SEGURIDAD SOCIAL. PROFESIONALES UNIVERSITARIOS (Ley Nº 17.437 of 2001) | 1 | Current text only (IMPO's text, last changed 2 May 2023), to today |
| `ley-17451/` | PERSONAS PUBLICAS NO ESTATALES. FONDO DE SOLIDARIDAD (Ley Nº 17.451 of 2002) | 1 | Current text only (IMPO's text, last changed 10 January 2002), to today |
| `ley-17453/` | LEY DE AJUSTE FISCAL (Ley Nº 17.453 of 2002) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-17502/` | LEY DE ESTABILIDAD FINANCIERA (Ley Nº 17.502 of 2002) | 1 | Current text only (IMPO's text, last changed 10 December 2002), to today |
| `ley-17503/` | CREACION DEL FONDO DE RECONSTRUCCION Y FOMENTO DE LA GRANJA (FRFG) (Ley Nº 17.503 of 2002) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-17523/` | LEY DE FORTALECIMIENTO DEL SISTEMA BANCARIO (Ley Nº 17.523 of 2002) | 1 | Current text only (IMPO's text, last changed 21 September 2018), to today |
| `ley-17524/` | TELECOMUNICACIONES - TELEFONIA CELULAR - TELEFONIA BASICA (Ley Nº 17.524 of 2002) | 1 | Current text only (IMPO's text, last changed 5 August 2002), to today |
| `ley-17542/` | MODIFICACION A LA LEY DE CHEQUES (Ley Nº 17.542 of 2002) | 1 | Current text only (IMPO's text, last changed 21 August 2002), to today |
| `ley-17555/` | APROBACION DE LA LEY DE REACTIVACION ECONOMICA. INDUSTRIA DE LA CONSTRUCCION (Ley Nº 17.555 of 2002) | 1 | Current text only (IMPO's text, last changed 3 November 2021), to today |
| `ley-17556/` | RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2001 (Ley Nº 17.556 of 2002) | 1 | Current text only (IMPO's text, last changed 20 October 2022), to today |
| `ley-17579/` | FUNCIONARIOS MILITARES - RETIRO MILITAR - RETIRO OBLIGATORIO (Ley Nº 17.579 of 2002) | 1 | Current text only (IMPO's text, last changed 29 October 2002), to today |
| `ley-17596/` | ENTES AUTONOMOS - MODIFICACION A LA CARTA ORGANICA DEL BANCO HIPOTECARIO DEL URUGUAY (Ley Nº 17.596 of 2002) | 1 | Current text only (IMPO's text, last changed 27 April 2007), to today |
| `ley-17663/` | CREACION DEL FONDO DE FINANCIAMIENTO Y RECOMPOSICION DE LA ACTIVIDAD ARROCERA (Ley Nº 17.663 of 2003) | 1 | Current text only (IMPO's text, last changed 14 October 2016), to today |
| `ley-17678/` | PROHIBICION DE INGRESO DE FUNCIONARIOS A LA ADMINISTRACION PUBLICA. EXCEPCION PERSONAS CON DISCAPACIDADES (Ley Nº 17.678 of 2003) | 1 | Current text only (IMPO's text, last changed 27 December 2006), to today |
| `ley-17707/` | MODIFICACION DEL CGP Y DE LA LEY ORGANICA DE LA JUDICATURA Y DE ORGANIZACION DE LOS TRIBUNALES (Ley Nº 17.707 of 2003) | 1 | Current text only (IMPO's text, last changed 7 November 2012), to today |
| `ley-17726/` | MODIFICACIONES AL CODIGO DEL PROCESO PENAL. PRISION PREVENTIVA DEL PROCESADO PRIMARIO. FALTAS O DELITOS PENADOS CON MULTA, SUSPENSION O INHABILITACION (Ley Nº 17.726 of 2003) | 1 | Current text only (IMPO's text, last changed 26 December 2003), to today |
| `ley-17735/` | AUTORIZACION AL MGAP LA TRANSFERENCIA DE LA TITULARIDAD DE LOS SILOS, PLANTAS, GRANEROS, ETC. A SUS ACTUALES TENEDORES. MODIFICACION (Ley Nº 17.735 of 2004) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-17792/` | CONSTITUCION DE UNA FUNDACION CON EL "INSTITUT PASTEUR"(FRANCIA) CON FINES DE INVESTIGACION (Ley Nº 17.792 of 2004) | 1 | Current text only (IMPO's text, last changed 15 October 2018), to today |
| `ley-17829/` | REGIMEN DE RETENCIONES A LOS SALARIOS Y PASIVIDADES (Ley Nº 17.829 of 2004) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-17841/` | LEY DE REESTRUCTURA Y FORTALECIMIENTO DEL SISTEMA FINANCIERO. CREACION DEL IMPUESTO A LOS SUELDOS Y PASIVIDADES BANCARIAS (Ley Nº 17.841 of 2004) | 1 | Current text only (IMPO's text, last changed 15 October 2004), to today |
| `ley-17843/` | EXONERACIONES A LA ACTIVIDAD FORESTAL (Ley Nº 17.843 of 2004) | 1 | Current text only (IMPO's text, last changed 21 October 2004), to today |
| `ley-17904/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2004 (Ley Nº 17.904 of 2005) | 1 | Current text only (IMPO's text, last changed 15 October 2018), to today |
| `ley-17921/` | DEROGACIONES A LA LEY ORGANICA DE LAS FUERZAS ARMADAS (Ley Nº 17.921 of 2005) | 1 | Current text only (IMPO's text, last changed 22 November 2005), to today |
| `ley-17930/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 2005 - 2009 (Ley Nº 17.930 of 2005) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-17945/` | LEY INTERPRETATIVA. COMPATIBILIDAD DE JUBILACION SERVIDA POR CAJA DE PROFESIONALES UNIVERSITARIOS (Ley Nº 17.945 of 2006) | 1 | Current text only (IMPO's text, last changed 5 January 2006), to today |
| `ley-17950/` | CREACION DEL SISTEMA NACIONAL DE ACREDITACION DE VETERINARIOS DE LIBRE EJERCICIO (Ley Nº 17.950 of 2006) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18046/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2005 (Ley Nº 18.046 of 2006) | 1 | Current text only (IMPO's text, last changed 3 November 2021), to today |
| `ley-18083/` | LEY DE REFORMA TRIBUTARIA (Ley Nº 18.083 of 2006) | 1 | Current text only (IMPO's text, last changed 12 March 2026), to today |
| `ley-18089/` | DEROGACION DE LA TASA "TIMBRE PALACIO DE JUSTICIA" Y DEL "TIMBRE INFRAESTRUCTURA JUDICIAL" (Ley Nº 18.089 of 2007) | 1 | Current text only (IMPO's text, last changed 7 January 2007), to today |
| `ley-18098/` | EMPRESAS PUBLICAS - CONTRATACION DE SERVICIOS CON TERCEROS (Ley Nº 18.098 of 2007) | 1 | Current text only (IMPO's text, last changed 12 January 2007), to today |
| `ley-18100/` | CREACION DEL FONDO DE FINANCIAMIENTO Y DESARROLLO SUSTENTABLE DE LA ACTIVIDAD LECHERA (FFDSAL) (Ley Nº 18.100 of 2007) | 1 | Current text only (IMPO's text, last changed 24 May 2024), to today |
| `ley-18127/` | FIDEICOMISOS FINANCIEROS. REGIMEN TRIBUTARIO ESPECIAL (Ley Nº 18.127 of 2007) | 1 | Current text only (IMPO's text, last changed 12 May 2007), to today |
| `ley-18172/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2006 (Ley Nº 18.172 of 2007) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18220/` | SISTEMA NACIONAL DE ARCHIVOS. REGULACION DE LA FUNCION ARCHIVISTICA. CONSERVACION Y ORGANIZACION DEL PATRIMONIO DOCUMENTAL DE LA NACION (Ley Nº 18.220 of 2007) | 1 | Current text only (IMPO's text, last changed 20 December 2007), to today |
| `ley-18222/` | OBLIGACION DEL BPS A REALIZAR RETENCIONES DE PASIVIDADES (Ley Nº 18.222 of 2007) | 1 | Current text only (IMPO's text, last changed 20 December 2007), to today |
| `ley-18268/` | DECLARACION DE INTERES NACIONAL. LUCHA CONTRA LA GARRAPATA COMUN DE BOVINO (Ley Nº 18.268 of 2008) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-18283/` | CREACION DEL REGISTRO DE PENSIONES. MINISTERIO DE VIVIENDA ORDENAMIENTO TERRITORIAL Y MEDIO AMBIENTE (Ley Nº 18.283 of 2008) | 1 | Current text only (IMPO's text, last changed 16 May 2008), to today |
| `ley-18314/` | SEGURIDAD SOCIAL. JUBILACIONES Y PENSIONES (Ley Nº 18.314 of 2008) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18358/` | RETENCIONES SOBRE SUELDOS Y PASIVIDADES (Ley Nº 18.358 of 2008) | 1 | Current text only (IMPO's text, last changed 26 September 2008), to today |
| `ley-18362/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2007 (Ley Nº 18.362 of 2008) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18385/` | INSCRIPCION PREDIOS PERTENECIENTES A COLONIAS DEL INSTITUTO NACIONAL DE COLONIZACION. PRORROGA DE PLAZO (Ley Nº 18.385 of 2008) | 1 | Current text only (IMPO's text, last changed 17 October 2008), to today |
| `ley-18395/` | MODIFICACIONES A LA LEY 16.713 DE SEGURIDAD SOCIAL. FLEXIBILIZACION DEL REGIMEN DE ACCESO A BENEFICIOS JUBILATORIOS (Ley Nº 18.395 of 2008) | 1 | Current text only (IMPO's text, last changed 2 May 2023), to today |
| `ley-18401/` | CARTA ORGANICA DEL BANCO CENTRAL DEL URUGUAY. MODIFICACION (Ley Nº 18.401 of 2008) | 1 | Current text only (IMPO's text, last changed 19 March 2026), to today |
| `ley-18410/` | DENOMINACION DE ESCUELA Nº 139. MONTEVIDEO (Ley Nº 18.410 of 2008) | 1 | Current text only (IMPO's text, last changed 30 October 2008), to today |
| `ley-18440/` | ADECUACION DE LAS COOPERATIVAS DE PROFESIONALES DE LA SALUD A LA NORMATIVA VIGENTE PARA LAS COOPERATIVAS DE TRABAJO. (Ley Nº 18.440 of 2008) | 1 | Current text only (IMPO's text, last changed 24 December 2008), to today |
| `ley-18465/` | FIJACION DE MEDIDAS PARA REDUCIR LOS INDICES DE INFLACION (Ley Nº 18.465 of 2009) | 1 | Current text only (IMPO's text, last changed 11 February 2009), to today |
| `ley-18486/` | COLONIZACION DE TIERRAS. REGULACION. PRORROGA (Ley Nº 18.486 of 2009) | 1 | Current text only (IMPO's text, last changed 15 May 2009), to today |
| `ley-18487/` | PARTICIPACION EQUITATIVA DE PERSONAS DE AMBOS SEXOS EN LA INTEGRACION DE LOS ORGANOS ELECTIVOS Y DIRECCION DE PARTIDOS POLITICOS. SISTEMA DE SUPLENTES (Ley Nº 18.487 of 2009) | 1 | Current text only (IMPO's text, last changed 15 May 2009), to today |
| `ley-18491/` | SEGURO OBLIGATORIO DE AUTOMOTORES POR ACCIDENTES QUE CAUSEN DAÑOS A TERCEROS. PRORROGA (Ley Nº 18.491 of 2009) | 1 | Current text only (IMPO's text, last changed 22 May 2009), to today |
| `ley-18498/` | LEY DE PESCA. MODIFICACION. INTEGRACION DE TRIPULACION EN BUQUES DE MATRICULA NACIONAL (Ley Nº 18.498 of 2009) | 1 | Current text only (IMPO's text, last changed 12 June 2009), to today |
| `ley-18564/` | REGULACION DEL USO Y MANEJO DE LAS AGUAS Y EL SUELO. SANCIONES POR INCUMPLIMIENTO (Ley Nº 18.564 of 2009) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-18573/` | SISTEMAS DE COMPENSACION Y LIQUIDACION DE PAGOS Y VALORES. REGULACION Y SUPERVISION (Ley Nº 18.573 of 2009) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18574/` | OTORGAMIENTO DE PRESTAMOS HIPOTECARIOS PARA VIVIENDA. NOTAS DE CREDITO HIPOTECARIAS (Ley Nº 18.574 of 2009) | 1 | Current text only (IMPO's text, last changed 14 September 2009), to today |
| `ley-18588/` | ESTUPEFACIENTES Y SUSTANCIAS SICOTROPICAS (Ley Nº 18.588 of 2009) | 1 | Current text only (IMPO's text, last changed 18 September 2009), to today |
| `ley-18663/` | COLONIZACION DE TIERRAS. REGULACION. PRORROGA (Ley Nº 18.663 of 2010) | 1 | Current text only (IMPO's text, last changed 27 May 2010), to today |
| `ley-18705/` | LEY DE COOPERATIVAS. PRORROGA PARA ADAPTACION DE ESTATUTOS (Ley Nº 18.705 of 2010) | 1 | Current text only (IMPO's text, last changed 25 November 2010), to today |
| `ley-18719/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 2010 - 2014 (Ley Nº 18.719 of 2010) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18728/` | SISTEMA NACIONAL DE SALUD. FONASA. INCORPORACION DE NUEVOS AFILIADOS. EX FUNCIONARIOS JUBILADOS DE OSE Y DE CHASSFOSE (Ley Nº 18.728 of 2011) | 1 | Current text only (IMPO's text, last changed 5 January 2011), to today |
| `ley-18731/` | INCORPORACION DE NUEVOS AFILIADOS AL SEGURO NACIONAL DE SALUD (Ley Nº 18.731 of 2011) | 1 | Current text only (IMPO's text, last changed 6 July 2012), to today |
| `ley-18756/` | DEROGACIONES Y MODIFICACIONES A LA LEY 11.029 RELATIVO AL INSTITUTO NACIONAL DE COLONIZACION (Ley Nº 18.756 of 2011) | 1 | Current text only (IMPO's text, last changed 9 July 2020), to today |
| `ley-18783/` | DEROGACION DEL ART. 178 DE LA LEY 16.713 RELATIVO A LAS CONTRIBUCIONES ESPECIALES DE EMPRESAS UNIPERSONALES (Ley Nº 18.783 of 2011) | 1 | Current text only (IMPO's text, last changed 19 July 2011), to today |
| `ley-18788/` | REGIMEN DE FACILIDADES DE OBLIGACIONES TRIBUTARIAS. ACTUALIZACION DE SANCIONES. JUICIO EJECUTIVO TRIBUTARIO (Ley Nº 18.788 of 2011) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18793/` | INCLUSION EN EL REGIMEN DE FISCALIZACION DE TRANSITO VEHICULAR DISPUESTO EN EL ART. 46 DE LA LEY 18.191 AL PERSONAL DE LA PREFECTURA NACIONAL NAVAL (Ley Nº 18.793 of 2011) | 1 | Current text only (IMPO's text, last changed 12 August 2011), to today |
| `ley-18834/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2010 (Ley Nº 18.834 of 2011) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-18846/` | FORTALECIMIENTO Y DESARROLLO DE LA INDUSTRIA NACIONAL DE LA VESTIMENTA (Ley Nº 18.846 of 2011) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-18860/` | CREACION DEL SISTEMA UNICO DE COBRO DE INGRESOS VEHICULARES (SUCIVE) Y ESTABLECENSE SUBSIDIOS PARA LA EXTENSION Y FOMENTO DE LA EFICIENCIA ENERGETICA DE LOS SISTEMAS DE ALUMBRADO PUBLICO DEPARTAMENTALES (Ley Nº 18.860 of 2011) | 1 | Current text only (IMPO's text, last changed 19 December 2015), to today |
| `ley-18922/` | INCORPORACION DE NUEVOS AFILIADOS AL SEGURO NACIONAL DE SALUD. MODIFICACION (Ley Nº 18.922 of 2012) | 1 | Current text only (IMPO's text, last changed 6 July 2012), to today |
| `ley-18937/` | INTERPRETACION DEL ART. 68 DE LA LEY 18.387 SOBRE CONTRATOS PENDIENTES DE EJECUCION EN EL PROCESO CONCURSAL (Ley Nº 18.937 of 2012) | 1 | Current text only (IMPO's text, last changed 20 July 2012), to today |
| `ley-18996/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2011 (Ley Nº 18.996 of 2012) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-19003/` | MODIFICACION DEL SISTEMA DE AJUSTE DE LOS MONTOS MINIMOS Y MAXIMOS DE LAS PRESTACIONES DE SEGURIDAD SOCIAL (Ley Nº 19.003 of 2012) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-19007/` | MODIFICACION DE DISPOSICIONES DEL CODIGO PENAL, SOBRE DELITOS DE FUNCIONARIOS PUBLICOS Y DETERMINADAS ACTIVIDADES DELICTIVAS RELACIONADAS CON TODAS LAS FORMAS DE COCAINA INCLUIDA LA PASTA BASE DE COCAINA (Ley Nº 19.007 of 2012) | 1 | Current text only (IMPO's text, last changed 16 November 2012), to today |
| `ley-19074/` | DEROGACION DEL ART. 288 DE LA LEY DE SOCIEDADES COMERCIALES (Ley Nº 19.074 of 2013) | 1 | Current text only (IMPO's text, last changed 3 May 2013), to today |
| `ley-19090/` | MODIFICACION DEL CODIGO GENERAL DEL PROCESO (Ley Nº 19.090 of 2013) | 1 | Current text only (IMPO's text, last changed 8 July 2013), to today |
| `ley-19093/` | DEROGACION DEL IMPUESTO A LA CONCENTRACION DE INMUEBLES RURALES (ICIR) (Ley Nº 19.093 of 2013) | 1 | Current text only (IMPO's text, last changed 17 June 2013), to today |
| `ley-19109/` | SUSPENSION DE LA VIGENCIA DEL ART. 309 DE LA LEY 18996 RELATIVO A ZONAS FRANCAS (Ley Nº 19.109 of 2013) | 1 | Current text only (IMPO's text, last changed 23 July 2013), to today |
| `ley-19120/` | MODIFICACION DEL CODIGO PENAL (Ley Nº 19.120 of 2013) | 1 | Current text only (IMPO's text, last changed 26 October 2018), to today |
| `ley-19138/` | CREACION DEL REGISTRO NACIONAL DE INDUSTRIALIZADORES Y COMERCIALIZADORES DE COBRE (Ley Nº 19.138 of 2013) | 1 | Current text only (IMPO's text, last changed 3 November 2021), to today |
| `ley-19147/` | CREACION DEL OBSERVATORIO AMBIENTAL NACIONAL (OAN), DE LA DIRECCION NACIONAL DE MEDIO AMBIENTE DEL MVOTMA (Ley Nº 19.147 of 2013) | 1 | Current text only (IMPO's text, last changed 17 July 2019), to today |
| `ley-19149/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2012 (Ley Nº 19.149 of 2013) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19162/` | MODIFICACION DEL REGIMEN DE AHORRO INDIVIDUAL JUBILATORIO (Ley Nº 19.162 of 2013) | 1 | Current text only (IMPO's text, last changed 2 May 2023), to today |
| `ley-19164/` | MODIFICACION DE DISPOSICIONES RELATIVAS A INSTITUCIONES DE ASISTENCIA MEDICA COLECTIVA (Ley Nº 19.164 of 2013) | 1 | Current text only (IMPO's text, last changed 15 November 2013), to today |
| `ley-19177/` | INSTRUMENTACION DE LA DECLARACION JURADA DE BIENES E INGRESOS REFERIDOS EN LOS ARTICULOS 10 A 19 DE LA LEY 17.060 (Ley Nº 19.177 of 2013) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19247/` | TIPIFICACION DE DELITOS Y MODIFICACION DEL CODIGO PENAL (Ley Nº 19.247 of 2014) | 1 | Current text only (IMPO's text, last changed 15 August 2014), to today |
| `ley-19322/` | SUSPENSION DE LA VIGENCIA DE LOS ARTICULOS 224, 225, 227 A 257, 269 Y 275 DE LA LEY 19.276, CODIGO ADUANERO (Ley Nº 19.322 of 2015) | 1 | Current text only (IMPO's text, last changed 29 May 2015), to today |
| `ley-19331/` | CREACION DE LA SECRETARIA NACIONAL DEL DEPORTE COMO ORGANO DESCONCENTRADO DEPENDIENTE DIRECTAMENTE DE LA PRESIDENCIA DE LA REPUBLICA (Ley Nº 19.331 of 2015) | 1 | Current text only (IMPO's text, last changed 20 October 2022), to today |
| `ley-19355/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 2015 - 2019 (Ley Nº 19.355 of 2015) | 1 | Current text only (IMPO's text, last changed 1 October 2026), to today |
| `ley-19394/` | SUSPENSION DE LA VIGENCIA DE LOS ARTICULOS 224, 225, 227 A 257 y 269 DE LA LEY 19.276, CODIGO ADUANERO (Ley Nº 19.394 of 2016) | 1 | Current text only (IMPO's text, last changed 20 May 2016), to today |
| `ley-19438/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2015 (Ley Nº 19.438 of 2016) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-19475/` | PRORROGA DE ENTRADA EN VIGENCIA DEL INCISO PRIMERO DEL ART. 35 Y ARTS. 36, 40 Y 41 DE LA LEY 19.210. LEY DE INCLUSION FINANCIERA (Ley Nº 19.475 of 2017) | 1 | Current text only (IMPO's text, last changed 3 January 2017), to today |
| `ley-19484/` | APROBACION DE NORMAS DE CONVERGENCIA CON LOS ESTANDARES INTERNACIONALES EN TRANSPARENCIA FISCAL INTERNACIONAL, PREVENCION Y CONTROL DEL LAVADO DE ACTIVOS Y FINANCIAMIENTO DEL TERRORISMO (Ley Nº 19.484 of 2017) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19506/` | PRORROGA DE ENTRADA EN VIGENCIA DEL INCISO PRIMERO Y QUINTO DEL ART. 35 Y ARTS. 36, 40 Y 41 DE LA LEY 19.210, LEY DE INCLUSION FINANCIERA (Ley Nº 19.506 of 2017) | 1 | Current text only (IMPO's text, last changed 30 June 2017), to today |
| `ley-19513/` | CREACION DE LA COMISION DE LUCHA CONTRA EL NARCOTRAFICO Y EL CRIMEN ORGANIZADO TRANSFRONTERIZO. MODIFICACIONES AL DECRETO LEY 14.294 SOBRE ESTUPEFACIENTES (Ley Nº 19.513 of 2017) | 1 | Current text only (IMPO's text, last changed 14 July 2017), to today |
| `ley-19535/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2016 (Ley Nº 19.535 of 2017) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-19590/` | MODIFICACION DEL REGIMEN JUBILATORIO PREVISTO POR LA LEY 16.713. LEY DE LOS CINCUENTONES (Ley Nº 19.590 of 2017) | 1 | Current text only (IMPO's text, last changed 28 December 2017), to today |
| `ley-19593/` | MODIFICACION DE LAS LEYES 18.910 Y 19.210 RELATIVAS A LA INCLUSION FINANCIERA (Ley Nº 19.593 of 2018) | 1 | Current text only (IMPO's text, last changed 9 July 2020), to today |
| `ley-19630/` | APROBACION DEL ACUERDO ENTRE URUGUAY Y SUDAFRICA DE ASISTENCIA MUTUA ENTRE ADMINISTRACIONES ADUANERAS (Ley Nº 19.630 of 2018) | 1 | Current text only (IMPO's text, last changed 22 June 2018), to today |
| `ley-19670/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2017 (Ley Nº 19.670 of 2018) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-19723/` | MODIFICACION DEL ART. 8 DE LA LEY 18.256 RELATIVO A LA PROTECCION DEL DERECHO AL MEDIO AMBIENTE LIBRE DE HUMO DE TABACO Y SU CONSUMO (Ley Nº 19.723 of 2018) | 1 | Current text only (IMPO's text, last changed 21 December 2018), to today |
| `ley-19733/` | CREACION DEL FONDO DE PERITAJES (Ley Nº 19.733 of 2018) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19747/` | MODIFICACION DEL CAPITULO XI DE LA LEY 17.823, CODIGO DE LA NIÑEZ Y LA ADOLESCENCIA (Ley Nº 19.747 of 2019) | 1 | Current text only (IMPO's text, last changed 19 April 2019), to today |
| `ley-19749/` | APROBACION DE LA LEY CONTRA EL FINANCIAMIENTO DEL TERRORISMO Y APLICACION DE SANCIONES FINANCIERAS CONTRA LAS PERSONAS Y ENTIDADES VINCULADAS AL TERRORISMO, SU FINANCIAMIENTO Y LA PROLIFERACION DE ARMAS DE DESTRUCCION MASIVA (Ley Nº 19.749 of 2019) | 1 | Current text only (IMPO's text, last changed 15 May 2019), to today |
| `ley-19788/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2018 (Ley Nº 19.788 of 2019) | 1 | Current text only (IMPO's text, last changed 30 August 2019), to today |
| `ley-19824/` | ACTUALIZACION DE LA NORMATIVA VIGENTE EN MATERIA DE TRANSITO Y SEGURIDAD VIAL (Ley Nº 19.824 of 2019) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19834/` | MODIFICACION DEL ART. 198 DE LA LEY 19.307. LEY DE MEDIOS. REGULACION DE LA PRESTACION DE SERVICIOS DE RADIO, TELEVISION Y OTROS SERVICIOS DE COMUNICACION AUDIOVISUAL (Ley Nº 19.834 of 2019) | 1 | Current text only (IMPO's text, last changed 23 September 2019), to today |
| `ley-19841/` | MODIFICACION DEL ESTATUTO DEL FUNCIONARIO DEL SERVICIO EXTERIOR DE LA REPUBLICA (Ley Nº 19.841 of 2019) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19847/` | DECLARACION DE INTERES PUBLICO LAS ACCIONES TENDIENTES A PROTEGER, PROMOVER Y MEJORAR LA SALUD PUBLICA MEDIANTE PRODUCTOS DE CALIDAD CONTROLADA Y ACCESIBLES, EN BASE A CANNABIS O CANNABINOIDES, ASI COMO EL ASESORAMIENTO MEDICO E INFORMACION SOBRE BENEFICIOS Y RIESGOS DE SU USO (Ley Nº 19.847 of 2019) | 1 | Current text only (IMPO's text, last changed 20 December 2019), to today |
| `ley-19859/` | SISTEMA NACIONAL INTEGRADO DE SALUD. PRESTACION GRATUITA Y VITALICIA A VICTIMAS DEL TERRORISMO DE ESTADO, COMPRENDIENDO A HIJOS, NIETOS, BIOLOGICOS O ADOPTIVOS (Ley Nº 19.859 of 2019) | 1 | Current text only (IMPO's text, last changed 23 December 2019), to today |
| `ley-19870/` | PRORROGA DE PLAZO ESTABLECIDO EN LOS ARTS. 27 Y 33 DE LA LEY 19.829, REFERENTE A GESTION INTEGRAL DE RESIDUOS (Ley Nº 19.870 of 2020) | 1 | Current text only (IMPO's text, last changed 2 April 2020), to today |
| `ley-19889/` | APROBACION DE LA LEY DE URGENTE CONSIDERACION. LUC. LEY DE URGENCIA (Ley Nº 19.889 of 2020) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19924/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 2020-2024 (Ley Nº 19.924 of 2020) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-19942/` | APROBACION DE NUEVAS MEDIDAS PARA MITIGAR EL IMPACTO ECONOMICO COMO CONSECUENCIA DE LA EMERGENCIA NACIONAL SANITARIA, POR COVID-19 (Ley Nº 19.942 of 2021) | 1 | Current text only (IMPO's text, last changed 10 June 2021), to today |
| `ley-19970/` | SUSPENSION DEL PLAZO ESTABLECIDO EN EL ART. 165 DE LA LEY 19.775, LEY ORGANICA DE LAS FUERZAS ARMADAS (Ley Nº 19.970 of 2021) | 1 | Current text only (IMPO's text, last changed 4 August 2021), to today |
| `ley-19996/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2020 (Ley Nº 19.996 of 2021) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-20071/` | PRORROGA DEL PLAZO DISPUESTO POR EL ART. 167 DE LA LEY 19.775, RELATIVO A LA LEY ORGANICA DE LAS FUERZAS ARMADAS (Ley Nº 20.071 of 2022) | 1 | Current text only (IMPO's text, last changed 23 September 2022), to today |
| `ley-20075/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2021 (Ley Nº 20.075 of 2022) | 1 | Current text only (IMPO's text, last changed 16 December 2025), to today |
| `ley-20108/` | PRORROGA DEL PLAZO DISPUESTO POR EL ART. 168 DE LA LEY 19.775, RELATIVO A LA LEY ORGANICA DE LAS FUERZAS ARMADAS (Ley Nº 20.108 of 2022) | 1 | Current text only (IMPO's text, last changed 27 December 2022), to today |
| `ley-20125/` | DEROGACION DE LA LEY 20.096 Y MODIFICACION DE LEY 19.043, RELATIVAS A LA CREACION DE LA UNIVERSIDAD TECNOLOGICA (UTEC) (Ley Nº 20.125 of 2023) | 1 | Current text only (IMPO's text, last changed 17 April 2023), to today |
| `ley-20130/` | LEY DE REFORMA DE LA SEGURIDAD SOCIAL. CREACION DE UN SISTEMA PREVISIONAL COMUN Y DETERMINACION DEL PROCEDIMIENTO DE CONVERGENCIA DE LOS REGIMENES ACTUALMENTE VIGENTES (Ley Nº 20.130 of 2023) | 1 | Current text only (IMPO's text, last changed 1 November 2023), to today |
| `ley-20145/` | MODIFICACION DE LA LEY 18.566 SOBRE NEGOCIACION COLECTIVA (Ley Nº 20.145 of 2023) | 1 | Current text only (IMPO's text, last changed 17 May 2023), to today |
| `ley-20208/` | MODIFICACION DE LOS ARTS. 18, 19, 21, 28, 34, 51, 52, 67 Y 82 DE LA LEY Nº 18.396 RELATIVO AL REGIMEN DE LA CAJA DE JUBILACIONES Y PENSIONES BANCARIAS (Ley Nº 20.208 of 2023) | 1 | Current text only (IMPO's text, last changed 1 November 2023), to today |
| `ley-20212/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2022 (Ley Nº 20.212 of 2023) | 1 | Current text only (IMPO's text, last changed 1 October 2026), to today |
| `ley-20313/` | PRORROGA DEL PLAZO DISPUESTO POR EL ART. 167 DE LA LEY 19.775, RELATIVO A LA LEY ORGANICA DE LAS FUERZAS ARMADAS (Ley Nº 20.313 of 2024) | 1 | Current text only (IMPO's text, last changed 14 August 2024), to today |
| `ley-20357/` | CREACION DE LA ADMINISTRACION NACIONAL DE BOMBEROS VOLUNTARIOS (Ley Nº 20.357 of 2024) | 1 | Current text only (IMPO's text, last changed 20 September 2024), to today |
| `ley-20410/` | MODIFICACION DE LA LEY ORGANICA DE LA CAJA DE JUBILACIONES Y PENSIONES DE PROFESIONALES UNIVERSITARIOS (Ley Nº 20.410 of 2025) | 1 | Current text only (IMPO's text, last changed 25 July 2025), to today |
| `ley-20446/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES. EJERCICIO 2025-2029 (Ley Nº 20.446 of 2025) | 1 | Current text only (IMPO's text, last changed 1 October 2026), to today |
| `ley-5392/` | CODIGO DE COMERCIO. MODIFICACION (Ley Nº 5.392 of 1916) | 1 | Current text only (IMPO's text, last changed 25 January 1916), to today |
| `ley-6962/` | CAJA DE JUBILACIONES Y PENSIONES DE EMPLEADOS Y OBREROS DE SERVICIOS PUBLICOS. CREACION (Ley Nº 6.962 of 1919) | 1 | Current text only (IMPO's text, last changed 2 December 1965), to today |
| `ley-7782/` | LEY DE REGISTRO CIVICO NACIONAL. MODIFICACION (Ley Nº 7.782 of 1924) | 1 | Current text only (IMPO's text, last changed 20 November 1924), to today |
| `ley-7912/` | ELECCIONES NACIONALES. CAMARA DE SENADORES. CAMARA DE DIPUTADOS. INTEGRACION. REGISTRO CIVICO NACIONAL. REGULACION (Ley Nº 7.912 of 1925) | 1 | Current text only (IMPO's text, last changed 16 December 2007), to today |
| `ley-8070/` | LEY DE ELECCIONES. MODIFICACION (Ley Nº 8.070 of 1927) | 1 | Current text only (IMPO's text, last changed 9 June 1999), to today |
| `ley-8080/` | DELITO DE PROXENETISMO (Ley Nº 8.080 of 1927) | 1 | Current text only (IMPO's text, last changed 12 July 1995), to today |
| `ley-8196/` | REGISTRO CIVICO NACIONAL. CIUDADANIA. REGLAMENTACION (Ley Nº 8.196 of 1928) | 1 | Current text only (IMPO's text, last changed 2 February 1928), to today |
| `ley-8239/` | PRESUPUESTO. MODIFICACION (Ley Nº 8.239 of 1928) | 1 | Current text only (IMPO's text, last changed 8 April 1986), to today |
| `ley-8301/` | CODIGO CIVIL. CODIGO DE COMERCIO. MODIFICACION (Ley Nº 8.301 of 1928) | 1 | Current text only (IMPO's text, last changed 15 October 1928), to today |
| `ley-8461/` | DECLARACION DE UTILIDAD PUBLICA PARA EXPROPIACION (Ley Nº 8.461 of 1929) | 1 | Current text only (IMPO's text, last changed 30 April 1974), to today |
| `ley-8733/` | LEY DE PROMESA DE ENAJENACION DE INMUEBLES A PLAZOS (Ley Nº 8.733 of 1931) | 1 | Current text only (IMPO's text, last changed 9 November 1992), to today |
| `ley-8888/` | VENCIMIENTO DE OBLIGACIONES. TITULOS VALORES (Ley Nº 8.888 of 1932) | 1 | Current text only (IMPO's text, last changed 28 September 1932), to today |
| `ley-8902/` | CONSTITUCION DE LA REPUBLICA. ENMIENDA. RATIFICACION (Ley Nº 8.902 of 1932) | 1 | Current text only (IMPO's text, last changed 27 October 1932), to today |
| `ley-8912/` | LEY DE ELECCIONES. MODIFICACION (Ley Nº 8.912 of 1932) | 1 | Current text only (IMPO's text, last changed 3 November 1932), to today |
| `ley-8927/` | DERECHOS CIVICOS DE LA MUJER (Ley Nº 8.927 of 1932) | 1 | Current text only (IMPO's text, last changed 16 December 1932), to today |
| `ley-9051/` | LEY DE ELECCIONES. MODIFICACION (Ley Nº 9.051 of 1933) | 1 | Current text only (IMPO's text, last changed 13 June 1933), to today |
| `ley-9189/` | FIJACION DE IMPUESTO. CONTRIBUCION INMOBILIARIA. PATENTES DE PERROS. INSTRUCCION PRIMARIA (Ley Nº 9.189 of 1934) | 1 | Current text only (IMPO's text, last changed 27 March 1953), to today |
| `ley-9385/` | BANCO HIPOTECARIO DEL URUGUAY (BHU). PRESTAMOS (Ley Nº 9.385 of 1934) | 1 | Current text only (IMPO's text, last changed 28 December 1964), to today |
| `ley-9570/` | CORTE ELECTORAL. AUTORIZACION (Ley Nº 9.570 of 1936) | 1 | Current text only (IMPO's text, last changed 19 June 1936), to today |
| `ley-9602/` | ADMINISTRACION NACIONAL DEL PUERTO DE MONTEVIDEO. CREACION. MODIFICACION (Ley Nº 9.602 of 1936) | 1 | Current text only (IMPO's text, last changed 23 September 1936), to today |
| `ley-9624/` | CONTADURIA GENERAL DE LA NACION. GARANTIA DE ALQUILERES (Ley Nº 9.624 of 1936) | 1 | Current text only (IMPO's text, last changed 18 December 2020), to today |
| `ley-9645/` | CORTE ELECTORAL. MODIFICACION (Ley Nº 9.645 of 1937) | 1 | Current text only (IMPO's text, last changed 15 January 1937), to today |
| `ley-9739/` | LEY DE DERECHOS DE AUTOR (Ley Nº 9.739 of 1937) | 1 | Current text only (IMPO's text, last changed 6 November 2023), to today |
| `ley-9892/` | MINISTERIO DE SALUD PUBLICA. PRESUPUESTO (Ley Nº 9.892 of 1939) | 1 | Current text only (IMPO's text, last changed 10 November 1987), to today |
| `ley-9919/` | PALACIO LEGISLATIVO. OBRAS PUBLICAS. EXPROPIACIONES (Ley Nº 9.919 of 1940) | 1 | Current text only (IMPO's text, last changed 24 June 1958), to today |
| `ley-9940/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 9.940 of 1940) | 1 | Current text only (IMPO's text, last changed 2 May 2023), to today |
| `ley-5378/` | CREACION DE IMPUESTO. ABASTO. ALUMBRADO. SEGURIDAD. SERENOS (Ley Nº 5.378 of 1916) | 1 | Current text only (IMPO's text, in force from 27 January 1934), to today |
| `ley-5391/` | DERECHOS HEREDITARIOS. HIJOS NATURALES (Ley Nº 5.391 of 1916) | 1 | Current text only (IMPO's text, in force from 10 February 1916), to today |
| `ley-5426/` | FIJACION DE IMPUESTO. ARTICULOS DE PERFUMERIA Y DE TOCADOR. VINOS. BEBIDAS ALCOHOLICAS (Ley Nº 5.426 of 1916) | 1 | Current text only (IMPO's text, in force from 1 January 1966), to today |
| `ley-5427/` | ACCIDENTES DE TRABAJO. MULTAS (Ley Nº 5.427 of 1916) | 1 | Current text only (IMPO's text, in force from 9 June 1916), to today |
| `ley-5560/` | LEY DE EXPROPIACIONES. AMPLIACION (Ley Nº 5.560 of 1917) | 1 | Current text only (IMPO's text, in force from 23 April 1917), to today |
| `ley-5616/` | LEY DE EXPROPIACIONES. AMPLIACION (Ley Nº 5.616 of 1917) | 1 | Current text only (IMPO's text, in force from 24 December 1917), to today |
| `ley-5654/` | REGISTRO DE ESTADO CIVIL. INSCRIPCIONES. PRORROGA (Ley Nº 5.654 of 1918) | 1 | Current text only (IMPO's text, in force from 13 April 1918), to today |
| `ley-6874/` | JUBILACIONES Y PENSIONES. PENSIONES A LA VEJEZ. CREACION. FIJACION DE IMPUESTO. PREVISION SOCIAL. SOBRETASA INMOBILIARIA. NAIPES. BEBIDAS ALCOHOLICAS (Ley Nº 6.874 of 1919) | 1 | Current text only (IMPO's text, in force from 9 November 1968), to today |
| `ley-6894/` | ASISTENCIA PUBLICA NACIONAL. PRESUPUESTO (Ley Nº 6.894 of 1919) | 1 | Current text only (IMPO's text, in force from 22 January 1965), to today |
| `ley-6950/` | JUBILACIONES Y PENSIONES. PENSIONES A LA VEJEZ. MODIFICACION (Ley Nº 6.950 of 1919) | 1 | Current text only (IMPO's text, in force from 6 January 1958), to today |
| `ley-6953/` | LEY DE EXPROPIACIONES. MODIFICACION. DECLARACION DE UTILIDAD PUBLICA PARA EXPROPIACION (Ley Nº 6.953 of 1919) | 1 | Current text only (IMPO's text, in force from 22 September 1919), to today |
| `ley-7012/` | EXPROPIACIONES. INDEMNIZACIONES (Ley Nº 7.012 of 1919) | 1 | Current text only (IMPO's text, in force from 13 November 1919), to today |
| `ley-7393/` | REGISTRO DE ESTADO CIVIL. NACIMIENTOS. DEFUNCIONES. INSCRIPCIONES (Ley Nº 7.393 of 1921) | 1 | Current text only (IMPO's text, in force from 23 July 1921), to today |
| `ley-7409/` | LEY DE EXPROPIACIONES. AMPLIACION (Ley Nº 7.409 of 1921) | 1 | Current text only (IMPO's text, in force from 17 September 1921), to today |
| `ley-7471/` | CAJA DE JUBILACIONES Y PENSIONES DE EMPLEADOS Y OBREROS DE SERVICIOS PUBLICOS. DIRECTORIO. MODIFICACION (Ley Nº 7.471 of 1922) | 1 | Current text only (IMPO's text, in force from 8 May 1922), to today |
| `ley-7624/` | BANCO DE SEGUROS DEL ESTADO (BSE). EMBARGO PREVENTIVO (Ley Nº 7.624 of 1923) | 1 | Current text only (IMPO's text, in force from 2 October 1923), to today |
| `ley-7742/` | FIJACION DE IMPUESTO. CONTRIBUCION INMOBILIARIA. SOBRETASA INMOBILIARIA. SOBRETASA TERRITORIAL. PRESTAMISTAS HIPOTECARIOS (Ley Nº 7.742 of 1924) | 1 | Current text only (IMPO's text, in force from 31 July 1924), to today |
| `ley-7800/` | FIJACION DE IMPUESTO. SOBRETASA TERRITORIAL (Ley Nº 7.800 of 1924) | 1 | Current text only (IMPO's text, in force from 9 January 1925), to today |
| `ley-7880/` | FIJACION DE IMPUESTO. PREVISION SOCIAL. BEBIDAS ALCOHOLICAS. CONTRIBUCION INMOBILIARIA. PATENTE A LA IMPORTACION DE AUTOMOVILES (Ley Nº 7.880 of 1925) | 1 | Current text only (IMPO's text, in force from 30 August 1925), to today |
| `ley-7975/` | LEY ORGANICA DEL BANCO DE SEGUROS DEL ESTADO (BSE). MODIFICACION (Ley Nº 7.975 of 1926) | 1 | Current text only (IMPO's text, in force from 31 October 1993), to today |
| `ley-8007/` | ADMINISTRACION GENERAL DE CORREOS, TELEGRAFOS Y TELEFONOS. PRESUPUESTO (Ley Nº 8.007 of 1926) | 1 | Current text only (IMPO's text, in force from 26 December 1960), to today |
| `ley-8053/` | AUTORIZACION PARA RESIDIR EN EL EXTRANJERO (Ley Nº 8.053 of 1926) | 1 | Current text only (IMPO's text, in force from 28 April 1933), to today |
| `ley-8139/` | DEROGACION DE IMPUESTO. GANADO. CARNE (Ley Nº 8.139 of 1927) | 1 | Current text only (IMPO's text, in force from 6 December 1927), to today |
| `ley-8153/` | LEY DE DESALOJOS (Ley Nº 8.153 of 1927) | 1 | Current text only (IMPO's text, in force from 19 May 1978), to today |
| `ley-8158/` | PODER EJECUTIVO. AUTORIZACION. OBRAS PUBLICAS (Ley Nº 8.158 of 1927) | 1 | Current text only (IMPO's text, in force from 18 January 1946), to today |
| `ley-8343/` | LEY DE VIALIDAD E HIDROGRAFIA (Ley Nº 8.343 of 1928) | 1 | Current text only (IMPO's text, in force from 26 December 1960), to today |
| `ley-8416/` | BANCO DE SEGUROS DEL ESTADO (BSE). FACULTADES (Ley Nº 8.416 of 1929) | 1 | Current text only (IMPO's text, in force from 22 June 1929), to today |
| `ley-8496/` | EXONERACION DE IMPUESTO. COMBUSTIBLES. PATENTE DE ADUANA (Ley Nº 8.496 of 1929) | 1 | Current text only (IMPO's text, in force from 20 November 1969), to today |
| `ley-8504/` | DEROGACION DE IMPUESTO. FIJACION DE IMPUESTO. ZONAS DE INFLUENCIA. CONTRIBUCION INMOBILIARIA. PRORROGA (Ley Nº 8.504 of 1929) | 1 | Current text only (IMPO's text, in force from 28 November 1929), to today |
| `ley-8761/` | VIALIDAD Y OBRAS PUBLICAS (Ley Nº 8.761 of 1931) | 1 | Current text only (IMPO's text, in force from 31 October 1931), to today |
| `ley-8776/` | FIJACION DE IMPUESTO. CONTRIBUCION INMOBILIARIA. ZONAS DE INFLUENCIA. PRORROGA (Ley Nº 8.776 of 1931) | 1 | Current text only (IMPO's text, in force from 6 November 1931), to today |
| `ley-8794/` | ELECCIONES NACIONALES. COMISION RECEPTORA DE VOTOS. CARGOS. SUPRESION (Ley Nº 8.794 of 1931) | 1 | Current text only (IMPO's text, in force from 7 November 1931), to today |
| `ley-9069/` | SEGURIDAD SOCIAL. PODER EJECUTIVO. AUTORIZACION EMISION DE "BONOS DE PREVISION SOCIAL 1933". (Ley Nº 9.069 of 1933) | 1 | Current text only (IMPO's text, in force from 26 December 1960), to today |
| `ley-9098/` | SALUD PUBLICA. PRESUPUESTO (Ley Nº 9.098 of 1933) | 1 | Current text only (IMPO's text, in force from 6 October 1933), to today |
| `ley-9121/` | COMBUSTIBLES. FISCALIZACION (Ley Nº 9.121 of 1933) | 1 | Current text only (IMPO's text, in force from 10 November 1933), to today |
| `ley-9196/` | CAJA DE JUBILACIONES DE LA INDUSTRIA, COMERCIO Y SERVICIOS PUBLICOS. CREACION (Ley Nº 9.196 of 1934) | 1 | Current text only (IMPO's text, in force from 24 October 1950), to today |
| `ley-9207/` | MINISTERIO DE SALUD PUBLICA. FUNCIONARIOS. REMUNERACIONES (Ley Nº 9.207 of 1934) | 1 | Current text only (IMPO's text, in force from 18 March 1934), to today |
| `ley-9320/` | FIJACION DE IMPUESTO. CONTRIBUCION INMOBILIARIA. PATENTES DE GIRO (Ley Nº 9.320 of 1934) | 1 | Current text only (IMPO's text, in force from 3 April 1934), to today |
| `ley-9328/` | FIJACION DE IMPUESTO. CONTRIBUCION INMOBILIARIA (Ley Nº 9.328 of 1934) | 1 | Current text only (IMPO's text, in force from 19 April 1934), to today |
| `ley-9358/` | CORTE ELECTORAL. FUNCIONARIOS (Ley Nº 9.358 of 1934) | 1 | Current text only (IMPO's text, in force from 18 May 1934), to today |
| `ley-9376/` | LEY DE VIALIDAD E HIDROGRAFIA. MODIFICACION (Ley Nº 9.376 of 1934) | 1 | Current text only (IMPO's text, in force from 18 May 1934), to today |
| `ley-9424/` | LEY DE REGISTRO CIVICO NACIONAL. MODIFICACION (Ley Nº 9.424 of 1934) | 1 | Current text only (IMPO's text, in force from 24 August 1934), to today |
| `ley-9460/` | PRESUPUESTO (Ley Nº 9.460 of 1935) | 1 | Current text only (IMPO's text, in force from 14 June 1953), to today |
| `ley-9461/` | LEY DE ORDENAMIENTO FINANCIERO (Ley Nº 9.461 of 1935) | 1 | Current text only (IMPO's text, in force from 1 January 1991), to today |
| `ley-9482/` | PLAGAS. LUCHA CONTRA LA SARNA OVINA (Ley Nº 9.482 of 1935) | 1 | Current text only (IMPO's text, in force from 16 February 1939), to today |
| `ley-9488/` | CAJA DE JUBILACIONES DE LA INDUSTRIA, COMERCIO Y SERVICIOS PUBLICOS. BANCO DE SEGUROS DEL ESTADO (BSE). ACCIDENTES DE TRABAJO. SEGUROS DE INVALIDEZ (Ley Nº 9.488 of 1935) | 1 | Current text only (IMPO's text, in force from 12 August 1935), to today |
| `ley-9496/` | BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY (BROU). DEUDA PUBLICA. EMISION. ENCAJE BANCARIO (Ley Nº 9.496 of 1935) | 1 | Current text only (IMPO's text, in force from 12 February 1938), to today |
| `ley-9498/` | PROMOCION INDUSTRIAL. FRANQUICIAS TRIBUTARIAS (Ley Nº 9.498 of 1935) | 1 | Current text only (IMPO's text, in force from 22 January 1965), to today |
| `ley-9506/` | DEUDA PUBLICA. EMISION (Ley Nº 9.506 of 1935) | 1 | Current text only (IMPO's text, in force from 24 October 1935), to today |
| `ley-9526/` | COOPERATIVA NACIONAL DE PRODUCTORES DE LECHE (CONAPROLE). CREACION. DECLARACION DE UTILIDAD PUBLICA PARA EXPROPIACION (Ley Nº 9.526 of 1935) | 1 | Current text only (IMPO's text, in force from 16 July 2000), to today |
| `ley-9535/` | GOBIERNOS DEPARTAMENTALES. PROCESOS JUDICIALES. JUICIO EJECUTIVO (Ley Nº 9.535 of 1935) | 1 | Current text only (IMPO's text, in force from 6 January 1936), to today |
| `ley-9538/` | PRESUPUESTO GENERAL DE GASTOS. EJERCICIO 1936 (Ley Nº 9.538 of 1935) | 1 | Current text only (IMPO's text, in force from 14 June 1953), to today |
| `ley-9539/` | LEY DE ORDENAMIENTO FINANCIERO. MODIFICACION (Ley Nº 9.539 of 1935) | 1 | Current text only (IMPO's text, in force from 21 January 1936), to today |
| `ley-9583/` | BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY (BROU). MONEDA (Ley Nº 9.583 of 1936) | 1 | Current text only (IMPO's text, in force from 25 August 1936), to today |
| `ley-9590/` | CORTE ELECTORAL. AUTORIZACION (Ley Nº 9.590 of 1936) | 1 | Current text only (IMPO's text, in force from 5 September 1936), to today |
| `ley-9638/` | MINISTERIO DE INSTRUCCION PUBLICA Y PREVISION SOCIAL. SERVICIO OFICIAL DE DIFUSION RADIOELECTRICA (SODRE). ORGANIZACION (Ley Nº 9.638 of 1936) | 1 | Current text only (IMPO's text, in force from 1 January 2012), to today |
| `ley-9639/` | PRESUPUESTO (Ley Nº 9.639 of 1936) | 1 | Current text only (IMPO's text, in force from 25 December 1960), to today |
| `ley-9640/` | LEY DE ORDENAMIENTO FINANCIERO. MODIFICACION (Ley Nº 9.640 of 1936) | 1 | Current text only (IMPO's text, in force from 24 January 1937), to today |
| `ley-9657/` | LEY DE ORDENAMIENTO FINANCIERO. MODIFICACION (Ley Nº 9.657 of 1937) | 1 | Current text only (IMPO's text, in force from 11 July 1937), to today |
| `ley-9722/` | DECLARACION DE UTILIDAD PUBLICA PARA EXPROPIACION (Ley Nº 9.722 of 1937) | 1 | Current text only (IMPO's text, in force from 8 July 1942), to today |
| `ley-9723/` | INSTITUTO NACIONAL DE VIVIENDAS ECONOMICAS (INVE). CREACION. DECLARACION DE UTILIDAD PUBLICA PARA EXPROPIACION (Ley Nº 9.723 of 1937) | 1 | Current text only (IMPO's text, in force from 12 December 1965), to today |
| `ley-9743/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 9.743 of 1937) | 1 | Current text only (IMPO's text, in force from 7 January 1938), to today |
| `ley-9760/` | MONEDA (Ley Nº 9.760 of 1938) | 1 | Current text only (IMPO's text, in force from 22 January 1965), to today |
| `ley-9774/` | DELITO DE IMPRENTA (Ley Nº 9.774 of 1938) | 1 | Current text only (IMPO's text, in force from 6 June 1938), to today |
| `ley-9791/` | PRESUPUESTO. NORMAS COMPLEMENTARIAS (Ley Nº 9.791 of 1938) | 1 | Current text only (IMPO's text, in force from 27 January 1942), to today |
| `ley-9812/` | PRESUPUESTO GENERAL DE GASTOS. EJERCICIO 1939 (Ley Nº 9.812 of 1939) | 1 | Current text only (IMPO's text, in force from 27 January 1942), to today |
| `ley-9831/` | LEY DE LEMAS (Ley Nº 9.831 of 1939) | 1 | Current text only (IMPO's text, in force from 8 June 1939), to today |
| `ley-9847/` | MINISTERIO DE DEFENSA NACIONAL. PRESUPUESTO (Ley Nº 9.847 of 1939) | 1 | Current text only (IMPO's text, in force from 20 August 1939), to today |
| `ley-9876/` | VIALIDAD Y OBRAS PUBLICAS. DECLARACION DE UTILIDAD PUBLICA PARA EXPROPIACION (Ley Nº 9.876 of 1939) | 1 | Current text only (IMPO's text, in force from 5 October 1951), to today |
| `ley-9877/` | DEUDA PUBLICA. EMISION (Ley Nº 9.877 of 1939) | 1 | Current text only (IMPO's text, in force from 10 October 1939), to today |
| `ley-9899/` | COOPERATIVA NACIONAL DE PRODUCTORES DE LECHE (CONAPROLE). PRODUCTORES. CUOTAS. DIRECTORIO. MODIFICACION (Ley Nº 9.899 of 1939) | 1 | Current text only (IMPO's text, in force from 7 February 1946), to today |
| `ley-9953/` | PODER EJECUTIVO. AUTORIZACION. OBRAS PUBLICAS (Ley Nº 9.953 of 1940) | 1 | Current text only (IMPO's text, in force from 1 October 1940), to today |
| `ley-9968/` | PRESUPUESTO. PRORROGA (Ley Nº 9.968 of 1940) | 1 | Current text only (IMPO's text, in force from 17 December 1940), to today |
| `ley-9973/` | CAJA DE JUBILACIONES DE LA INDUSTRIA, COMERCIO Y SERVICIOS PUBLICOS. BENEFICIOS JUBILATORIOS (Ley Nº 9.973 of 1940) | 1 | Current text only (IMPO's text, in force from 24 October 1950), to today |
| `ley-9995/` | JUBILACIONES Y PENSIONES. INTERPOSICION DE RECURSOS (Ley Nº 9.995 of 1940) | 1 | Current text only (IMPO's text, in force from 24 January 1941), to today |
| `ley-9999/` | CAJA DE JUBILACIONES DE LA INDUSTRIA, COMERCIO Y SERVICIOS PUBLICOS. BENEFICIOS JUBILATORIOS (Ley Nº 9.999 of 1941) | 1 | Current text only (IMPO's text, in force from 20 March 1975), to today |
| `ley-10000/` | MINISTERIO DE HACIENDA. INSTITUTO DE CONTRALOR DE EXPORTACIONES E IMPORTACIONES DEL ESTADO. DEPENDENCIA. CREACION (Ley Nº 10.000 of 1941) | 1 | Current text only (IMPO's text, in force from 27 January 1957), to today |
| `ley-10039/` | TRABAJADORES. SEGURO DE PARO. PRORROGA (Ley Nº 10.039 of 1941) | 1 | Current text only (IMPO's text, in force from 24 August 1941), to today |
| `ley-10054/` | PODER EJECUTIVO. AUTORIZACION. DEUDA PUBLICA. EMISION. FIJACION DE IMPUESTO. VENTAS Y TRANSACCIONES (Ley Nº 10.054 of 1941) | 1 | Current text only (IMPO's text, in force from 22 September 1967), to today |
| `ley-10056/` | FIJACION DE IMPUESTO. VENTAS Y TRANSACCIONES (Ley Nº 10.056 of 1941) | 1 | Current text only (IMPO's text, in force from 3 November 1941), to today |
| `ley-10085/` | LEY ORGANICA MILITAR. MODIFICACION (Ley Nº 10.085 of 1941) | 1 | Current text only (IMPO's text, in force from 22 December 1941), to today |
| `ley-10093/` | FUNCIONARIOS JUDICIALES. REMUNERACIONES (Ley Nº 10.093 of 1941) | 1 | Current text only (IMPO's text, in force from 3 January 1942), to today |
| `ley-10107/` | PRESUPUESTO. PRORROGA (Ley Nº 10.107 of 1941) | 1 | Current text only (IMPO's text, in force from 9 February 1968), to today |
| `ley-10117/` | FUNCIONARIOS. DOCENTES. REMUNERACIONES (Ley Nº 10.117 of 1942) | 1 | Current text only (IMPO's text, in force from 25 July 1949), to today |
| `ley-10436/` | FONDO DE ASISTENCIA Y PREVISION SOCIAL. CREACION (Ley Nº 10.436 of 1943) | 1 | Current text only (IMPO's text, in force from 13 October 1950), to today |
| `ley-10444/` | TRABAJADORES. SEGURO DE PARO. PRORROGA (Ley Nº 10.444 of 1943) | 1 | Current text only (IMPO's text, in force from 23 September 1943), to today |
| `ley-10469/` | PRESUPUESTO. PRORROGA (Ley Nº 10.469 of 1944) | 1 | Current text only (IMPO's text, in force from 27 January 1944), to today |
| `ley-10471/` | CONSEJOS DE SALARIOS. TRABAJADORES (Ley Nº 10.471 of 1944) | 1 | Current text only (IMPO's text, in force from 27 March 1944), to today |
| `ley-10491/` | DOCUMENTOS HISTORICOS. ARCHIVO ARTIGAS. CREACION (Ley Nº 10.491 of 1944) | 1 | Current text only (IMPO's text, in force from 1 January 1962), to today |
| `ley-10492/` | OTORGAMIENTO DE SUBSIDIO. MODIFICACION (Ley Nº 10.492 of 1944) | 1 | Current text only (IMPO's text, in force from 1 July 1944), to today |
| `ley-10494/` | COMERCIO. REGIMEN HORARIO. FIJACION (Ley Nº 10.494 of 1944) | 1 | Current text only (IMPO's text, in force from 3 July 1944), to today |
| `ley-10496/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 10.496 of 1944) | 1 | Current text only (IMPO's text, in force from 8 July 1944), to today |
| `ley-10502/` | CAJA DE JUBILACIONES Y PENSIONES BANCARIAS. BENEFICIOS JUBILATORIOS (Ley Nº 10.502 of 1944) | 1 | Current text only (IMPO's text, in force from 12 August 1944), to today |
| `ley-10511/` | PODER EJECUTIVO. AUTORIZACION. OBRAS PUBLICAS. FIJACION DE IMPUESTO. SUPRESION DE IMPUESTO. INSTRUCCION PUBLICA. INSTRUCCION PRIMARIA. PATENTE DE PERROS (Ley Nº 10.511 of 1944) | 1 | Current text only (IMPO's text, in force from 26 December 1960), to today |
| `ley-10513/` | PRESUPUESTO. MODIFICACION (Ley Nº 10.513 of 1944) | 1 | Current text only (IMPO's text, in force from 25 July 1949), to today |
| `ley-10521/` | TRABAJADORES. SEGURO DE PARO. PRORROGA (Ley Nº 10.521 of 1944) | 1 | Current text only (IMPO's text, in force from 15 September 1944), to today |
| `ley-10568/` | FUNCIONARIOS MILITARES. CUERPO TECNICO DE OFICIALES. CREACION (Ley Nº 10.568 of 1944) | 1 | Current text only (IMPO's text, in force from 27 July 1963), to today |
| `ley-10589/` | EMISION DE DEUDA PUBLICA CON DESTINO A OBRA PUBLICA Y VIALIDAD (Ley Nº 10.589 of 1944) | 1 | Current text only (IMPO's text, in force from 1 January 1988), to today |
| `ley-10590/` | BANCO HIPOTECARIO DEL URUGUAY (BHU). DEPARTAMENTO DE AHORRO Y PRESTAMOS. CREACION (Ley Nº 10.590 of 1944) | 1 | Current text only (IMPO's text, in force from 19 November 1953), to today |
| `ley-10604/` | FIJACION DE IMPUESTO. VENTAS Y TRANSACCIONES. BEBIDAS ALCOHOLICAS. MERCADERIAS SUNTUARIAS. TIMBRES Y PAPEL SELLADO (Ley Nº 10.604 of 1945) | 1 | Current text only (IMPO's text, in force from 16 April 1953), to today |
| `ley-10629/` | JUBILACIONES Y PENSIONES. MODIFICACION (Ley Nº 10.629 of 1945) | 1 | Current text only (IMPO's text, in force from 16 August 1945), to today |
| `ley-10652/` | TRABAJADORES. SEGURO DE PARO. EXTENSION (Ley Nº 10.652 of 1945) | 1 | Current text only (IMPO's text, in force from 5 October 1945), to today |
| `ley-10662/` | CAJA DE JUBILACIONES DE LA INDUSTRIA, COMERCIO Y SERVICIOS PUBLICOS. ACUMULACION DE INGRESOS (Ley Nº 10.662 of 1945) | 1 | Current text only (IMPO's text, in force from 7 February 1947), to today |
| `ley-10663/` | JUBILACIONES Y PENSIONES. MODIFICACION. INCAPACIDAD (Ley Nº 10.663 of 1945) | 1 | Current text only (IMPO's text, in force from 15 November 1945), to today |
| `ley-10690/` | PODER EJECUTIVO. AUTORIZACION. DEUDA PUBLICA. EMISION. AMPLIACION (Ley Nº 10.690 of 1945) | 1 | Current text only (IMPO's text, in force from 18 December 2011), to today |
| `ley-10707/` | COOPERATIVA NACIONAL DE PRODUCTORES DE LECHE (CONAPROLE). ORGANIZACION (Ley Nº 10.707 of 1946) | 1 | Current text only (IMPO's text, in force from 16 July 2000), to today |
| `ley-10730/` | LEY DE ORDENAMIENTO FINANCIERO. MODIFICACION (Ley Nº 10.730 of 1946) | 1 | Current text only (IMPO's text, in force from 11 June 1946), to today |
| `ley-10756/` | FUNCIONARIOS. REMUNERACIONES. RECURSOS. MODIFICACION DE IMPUESTO. HERENCIAS, LEGADOS Y DONACIONES. ALCOHOLES Y BEBIDAS ALCOHOLICAS. SOBRETASA INMOBILIARIA (Ley Nº 10.756 of 1946) | 1 | Current text only (IMPO's text, in force from 26 December 1960), to today |
| `ley-10781/` | TRABAJADORES. SEGURO DE PARO. PRORROGA (Ley Nº 10.781 of 1946) | 1 | Current text only (IMPO's text, in force from 4 October 1946), to today |
| `ley-10837/` | BANCO HIPOTECARIO DEL URUGUAY (BHU). DEUDA PUBLICA. EMISION. PRESTAMOS (Ley Nº 10.837 of 1946) | 1 | Current text only (IMPO's text, in force from 13 October 1950), to today |
| `ley-10879/` | PRESUPUESTO. MODIFICACION (Ley Nº 10.879 of 1946) | 1 | Current text only (IMPO's text, in force from 24 November 1950), to today |
| `ley-10895/` | PRESUPUESTO. MODIFICACION (Ley Nº 10.895 of 1947) | 1 | Current text only (IMPO's text, in force from 8 December 1963), to today |
| `ley-10942/` | FIJACION DE IMPUESTO. VENTAS Y TRANSACCIONES (Ley Nº 10.942 of 1947) | 1 | Current text only (IMPO's text, in force from 11 October 1947), to today |
| `ley-10959/` | INSTITUTO DE JUBILACIONES Y PENSIONES DEL URUGUAY. AUMENTO DE PASIVIDADES (Ley Nº 10.959 of 1947) | 1 | Current text only (IMPO's text, in force from 1 January 1962), to today |
| `ley-10966/` | COMPUTO DE SERVICIOS A EFECTOS JUBILATORIOS (Ley Nº 10.966 of 1947) | 1 | Current text only (IMPO's text, in force from 9 December 1947), to today |
| `ley-10971/` | CAJA DE JUBILACIONES BANCARIAS. MODIFICACION (Ley Nº 10.971 of 1947) | 1 | Current text only (IMPO's text, in force from 27 July 1950), to today |
| `ley-10997/` | INSTITUTO NACIONAL DE ALIMENTACION. MODIFICACION (Ley Nº 10.997 of 1947) | 1 | Current text only (IMPO's text, in force from 19 January 1948), to today |
| `ley-10998/` | FIJACION DE IMPUESTO. VENTAS Y TRANSACCIONES (Ley Nº 10.998 of 1947) | 1 | Current text only (IMPO's text, in force from 24 January 1948), to today |
| `ley-11035/` | COMPUTO DE SERVICIOS A EFECTOS JUBILATORIOS (Ley Nº 11.035 of 1948) | 1 | Current text only (IMPO's text, in force from 3 February 1948), to today |
| `ley-11053/` | BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY (BROU). PRESTAMOS (Ley Nº 11.053 of 1948) | 1 | Current text only (IMPO's text, in force from 1 January 1966), to today |
| `ley-11056/` | ENSEÑANZA. DOCENTES (Ley Nº 11.056 of 1948) | 1 | Current text only (IMPO's text, in force from 24 December 1960), to today |
| `ley-11073/` | SOCIEDADES COMERCIALES. SOCIEDADES ANONIMAS FINANCIERAS DE INVERSION (SAFI) (Ley Nº 11.073 of 1948) | 1 | Current text only (IMPO's text, in force from 12 June 1993), to today |
| `ley-11145/` | LEY ORGANICA MILITAR. MODIFICACION (Ley Nº 11.145 of 1948) | 1 | Current text only (IMPO's text, in force from 15 January 1949), to today |
| `ley-11197/` | LEY ORGANICA MILITAR. MODIFICACION (Ley Nº 11.197 of 1948) | 1 | Current text only (IMPO's text, in force from 25 January 1949), to today |
| `ley-11243/` | FIJACION DE IMPUESTO. GANACIAS ELEVADAS. PRORROGA (Ley Nº 11.243 of 1949) | 1 | Current text only (IMPO's text, in force from 7 February 1949), to today |
| `ley-11389/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 11.389 of 1949) | 1 | Current text only (IMPO's text, in force from 9 January 1950), to today |
| `ley-11419/` | EX INSTITUTO DE JUBILACIONES Y PENSIONES DEL URUGUAY. JUBILACIONES Y PENSIONES. CUOTA SUPLEMENTARIA. PRORROGA (Ley Nº 11.419 of 1950) | 1 | Current text only (IMPO's text, in force from 1 June 1950), to today |
| `ley-11495/` | JUBILACIONES Y PENSIONES. AUMENTO DE PASIVIDADES (Ley Nº 11.495 of 1950) | 1 | Current text only (IMPO's text, in force from 18 September 1975), to today |
| `ley-11496/` | CAJA DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO. AUTORIZACION. REGISTRO NACIONAL DE EMPRESAS. CREACION (Ley Nº 11.496 of 1950) | 1 | Current text only (IMPO's text, in force from 14 January 1973), to today |
| `ley-11520/` | ESTADO CIVIL. ADOPCION (Ley Nº 11.520 of 1950) | 1 | Current text only (IMPO's text, in force from 9 November 1950), to today |
| `ley-11584/` | LEY DE DESALOJOS. MODIFICACION (Ley Nº 11.584 of 1950) | 1 | Current text only (IMPO's text, in force from 20 November 1950), to today |
| `ley-11587/` | PRESUPUESTO. MODIFICACION (Ley Nº 11.587 of 1950) | 1 | Current text only (IMPO's text, in force from 24 November 1950), to today |
| `ley-11603/` | CORTE ELECTORAL. IMPRESION DE HOJAS DE VOTACION (Ley Nº 11.603 of 1950) | 1 | Current text only (IMPO's text, in force from 17 November 1950), to today |
| `ley-11617/` | CAJA DE JUBILACIONES Y PENSIONES DE LOS TRABAJADORES RURALES Y DOMESTICOS Y DE PENSIONES A LA VEJEZ. DENOMINACION (Ley Nº 11.617 of 1950) | 1 | Current text only (IMPO's text, in force from 1 January 1966), to today |
| `ley-11625/` | LEY ORGANICA DEL BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY (BROU). MODIFICACION (Ley Nº 11.625 of 1950) | 1 | Current text only (IMPO's text, in force from 1 January 1962), to today |
| `ley-11660/` | PODER EJECUTIVO. AUTORIZACION. MARINA (Ley Nº 11.660 of 1951) | 1 | Current text only (IMPO's text, in force from 24 December 1960), to today |
| `ley-11708/` | PODER EJECUTIVO. AUTORIZACION. DEUDA PUBLICA. AMPLIACION (Ley Nº 11.708 of 1951) | 1 | Current text only (IMPO's text, in force from 5 October 1951), to today |
| `ley-11740/` | PRIMERAS LINEAS URUGUAYAS DE NAVEGACION AEREA (PLUNA). CREACION (Ley Nº 11.740 of 1951) | 1 | Current text only (IMPO's text, in force from 17 October 1991), to today |
| `ley-11746/` | BANCO HIPOTECARIO DEL URUGUAY (BHU). PRESTAMOS. AMPLIACION (Ley Nº 11.746 of 1951) | 1 | Current text only (IMPO's text, in force from 10 December 1951), to today |
| `ley-11823/` | EXONERACION DE IMPUESTO. LANAS (Ley Nº 11.823 of 1952) | 1 | Current text only (IMPO's text, in force from 2 June 1952), to today |
| `ley-11828/` | COMISION HONORARIA PARA LA LUCHA ANTITUBERCULOSA. AMPLIACION DE FACULTADES (Ley Nº 11.828 of 1952) | 1 | Current text only (IMPO's text, in force from 14 August 1952), to today |
| `ley-11839/` | LEY ORGANICA DE LA CAJA DE JUBILACIONES BANCARIAS. MODIFICACION (Ley Nº 11.839 of 1952) | 1 | Current text only (IMPO's text, in force from 27 July 1952), to today |
| `ley-11846/` | EXONERACION DE IMPUESTO. LANAS. PRORROGA (Ley Nº 11.846 of 1952) | 1 | Current text only (IMPO's text, in force from 28 August 1952), to today |
| `ley-11861/` | EXONERACION DE IMPUESTO. LANAS. PRORROGA (Ley Nº 11.861 of 1952) | 1 | Current text only (IMPO's text, in force from 30 October 1952), to today |
| `ley-11869/` | PODER EJECUTIVO. AUTORIZACION. DEUDA PUBLICA. AMPLIACION. MODIFICACION DE IMPUESTO. TIMBRES Y PAPEL SELLADO (Ley Nº 11.869 of 1952) | 1 | Current text only (IMPO's text, in force from 13 November 1952), to today |
| `ley-11886/` | EXONERACION DE IMPUESTO. LANAS (Ley Nº 11.886 of 1952) | 1 | Current text only (IMPO's text, in force from 19 December 1952), to today |
| `ley-11921/` | ARRENDAMIENTOS. PRECIOS. DESALOJOS. LANZAMIENTOS (Ley Nº 11.921 of 1953) | 1 | Current text only (IMPO's text, in force from 30 January 1958), to today |
| `ley-11929/` | EXONERACION DE IMPUESTO. LANAS (Ley Nº 11.929 of 1953) | 1 | Current text only (IMPO's text, in force from 12 May 1953), to today |
| `ley-11948/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 11.948 of 1953) | 1 | Current text only (IMPO's text, in force from 25 July 1953), to today |
| `ley-11953/` | INSTITUTO JOSE BATLLE Y ORDOÑEZ. JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 11.953 of 1953) | 1 | Current text only (IMPO's text, in force from 4 November 1963), to today |
| `ley-11988/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 11.988 of 1953) | 1 | Current text only (IMPO's text, in force from 6 September 1953), to today |
| `ley-11990/` | CAJA DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO. BENEFICIOS JUBILATORIOS (Ley Nº 11.990 of 1953) | 1 | Current text only (IMPO's text, in force from 19 September 1953), to today |
| `ley-12003/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 12.003 of 1953) | 1 | Current text only (IMPO's text, in force from 9 October 1953), to today |
| `ley-12016/` | FUNCIONARIOS. REMUNERACIONES (Ley Nº 12.016 of 1953) | 1 | Current text only (IMPO's text, in force from 21 January 1961), to today |
| `ley-12032/` | CAJA DE JUBILACIONES Y PENSIONES. REGULACION (Ley Nº 12.032 of 1953) | 1 | Current text only (IMPO's text, in force from 10 September 1960), to today |
| `ley-12048/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 12.048 of 1953) | 1 | Current text only (IMPO's text, in force from 10 January 1954), to today |
| `ley-12049/` | JUBILACIONES Y PENSIONES. BENEFICIOS JUBILATORIOS (Ley Nº 12.049 of 1953) | 1 | Current text only (IMPO's text, in force from 8 January 1954), to today |
| `ley-12071/` | LEY ORGANICA MILITAR. MODIFICACION (Ley Nº 12.071 of 1953) | 1 | Current text only (IMPO's text, in force from 2 January 1954), to today |
| `ley-12075/` | JUBILACIONES Y PENSIONES. MODIFICACION DE IMPUESTO. REMUNERACIONES (Ley Nº 12.075 of 1953) | 1 | Current text only (IMPO's text, in force from 14 January 1954), to today |
| `ley-12080/` | PRESUPUESTO. MODIFICACION (Ley Nº 12.080 of 1953) | 1 | Current text only (IMPO's text, in force from 15 January 1954), to today |
| `ley-12081/` | JUBILACIONES Y PENSIONES. AUMENTO DE PASIVIDADES (Ley Nº 12.081 of 1953) | 1 | Current text only (IMPO's text, in force from 15 January 2011), to today |
| `ley-12088/` | CAJA DE JUBILACIONES BANCARIAS. AUTORIZACION. PRESTAMOS. AFILIADOS. VIVIENDA (Ley Nº 12.088 of 1953) | 1 | Current text only (IMPO's text, in force from 3 August 1964), to today |
| `ley-12100/` | LEY DE ARRENDAMIENTOS RURALES (Ley Nº 12.100 of 1954) | 1 | Current text only (IMPO's text, in force from 30 October 1970), to today |
| `ley-12108/` | CAJA DE JUBILACIONES Y PENSIONES. AUTORIZACION. FUNCIONARIOS. PRESTAMOS. VIVIENDA (Ley Nº 12.108 of 1954) | 1 | Current text only (IMPO's text, in force from 9 February 1968), to today |
| `ley-12132/` | CAJA DE JUBILACIONES BANCARIAS. BENEFICIO DE RETIRO (Ley Nº 12.132 of 1954) | 1 | Current text only (IMPO's text, in force from 8 November 1958), to today |
| `ley-12140/` | ADMINISTRACION DE FERROCARRILES DEL ESTADO (AFE). PRORROGA (Ley Nº 12.140 of 1954) | 1 | Current text only (IMPO's text, in force from 8 November 1956), to today |
| `ley-12141/` | ARRENDAMIENTOS. MODIFICACION. PRECIOS. DESALOJOS. LANZAMIENTOS. SUSPENSION (Ley Nº 12.141 of 1954) | 1 | Current text only (IMPO's text, in force from 5 November 1954), to today |
| `ley-12142/` | CAJA DE JUBILACIONES Y PENSIONES DE LOS TRABAJADORES RURALES Y DOMESTICOS Y DE PENSIONES A LA VEJEZ. MODIFICACION (Ley Nº 12.142 of 1954) | 1 | Current text only (IMPO's text, in force from 16 November 1954), to today |
| `ley-12143/` | CAJA DE JUBILACIONES Y PENSIONES. REGULACION (Ley Nº 12.143 of 1954) | 1 | Current text only (IMPO's text, in force from 16 November 1954), to today |
| `ley-12145/` | CORTE ELECTORAL. ELECCIONES NACIONALES. GASTOS ELECCIONARIOS DE LOS PARTIDOS POLITICOS (Ley Nº 12.145 of 1954) | 1 | Current text only (IMPO's text, in force from 5 November 1954), to today |
| `ley-12159/` | ARRENDAMIENTOS. PRECIOS (Ley Nº 12.159 of 1954) | 1 | Current text only (IMPO's text, in force from 15 November 1954), to today |
| `ley-12169/` | LEY ORGANICA DE LA CAJA DE JUBILACIONES BANCARIAS. MODIFICACION (Ley Nº 12.169 of 1954) | 1 | Current text only (IMPO's text, in force from 21 January 1961), to today |
| `ley-12179/` | CONTRALOR DE LA CORTE ELECTORAL EN LAS ELECCIONES DE LAS INSTITUCIONES QUE GOCEN DE CONCESIONES DEL ESTADO (Ley Nº 12.179 of 1955) | 1 | Current text only (IMPO's text, in force from 30 January 2014), to today |
| `ley-12182/` | PRORROGA DE PLAZO OTORGADO POR EL BROU RELATIVO A SU CARTERA DE DOCUMENTOS REDESCONTADOS (Ley Nº 12.182 of 1955) | 1 | Current text only (IMPO's text, in force from 1 February 1955), to today |
| `ley-12190/` | PRORROGA DE PLAZO PARA EL PAGO DE APORTES A LA CAJA DE JUBILACIONES Y PENSIONES DE LOS TRABAJADORES RURALES Y DOMESTICOS Y DE PENSIONES A LA VEJEZ (Ley Nº 12.190 of 1955) | 1 | Current text only (IMPO's text, in force from 30 June 1955), to today |
| `ley-12202/` | FIJACION DE SUELDOS FICTOS Y PASIVIDADES DE CAJA NOTARIAL DE JUBILACIONES Y PENSIONES (Ley Nº 12.202 of 1955) | 1 | Current text only (IMPO's text, in force from 29 July 1955), to today |
| `ley-12231/` | EMISION DE TITULOS HIPOTECARIOS. BHU (Ley Nº 12.231 of 1955) | 1 | Current text only (IMPO's text, in force from 27 January 1957), to today |
| `ley-12264/` | MODIFICACION DEL ART. 8º DE LEY 9.899 RELATIVO A LA DIRECCION DE CONAPROLE (Ley Nº 12.264 of 1956) | 1 | Current text only (IMPO's text, in force from 26 January 1956), to today |
| `ley-12275/` | MODIFICACION DE LOS ARTICULOS 11 Y 12 DE LA LEY 12.070 RELATIVO A ASCENSOS DE FUNCIONARIOS MILITARES (Ley Nº 12.275 of 1956) | 1 | Current text only (IMPO's text, in force from 3 April 1956), to today |
| `ley-12280/` | AUTORIZACION DE DONACION DE BUQUES DE LA ARMADA NACIONAL (Ley Nº 12.280 of 1956) | 1 | Current text only (IMPO's text, in force from 7 June 1956), to today |
| `ley-12282/` | PRORROGA DE PLAZO PARA LA INSCRIPCION DE CONTRATOS DE ARRENDAMIENTOS RURALES (Ley Nº 12.282 of 1956) | 1 | Current text only (IMPO's text, in force from 10 June 1956), to today |
| `ley-12290/` | INDEMNIZACION POR ACCIDENTES DE TRABAJO Y ENFERMEDADES PROFESIONALES Y FIJACION DE SALARIOS MAXIMOS (Ley Nº 12.290 of 1956) | 1 | Current text only (IMPO's text, in force from 7 January 1962), to today |
| `ley-12324/` | MODIFICACION DE LA LEYES NROS. 10.131 Y 10.568 RELATIVO AL ASCENSO DE FUNCIONARIOS MILITARES DEL CUERPO TECNICO DE ARMAMENTOS Y EXPLOSIVOS (Ley Nº 12.324 of 1956) | 1 | Current text only (IMPO's text, in force from 2 December 1956), to today |
| `ley-12346/` | CONCESION DE PRESTAMOS. COOPERATIVA BANCARIA (Ley Nº 12.346 of 1956) | 1 | Current text only (IMPO's text, in force from 1 January 1957), to today |
| `ley-12374/` | DETERMINASE LA SUSPENSION DE LANZAMIENTOS CONTRA ARRENDATARIOS O SUBARRENDATARIOS BUENOS PAGADORES Y EL CUMPLIMIENTO DE RESOLUCIONES DE ALQUILER RAZONABLE (Ley Nº 12.374 of 1957) | 1 | Current text only (IMPO's text, in force from 7 February 1957), to today |
| `ley-12380/` | INCREMENTO DE LAS JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO (Ley Nº 12.380 of 1957) | 1 | Current text only (IMPO's text, in force from 1 August 2023), to today |
| `ley-12381/` | REGULACION DEL REGIMEN JUBILATORIO. AFILIADOS DE LA CAJA DE JUBILACIONES Y PENSIONES CIVILES Y ESCOLARES (Ley Nº 12.381 of 1957) | 1 | Current text only (IMPO's text, in force from 5 March 1957), to today |
| `ley-12391/` | PRORROGA DE PLAZO. DESALOJOS RURALES (Ley Nº 12.391 of 1957) | 1 | Current text only (IMPO's text, in force from 25 June 1957), to today |
| `ley-12403/` | PRORROGA LA LEY 12.374 RELATIVO A LA SUSPENSION DE LANZAMIENTOS CONTRA ARRENDATARIOS O SUBARRENDATARIOS (Ley Nº 12.403 of 1957) | 1 | Current text only (IMPO's text, in force from 19 September 1957), to today |
| `ley-12425/` | INCORPORACION A LOS EFECTIVOS OFICIALES COMO SERVICIOS AUXILIARES. AERONAUTICA MILITAR (Ley Nº 12.425 of 1957) | 1 | Current text only (IMPO's text, in force from 9 December 1957), to today |
| `ley-12463/` | SE ESTABLECE UN PLAN DE OBRAS PUBLICAS Y SE CONCEDEN RECURSOS PARA REALIZARLAS. (Ley Nº 12.463 of 1957) | 1 | Current text only (IMPO's text, in force from 24 April 1979), to today |
| `ley-12467/` | CREACION DE LAS COMISIONES DE BOLSA DE TRABAJO DE ESTIBA (Ley Nº 12.467 of 1957) | 1 | Current text only (IMPO's text, in force from 29 December 1960), to today |
| `ley-12480/` | INSCRIPCION DE DOCUMENTOS EN EL REGISTRO GENERAL DE INHIBICIONES. (Ley Nº 12.480 of 1957) | 1 | Current text only (IMPO's text, in force from 1 January 1993), to today |
| `ley-12492/` | ARRENDAMIENTOS. FIJACION DE PRECIOS. SUSPENSION DE DESALOJOS (Ley Nº 12.492 of 1958) | 1 | Current text only (IMPO's text, in force from 17 October 1964), to today |
| `ley-12499/` | CAJA DE COMPENSACION POR DESOCUPACION EN LA INDUSTRIA FRIGORIFICA. FRIGORIFICO SWIFT Y ARTIGAS. JUEGOS DE QUINIELA. TRIBUTOS (Ley Nº 12.499 of 1958) | 1 | Current text only (IMPO's text, in force from 10 May 1958), to today |
| `ley-12506/` | ARRENDAMIENTOS RURALES. PRORROGA DE REGIMEN DE ESTABILIZACION DE CONTRATOS Y JUICIOS DE DESALOJOS (Ley Nº 12.506 of 1958) | 1 | Current text only (IMPO's text, in force from 28 June 1958), to today |
| `ley-12528/` | INSTITUTO NACIONAL DE VIVIENDAS ECONOMICAS. CONSTRUCCION VENTA Y ARRENDAMIENTO DE VIVIENDAS (Ley Nº 12.528 of 1958) | 1 | Current text only (IMPO's text, in force from 11 October 1958), to today |
| `ley-12539/` | MODIFICACION DE HORARIOS DE TRABAJO A FUNCIONARIOS DE SALUD PUBLICA (Ley Nº 12.539 of 1958) | 1 | Current text only (IMPO's text, in force from 18 October 1959), to today |
| `ley-12550/` | REGIMEN JUBILATORIO ESPECIAL. FUNCIONARIOS DE LA SALUD (Ley Nº 12.550 of 1958) | 1 | Current text only (IMPO's text, in force from 2 November 1958), to today |
| `ley-12551/` | SEGURIDAD SOCIAL. TRABAJADORES DEL TURF (Ley Nº 12.551 of 1958) | 1 | Current text only (IMPO's text, in force from 5 January 1962), to today |
| `ley-12565/` | OBRAS PUBLICAS (Ley Nº 12.565 of 1958) | 1 | Current text only (IMPO's text, in force from 21 November 1958), to today |
| `ley-12570/` | CREACION DEL SEGURO DE PARO OBLIGATORIO PARA TRABAJADORES DE LA ACTIVIDAD REMUNERADA. SE COMETE LA ORGANIZACION DE BOLSAS DE TRABAJO A LA CAJA DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO (Ley Nº 12.570 of 1958) | 1 | Current text only (IMPO's text, in force from 24 November 1962), to today |
| `ley-12572/` | REGIMEN ESPECIAL DE SALARIOS DE MATERNIDAD (Ley Nº 12.572 of 1958) | 1 | Current text only (IMPO's text, in force from 24 December 1960), to today |
| `ley-12577/` | APORTES A LA CAJA DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO Y CAJA DE ASIGNACIONES FAMILIARES. SE CONCEDEN EXONERACIONES DE MULTAS, RECARGOS E INTERESES A MOROSOS (Ley Nº 12.577 of 1958) | 1 | Current text only (IMPO's text, in force from 7 November 1958), to today |
| `ley-12580/` | ACTIVIDAD HIPICA. REGIMEN JUBILATORIO DE LOS TRABAJADORES DEL TURF (Ley Nº 12.580 of 1958) | 1 | Current text only (IMPO's text, in force from 5 January 1962), to today |
| `ley-12588/` | REGIMEN ESPECIAL DE RETIROS Y PENSIONES PARA INTEGRANTES DE LAS FUERZAS ARMADAS FALLECIDOS EN ACTO DEL SERVICIO (Ley Nº 12.588 of 1958) | 1 | Current text only (IMPO's text, in force from 6 December 1970), to today |
| `ley-12589/` | MODIFICACION DEL ESTATUTO PARA EL TRABAJADOR RURAL. AUMENTO DE SALARIOS MINIMOS (Ley Nº 12.589 of 1958) | 1 | Current text only (IMPO's text, in force from 17 January 1959), to today |
| `ley-12595/` | IMPUESTO A LAS GANANCIAS ELEVADAS. REVALUACION DE BIENES MUEBLES AMORTIZABLES (Ley Nº 12.595 of 1958) | 1 | Current text only (IMPO's text, in force from 25 January 1959), to today |
| `ley-12599/` | CREACION DE LA JUNTA NACIONAL DE COORDINACION DE TRANSPORTES DE CARGA (Ley Nº 12.599 of 1959) | 1 | Current text only (IMPO's text, in force from 25 January 1965), to today |
| `ley-12603/` | ARRENDAMIENTOS RURALES. PRORROGA DE REGIMEN DE ESTABILIZACION DE CONTRATOS Y JUICIOS DE DESALOJOS (Ley Nº 12.603 of 1959) | 1 | Current text only (IMPO's text, in force from 17 May 1959), to today |
| `ley-12669/` | PLAN ANUAL DE OBRAS PUBLICAS (Ley Nº 12.669 of 1959) | 1 | Current text only (IMPO's text, in force from 2 January 1960), to today |
| `ley-12670/` | LEY DE REFORMA CAMBIARIA Y MONETARIA. TRIBUTOS A LA IMPORTACION. DETRACCIONES (Ley Nº 12.670 of 1959) | 1 | Current text only (IMPO's text, in force from 19 January 1978), to today |
| `ley-12689/` | REGISTRO DE ESTADO CIVIL (Ley Nº 12.689 of 1959) | 1 | Current text only (IMPO's text, in force from 22 January 1960), to today |
| `ley-12707/` | AUTORIZACION PARA CONCESION DE PRESTAMOS PARA ADQUISICION DE VIVIENDAS (Ley Nº 12.707 of 1960) | 1 | Current text only (IMPO's text, in force from 7 May 1960), to today |
| `ley-12738/` | DEUDA PUBLICA. FMI. BIRF (Ley Nº 12.738 of 1960) | 1 | Current text only (IMPO's text, in force from 15 August 1965), to today |
| `ley-12778/` | SEGURIDAD SOCIAL. COMPUTO JUBILATORIO. ASISTENCIA MEDICA Y ODONTOLOGICA HONORARIA (Ley Nº 12.778 of 1960) | 1 | Current text only (IMPO's text, in force from 1 January 1966), to today |
| `ley-12805/` | POLITICA DE VIVIENDA. PRESTAMOS HIPOTECARIOS (Ley Nº 12.805 of 1960) | 1 | Current text only (IMPO's text, in force from 22 December 1960), to today |
| `ley-12807/` | MODIFICACIONES A LA LEY 12.467 SOBRE CREACION DE LA BOLSA DE TRABAJO DE ESTIBA DE LOS PUERTOS DEL LITORAL E INTERIOR (Ley Nº 12.807 of 1960) | 1 | Current text only (IMPO's text, in force from 29 December 1960), to today |
| `ley-12839/` | SEGURO DE ENFERMEDAD, INVALIDEZ, ASISTENCIA, PRESTACIONES MEDICAS Y FARMACEUTICAS. OBREROS Y EMPLEADOS DE LA INDUSTRIA DE LA CONSTRUCCION Y RAMAS CONEXAS (Ley Nº 12.839 of 1960) | 1 | Current text only (IMPO's text, in force from 10 November 1968), to today |
| `ley-12842/` | MODIFICACION DEL ESTATUTO DEL TRABAJADOR RURAL (Ley Nº 12.842 of 1960) | 1 | Current text only (IMPO's text, in force from 14 January 1961), to today |
| `ley-12882/` | REGIMEN DE BENEFICIOS JUBILATORIOS Y RETIROS. MAESTROS ESPECIALES (Ley Nº 12.882 of 1961) | 1 | Current text only (IMPO's text, in force from 17 July 1961), to today |
| `ley-12930/` | SEGURIDAD SOCIAL. BENEFICIOS PARA TRABAJADORES CESANTES DE LA INDUSTRIA TABACALERA (Ley Nº 12.930 of 1961) | 1 | Current text only (IMPO's text, in force from 1 January 1962), to today |
| `ley-12934/` | SEGURIDAD SOCIAL. SUELDO FICTO PATRONAL. REGIMEN JUBILATORIO (Ley Nº 12.934 of 1961) | 1 | Current text only (IMPO's text, in force from 20 March 1975), to today |
| `ley-12937/` | SANIDAD ANIMAL. LUCHA CONTRA LA BRUCELOSIS (Ley Nº 12.937 of 1961) | 1 | Current text only (IMPO's text, in force from 30 October 1970), to today |
| `ley-12952/` | SE DETERMINAN CAUSALES PARA JUBILACIONES BANCARIAS (Ley Nº 12.952 of 1961) | 1 | Current text only (IMPO's text, in force from 21 December 1961), to today |
| `ley-12999/` | REGIMEN DE JUBILACIONES Y PENSIONES BANCARIAS (Ley Nº 12.999 of 1961) | 1 | Current text only (IMPO's text, in force from 5 January 1962), to today |
| `ley-13000/` | ACTIVIDAD HIPICA. REGIMEN JUBILATORIO (Ley Nº 13.000 of 1961) | 1 | Current text only (IMPO's text, in force from 30 January 1962), to today |
| `ley-13002/` | EXPLOTACION DE JUEGOS DE AZAR. GOBIERNO DEPARTAMENTAL DE MONTEVIDEO (Ley Nº 13.002 of 1961) | 1 | Current text only (IMPO's text, in force from 29 December 1961), to today |
| `ley-13031/` | REGIMEN DE JUBILACIONES Y PENSIONES BANCARIAS (Ley Nº 13.031 of 1961) | 1 | Current text only (IMPO's text, in force from 5 January 1962), to today |
| `ley-13033/` | REESTRUCTURA EL REGIMEN DE PENSIONES MILITARES (Ley Nº 13.033 of 1961) | 1 | Current text only (IMPO's text, in force from 10 January 2021), to today |
| `ley-13035/` | ESTATUTO DEL TRABAJADOR RURAL. MINISTERIO DE GANADERIA Y AGRICULTURA (Ley Nº 13.035 of 1962) | 1 | Current text only (IMPO's text, in force from 3 February 1962), to today |
| `ley-13037/` | POLITICA DE VIVIENDAS. TOPE A PRESTAMOS (Ley Nº 13.037 of 1962) | 1 | Current text only (IMPO's text, in force from 11 February 1962), to today |
| `ley-13048/` | FIJACION DE DETRACCIONES A LAS EXPORTACIONES DE CUEROS BOVINOS (Ley Nº 13.048 of 1962) | 1 | Current text only (IMPO's text, in force from 9 November 1968), to today |
| `ley-13052/` | PLAN DE INVERSIONES AGROPECUARIAS (Ley Nº 13.052 of 1962) | 1 | Current text only (IMPO's text, in force from 21 December 1964), to today |
| `ley-13103/` | PLAN DE INVERSIONES PUBLICAS. EJERCICIO 1961 (Ley Nº 13.103 of 1962) | 1 | Current text only (IMPO's text, in force from 23 November 1962), to today |
| `ley-13106/` | SEGURO DE ENFERMEDAD, INVALIDEZ, ASISTENCIA, PRESTACIONES MEDICAS Y FARMACEUTICAS. OBREROS Y EMPLEADOS DE LA INDUSTRIA DE LA CONSTRUCCION (Ley Nº 13.106 of 1962) | 1 | Current text only (IMPO's text, in force from 16 November 1962), to today |
| `ley-13108/` | OBLIGATORIEDAD DEL SEGURO DE PARO. MODIFICACIONES (Ley Nº 13.108 of 1962) | 1 | Current text only (IMPO's text, in force from 24 November 1962), to today |
| `ley-13117/` | CAJAS DE COMPENSACIONES POR DESOCUPACION EN LAS BARRACAS DE LANAS CUEROS Y AFINES. PRESTAMOS HIPOTECARIOS PARA VIVIENDAS (Ley Nº 13.117 of 1962) | 1 | Current text only (IMPO's text, in force from 21 January 1967), to today |
| `ley-13122/` | MODIFICACION DE LA CARTA ORGANICA DEL BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY (Ley Nº 13.122 of 1963) | 1 | Current text only (IMPO's text, in force from 25 April 1963), to today |
| `ley-13133/` | EMISION DE TITULOS HIPOTECARIOS. BANCO HIPOTECARIO DEL URUGUAY (Ley Nº 13.133 of 1963) | 1 | Current text only (IMPO's text, in force from 8 July 1963), to today |
| `ley-13150/` | DEUDA PUBLICA. PRESTAMO PARA MEJORAMIENTO DE RUTA Nº 5 (Ley Nº 13.150 of 1963) | 1 | Current text only (IMPO's text, in force from 2 September 1963), to today |
| `ley-13168/` | OTORGAMIENTO DE PENSIONES GRACIABLES. FUNDADORES DE LICEOS PUBLICOS. DIRECTORES Y PROFESORES DESIGNADOS INSPECTORES (Ley Nº 13.168 of 1963) | 1 | Current text only (IMPO's text, in force from 1 January 1966), to today |
| `ley-13223/` | ASISTENCIA INTEGRAL GRATUITA PARA FUNCIONARIOS Y EX FUNCIONARIOS DEL MINISTERIO DE SALUD PUBLICA Y TRABAJADORES DE LA COMISION HONORARIA DE LA LUCHA ANTITUBERCULOSA (Ley Nº 13.223 of 1963) | 1 | Current text only (IMPO's text, in force from 25 October 2008), to today |
| `ley-13229/` | APROBACION DE CONTRATO DE PRESTAMO CON EL BID. FINANCIAMIENTO DE PROGRAMA DEL PLAN NACIONAL DE VIVIENDAS (Ley Nº 13.229 of 1963) | 1 | Current text only (IMPO's text, in force from 19 January 1970), to today |
| `ley-13242/` | SEGURO DE ENFERMEDAD DE INVALIDEZ Y DE ASISTENCIA MEDICA. INDUSTRIA DE LA CONSTRUCCION Y RAMAS ANEXAS (Ley Nº 13.242 of 1964) | 1 | Current text only (IMPO's text, in force from 8 March 1964), to today |
| `ley-13245/` | MODIFICACION DEL ESTATUTO PARA EL TRABAJADOR RURAL (Ley Nº 13.245 of 1964) | 1 | Current text only (IMPO's text, in force from 29 March 1964), to today |
| `ley-13251/` | ARRENDAMIENTOS RURALES. PRORROGA DE LA SUSPENSION DE LANZAMIENTOS (Ley Nº 13.251 of 1964) | 1 | Current text only (IMPO's text, in force from 25 May 1964), to today |
| `ley-13261/` | CONSTRUCCION DE CENTRALES TERMICAS DE GENERACION. CENTRAL HIDRAULICA. USINAS DE RINCON DEL BONETE. APROBACION DE PLAN GENERAL DE OBRAS DE LA UTE (Ley Nº 13.261 of 1964) | 1 | Current text only (IMPO's text, in force from 19 June 1964), to today |
| `ley-13270/` | ACTUALIZACION DE MONTOS DE TIMBRES PROFESIONALES (Ley Nº 13.270 of 1964) | 1 | Current text only (IMPO's text, in force from 3 August 1964), to today |
| `ley-13271/` | OTORGAMIENTO DE PRESTAMOS PARA AFILIADOS A LA CAJA DE JUBILACIONES BANCARIAS (Ley Nº 13.271 of 1964) | 1 | Current text only (IMPO's text, in force from 3 August 1964), to today |
| `ley-13301/` | PLAN DE INVERSIONES AGROPECUARIAS. EJERCICIO 1963 (Ley Nº 13.301 of 1964) | 1 | Current text only (IMPO's text, in force from 21 December 1964), to today |
| `ley-13350/` | AUTORIZACION AL PODER EJECUTIVO A CAUCIONAR EN EL BANCO DE LA REPUBLICA LOS SALDOS DE DEUDA PUBLICA (Ley Nº 13.350 of 1965) | 1 | Current text only (IMPO's text, in force from 9 February 1968), to today |
| `ley-13387/` | ARRENDAMIENTOS URBANOS. INCREMENTO DE ALQUILERES (Ley Nº 13.387 of 1965) | 1 | Current text only (IMPO's text, in force from 5 July 1970), to today |
| `ley-13390/` | REGIMEN DE SERVICIO DE VIGILANCIA A BORDO DE BUQUES (Ley Nº 13.390 of 1965) | 1 | Current text only (IMPO's text, in force from 1 January 1993), to today |
| `ley-13454/` | MODIFICACIONES AL REGIMEN DE ARRENDAMIENTOS DESALOJOS Y LANZAMIENTOS (Ley Nº 13.454 of 1965) | 1 | Current text only (IMPO's text, in force from 7 January 1966), to today |
| `ley-13459/` | HIDATIDOSIS. DECLARACION DE PLAGA NACIONAL. CREACION DE COMISION NACIONAL HONORARIA DE LUCHA CONTRA LA HIDATIDOSIS (Ley Nº 13.459 of 1965) | 1 | Current text only (IMPO's text, in force from 1 January 2006), to today |
| `ley-13479/` | IMPUESTO UNICO A LA ACTIVIDAD BANCARIA Y CREACION DEL FONDO DE SUBSIDIO Y CENSO (Ley Nº 13.479 of 1966) | 1 | Current text only (IMPO's text, in force from 6 March 1967), to today |
| `ley-13484/` | BOLSA DE TRABAJO. PANADERIAS DE MONTEVIDEO (Ley Nº 13.484 of 1966) | 1 | Current text only (IMPO's text, in force from 8 August 1966), to today |
| `ley-13487/` | SERVICIOS DE COBRANZA DOMICILIARIA (Ley Nº 13.487 of 1966) | 1 | Current text only (IMPO's text, in force from 3 September 1966), to today |
| `ley-13524/` | PROMESAS DE ENAJENACION DE INMUEBLES A PLAZO. ESCRITURACION FORZADA (Ley Nº 13.524 of 1966) | 1 | Current text only (IMPO's text, in force from 11 November 1966), to today |
| `ley-13550/` | SEGURIDAD SOCIAL. AMPLIACION DE SEGURO DE ENFERMEDAD, DE INVALIDEZ Y DE ASISTENCIA MEDICA DE EMPLEADOS Y OBREROS DE LA INDUSTRIA DEL METAL Y RAMAS AFINES (Ley Nº 13.550 of 1966) | 1 | Current text only (IMPO's text, in force from 6 March 1967), to today |
| `ley-13552/` | SEGURIDAD SOCIAL. CREACION DE CAJA DE COMPENSACIONES POR DESOCUPACION EN LA INDUSTRIA FRIGORIFICA DEL INTERIOR (Ley Nº 13.552 of 1966) | 1 | Current text only (IMPO's text, in force from 21 November 1980), to today |
| `ley-13559/` | ACTIVIDAD PRIVADA. COMPENSACION POR HOGAR CONSTITUIDO (Ley Nº 13.559 of 1966) | 1 | Current text only (IMPO's text, in force from 6 March 1967), to today |
| `ley-13574/` | ACTO ELECCIONARIO DEL 27 DE NOVIEMBRE DE 1966. AMPLIACION DE TITULOS DE DEUDA PUBLICA (Ley Nº 13.574 of 1966) | 1 | Current text only (IMPO's text, in force from 14 November 1966), to today |
| `ley-13576/` | SEGURIDAD SOCIAL. CAJA DE COMPENSACIONES POR DESOCUPACION EN LA INDUSTRIA FRIGORIFICA (Ley Nº 13.576 of 1966) | 1 | Current text only (IMPO's text, in force from 15 January 1968), to today |
| `ley-13583/` | IMPUESTOS. BEBIDAS ALCOHOLICAS. ESPECTACULOS PUBLICOS. TELEFONOS (Ley Nº 13.583 of 1967) | 1 | Current text only (IMPO's text, in force from 9 March 1967), to today |
| `ley-13585/` | SEGURIDAD SOCIAL. TRABAJADORES DE LOS PUERTOS DEL LITORAL E INTERIOR. (Ley Nº 13.585 of 1967) | 1 | Current text only (IMPO's text, in force from 9 March 1967), to today |
| `ley-13597/` | SEGURIDAD SOCIAL. AFILIACIONES. DEUDAS BANCARIAS Y PRESTAMOS A PRODUCTORES E INDUSTRIALES (Ley Nº 13.597 of 1967) | 1 | Current text only (IMPO's text, in force from 27 January 1980), to today |
| `ley-13603/` | ARRENDAMIENTOS RURALES. SUSPENSION DE DESALOJOS Y LANZAMIENTOS (Ley Nº 13.603 of 1967) | 1 | Current text only (IMPO's text, in force from 30 October 1970), to today |
| `ley-13645/` | IMPUESTO A LOS ARRENDAMIENTOS (Ley Nº 13.645 of 1968) | 1 | Current text only (IMPO's text, in force from 27 April 1968), to today |
| `ley-13652/` | ARRENDAMIENTOS RURALES. SUSPENSION DE DESALOJOS Y LANZAMIENTOS (Ley Nº 13.652 of 1968) | 1 | Current text only (IMPO's text, in force from 12 May 1968), to today |
| `ley-13666/` | SEGURIDAD SOCIAL (Ley Nº 13.666 of 1968) | 1 | Current text only (IMPO's text, in force from 30 March 1973), to today |
| `ley-13668/` | IMPUESTO A LA PENSION GRACIABLE (Ley Nº 13.668 of 1968) | 1 | Current text only (IMPO's text, in force from 6 July 1968), to today |
| `ley-13738/` | ARRENDAMIENTOS. REGIMEN DE PLAZOS. JUICIO DE DESALOJO (Ley Nº 13.738 of 1969) | 1 | Current text only (IMPO's text, in force from 23 May 1969), to today |
| `ley-13760/` | EXTENSION DEL PLAZO DE CANCELACION DE DEUDAS HIPOTECARIAS (Ley Nº 13.760 of 1969) | 1 | Current text only (IMPO's text, in force from 23 August 1969), to today |
| `ley-13818/` | FUNCIONARIOS MILITARES EN SITUACION DE RETIRO (Ley Nº 13.818 of 1969) | 1 | Current text only (IMPO's text, in force from 2 January 1970), to today |
| `ley-13831/` | REMUNERACIONES DE LA CAJA DE JUBILACIONES Y PENSIONES DE PROFESIONALES UNIVERSITARIOS (Ley Nº 13.831 of 1969) | 1 | Current text only (IMPO's text, in force from 5 January 1970), to today |
| `ley-13836/` | EXPROPIACION DE BIEN INMUEBLE. MONTEVIDEO (Ley Nº 13.836 of 1970) | 1 | Current text only (IMPO's text, in force from 19 February 1972), to today |
| `ley-13837/` | PRESTAMOS SOCIALES OTORGADOS POR LA CAJA DE COMPENSACIONES POR DESOCUPACION EN LA INDUSTRIA FRIGORIFICA (Ley Nº 13.837 of 1970) | 1 | Current text only (IMPO's text, in force from 19 January 1978), to today |
| `ley-13864/` | COMPRAVENTA DE VIVIENDAS ARRENDADAS DEL INSTITUTO NACIONAL DE VIVIENDAS ECONOMICAS (Ley Nº 13.864 of 1970) | 1 | Current text only (IMPO's text, in force from 19 May 1974), to today |
| `ley-13939/` | EXPROPIACION DE BIEN INMUEBLE. MONTEVIDEO (Ley Nº 13.939 of 1971) | 1 | Current text only (IMPO's text, in force from 1 January 2006), to today |
| `ley-13963/` | LEY ORGANICA POLICIAL (Ley Nº 13.963 of 1971) | 1 | Current text only (IMPO's text, in force from 29 July 1995), to today |
| `ley-13987/` | PRORROGA DEL PLAZO PARA PRESTAMOS DE VIVIENDAS (Ley Nº 13.987 of 1971) | 1 | Current text only (IMPO's text, in force from 29 July 1971), to today |
| `ley-14003/` | REVALUACION DE PASIVIDADES (Ley Nº 14.003 of 1971) | 1 | Current text only (IMPO's text, in force from 20 August 1971), to today |
| `ley-14012/` | CREACION DE RECURSOS PARA GASTOS DE REALIZACION DE ACTO ELECTORAL (Ley Nº 14.012 of 1971) | 1 | Current text only (IMPO's text, in force from 18 September 1971), to today |
| `ley-14020/` | REGIMEN DE SUBSIDIOS Y PENSIONES MILITARES (Ley Nº 14.020 of 1971) | 1 | Current text only (IMPO's text, in force from 26 September 1971), to today |
| `ley-14050/` | LEY ORGANICA POLICIAL (Ley Nº 14.050 of 1971) | 1 | Current text only (IMPO's text, in force from 28 January 1972), to today |
| `ley-14069/` | REGULARIZACION DE DEUDAS A LAS CAJAS DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO (Ley Nº 14.069 of 1972) | 1 | Current text only (IMPO's text, in force from 11 August 1972), to today |
| `ley-14083/` | ARRENDAMIENTOS. SUSPENSION DE LANZAMIENTOS CONTRA ARRENDATARIOS Y SUBARRENDATARIOS BUENOS PAGADORES Y SUS EXCEPCIONES (Ley Nº 14.083 of 1972) | 1 | Current text only (IMPO's text, in force from 24 September 1972), to today |
| `ley-14104/` | MODIFICACIONES A LA LEY DE VIVIENDAS. FONDO NACIONAL DE VIVIENDAS (Ley Nº 14.104 of 1973) | 1 | Current text only (IMPO's text, in force from 9 February 1973), to today |
| `ley-14105/` | MODIFICACIONES A LA LEY DE VIVIENDAS. FONDO NACIONAL DE VIVIENDAS (Ley Nº 14.105 of 1973) | 1 | Current text only (IMPO's text, in force from 4 February 1973), to today |
| `ley-14123/` | CONTRABANDO. DEFRAUDACION (Ley Nº 14.123 of 1973) | 1 | Current text only (IMPO's text, in force from 2 June 1973), to today |
| `ley-14143/` | VEHICULOS AUTOMOTORES. TASA DE CERTIFICACION DE REGISTRO (Ley Nº 14.143 of 1973) | 1 | Current text only (IMPO's text, in force from 22 July 1973), to today |
| `ley-15738/` | CONVALIDACION DE LOS ACTOS LEGISLATIVOS DICTADOS POR EL CONSEJO DE ESTADO DESDE EL 19 DE DICIEMBRE DE 1973 HASTA EL 14 DE FEBRERO DE 1985, EXCEPTO LAS DECLARACIONES DE NULIDAD Y LAS DEROGACIONES QUE SE DETERMINAN (Ley Nº 15.738 of 1985) | 1 | Current text only (IMPO's text, in force from 1 April 1985), to today |
| `ley-15746/` | MODIFICACION A LA LEY DE EMERGENCIA PARA LA ENSEÑANZA PUBLICA. ANEP (Ley Nº 15.746 of 1985) | 1 | Current text only (IMPO's text, in force from 30 June 1985), to today |
| `ley-15753/` | PLAN DE PROMOCION GRANJERA - INDEMNIZACION A LOS PRODUCTORES AFECTADOS POR FENOMENOS CLIMATICOS (Ley Nº 15.753 of 1985) | 1 | Current text only (IMPO's text, in force from 12 July 1985), to today |
| `ley-15756/` | PRORROGA DE VIGENCIA DEL DECRETO-LEY 15.514, LEY DE REGISTROS PUBLICOS (Ley Nº 15.756 of 1985) | 1 | Current text only (IMPO's text, in force from 27 July 1985), to today |
| `ley-15781/` | APROBACION DEL REGIMEN DE FACILIDADES DE PAGO PARA DEUDORES DE LA DIRECCION GENERAL DE LA SEGURIDAD SOCIAL Y LA DGI (Ley Nº 15.781 of 1985) | 1 | Current text only (IMPO's text, in force from 23 January 1988), to today |
| `ley-15786/` | APROBACION DE LA LEY DE REFINANCIACION DEL ENDEUDAMIENTO INTERNO (Ley Nº 15.786 of 1985) | 1 | Current text only (IMPO's text, in force from 20 January 1991), to today |
| `ley-15791/` | MODIFICACION DEL CODIGO DE COMERCIO RELATIVO AL CAPITAL MINIMO DE SOCIEDADES ANONIMAS (Ley Nº 15.791 of 1985) | 1 | Current text only (IMPO's text, in force from 5 January 1986), to today |
| `ley-15820/` | SALUD PUBLICA - INSTITUCIONES DE ASISTENCIA MEDICA COLECTIVA (Ley Nº 15.820 of 1986) | 1 | Current text only (IMPO's text, in force from 28 September 1986), to today |
| `ley-15845/` | BIENES INMUEBLES - REPRESA DE SALTO GRANDE (Ley Nº 15.845 of 1986) | 1 | Current text only (IMPO's text, in force from 1 January 2014), to today |
| `ley-15900/` | SEGURIDAD SOCIAL - PASIVIDADES (Ley Nº 15.900 of 1987) | 1 | Current text only (IMPO's text, in force from 5 November 1987), to today |
| `ley-15914/` | FUNCIONARIOS - ADQUISICION DE OBRAS LITERARIAS (Ley Nº 15.914 of 1987) | 1 | Current text only (IMPO's text, in force from 27 December 1987), to today |
| `ley-15925/` | MODIFICACION A LA LEY DE EMERGENCIA PARA LA ENSEÑANZA PUBLICA - ESTATUTO DEL FUNCIONARIO (Ley Nº 15.925 of 1987) | 1 | Current text only (IMPO's text, in force from 23 January 1988), to today |
| `ley-15927/` | MODIFICACION DEL TEXTO ORDENADO DGI, RELATIVO AL IVA (Ley Nº 15.927 of 1987) | 1 | Current text only (IMPO's text, in force from 1 January 1992), to today |
| `ley-16014/` | LEY DE REGISTROS PUBLICOS - VIGENCIA (Ley Nº 16.014 of 1988) | 1 | Current text only (IMPO's text, in force from 23 January 1989), to today |
| `ley-16018/` | EMPRESAS AGROPECUARIAS - CONTRIBUCION JUBILATORIA PATRONAL (Ley Nº 16.018 of 1989) | 1 | Current text only (IMPO's text, in force from 15 April 1989), to today |
| `ley-16083/` | ELECCIONES NACIONALES (Ley Nº 16.083 of 1989) | 1 | Current text only (IMPO's text, in force from 13 October 1994), to today |
| `ley-16087/` | TASA BROMATOLOGICA. CONTRIBUCION INMOBILIARIA. IMPUESTO A LOS REMATES. RECIBOS DE PAGO (Ley Nº 16.087 of 1989) | 1 | Current text only (IMPO's text, in force from 9 December 1989), to today |
| `ley-16090/` | PRECIOS - POSTALES CONMEMORATIVAS (Ley Nº 16.090 of 1989) | 1 | Current text only (IMPO's text, in force from 20 January 1991), to today |
| `ley-16144/` | MODIFICACION A LA LEY DE REGISTRO DE ESTADO CIVIL (Ley Nº 16.144 of 1990) | 1 | Current text only (IMPO's text, in force from 9 December 1990), to today |
| `ley-16201/` | DECLARACION DE INTERES NACIONAL. PROMOCION DE LAS MICRO PEQUEÑAS Y MADIANAS EMPRESAS (Ley Nº 16.201 of 1991) | 1 | Current text only (IMPO's text, in force from 18 January 2026), to today |
| `ley-16213/` | DEROGACION DEL ART. 17 DEL DECRETO-LET 14.181 (LEY DE MINERIA. LEY DE HIDROCARBUROS) (Ley Nº 16.213 of 1991) | 1 | Current text only (IMPO's text, in force from 16 December 1991), to today |
| `ley-16225/` | DEUDA PUBLICA (Ley Nº 16.225 of 1991) | 1 | Current text only (IMPO's text, in force from 15 January 1994), to today |
| `ley-16230/` | TOPES DE ACUMULACION DE PASIVIDADES (Ley Nº 16.230 of 1991) | 1 | Current text only (IMPO's text, in force from 16 December 1991), to today |
| `ley-16241/` | FIJACION DE FECHA PARA ELECCIONES DE REPRESENTANTES DEL DIRECTORIO DEL BPS (Ley Nº 16.241 of 1992) | 1 | Current text only (IMPO's text, in force from 24 July 2020), to today |
| `ley-16311/` | CREACION DEL FONDO DE PROTECCION INTEGRAL DE LOS VIÑEDOS (Ley Nº 16.311 of 1992) | 1 | Current text only (IMPO's text, in force from 12 February 2009), to today |
| `ley-16323/` | MODIFICACION DE LA LEY 8.733 SOBRE ENAJENACION DE INMUEBLES A PLAZOS. CADUCIDAD DE LAS INSCRIPCIONES (Ley Nº 16.323 of 1992) | 1 | Current text only (IMPO's text, in force from 3 February 2000), to today |
| `ley-16339/` | SANIDAD ANIMAL (Ley Nº 16.339 of 1992) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-16405/` | TRIBUTOS. JUEGOS DE AZAR (Ley Nº 16.405 of 1993) | 1 | Current text only (IMPO's text, in force from 5 September 1993), to today |
| `ley-16449/` | SEGURIDAD SOCIAL - PASIVIDADES (Ley Nº 16.449 of 1993) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-16460/` | FUNCIONARIOS PUBLICOS - SEGURIDAD SOCIAL (Ley Nº 16.460 of 1993) | 1 | Current text only (IMPO's text, in force from 20 January 1994), to today |
| `ley-16464/` | SEGURIDAD SOCIAL - PASIVIDADES (Ley Nº 16.464 of 1994) | 1 | Current text only (IMPO's text, in force from 29 January 1994), to today |
| `ley-16476/` | SALVAMENTO MARITIMO (Ley Nº 16.476 of 1994) | 1 | Current text only (IMPO's text, in force from 4 June 1994), to today |
| `ley-16491/` | PARTIDAS PRESUPUESTALES (Ley Nº 16.491 of 1994) | 1 | Current text only (IMPO's text, in force from 18 June 1994), to today |
| `ley-16575/` | PROPIEDAD HORIZONTAL (Ley Nº 16.575 of 1994) | 1 | Current text only (IMPO's text, in force from 9 October 1994), to today |
| `ley-16624/` | CREACION DEL FONDO NACIONAL DE MUSICA Y DE LA COMISION DEL FONDO NACIONAL DE MUSICA (Ley Nº 16.624 of 1994) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-16683/` | REGISTROS PUBLICOS (Ley Nº 16.683 of 1994) | 1 | Current text only (IMPO's text, in force from 12 January 1995), to today |
| `ley-16688/` | MEDIO AMBIENTE - ECOLOGIA (Ley Nº 16.688 of 1994) | 1 | Current text only (IMPO's text, in force from 17 December 2012), to today |
| `ley-16739/` | HIDROCARBUROS. IMPUESTO A LA CIRCULACION DE LOS VEHICULOS AUTOMOTORES TERRESTRES CUYO MOTOR UTILICE EL GASOIL COMO COMBUSTIBLE (Ley Nº 16.739 of 1996) | 1 | Current text only (IMPO's text, in force from 21 April 1996), to today |
| `ley-16753/` | DEROGACION DEL MONOPOLIO DE DE ALCOHOLES Y BEBIDAS ALCOHOLICAS ESTABLECIDO EN BENEFICIO DE ANCAP (Ley Nº 16.753 of 1996) | 1 | Current text only (IMPO's text, in force from 13 October 2022), to today |
| `ley-16766/` | REGISTROS PUBLICOS (Ley Nº 16.766 of 1996) | 1 | Current text only (IMPO's text, in force from 8 September 1996), to today |
| `ley-16814/` | CONTRATACION DE POLICIAS PARA LA CREACION DE UNA POLICIA CIUDADANA (Ley Nº 16.814 of 1997) | 1 | Current text only (IMPO's text, in force from 16 July 2000), to today |
| `ley-16824/` | SEGURIDAD SOCIAL (Ley Nº 16.824 of 1997) | 1 | Current text only (IMPO's text, in force from 19 May 1997), to today |
| `ley-16840/` | PRESUPUESTO NACIONAL DE SUELDOS GASTOS E INVERSIONES - CONTRATACIONES DEL ESTADO (Ley Nº 16.840 of 1997) | 1 | Current text only (IMPO's text, in force from 21 July 1997), to today |
| `ley-16844/` | LEY DE REGISTROS PUBLICOS. VIGENCIA (Ley Nº 16.844 of 1997) | 1 | Current text only (IMPO's text, in force from 27 July 1997), to today |
| `ley-16866/` | SEGURIDAD SOCIAL - CONTRIBUYENTES MOROSOS (Ley Nº 16.866 of 1997) | 1 | Current text only (IMPO's text, in force from 5 October 1997), to today |
| `ley-16868/` | LEY DE REGISTROS PUBLICOS.VIGENCIA (Ley Nº 16.868 of 1997) | 1 | Current text only (IMPO's text, in force from 12 October 1997), to today |
| `ley-16904/` | MODIFICACION A LA LEY DE AJUSTE FISCAL - NUEVO REGIMEN FISCAL Y DE MEJORA DE LA COMPETITIVIDAD DEL SECTOR (Ley Nº 16.904 of 1997) | 1 | Current text only (IMPO's text, in force from 30 January 1998), to today |
| `ley-16970/` | SEGURIDAD SOCIAL - PASIVIDADES (Ley Nº 16.970 of 1998) | 1 | Current text only (IMPO's text, in force from 4 July 1998), to today |
| `ley-16994/` | CODIGO GENERAL DEL PROCESO - VIGENCIA (Ley Nº 16.994 of 1998) | 1 | Current text only (IMPO's text, in force from 14 September 1998), to today |
| `ley-17006/` | BIENES DEL ESTADO - MONUMENTO HISTORICO NACIONAL. MONTEVIDEO (Ley Nº 17.006 of 1998) | 1 | Current text only (IMPO's text, in force from 1 January 2014), to today |
| `ley-17045/` | REGULACION DE LA PUBLICIDAD ELECTORAL (Ley Nº 17.045 of 1998) | 1 | Current text only (IMPO's text, in force from 8 July 2024), to today |
| `ley-17071/` | ENTES AUTONOMOS - SERVICIOS DESCENTRALIZADOS (Ley Nº 17.071 of 1998) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-17115/` | LEY DE DESARROLLO APICOLA (Ley Nº 17.115 of 1999) | 1 | Current text only (IMPO's text, in force from 15 January 2011), to today |
| `ley-17124/` | SOCIEDADES COMERCIALES (Ley Nº 17.124 of 1999) | 1 | Current text only (IMPO's text, in force from 16 July 1999), to today |
| `ley-17142/` | INTERPRETACIONES AL CODIGO DE AGUAS (Ley Nº 17.142 of 1999) | 1 | Current text only (IMPO's text, in force from 28 August 1999), to today |
| `ley-17143/` | SEGURIDAD SOCIAL (Ley Nº 17.143 of 1999) | 1 | Current text only (IMPO's text, in force from 28 August 1999), to today |
| `ley-17295/` | REGULACION DE LA PRODUCCION ELABORACION Y COMERCIALIZACION DE LA SIDRA (Ley Nº 17.295 of 2001) | 1 | Current text only (IMPO's text, in force from 8 April 2001), to today |
| `ley-17412/` | CONTRIBUCIONES ESPECIALES A LA SEGURIDAD SOCIAL. IMPUESTO A LA COMPRA DE MONEDA EXTRANJERA (Ley Nº 17.412 of 2001) | 1 | Current text only (IMPO's text, in force from 18 November 2001), to today |
| `ley-17508/` | CONTRIBUCION INMOBILIARIA RURAL (Ley Nº 17.508 of 2002) | 1 | Current text only (IMPO's text, in force from 12 July 2002), to today |
| `ley-17581/` | INVERSIONES PUBLICAS (Ley Nº 17.581 of 2002) | 1 | Current text only (IMPO's text, in force from 1 January 2013), to today |
| `ley-17595/` | IMPUESTO ESPECIFICO A LOS SERVICIOS DE SALUD (IMESSA) (Ley Nº 17.595 of 2002) | 1 | Current text only (IMPO's text, in force from 28 December 2002), to today |
| `ley-17620/` | INTERPRETACION DEL ART.1 DE LA LEY 16.824. FACULTAD DE LOS FUNCIONARIOS DOCENTES REINCORPORADOS DEPENDIENTES DE LA ANEP DE EJERCER LOS DERECHOS ANTE EL BPS (Ley Nº 17.620 of 2003) | 1 | Current text only (IMPO's text, in force from 8 March 2003), to today |
| `ley-17651/` | REGULACION DEL IVA A LOS SERVICIOS DE TRANSPORTE TERRESTRE DE PASAJEROS (Ley Nº 17.651 of 2003) | 1 | Current text only (IMPO's text, in force from 1 July 2007), to today |
| `ley-17672/` | REGULACION DE LOS RETIROS INCENTIVADOS DE LOS FUNCIONARIOS PUBLICOS (Ley Nº 17.672 of 2003) | 1 | Current text only (IMPO's text, in force from 2 August 2003), to today |
| `ley-17693/` | PRESTACION DIRECTA DE LOS SERVICIOS MEDICOS Y ODONTOLOGICOS POR ORGANISMOS DEL ESTADO A SUS FUNCIONARIOS. DEROGACION ART. 22 DE LA LEY 17.556 (Ley Nº 17.693 of 2003) | 1 | Current text only (IMPO's text, in force from 23 October 2003), to today |
| `ley-17729/` | REGULACION DE LAS EMPRESAS FABRICANTES DE BEBIDAS SIN ALCOHOL GRAVADAS CON IMESI (Ley Nº 17.729 of 2003) | 1 | Current text only (IMPO's text, in force from 15 January 2011), to today |
| `ley-17775/` | DECLARACION DE INTERES GENERAL. REGULACION DE LA CONTAMINACION POR PLOMO (Ley Nº 17.775 of 2004) | 1 | Current text only (IMPO's text, in force from 1 January 2008), to today |
| `ley-17802/` | EXONERACION DE IMPUESTOS A PELICULAS CINEMATOGRAFICAS (Ley Nº 17.802 of 2004) | 1 | Current text only (IMPO's text, in force from 10 September 2004), to today |
| `ley-17820/` | AUTORIZACION DE PASES Y REDISTRIBUCION DE FUNCIONARIOS PUBLICOS PARA LA URSEC. CREACION DE LA TASA DE CONTROL DEL MARCO REGULATORIO DE COMUNICACIONES (Ley Nº 17.820 of 2004) | 1 | Current text only (IMPO's text, in force from 1 January 2007), to today |
| `ley-17836/` | FUNCIONARIOS POLICIALES (Ley Nº 17.836 of 2004) | 1 | Current text only (IMPO's text, in force from 9 October 2004), to today |
| `ley-17847/` | REGULACION DE LAS PENSIONES POR INVALIDEZ (Ley Nº 17.847 of 2004) | 1 | Current text only (IMPO's text, in force from 1 August 2023), to today |
| `ley-17869/` | REGULACION DEL PLAN NACIONAL DE EMERGENCIA SOCIAL (Ley Nº 17.869 of 2005) | 1 | Current text only (IMPO's text, in force from 1 January 2007), to today |
| `ley-17887/` | PROHIBICION DE LA IMPORTACION DE VEHICULOS USADOS (Ley Nº 17.887 of 2005) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-17934/` | AUTORIZACION AL PODER EJECUTIVO REDUCIR LA TASA DEL IVA EN ACTIVIDADES VINCULADAS AL TURISMO QUE SE DETERMINAN (Ley Nº 17.934 of 2005) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-17948/` | INTERMEDIACION FINANCIERA (Ley Nº 17.948 of 2006) | 1 | Current text only (IMPO's text, in force from 18 January 2026), to today |
| `ley-17974/` | DEROGACION DEL DESCUENTO DE TESORERIA. CAJA DE JUBILACIONES Y PENSIONES DE LA INDUSTRIA Y COMERCIO (Ley Nº 17.974 of 2006) | 1 | Current text only (IMPO's text, in force from 8 July 2006), to today |
| `ley-17997/` | DECLARACION DE INTERES NACIONAL. SISTEMA DE IDENTIFICACION Y REGISTRO ANIMAL (Ley Nº 17.997 of 2006) | 1 | Current text only (IMPO's text, in force from 15 January 2011), to today |
| `ley-18062/` | CODIGO DE ORGANIZACION DE LOS TRIBUNALES MILITARES. MODIFICACION (Ley Nº 18.062 of 2006) | 1 | Current text only (IMPO's text, in force from 15 December 2006), to today |
| `ley-18064/` | CREACION DEL IMPUESTO ADICIONAL AL IMPUESTO A LAS TRASMISIONES PATRIMONIALES (ITP) SOBRE LOS INMUEBLES RURALES (Ley Nº 18.064 of 2006) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-18079/` | LEY DE REESTRUCTURA Y FORTALECIMIENTO DEL SISTEMA FINANCIERO. SEGURIDAD SOCIAL. IMPUESTO A LOS SUELDOS Y PASIVIDADES BANCARIAS. CAJA DE JUBILACIONES Y PENSIONES BANCARIAS (Ley Nº 18.079 of 2006) | 1 | Current text only (IMPO's text, in force from 8 January 2007), to today |
| `ley-18092/` | SOCIEDADES ANONIMAS. TITULARIDAD DE INMUEBLES RURALES Y EXPLOTACIONES AGROPECUARIAS (Ley Nº 18.092 of 2007) | 1 | Current text only (IMPO's text, in force from 12 February 2009), to today |
| `ley-18096/` | LIMITACION DEL ALCANCE DE EXONERACIONES GENERICAS DE TRIBUTOS (Ley Nº 18.096 of 2007) | 1 | Current text only (IMPO's text, in force from 26 January 2007), to today |
| `ley-18221/` | MODIFICACION DEL MONTO IMPONIBLE DEL IMESI. IMPORTACIONES. COMBUSTIBLES (Ley Nº 18.221 of 2007) | 1 | Current text only (IMPO's text, in force from 22 January 2016), to today |
| `ley-18243/` | LEY ORGANICA DEL BANCO DE SEGUROS DEL ESTADO (Ley Nº 18.243 of 2007) | 1 | Current text only (IMPO's text, in force from 19 January 2008), to today |
| `ley-18340/` | MODIFICANSE DISPOSICIONES REFERIDAS A LA ADMINISTRACION DE VIVIENDAS PARA JUBILADOS Y PENSIONISTAS DEL BPS (Ley Nº 18.340 of 2008) | 1 | Current text only (IMPO's text, in force from 13 September 2008), to today |
| `ley-18439/` | CREACION DEL FONDO DE GARANTIA PARA LA REESTRUCTURACION DE PASIVOS DE LAS INSTITUCIONES DE ASISTENCIA MEDICA COLECTIVA. FONDO DE GARANTIA IAMC (Ley Nº 18.439 of 2008) | 1 | Current text only (IMPO's text, in force from 11 October 2026), to today |
| `ley-18461/` | SOCIEDADES ANONIMAS. TITULARIDAD DE INMUEBLES RURALES (Ley Nº 18.461 of 2009) | 1 | Current text only (IMPO's text, in force from 22 January 2010), to today |
| `ley-18501/` | CREACION DEL ARCHIVO AUDIOVISUAL DEPENDIENTE DEL SODRE (Ley Nº 18.501 of 2009) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-18532/` | PROHIBICION IMPORTACION DE VEHICULOS USADOS. PRORROGA (Ley Nº 18.532 of 2009) | 1 | Current text only (IMPO's text, in force from 5 September 2009), to today |
| `ley-18565/` | CREACION DEL FONDO DE INVERSION DEPARTAMENTAL (Ley Nº 18.565 of 2009) | 1 | Current text only (IMPO's text, in force from 17 October 2009), to today |
| `ley-18592/` | LEY INTERPRETATIVA DEL ARTICULO 6 DE LA LEY Nº 18.439. ESCISION DE LOS SERVICIOS ASISTENCIALES DEL SINDICATO MEDICO DEL URUGUAY (Ley Nº 18.592 of 2009) | 1 | Current text only (IMPO's text, in force from 24 October 2009), to today |
| `ley-18623/` | LEY DE ABREVIACION DE PROCESOS LABORALES. PRORROGA VIGENCIA (Ley Nº 18.623 of 2009) | 1 | Current text only (IMPO's text, in force from 30 November 2009), to today |
| `ley-18677/` | DECLARACION DEL 2011 COMO AÑO DE LA "CELEBRACION DEL BICENTENARIO DEL PROCESO DE EMANCIPACION ORIENTAL. COMISION DEL BICENTENARIO DE LA REVOLUCION DE INDEPENDENCIA DEL RIO DE LA PLATA 2010 - 2015 (Ley Nº 18.677 of 2010) | 1 | Current text only (IMPO's text, in force from 1 January 2014), to today |
| `ley-18771/` | CREACION DEL SISTEMA DE RESPONSABILIDAD PENAL ADOLESCENTE (SIRPA) (Ley Nº 18.771 of 2011) | 1 | Current text only (IMPO's text, in force from 14 October 2012), to today |
| `ley-18791/` | VENTA EN SUBASTA PUBLICA DE DETERMINADOS VEHICULOS AUTOMOTORES Y DEROGACION DEL DECRETO LEY 15.086 (Ley Nº 18.791 of 2011) | 1 | Current text only (IMPO's text, in force from 5 October 2019), to today |
| `ley-18794/` | INCLUSION EN EL SERVICIO 222 A LA POLICIA AEREA NACIONAL (Ley Nº 18.794 of 2011) | 1 | Current text only (IMPO's text, in force from 5 September 2011), to today |
| `ley-18802/` | PRORROGA POR EL TERMINO DE DOCE MESES LA PROHIBICION ESTABLECIDA POR EL ART. 1º DE LA LEY 17.887 RELATIVA A LA IMPORTACION DE VEHICULOS USADOS (Ley Nº 18.802 of 2011) | 1 | Current text only (IMPO's text, in force from 29 September 2011), to today |
| `ley-18812/` | REGULACION PARA GARANTIZAR EL DERECHO DE PROTECCION DE DATOS PERSONALES (Ley Nº 18.812 of 2011) | 1 | Current text only (IMPO's text, in force from 1 January 2013), to today |
| `ley-18832/` | CREACION DE LA UNIDAD AGROALIMENTARIA METROPOLITANA AHORA DENOMINADA UNIDAD ALIMENTARIA DE MONTEVIDEO (Ley Nº 18.832 of 2011) | 1 | Current text only (IMPO's text, in force from 7 September 2024), to today |
| `ley-18833/` | DECLARACION DE INTERES NACIONAL. FOMENTO DEL DEPORTE NACIONAL. BENEFICIOS FISCALES (Ley Nº 18.833 of 2011) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-18849/` | CREACION DEL REGISTRO NACIONAL DE HUELLAS GENETICAS. DIRECCION NACIONAL DE POLICIA TECNICA (Ley Nº 18.849 of 2011) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-18861/` | APROBACION DEL CONVENIO CONSTITUTIVO DEL BANCO DEL SUR (Ley Nº 18.861 of 2011) | 1 | Current text only (IMPO's text, in force from 1 January 2013), to today |
| `ley-18964/` | PRORROGA DE PLAZO PARA LA PROHIBICION DE IMPORTAR BIENES MUEBLES USADOS (Ley Nº 18.964 of 2012) | 1 | Current text only (IMPO's text, in force from 15 September 2012), to today |
| `ley-18969/` | TRANSFERENCIA A LA FUNDACION DEPORTE URUGUAY EL CONTRALOR SOBRE EL DOPAJE EN LAS COMPETENCIAS DEPORTIVAS (Ley Nº 18.969 of 2012) | 1 | Current text only (IMPO's text, in force from 13 December 2012), to today |
| `ley-18970/` | MODIFICACION DEL SISTEMA DE RESPONSABILIDAD PENAL ADOLESCENTE (SIRPA) (Ley Nº 18.970 of 2012) | 1 | Current text only (IMPO's text, in force from 13 October 2017), to today |
| `ley-18975/` | EXTENSION DE PLAZO Y EXONERACIONES FISCALES RELATIVO A LAS COOPERATIVAS DE PROFESIONALES DE LA SALUD (Ley Nº 18.975 of 2012) | 1 | Current text only (IMPO's text, in force from 21 October 2012), to today |
| `ley-18978/` | APLICACION DEL TOPE MAXIMO JUBILATORIO DE PASIVIDADES A LOS MAGISTRADOS DEL TCA (Ley Nº 18.978 of 2012) | 1 | Current text only (IMPO's text, in force from 2 November 2012), to today |
| `ley-18992/` | FIJACION DE NORMAS PARA LA LIQUIDACION DE CONTRIBUCIONES QUE DEBEN EFECTUAR LOS BENEFICIARIOS DE LA DIRECCION NACIONAL DE SANIDAD DE LAS FUERZAS ARMADAS (Ley Nº 18.992 of 2012) | 1 | Current text only (IMPO's text, in force from 1 December 2012), to today |
| `ley-18994/` | DEROGACION DE NORMAS RELATIVAS A LA TRANSFERENCIA DE LA DIRECCION NACIONAL DE METEOROLOGIA AL MVOTMA (Ley Nº 18.994 of 2012) | 1 | Current text only (IMPO's text, in force from 19 November 2012), to today |
| `ley-19056/` | FIJACION DE NORMAS TENDIENTES A ASEGURAR LA PROTECCION Y LA SEGURIDAD RADIOLOGICA DE PERSONAS, BIENES Y MEDIO AMBIENTE (Ley Nº 19.056 of 2013) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-19059/` | EXTENSION DE PLAZO Y EXONERACIONES FISCALES RELATIVO A LAS COOPERATIVAS DE PROFESIONALES DE LA SALUD (Ley Nº 19.059 of 2013) | 1 | Current text only (IMPO's text, in force from 27 May 2013), to today |
| `ley-19111/` | REGULACION DEL REGIMEN SANCIONATORIO EN LO RELATIVO A LA CERTIFICACION DE ORIGEN (Ley Nº 19.111 of 2013) | 1 | Current text only (IMPO's text, in force from 18 January 2026), to today |
| `ley-19135/` | DEROGACION DE DETERMINADAS LEYES QUE DISPONEN SORTEOS ESPECIALES CON DESTINO A LOS HOSPITALES MACIEL, PASTEUR Y PEREIRA ROSSELL (Ley Nº 19.135 of 2013) | 1 | Current text only (IMPO's text, in force from 23 October 2017), to today |
| `ley-19146/` | DEROGACION DEL INC. SEGUNDO, LITERAL B) DEL ART. 219 DEL DECRETO-LEY 14.157 (LEY ORGANICA MILITAR) (Ley Nº 19.146 of 2013) | 1 | Current text only (IMPO's text, in force from 23 December 2013), to today |
| `ley-19159/` | CREACION DE LOS TALLERES DE PRODUCCION PROTEGIDA (Ley Nº 19.159 of 2013) | 1 | Current text only (IMPO's text, in force from 25 November 2013), to today |
| `ley-19171/` | PRORROGA DE PLAZO PARA LA PROHIBICION DE IMPORTAR VEHICULOS USADOS (Ley Nº 19.171 of 2013) | 1 | Current text only (IMPO's text, in force from 5 January 2014), to today |
| `ley-19231/` | CREACION DEL FONDO NACIONAL DE COLONIZACION. MODIFICACION DEL ART. 7 DE LA LEY 18.064 RELATIVO A LA TRANSFERENCIA DE RECURSOS I.N.C (Ley Nº 19.231 of 2014) | 1 | Current text only (IMPO's text, in force from 1 August 2014), to today |
| `ley-19252/` | REGULACION DE LOS PREMIOS QUE SE OTORGAN A LA LABOR LITERARIA E INTELECTUAL EN NUESTRO PAIS (Ley Nº 19.252 of 2014) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-19264/` | CONTROL DEL CUMPLIMIENTO DE LAS ESPECIFICACIONES TECNICAS PARA LOS BIENES Y SERVICIOS DESTINADOS AL USO Y CONSUMO (Ley Nº 19.264 of 2014) | 1 | Current text only (IMPO's text, in force from 18 January 2026), to today |
| `ley-19275/` | APROBACION DE RENDICION DE CUENTAS Y BALANCE DE EJECUCION PRESUPUESTAL. EJERCICIO 2013 (Ley Nº 19.275 of 2014) | 1 | Current text only (IMPO's text, in force from 5 October 2014), to today |
| `ley-19285/` | PRORROGA DE PLAZO ESTABLECIDO EN EL ART. 277 DE LA LEY 16.170 PARA LA INTEGRACION DE CAPITAL ENTRE EL MGAP Y LOS TENEDORES DE SILOS, PLANTAS DE ALMACENAJE Y DEPOSITOS ADMINISTRADOS POR LA COMISION TECNICA DEL PLAN NACIONAL DE SILOS (Ley Nº 19.285 of 2014) | 1 | Current text only (IMPO's text, in force from 1 November 2014), to today |
| `ley-19291/` | CREACION DE UN REGIMEN DE APORTACION PREVISIONAL PARA PEQUEÑAS OBRAS DE CONSTRUCCION (Ley Nº 19.291 of 2014) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-19292/` | DECLARACION DE INTERES GENERAL. PRODUCCION FAMILIAR AGROPECUARIA Y PESCA ARTESANAL (Ley Nº 19.292 of 2014) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-19301/` | REGIMEN DE RESIDENCIAS MEDICAS HOSPITALARIAS. DEROGACION DE LAS LEYES 18.438 Y 18.459 (Ley Nº 19.301 of 2014) | 1 | Current text only (IMPO's text, in force from 1 January 2018), to today |
| `ley-19333/` | RESTABLECIMIENTO DEL IMPUESTO ANUAL DE ENSEÑANZA PRIMARIA A LOS INMUEBLES RURALES (Ley Nº 19.333 of 2015) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-19368/` | AUTORIZACION AL PODER EJECUTIVO A CAPITALIZAR LA ADMINISTRACION NACIONAL DE COMBUSTIBLES, ALCOHOL Y PORTLAND (Ley Nº 19.368 of 2016) | 1 | Current text only (IMPO's text, in force from 22 January 2016), to today |
| `ley-19572/` | SUPRESION DEL ENTE AUTONOMO PRIMERAS LINEAS URUGUAYAS DE NAVEGACION AEREA (PLUNA) (Ley Nº 19.572 of 2017) | 1 | Current text only (IMPO's text, in force from 8 January 2018), to today |
| `ley-19578/` | PRORROGA DE VIGENCIA DEL ART. 116 DE LA LEY 19.535 RELATIVO AL MANTENIMIENTO DE UNA DOTACION DE PERSONAL GARANTIZANDOLES UN MINIMO DE JORNALES Y REGULACION DEL PERSONAL EVENTUAL (Ley Nº 19.578 of 2017) | 1 | Current text only (IMPO's text, in force from 19 January 2018), to today |
| `ley-19602/` | DEVOLUCION DE IVA EN LA ADQUISICION DE GASOIL A LOS PRODUCTORES RURALES (Ley Nº 19.602 of 2018) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-19620/` | AUTORIZACION AL PODER EJECUTIVO A TRANSFERIR EL MONTO EXCEDENTE DEL FONDO DE ESTABILIZACION ENERGETICA A RENTAS GENERALES (Ley Nº 19.620 of 2018) | 1 | Current text only (IMPO's text, in force from 24 July 2020), to today |
| `ley-19634/` | PRORROGA DE ENTRADA EN VIGENCIA DEL ART. 116 DE LA LEY 19.535 RELATIVO AL MANTENIMIENTO DE UNA DOTACION DE PERSONAL GARANTIZANDOLES UN MINIMO DE JORNALES Y REGULACION DEL PERSONAL EVENTUAL (Ley Nº 19.634 of 2018) | 1 | Current text only (IMPO's text, in force from 19 July 2018), to today |
| `ley-19666/` | APROBACION DE NORMAS PARA LA DESIGNACION Y FUNCIONAMIENTO DE LOS CENTROS O SERVICIOS DE REFERENCIA EN SALUD QUE GARANTICEN LA EQUIDAD EN EL ACCESO A LA ATENCION DE CALIDAD DE PATOLOGIAS COMPLEJAS (Ley Nº 19.666 of 2018) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-19695/` | APROBACION DE LAS MODIFICACIONES AL SISTEMA DE PREVISION SOCIAL MILITAR (Ley Nº 19.695 of 2018) | 1 | Current text only (IMPO's text, in force from 1 August 2023), to today |
| `ley-19728/` | DECLARACION DE INTERES NACIONAL EL TRATAMIENTO DE LA FIBROMIALGIA (Ley Nº 19.728 of 2018) | 1 | Current text only (IMPO's text, in force from 1 August 2023), to today |
| `ley-19734/` | DECLARACION DE PRORROGA DEL PLAZO ESTABLECIDO EN EL ART. 6 DE LA LEY 19.247, RELATIVO A LA TENENCIA DE ARMAS (Ley Nº 19.734 of 2019) | 1 | Current text only (IMPO's text, in force from 28 January 2019), to today |
| `ley-19735/` | PRORROGA DE LA ENTRADA EN VIGENCIA DEL ART. 116 DE LA LEY 19.535, RELATIVA A TRABAJADORES DE LAS EMPRESAS PRESTADORAS DE SERVICIOS DE DEPOSITOS PORTUARIOS, EXTRAPORTUARIOS, MUELLES, Y EXPLANADAS (Ley Nº 19.735 of 2019) | 1 | Current text only (IMPO's text, in force from 7 February 2019), to today |
| `ley-19739/` | OTORGAMIENTO DE CREDITO FISCAL A EMPRESAS PRIVADAS PARA ACTIVIDADES DE INVESTIGACION Y DESARROLLO (Ley Nº 19.739 of 2019) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-19772/` | REGULACION DEL ORDENAMIENTO TERRITORIAL Y DESARROLLO SOSTENIBLE DEL ESPACIO COSTERO DEL OCEANO ATLANTICO Y DEL RIO DE LA PLATA (Ley Nº 19.772 of 2019) | 1 | Current text only (IMPO's text, in force from 17 January 2020), to today |
| `ley-19783/` | APROBACION DE NORMATIVA PARA LA PROMOCION DE INOCUIDAD Y TRANSPARENCIA EN LA COMERCIALIZACION DE CARNES (Ley Nº 19.783 of 2019) | 1 | Current text only (IMPO's text, in force from 24 July 2020), to today |
| `ley-19787/` | CREACION DE NUEVO REGIMEN QUE ASEGURA UN MINIMO DE JORNALES PARA EL PERSONAL DEPENDIENTE EN DEPOSITOS PORTUARIOS Y EXTRAPORTUARIOS EN EMPRESAS PRESTADORAS DE DICHOS SERVICIOS. DEROGACION DEL ART. 116 DE LA LEY 19.535 (Ley Nº 19.787 of 2019) | 1 | Current text only (IMPO's text, in force from 27 September 2019), to today |
| `ley-19826/` | MODIFICACION DEL REGIMEN PREVISIONAL DE LA CAJA NOTARIAL DE SEGURIDAD SOCIAL (Ley Nº 19.826 of 2019) | 1 | Current text only (IMPO's text, in force from 1 July 2020), to today |
| `ley-19848/` | DECLARACION DE INTERES NACIONAL LA PROMOCION, DIFUSION, ESTIMULO Y DESARROLLO DE LA ECONOMIA SOCIAL Y SOLIDARIA, EN CUALQUIERA DE SUS EXPRESIONES (Ley Nº 19.848 of 2019) | 1 | Current text only (IMPO's text, in force from 1 January 2021), to today |
| `ley-19852/` | CREACION DEL INSTITUTO NACIONAL DE ACREDITACION Y EVALUACION DE LA EDUCACION TERCIARIA (INAEET) (Ley Nº 19.852 of 2019) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-19854/` | APLICACION DE NORMATIVA EN LA RESERVA DE IDENTIDAD DE TESTIGOS Y DENUNCIANTES DURANTE LAS INSPECCIONES REALIZADAS POR LA INSPECCION GENERAL DEL TRABAJO Y DE LA SEGURIDAD SOCIAL (Ley Nº 19.854 of 2019) | 1 | Current text only (IMPO's text, in force from 18 January 2026), to today |
| `ley-19857/` | MODIFICACION A LA LEY DE DERECHOS DE AUTOR, EXTENDIENDO EL PLAZO PREVISTO A SETENTA AÑOS. LEY DE PROTECCION A LA PROPIEDAD INTELECTUAL (Ley Nº 19.857 of 2019) | 1 | Current text only (IMPO's text, in force from 17 January 2020), to today |
| `ley-19915/` | PRORROGA DE PLAZO ESTABLECIDO EN EL ART. 6º DE LA LEY 19.247, RELATIVA A LA TIPIFICACION DE DELITOS Y MODIFICACION DEL CODIGO PENAL (Ley Nº 19.915 of 2020) | 1 | Current text only (IMPO's text, in force from 4 December 2020), to today |
| `ley-19946/` | PRORROGA DE VIGENCIA DEL ART. 30 DE LA LEY 19.924, REFERENTE A LA APLICACION DEL SUBSIDIO POR ENFERMEDAD (Ley Nº 19.946 of 2021) | 1 | Current text only (IMPO's text, in force from 30 April 2021), to today |
| `ley-19956/` | EXONERACION DE LOS APORTES JUBILATORIOS PATRONALES A LA SEGURIDAD SOCIAL A DETERMINADAS EMPRESAS. 1º DE ENERO DE 2021 - 30 DE JUNIO DE 2021 (Ley Nº 19.956 of 2021) | 1 | Current text only (IMPO's text, in force from 2 July 2021), to today |
| `ley-19968/` | PRORROGA DEL PLAZO ESTABLECIDO EN EL ART. 374 DE LA LEY 19.889 (LEY DE URGENTE CONSIDERACION. LUC. LEY DE URGENCIA). 31 DE DICIEMBRE DE 2021 (Ley Nº 19.968 of 2021) | 1 | Current text only (IMPO's text, in force from 13 August 2021), to today |
| `ley-19989/` | EXTENSION DE LOS BENEFICIOS TRIBUTARIOS PARA EMPRESAS AFECTADAS POR LA PANDEMIA CAUSADA POR EL COVID-19 (Ley Nº 19.989 of 2021) | 1 | Current text only (IMPO's text, in force from 11 October 2021), to today |
| `ley-20046/` | PRORROGA DEL PLAZO ESTABLECIDO EN EL ART. 6º DE LA LEY 19.247, SOBRE TENENCIA DE ARMAS (Ley Nº 20.046 of 2022) | 1 | Current text only (IMPO's text, in force from 4 July 2022), to today |
| `ley-20052/` | CREACION DE LA PERSONA JURIDICA DE DERECHO PUBLICO NO ESTATAL CENTRAL HORTICOLA DEL NORTE (CHN) (Ley Nº 20.052 of 2022) | 1 | Current text only (IMPO's text, in force from 1 January 2023), to today |
| `ley-20061/` | PRORROGA DEL PLAZO ESTABLECIDO EN EL INCISO SEGUNDO DEL ART. 467 DE LA LEY 19.889, QUE APROBO LA LEY DE URGENTE CONSIDERACION. LUC. LEY DE URGENCIA (Ley Nº 20.061 of 2022) | 1 | Current text only (IMPO's text, in force from 8 August 2022), to today |
| `ley-20079/` | MODIFICACION DEL INC. SEGUNDO DEL ART. 1º DE LA LEY 19.695, RELATIVA AL SISTEMA DE PREVISION SOCIAL MILITAR (Ley Nº 20.079 of 2022) | 1 | Current text only (IMPO's text, in force from 24 November 2022), to today |
| `ley-20112/` | CREACION DEL FONDO DE RECONVERSION DE INDUSTRIAS LACTEAS Y DEROGACION DEL ART. 5º DE LA LEY Nº 19.971 (Ley Nº 20.112 of 2023) | 1 | Current text only (IMPO's text, in force from 16 June 2023), to today |
| `ley-20129/` | REGULACION DEL DERECHO DE TODAS LAS TRABAJADORAS Y TRABAJADORES A AUSENTARSE DEL TRABAJO PARA REALIZACION DE CONTROLES DE EMBARAZO (Ley Nº 20.129 of 2023) | 1 | Current text only (IMPO's text, in force from 1 January 2024), to today |
| `ley-20209/` | CREACION DEL "FIDEICOMISO II DE LA SEGURIDAD SOCIAL" (Ley Nº 20.209 of 2023) | 1 | Current text only (IMPO's text, in force from 18 November 2023), to today |
| `ley-20273/` | APROBACION PARA LA ASISTENCIA POR PARTE DEL FONDO DE FINANCIAMIENTO Y DESARROLLO SUSTENTABLE DE LA ACTIVIDAD LECHERA (FFDSAL) A LOS PRODUCTORES REMITENTES DE LECHE A INDUSTRIAS (Ley Nº 20.273 of 2024) | 1 | Current text only (IMPO's text, in force from 12 October 2024), to today |
| `ley-20325/` | HABILITACION AL CASMU-IAMPP ACCESO POR UNICA VEZ AL FONDO DE GARANTIA PARA LA REESTRUCTURACION DE PASIVOS DE LAS INSTITUCIONES DE ASISTENCIA MEDICA COLECTIVA (Ley Nº 20.325 of 2024) | 1 | Current text only (IMPO's text, in force from 4 May 2025), to today |
| `ley-20371/` | PRORROGA DEL PLAZO PREVISTO EN EL ART. 499 DE LA LEY 20.075, RELATIVO AL OTORGAMIENTO DE CREDITO FISCAL PARA LAS INSTITUCIONES DE ASISTENCIA MEDICA COLECTIVA (Ley Nº 20.371 of 2024) | 1 | Current text only (IMPO's text, in force from 12 October 2024), to today |
| `ley-20379/` | INTERPRETACION DEL ART. 649 DE LA LEY 20.212, RELATIVO A LOS TRABAJADORES CONTRATADOS (Ley Nº 20.379 of 2024) | 1 | Current text only (IMPO's text, in force from 17 October 2024), to today |
| `ley-20383/` | REGULACION DE LA ACTIVIDAD DE LOS SERVICIOS DE DIFUSION DE CONTENIDO AUDIOVISUAL POR RADIOFUSION O SUSCRIPCION (Ley Nº 20.383 of 2024) | 1 | Current text only (IMPO's text, in force from 18 January 2026), to today |
| `ley-20416/` | APROBACION DE LA RENDICION DE CUENTAS Y BALANCE DE EJECUCIÓN PRESUPUESTAL. EJERCICIO 2024 (Ley Nº 20.416 of 2025) | 1 | Current text only (IMPO's text, in force from 21 August 2025), to today |
| `ley-20528/` | FIJACION DEL ACCESO AL FONDO DE GARANTIA PARA LA REESTRUCTURACION DE PASIVOS DE LAS INSTITUCIONES DE ASISTENCIA MEDICA COLECTIVA, AL CASMU - IAMPP (Ley Nº 20.528 of 2026) | 1 | Current text only (IMPO's text, in force from 11 October 2026), to today |
| `ley-17819/` | SEGURIDAD SOCIAL. SERVICIOS LEGALMENTE COMPUTABLES (Ley Nº 17.819 of 2004) | 1 | Current text only (IMPO's text, in force from 1 December 2023), to today |

**Current text only.** The acts whose History reads "Current text only" have one version: IMPO's consolidated text as published today, the oldest version available here, credited to IMPO and not to a law. Where the History says "in force from", the version is dated by its in-force day: that of the last law IMPO's notes name as changing the text, or the law's own when the notes name none, each found as for the other acts (a law's own vigencia article, else ten days after its publication). Where it says "last changed", the version is dated by the latest date IMPO's notes give for a change (for a law, the date IMPO prints for it) or by the law's promulgation; those dates are to be corrected to in-force days. Articles IMPO marks repealed whole, bare "(*)" articles of amendments and articles IMPO prints without text are not included. A law IMPO marks repealed whole ends with a commit, credited to the repealing law, that removes every article. Their titles are IMPO's own names of the laws, as IMPO prints them. Earlier versions of these acts may be added later.

The articles are `<act>/art-NNN.md` (`art-009-bis.md` for Artículo 9 BIS; four digits in the Código Civil, `art-1782.md`); the Constitution's Disposiciones Transitorias y Especiales are `constitucion/disp-trans-<letter>.md` (`-prima` for V'), Z'), `-segunda` for Z")). The per-act `README.md` lists every provision, how often it changed and when.

**How a law's history is rebuilt.** IMPO publishes only today's text of a law, but under each amended article it names the amending law and article ("Inciso 2º) redacción dada por: Ley Nº 18.719 de 27/12/2010 artículo 152", "Literal Ñ) agregado/s por: …") and links the article as originally published ("TEXTO ORIGINAL"). So the first version of each amended article is IMPO's original text, and every later version is today's text. Where one article was amended by two laws on different days, the text in between is taken only from a source: the wording the earlier amending law quotes (IMPO's original of that law), applied word for word to the text it amended (the items it replaces or adds, or an expression it substitutes, and nothing else), or today's text without an item that IMPO says the later law added (or that the later law's own article adds in the same words, where IMPO only points to that article). Every step and how it was rebuilt is listed in [`data/verification.json`](data/verification.json). Each amending law takes effect on the day its own vigencia article gives (Leyes 18.996, 19.355, 19.670, 19.924 and 20.075 each say "regirá a partir del 1° de enero de …"), or else ten days after publication (Código Civil art. 1). No law is backdated: where the day a law gives itself falls before its promulgation or its publication, it is dated ten days after its publication, and the day it states is listed in the decisions.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 67 of the Constitution say on 1 January 1990? | `python tools/on.py 1990-01-01 constitucion 67` |
| The same, naming the reform behind the text | `python tools/on.py --law 1990-01-01 constitucion 67` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="1990-01-01T23:59:59Z" main -- constitucion/art-067.md):constitucion/art-067.md` |
| Which reform wrote each paragraph of art. 77? | `git blame constitucion/art-077.md` |
| Every change to art. 47, word by word | `git log -p --word-diff constitucion/art-047.md` |
| Every reform in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one reform changed | `git show law/plebiscito-1996-12-08` (tags `law/<key>` mark each law's commit) |
| The whole Constitution on a date | `python tools/on.py 1995-06-01 constitucion` |
| The Constitution as of a version | `git show constitucion/1990-05-01` (tags `<act>/<in-force day>`) |
| Laws passed but not yet in force | `git log main..futuro` (it also lists main's newer commits, replayed: see "The `futuro` branch") |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Montevideo, on the day the change took effect**. The plebiscite day is the `Enacted:` trailer, and the in-force day is in `In-force:`, which the tools read.
- **1967.** The Constitution was approved by plebiscite on 27 November 1966. Its transitional provision A), as the Parlamento prints the 1967 text, put it in force on 15 February 1967 (Secciones VIII to XI and XVI from 1 March 1967, provision B). Git cannot store dates before 1970, so this first commit is dated 1 January 1970; its real day is in the `In-force:` trailer, which `tools/on.py` reads.
- **1989 reform** (plebiscite of 26 November 1989: art. 67 incisos 2 and 3, provision V)). Provision V) puts the reform of art. 67 in force on 1 May 1990, and that is the version's day.
- **1994, 1996 and 2004 reforms.** A reform approved by plebiscite takes effect when the Corte Electoral proclaims the result (the 1996 text of provision A)). No source we read dates those proclamations, so **these versions are dated on the plebiscite day** (27 November 1994, 8 December 1996, 31 October 2004), and each commit says so. The Parlamento files the 1994 and 1996 texts as "vigencia 1995" and "vigencia 1997"; Decreto 435/004 of 13 December 2004 (IMPO) states that the 2004 reform was then in force. For a day between a plebiscite and its proclamation, the history shows the new text one step early.
- **Default rule for laws.** Código Civil art. 1: laws are binding by their promulgation by the Poder Ejecutivo, which is deemed known ten days after it is verified in the capital. A law's own vigencia clause overrides it. Ley 18.331 took effect on 28 August 2008, ten days after its publication on 18 August 2008 (it has no vigencia clause). No change is dated before its law was promulgated and published: where a law's own clause gives an earlier day (Ley 18.719, enacted 27 December 2010 and published 5 January 2011, "regirá a partir del 1° de enero de 2011"; other budget laws published after the 1 January they name; laws in force "desde su promulgación" but published later; retroactive clauses), the law is dated by the default rule, ten days after its publication (Ley 18.719: 15 January 2011), and the day it states is kept in the decisions. A law published before the day it names keeps that day.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## The `futuro` branch

Laws already passed but not yet in force are on the branch `futuro`, each dated by the day it will take effect. Published history only grows, on `main` and on `futuro` alike: when `main` gains newer commits, the future branch replays main's newer commits on top of its own (the same text, author, date and message, as new commits), and then adds any new laws not yet in force. So `git log main..futuro` lists those replayed copies too. The `In-force` trailer of each commit gives the day it takes effect, and `tools/on.py` reads the branch by that day.

## How it is checked

- **Every version is the Parlamento's own dated edition.** The Parlamento publishes the Constitution as approved in 1966 and as amended in 1989, 1994, 1996 and 2004. Each version's units have exactly the words of that edition, except units where the Parlamento's and IMPO's transcriptions differ in a few words (see below). [`data/verification.json`](data/verification.json) lists every such unit and every word that differs.
- **The reforms agree between two publishers.** The units each reform changed come from comparing consecutive Parlamento editions word by word. The parser stops unless they are exactly the units that IMPO's own notes ("La redacción de este artículo fue dada por la Reforma Constitucional, aprobada por plebiscito de fecha …", "El inciso final fue agregado por …") assign to that plebiscite. All four reforms match: 2 units (1989), 1 (1994), 34 (1996), 3 (2004).
- **Today's text is IMPO's consolidated text**, unit for unit, for every act, except the two literales of Ley 18.602 art. 4 left out below.
- **Ley 18.331, the Código Civil and the Código Penal:** the first version of each amended article is IMPO's original text of the law; every change step, the laws credited and the words that changed are in `data/verification.json`.
- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`), and must match `corpus.json`: 0 mismatches. No merge commits on `main`, commit dates never go backwards, nothing is dated in the future, and every commit's trailers parse.
- The repository is rebuilt from the same data a second time and gives identical hashes. Details in [`REPRODUCE.md`](REPRODUCE.md).

## What "author" means

The author of a commit is the reform or law that made the change, with an e-mail address that cannot exist (`plebiscito-1996-12-08@impo.invalid`, `ley-18719@impo.invalid`), so `git blame` and `git log --author` name them. The committer is always Lexifina.

- **Credits come only from the sources.** A unit of the Constitution is credited to a reform only when the Parlamento's editions show it changing at that reform and IMPO's note on the unit names that plebiscite. An article of a law is credited only to the laws IMPO's notes on that article name. There are no unexplained changes.
- **Transcription differences are not changes.** IMPO and the Parlamento transcribe the same text with small differences in about 40 units ("aun"/"aún", "hayan"/"haya", "presupuesto"/"presupuestos", ordinals in words or figures). A unit uses IMPO's text from its last reform on (throughout, if no reform touched it), and the Parlamento's text only before that, so these differences never show as changes. Inside a unit a reform rewrote, the reform's commit can also show such differences; `git log -p --word-diff` shows them.
- **Incisos added later.** Where a reform added incisos to an article (arts. 47, 67, 188), the earlier text is IMPO's text without those incisos, which has exactly the Parlamento's earlier words.
- The Parlamento's 2004 edition also changes words in arts. 7, 135, 197, 275 and 313 that no reform and no IMPO note explains; IMPO's text agrees with the earlier editions, so they are not changes here.
- Blame credits whole lines (one paragraph or item per line).

## What it does not show

- Changes to the Código Penal between 1934 and 1969. IMPO's text is the update of the Versión Oficial of 26 October 1967 (Decreto 698/967) and its notes name no amending law before Ley 13.737 (1969). If an article changed in that period, the change appears inside the next recorded change of that article. A sample of 11 articles IMPO marks as never amended has exactly the words of IMPO's 1933 original text.
- Intermediate texts no source gives (25 articles of the Código Penal, 2 of the Código Civil, listed as unresolved in `data/verification.json`): there the change is shown on the next day whose text is known, credited to every law in between, so for the days between those laws the file shows the older text. Where IMPO has no original text at all, the article shows today's text from the start.
- Ley 19.138 (Código Penal art. 350 BIS) takes effect ten days after its regulation, which we did not date; it is dated ten days after publication.
- The Código Civil before 1 December 1994. Its first commit is "oldest version available": the re-edition approved by Ley Nº 16.603, which IMPO consolidates.
- The Constitutions before 1967 (1830, 1918, 1934, 1942, 1952). The Parlamento publishes them, but this repository starts with the 1967 Constitution, which is a new text, not an amendment.
- Plebiscites that rejected a reform. They changed no words and are not recorded yet.
- The exact proclamation day of the 1994, 1996 and 2004 reforms (see Dates).
- Section and chapter headings, which are not units. IMPO's headings are not part of the article text.
- Changes to a law that IMPO's notes do not record. The history of a law is only as complete as IMPO's notes.
- A check against the original for Leyes 10.783 (1946) and 12.840 (1960). IMPO gives no original text of either as data, only an image of the Diario Oficial, so their single version is IMPO's text with no amendment recorded, not compared word for word with the text as published.
- The Ley de Urgente Consideración (Ley 19.889) as an act of its own: IMPO's consolidated text of it gives 253 of its 476 articles only as pointers to the laws they amended. Its changes are in those laws' histories (here the Códigos Civil, Penal, de Comercio, General del Proceso, del Proceso Penal and de la Niñez y la Adolescencia).
- In the Código Tributario, art. 40 has words ("ficta; se notifique la resolución definitiva") that its 1974 original lacks and no amending law IMPO names explains; like every article IMPO records no change to, it shows today's text throughout.
- Interpretative laws (for example Ley 19.355 art. 84 on Ley 18.331 arts. 9 and 17), which change no words.
- Items whose start the sources do not let us place. Ley 18.602 art. 4 literal L) (added by Ley 19.337 in 2015) and literal M) (added by Ley 19.472 in 2016, its wording repealed from 1 January 2021) could only be shown from 2021, years late, so they are left out of every version, including today's; the article has literales A) to K).
- Acts whose in-between texts cannot be rebuilt are left out rather than shown with old words for years: for example Ley 16.343 (Fondo Nacional de Recursos), whose 1993 wording of arts. 3 and 5 would stand until 2024 and 2026, and Ley 16.426 (seguros). The same goes for words today's text has that no law explains, when they are too large to treat as a transcription difference: Decreto-Ley 15.688 (Ley Orgánica del Ejército), whose art. 189 has a third inciso (about 90 words, on the day a retirement takes effect) that IMPO's original text lacks, with no note and no amending law found that added it, so the day it entered the law cannot be placed.

Only the texts published by the Parlamento and IMPO are authoritative. This repository is a research aid, not legal advice.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The history is built from IMPO's consolidated text of the Constitution, its transitional provisions and each law, with every original article and amending article their notes point to, and from the Parlamento's dated editions of the Constitution. Lexifina's code reads those texts and writes `corpus.json`; The same texts give the same bytes and the same commit hashes.

## Sources

| Source | What it gives | Dated versions | Names the amending act | Access |
| --- | --- | --- | --- | --- |
| [IMPO, Base de datos de normativa](https://www.impo.com.uy/bases) | Consolidated text in force of the Constitution, codes and laws | No (the original text of an amended article, for laws) | Yes, per article ("redacción dada por", "agregado por") | JSON |
| [Parlamento, Constitución de la República](https://parlamento.gub.uy/documentosyleyes/constitucion) | The Constitution as of 1967, 1989, 1994, 1997 and 2004, and the earlier constitutions | Yes | Footnotes on transitional provisions | HTML; Internet Archive copies of its pages, captures dated in Lexifina's code |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The texts are the official texts published by IMPO (www.impo.com.uy/bases) and the Parlamento del Uruguay (parlamento.gub.uy), cited as the source of every version. We make no claim to the legal text. The history, commit messages, tables and tools are released under [CC0 1.0](LICENSE).

**Nota de origen (IMPO open data).** The texts and data from IMPO are used under the [Licencia de Datos Abiertos – Uruguay, version 0.1](https://www.impo.com.uy/wp_impo/wp-content/uploads/2018/06/licencia-de-datos-abiertos.pdf).
- Provider: IMPO, Dirección Nacional de Impresiones y Publicaciones Oficiales.
- Licence: "Licencia de Datos Abiertos – Uruguay", version 0.1 (https://www.impo.com.uy/wp_impo/wp-content/uploads/2018/06/licencia-de-datos-abiertos.pdf).
- Datasets used: the IMPO legislation database (Base de datos de normativa, https://www.impo.com.uy/bases), above all Leyes, with Decretos-Ley, the codes, the Constitución and the original texts of laws.
- Changes: the texts were changed. They were assembled into a dated version history (one file per provision, one commit per amending law, earlier wordings rebuilt from IMPO's original texts and the amending laws' own words), with formatting normalised (line breaks rejoined into paragraphs, spacing and file layout made uniform).

---

## En español

La Constitución de la República Oriental del Uruguay como historia git: un archivo por artículo o disposición transitoria, y un commit por cada reforma plebiscitada (1989, 1994, 1996, 2004), con la reforma como autor y fechado el día en que entró en vigencia.

- **Fuentes:** las ediciones fechadas de la Constitución que publica el Parlamento (1967, 1989, 1994, 1997, 2004) y el texto actualizado de IMPO. Las unidades que cambió cada reforma coinciden exactamente con las notas de IMPO ("La redacción de este artículo fue dada por la Reforma Constitucional…").
- **Fechas:** la Constitución de 1967 rige desde el 15 de febrero de 1967; la reforma de 1989 desde el 1º de mayo de 1990 (disposición V). Las reformas de 1994, 1996 y 2004 rigen desde la proclamación de la Corte Electoral, que no hemos podido fechar con una fuente oficial: esas versiones llevan la fecha del plebiscito.
- **Diferencias de transcripción** entre IMPO y el Parlamento (por ejemplo "aun"/"aún") no se registran como cambios.
- **Leyes** (Ley Nº 18.331 de Protección de Datos Personales): la primera versión de cada artículo modificado es el texto original que publica IMPO, y cada cambio se atribuye a la ley que nombran las notas de IMPO ("redacción dada por", "agregado/s por"), en la fecha de vigencia que fija la propia ley o, en su defecto, diez días después de su publicación (Código Civil, art. 1). Ninguna ley se fecha antes de su promulgación y publicación: si la fecha que fija es anterior, rige la regla general (diez días después de la publicación).

**Solo texto vigente.** Las leyes cuya historia dice "Current text only" tienen una sola versión: el texto actualizado de IMPO. Con "in force from" está fechada el día en que entró en vigencia (el de la última ley modificativa que nombran las notas de IMPO, o el de la propia ley); con "last changed", el último día de cambio que dan las notas de IMPO (o la promulgación), fecha que se corregirá. Una ley que IMPO marca como derogada termina con un commit, atribuido a la ley derogatoria, que retira todos sus artículos.

Solo los textos del Parlamento y de IMPO son oficiales.

**Nota de origen (datos abiertos de IMPO).** Los textos y datos de IMPO se utilizan bajo la [Licencia de Datos Abiertos – Uruguay, versión 0.1](https://www.impo.com.uy/wp_impo/wp-content/uploads/2018/06/licencia-de-datos-abiertos.pdf).
- Proveedor: IMPO, Dirección Nacional de Impresiones y Publicaciones Oficiales.
- Licencia: "Licencia de Datos Abiertos – Uruguay", versión 0.1 (https://www.impo.com.uy/wp_impo/wp-content/uploads/2018/06/licencia-de-datos-abiertos.pdf).
- Conjuntos de datos utilizados: la base de datos de normativa de IMPO (https://www.impo.com.uy/bases), sobre todo Leyes, además de Decretos-Ley, los códigos, la Constitución y los textos originales de las leyes.
- Cambios: los textos fueron modificados. Se ordenaron en una historia de versiones fechadas (un archivo por disposición, un commit por ley modificativa; las redacciones anteriores se reconstruyen a partir de los textos originales de IMPO y de las propias leyes modificativas) y se normalizó el formato (párrafos recompuestos, espaciado y estructura de archivos uniformes).
