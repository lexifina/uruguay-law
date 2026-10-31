# Uruguay: law history in git

The law of Uruguay as a git history: one file per provision, one commit per law (or plebiscite) on the day it took effect, and the law that made each change as the commit's author. `git blame` names the reform behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `uy/`.

*En español: [más abajo](#en-español).*

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución de la República Oriental del Uruguay (1967) | 5 | From its entry into force (15 February 1967) through the reforms approved by plebiscite in 1989, 1994, 1996 and 2004, to today |
| `codigo-civil/` | Código Civil, as approved by Ley Nº 16.603 (1994) | 18 | From the re-edition approved by Ley 16.603 (in force 1 December 1994) through 20 amending laws (Leyes 16.719 to 20.446), to today. The code of 1868 and its changes before 1994 are not included |
| `codigo-penal/` | Código Penal (Ley Nº 9.155 of 1933) | 36 | As enacted (in force 1 August 1934, Ley 9.414 art. 2), then 47 amending laws from Ley 13.737 (1969) to Ley 20.353 (2024), to today. IMPO records no amendment between 1934 and 1969 (see below) |
| `ley-18331/` | Ley Nº 18.331 de Protección de Datos Personales (2008) | 7 | As enacted (in force 28 August 2008), then every amending law IMPO names: Leyes 18.719, 18.996, 19.355, 19.670, 19.924 and 20.075, to today |
| `codigo-general-proceso/` | Código General del Proceso (Ley Nº 15.982 of 1988) | 28 | From its entry into force (20 November 1989, art. 547), with Ley 16.053's earlier changes, through 36 amending laws to today |
| `codigo-comercio/` | Código de Comercio (1865) | 14 | The 1865 code as IMPO gives it, dated 24 January 1866 (Ley 841), through 15 amending laws and decree-laws to today; Libro IV (quiebras) reads a placeholder from 1879, as no source gives its 1878 and 1900 texts |
| `codigo-proceso-penal/` | Código del Proceso Penal (Ley Nº 19.293 of 2014) | 12 | From its entry into force (1 November 2017, art. 403), with the laws that changed it before that day, through 12 amending laws to today |
| `codigo-tributario/` | Código Tributario (Decreto-Ley Nº 14.306 of 1974) | 10 | As enacted (in force 16 December 1974), then 13 amending decree-laws and laws from Decreto-Ley 14.416 (1975) to Ley 20.446 (2025), to today |
| `ley-16060/` | Ley Nº 16.060 de Sociedades Comerciales (1989) | 21 | As enacted (in force 31 December 1989, art. 511), then 21 amending laws from Ley 16.296 (1992) to Ley 19.924 (2020), to today |
| `ley-17250/` | Ley Nº 17.250 de Relaciones de Consumo (2000) | 7 | As enacted (in force 27 August 2000), then Leyes 18.046, 18.362, 19.149, 19.355, 19.924 and 20.212, to today. Ley 20.531 (in force 1 January 2027) is not in IMPO's consolidated text yet |
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
| `ley-18387/` | Ley de Declaración Judicial del Concurso y Reorganización Empresarial (Ley Nº 18.387 of 2008) | 6 | As enacted (in force 2 November 2008), then 6 amending laws from Ley 18.411 (2008) to Ley 20.404 (2025), to today |
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
| `ley-17940/` | Ley de Libertad Sindical (Ley Nº 17.940 of 2006) | 1 | As enacted (in force 2 January 2006), with no amendment recorded by IMPO, to today |
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
| `ley-17897/` | Ley de Humanización y Modernización del Sistema Carcelario (Ley Nº 17.897 of 2005) | 5 | As enacted (in force 14 September 2005), then 4 amending laws from Ley 18.172 (2007) to Ley 20.446 (2025), to today |
| `ley-15750/` | Ley Orgánica de la Judicatura y de Organización de los Tribunales (Ley Nº 15.750 of 1985) | 15 | As enacted (in force 24 June 1985), then 15 amending laws from Ley 15.860 (1987) to Ley 19.996 (2021), to today |
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
| `ley-15848/` | Ley de Caducidad de la Pretensión Punitiva del Estado (Ley Nº 15.848 of 1986) | 1 | As enacted (in force 22 December 1986), with no amendment recorded by IMPO, to today |
| `ley-18831/` | Ley de Restablecimiento de la Pretensión Punitiva del Estado (Ley Nº 18.831 of 2011) | 1 | As enacted (in force 27 October 2011), with no amendment recorded by IMPO, to today |
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
| `ley-18786/` | Ley de Participación Público-Privada (Ley Nº 18.786 of 2011) | 3 | As enacted (in force 18 August 2011), then Ley 19.553, Ley 19.924, to today |
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

The articles are `<act>/art-NNN.md` (`art-009-bis.md` for Artículo 9 BIS; four digits in the Código Civil, `art-1782.md`); the Constitution's Disposiciones Transitorias y Especiales are `constitucion/disp-trans-<letter>.md` (`-prima` for V'), Z'), `-segunda` for Z")). The per-act `README.md` lists every provision, how often it changed and when.

