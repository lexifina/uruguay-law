# Uruguay: law history in git

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
| Laws passed but not yet in force | `git log main..futuro` (none today) |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Montevideo, on the day the change took effect**. The plebiscite day is the `Enacted:` trailer, and the in-force day is in `In-force:`, which the tools read.
- **1967.** The Constitution was approved by plebiscite on 27 November 1966. Its transitional provision A), as the Parlamento prints the 1967 text, put it in force on 15 February 1967 (Secciones VIII to XI and XVI from 1 March 1967, provision B). Git cannot store dates before 1970, so this first commit is dated 1 January 1970; its real day is in the `In-force:` trailer, which `tools/on.py` reads.
- **1989 reform** (plebiscite of 26 November 1989: art. 67 incisos 2 and 3, provision V)). Provision V) puts the reform of art. 67 in force on 1 May 1990, and that is the version's day.
- **1994, 1996 and 2004 reforms.** A reform approved by plebiscite takes effect when the Corte Electoral proclaims the result (the 1996 text of provision A)). No source we read dates those proclamations, so **these versions are dated on the plebiscite day** (27 November 1994, 8 December 1996, 31 October 2004), and each commit says so. The Parlamento files the 1994 and 1996 texts as "vigencia 1995" and "vigencia 1997"; Decreto 435/004 of 13 December 2004 (IMPO) states that the 2004 reform was then in force. For a day between a plebiscite and its proclamation, the history shows the new text one step early.
- **Default rule for laws.** Código Civil art. 1: laws are binding by their promulgation by the Poder Ejecutivo, which is deemed known ten days after it is verified in the capital. A law's own vigencia clause overrides it. Ley 18.331 took effect on 28 August 2008, ten days after its publication on 18 August 2008 (it has no vigencia clause). No change is dated before its law was promulgated and published: where a law's own clause gives an earlier day (Ley 18.719, enacted 27 December 2010 and published 5 January 2011, "regirá a partir del 1° de enero de 2011"; other budget laws published after the 1 January they name; laws in force "desde su promulgación" but published later; retroactive clauses), the law is dated by the default rule, ten days after its publication (Ley 18.719: 15 January 2011), and the day it states is kept in the decisions. A law published before the day it names keeps that day.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

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

The texts are the official texts published by IMPO (www.impo.com.uy/bases) and the Parlamento del Uruguay (parlamento.gub.uy), cited as the source of every version. We found no licence statement on either site and make no claim to the legal text. The history, commit messages, tables and tools are released under [CC0 1.0](LICENSE).

---

## En español

La Constitución de la República Oriental del Uruguay como historia git: un archivo por artículo o disposición transitoria, y un commit por cada reforma plebiscitada (1989, 1994, 1996, 2004), con la reforma como autor y fechado el día en que entró en vigencia.

- **Fuentes:** las ediciones fechadas de la Constitución que publica el Parlamento (1967, 1989, 1994, 1997, 2004) y el texto actualizado de IMPO. Las unidades que cambió cada reforma coinciden exactamente con las notas de IMPO ("La redacción de este artículo fue dada por la Reforma Constitucional…").
- **Fechas:** la Constitución de 1967 rige desde el 15 de febrero de 1967; la reforma de 1989 desde el 1º de mayo de 1990 (disposición V). Las reformas de 1994, 1996 y 2004 rigen desde la proclamación de la Corte Electoral, que no hemos podido fechar con una fuente oficial: esas versiones llevan la fecha del plebiscito.
- **Diferencias de transcripción** entre IMPO y el Parlamento (por ejemplo "aun"/"aún") no se registran como cambios.
- **Leyes** (Ley Nº 18.331 de Protección de Datos Personales): la primera versión de cada artículo modificado es el texto original que publica IMPO, y cada cambio se atribuye a la ley que nombran las notas de IMPO ("redacción dada por", "agregado/s por"), en la fecha de vigencia que fija la propia ley o, en su defecto, diez días después de su publicación (Código Civil, art. 1). Ninguna ley se fecha antes de su promulgación y publicación: si la fecha que fija es anterior, rige la regla general (diez días después de la publicación).

Solo los textos del Parlamento y de IMPO son oficiales.
