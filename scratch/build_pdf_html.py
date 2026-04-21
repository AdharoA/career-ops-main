import os

template_path = "templates/cv-template.html"
output_path = "output/cv-fabian-falcon.html"

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "{{LANG}}": "es",
    "{{PAGE_WIDTH}}": "8.5in",
    "{{NAME}}": "Fabian Falcón",
    "{{PHONE}}": "904 919 619",
    "{{EMAIL}}": "adharo846270@gmail.com",
    "{{LINKEDIN_URL}}": "",
    "{{LINKEDIN_DISPLAY}}": "",
    "{{PORTFOLIO_URL}}": "",
    "{{PORTFOLIO_DISPLAY}}": "",
    "{{LOCATION}}": "Ica, Perú",
    "{{SECTION_SUMMARY}}": "Resumen Profesional",
    "{{SUMMARY_TEXT}}": "Estudiante de ingeniería de sistemas enfocado en asegurar la continuidad operativa en entornos exigentes. Tengo buena capacidad para adaptarme a múltiples requerimientos tecnológicos, demostrando habilidades para resolver incidentes bajo alta presión, tanto en redes como en soporte informático presencial. Acostumbrado a colaborar en equipo con empatía y vocación de servicio.",
    "{{SECTION_COMPETENCIES}}": "Competencias Clave",
    "{{COMPETENCIES}}": '''
      <span class="competency-tag">Soporte Windows y S.O.</span>
      <span class="competency-tag">Mantenimiento de Hardware</span>
      <span class="competency-tag">Configuración de Redes LAN/WLAN</span>
      <span class="competency-tag">Gestión e Instalación CCTV</span>
      <span class="competency-tag">Soporte a Impresoras de Red</span>
      <span class="competency-tag">Helpdesk y Trato al Usuario</span>
    ''',
    "{{SECTION_EXPERIENCE}}": "Experiencia Laboral",
    "{{EXPERIENCE}}": '''
  <div class="job">
    <div class="job-header">
      <div class="job-company">I.E 22488 JORGE CHAVEZ DARTNELL <span class="job-location">(Ica, Pisco)</span></div>
      <div class="job-period">Mantenimiento / Soporte</div>
    </div>
    <div class="job-role">Soporte Técnico</div>
    <ul>
      <li>Brindé <strong>helpdesk y soporte a usuarios</strong> (área docente y administrativa) garantizando la continuidad operativa en tareas críticas.</li>
      <li>Realicé <strong>configuración de S.O., redes locales periféricos e impresoras</strong>.</li>
      <li>Efectué <strong>mantenimiento preventivo y correctivo</strong> de PCs e infraestructura computacional.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-header">
      <div class="job-company">Inmobiliaria URBANIZA <span class="job-location">(Ica)</span></div>
      <div class="job-period">Atención al Cliente</div>
    </div>
    <div class="job-role">Promotor Inmobiliario</div>
    <ul>
      <li>Alta capacidad de persuasión y resolución de consultas; el trato exigente me permite atender a usuarios con tolerancia y mucha paciencia corporativa a nivel de Helpdesk.</li>
    </ul>
  </div>
    ''',
    "{{SECTION_PROJECTS}}": "",
    "{{PROJECTS}}": "",
    "{{SECTION_EDUCATION}}": "Educación",
    "{{EDUCATION}}": '''
  <div class="edu-item">
    <div class="edu-header">
      <div class="edu-title">Ingeniería de Sistemas e Informática</div>
      <div class="edu-year">2020 - 2025</div>
    </div>
    <div class="edu-org">Universidad Tecnológica del Perú (UTP)</div>
    <div class="edu-desc">Sólida formación y conocimientos técnicos aplicables a entornos corporativos empresariales.</div>
  </div>
    ''',
    "{{SECTION_CERTIFICATIONS}}": "",
    "{{CERTIFICATIONS}}": "",
    "{{SECTION_SKILLS}}": "Habilidades Transversales",
    "{{SKILLS}}": '''
  <div class="skills-grid">
    <div class="skill-category">Perfil:</div>
    <div class="skill-item">Proactividad, Rápida curva de aprendizaje, Comunicación asertiva, Trabajo bajo alta presión, Diligencia y compromiso.</div>
  </div>
    '''
}

for k, v in replacements.items():
    html = html.replace(k, v)

# Limpieza de anclas vacias o modulos no requeridos.
html = html.replace('<div class="section avoid-break">\n    <div class="section-title"></div>\n    \n  </div>', '')
html = html.replace('<a href=""></a>', '')
html = html.replace('<a href=""></a>', '')
html = html.replace('<span class="separator">|</span>\n      \n      <span class="separator">|</span>\n      \n      <span class="separator">|</span>', '<span class="separator">|</span>')


cover_letter = '''
<div style="page-break-before: always; padding-top: 50px; font-family: 'DM Sans', sans-serif; font-size: 11.5px; color: #2f2f2f; line-height: 1.8;">
  <p>Ica, 18 de Abril de 2026</p>
  <br>
  <p><strong>Equipo de Selección (T.I.)</strong><br>
  Agrícola Miranda<br>
  Salas, Ica.</p>
  <br>
  <p>Estima área de reclutamiento,</p>
  <br>
  <p>Me es grato postular a la vacante de <strong>Técnico de Soporte Informático</strong> a fin de cubrir y apoyar la operatividad tecnológica y de infraestructura para sus predios/fundos. Como estudiante de Ingeniería de Sistemas de zona residente en Ica, estoy muy habituado a la exigencia operativa.</p>
  <p>Tengo trayectoria práctica prestando soporte a nivel Helpdesk para personal ofimático en la I.E. 22488 Jorge Chavez. Ese desafío fortaleció mi destreza configurando Windows, PCs, periféricos (CCTV/impresoras) y solucionando fallas de hardware, manteniéndolo siempre disponible en jornadas prolongadas. Adiciono a esto mi experiencia formal trabajando en atención al cliente la cual me enseñó a entender, empatizar y solucionar el estrés informático de los usuarios con profesionalismo y rapidez.</p>
  <br>
  <p>Mi intención es pertenecer a la familia de Agrícola Miranda contribuyendo directamente a evitar caídas del sistema y facilitar la fluidez laboral del personal de planta durante sus picos de actividades laborales y de campañas agrarias.</p>
  <br>
  <p>Agradezco de antemano el tiempo dedicado a mi currículo adjunto, quedando libre para una primera entrevista donde detallar mejor mi entusiasmo para ejercer este cargo.</p>
  <br>
  <p>Cordialmente,</p>
  <br>
  <p><strong>Fabián Falcón</strong><br>
  +51 904 919 619 | adharo846270@gmail.com</p>
</div>
'''

html = html.replace('</div>\n</body>', cover_letter + '\n</div>\n</body>')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML compilation success!")