**How a law's history is rebuilt.** IMPO publishes only today's text of a law, but under each amended article it names the amending law and article ("Inciso 2º) redacción dada por: Ley Nº 18.719 de 27/12/2010 artículo 152", "Literal Ñ) agregado/s por: …") and links the article as originally published ("TEXTO ORIGINAL"). So the first version of each amended article is IMPO's original text, and every later version is today's text. Where one article was amended by two laws on different days, the text in between is taken only from a source: the wording the earlier amending law quotes (IMPO's original of that law), or today's text without an item that IMPO says the later law added. Every step and how it was rebuilt is listed in [`data/verification.json`](data/verification.json). Each amending law takes effect on the day its own vigencia article gives (Leyes 18.719, 18.996, 19.355, 19.670, 19.924 and 20.075 each say "regirá a partir del 1° de enero de …"), or else ten days after publication (Código Civil art. 1).

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
- **Default rule for laws.** Código Civil art. 1: laws are binding by their promulgation by the Poder Ejecutivo, which is deemed known ten days after it is verified in the capital. A law's own vigencia clause overrides it. Ley 18.331 took effect on 28 August 2008, ten days after its publication on 18 August 2008 (it has no vigencia clause). Leyes 18.719 (enacted 27 December 2010, published 5 January 2011) and the other budget laws take effect on 1 January by their own vigencia article, so a change can take effect a few days before the law was published; the `Published:` trailer shows it.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- **Every version is the Parlamento's own dated edition.** The Parlamento publishes the Constitution as approved in 1966 and as amended in 1989, 1994, 1996 and 2004. Each version's units have exactly the words of that edition, except units where the Parlamento's and IMPO's transcriptions differ in a few words (see below). [`data/verification.json`](data/verification.json) lists every such unit and every word that differs.
- **The reforms agree between two publishers.** The units each reform changed come from comparing consecutive Parlamento editions word by word. The parser stops unless they are exactly the units that IMPO's own notes ("La redacción de este artículo fue dada por la Reforma Constitucional, aprobada por plebiscito de fecha …", "El inciso final fue agregado por …") assign to that plebiscite. All four reforms match: 2 units (1989), 1 (1994), 34 (1996), 3 (2004).
- **Today's text is IMPO's consolidated text**, unit for unit, for every act.
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
- The Ley de Urgente Consideración (Ley 19.889) as an act of its own: IMPO's consolidated text of it gives 253 of its 476 articles only as pointers to the laws they amended. Its changes are in those laws' histories (here the Códigos Civil, Penal, de Comercio, General del Proceso, del Proceso Penal and de la Niñez y la Adolescencia).
- In the Código Tributario, art. 40 has words ("ficta; se notifique la resolución definitiva") that its 1974 original lacks and no amending law IMPO names explains; like every article IMPO records no change to, it shows today's text throughout.
- Interpretative laws (for example Ley 19.355 art. 84 on Ley 18.331 arts. 9 and 17), which change no words.

Only the texts published by the Parlamento and IMPO are authoritative. This repository is a research aid, not legal advice.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

## Sources

| Source | What it gives | Dated versions | Names the amending act | Access |
| --- | --- | --- | --- | --- |
| [IMPO, Base de datos de normativa](https://www.impo.com.uy/bases) | Consolidated text in force of the Constitution, codes and laws | No (the original text of an amended article, for laws) | Yes, per article ("redacción dada por", "agregado por") | JSON (`?json=true`) |
| [Parlamento, Constitución de la República](https://parlamento.gub.uy/documentosyleyes/constitucion) | The Constitution as of 1967, 1989, 1994, 1997 and 2004, and the earlier constitutions | Yes | Footnotes on transitional provisions | HTML; read from Internet Archive copies, capture timestamps pinned in Lexifina's code |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The texts are the official texts published by IMPO (www.impo.com.uy/bases) and the Parlamento del Uruguay (parlamento.gub.uy), cited as the source of every version. We found no licence statement on either site and make no claim to the legal text. The history, commit messages, tables and tools are released under [CC0 1.0](LICENSE).

---

## En español

La Constitución de la República Oriental del Uruguay como historia git: un archivo por artículo o disposición transitoria, y un commit por cada reforma plebiscitada (1989, 1994, 1996, 2004), con la reforma como autor y fechado el día en que entró en vigencia.

- **Fuentes:** las ediciones fechadas de la Constitución que publica el Parlamento (1967, 1989, 1994, 1997, 2004) y el texto actualizado de IMPO. Las unidades que cambió cada reforma coinciden exactamente con las notas de IMPO ("La redacción de este artículo fue dada por la Reforma Constitucional…").
- **Fechas:** la Constitución de 1967 rige desde el 15 de febrero de 1967; la reforma de 1989 desde el 1º de mayo de 1990 (disposición V). Las reformas de 1994, 1996 y 2004 rigen desde la proclamación de la Corte Electoral, que no hemos podido fechar con una fuente oficial: esas versiones llevan la fecha del plebiscito.
- **Diferencias de transcripción** entre IMPO y el Parlamento (por ejemplo "aun"/"aún") no se registran como cambios.
- **Leyes** (Ley Nº 18.331 de Protección de Datos Personales): la primera versión de cada artículo modificado es el texto original que publica IMPO, y cada cambio se atribuye a la ley que nombran las notas de IMPO ("redacción dada por", "agregado/s por"), en la fecha de vigencia que fija la propia ley o, en su defecto, diez días después de su publicación (Código Civil, art. 1).

Solo los textos del Parlamento y de IMPO son oficiales.
