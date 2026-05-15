import re

with open('agencia-de-google-ads.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header
head_end = html.find('<!-- H1 Header Section -->')
head_content = html[:head_end]

# Extract footer
footer_start = html.find('<!-- Footer -->')
footer_content = html[footer_start:]

# Replace title and description in head
head_content = re.sub(r'<title>.*?</title>', '<title>Agencia SEO en Monterrey | Posicionamiento Orgánico, GEO y LLM | Futurité</title>', head_content)
head_content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="En Futurité ayudamos a empresas a crecer mediante estrategias avanzadas de posicionamiento orgánico, SEO tradicional, y optimización en motores impulsados por inteligencia artificial.">', head_content)

# Replace Schema FAQ
schema_faq = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "¿Qué es el SEO (posicionamiento web)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "El SEO es el conjunto de estrategias que permiten mejorar la visibilidad de un sitio web en los resultados orgánicos de buscadores como Google."
        }
      },{
        "@type": "Question",
        "name": "¿Cómo funciona el posicionamiento SEO?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Funciona optimizando distintos factores como contenido, estructura del sitio, autoridad del dominio y experiencia del usuario para mejorar el ranking en buscadores."
        }
      },{
        "@type": "Question",
        "name": "¿Cuál es la diferencia entre SEO y SEM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "El SEO se enfoca en resultados orgánicos a mediano y largo plazo, mientras que el SEM (como Google Ads) se basa en publicidad pagada para obtener resultados inmediatos."
        }
      },{
        "@type": "Question",
        "name": "¿Cuánto tarda una estrategia SEO en mostrar resultados?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Depende del mercado y la competencia, pero generalmente los resultados sólidos de una estrategia SEO profesional comienzan a notarse entre el tercer y sexto mes de ejecución continua."
        }
      }]
    }
    </script>
"""
head_content = re.sub(r'<script type="application/ld\+json">\s*{\s*"@context": "https://schema\.org",\s*"@type": "FAQPage".*?</script>', schema_faq, head_content, flags=re.DOTALL)


main_content = """
    <!-- H1 Header Section -->
    <section class="nosotros-header" style="position: relative; padding: 450px 0 100px; text-align: center; background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100%); color: var(--clr-base); overflow: hidden;">
        <div class="container" style="position: relative; z-index: 2;">
            <span style="display: block; font-size: 1.25rem; color: var(--clr-primary); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px;">Especialistas en Posicionamiento</span>
            <h1 style="font-size: clamp(3rem, 5vw, 4rem); font-family: var(--font-heading); font-weight: 800; letter-spacing: -2px; margin-bottom: 0; line-height: 1.1; color: var(--clr-contrast);">
                Agencia SEO: Liderazgo en Posicionamiento Orgánico, GEO y LLM SEO</h1>
        </div>
    </section>

    <!-- Main Content Wrapper (White Background) -->
    <main style="background-color: var(--clr-base); border-radius: 0; padding: 60px 0 0; position: relative; z-index: 10;">

        <!-- Green Banner Container -->
        <div class="container" style="margin-top: -110px; margin-bottom: 80px; position: relative; z-index: 10;">
            <div style="background-color: var(--clr-accent); color: var(--clr-contrast); padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(202, 254, 103, 0.2);">
                <p style="font-size: 1.5rem; font-weight: 600; margin: 0;">En Futurité ayudamos a empresas a crecer mediante estrategias avanzadas de posicionamiento orgánico que van más allá del SEO tradicional.</p>
            </div>
        </div>

        <!-- Intro Section -->
        <section class="container" style="margin-top: 40px; margin-bottom: 80px; text-align: center;">
            <p style="font-size: 1.25rem; color: var(--clr-muted); line-height: 1.6; margin: 0 auto 40px; text-align: justify;">
                Combinamos análisis de datos, optimización técnica y contenido estratégico para posicionar tu marca en buscadores y en entornos impulsados por inteligencia artificial como Google AI Overviews, ChatGPT y motores generativos. Nuestro enfoque no es solo atraer tráfico, sino convertirlo en clientes reales dentro de tu estrategia de marketing digital.
            </p>
        </section>
        
        <section class="container" style="margin-bottom: 120px;">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: var(--clr-contrast);">No generamos solo clics, convertimos visitas en clientes</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin: 20px auto 0;">El SEO moderno no se trata únicamente de posicionar palabras clave, sino de generar impacto en el negocio. En nuestra agencia de marketing digital trabajamos con un enfoque integral:</p>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; text-align: center;">
                <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); border-radius: 24px; padding: 40px 30px;">
                    <i class="fa-solid fa-users" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 20px;"></i>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 15px;">Atraemos tráfico calificado</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Enfocamos nuestros esfuerzos en palabras clave con alta intención de compra, atrayendo a quienes ya te buscan.</p>
                </div>
                <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); border-radius: 24px; padding: 40px 30px;">
                    <i class="fa-solid fa-desktop" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 20px;"></i>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 15px;">Mejoramos la experiencia</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Optimizamos la experiencia del usuario (UX) en tu sitio web para asegurar que ese tráfico aumente tus conversiones.</p>
                </div>
                <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); border-radius: 24px; padding: 40px 30px;">
                    <i class="fa-solid fa-funnel-dollar" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 20px;"></i>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 15px;">Optimizamos el embudo</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Cada acción está alineada a objetivos comerciales: más leads, más ventas y crecimiento sostenible a largo plazo.</p>
                </div>
            </div>
        </section>

        <!-- H2: Nuestra Metodología SEO de Alto Impacto -->
        <section style="background: var(--clr-contrast); padding: 120px 0; color: #fff;">
            <div class="container">
                <div style="text-align: center; margin-bottom: 60px;">
                    <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: #fff;">Nuestra Metodología SEO de Alto Impacto</h2>
                    <p style="font-size: 1.1rem; opacity: 0.9; max-width: 800px; margin: 20px auto 0;">Nuestra metodología está diseñada para lograr resultados medibles a mediano y largo plazo.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px;">
                    <!-- H3: Estrategia SEO y Benchmark -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 40px;">
                        <h3 style="font-family: var(--font-heading); font-weight: 800; font-size: 1.75rem; color: var(--clr-accent); margin-bottom: 16px;">Estrategia SEO y Benchmark</h3>
                        <p style="font-size: 1rem; opacity: 0.9; margin-bottom: 20px;">Analizamos tu mercado, competencia y oportunidades reales de posicionamiento. Desarrollamos una estrategia basada en:</p>
                        <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem;">
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Benchmark competitivo</span></li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Análisis de tendencias de búsqueda</span></li>
                            <li style="display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Identificación de oportunidades de crecimiento</span></li>
                        </ul>
                    </div>
                    
                    <!-- H3: Análisis de Keywords y SEO On-Page -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 40px;">
                        <h3 style="font-family: var(--font-heading); font-weight: 800; font-size: 1.75rem; color: var(--clr-accent); margin-bottom: 16px;">Análisis de Keywords y SEO On-Page</h3>
                        <p style="font-size: 1rem; opacity: 0.9; margin-bottom: 20px;">Identificamos las palabras clave que realmente generan negocio. Optimizamos tu sitio web con:</p>
                        <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem;">
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Arquitectura de contenidos</span></li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Optimización de encabezados y metadata</span></li>
                            <li style="display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Copywriting SEO enfocado en intención de búsqueda</span></li>
                        </ul>
                    </div>

                    <!-- H3: Optimización con SEO Técnico -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 40px;">
                        <h3 style="font-family: var(--font-heading); font-weight: 800; font-size: 1.75rem; color: var(--clr-accent); margin-bottom: 16px;">Optimización con SEO Técnico</h3>
                        <p style="font-size: 1rem; opacity: 0.9; margin-bottom: 20px;">El rendimiento técnico es clave para posicionar correctamente. Trabajamos en:</p>
                        <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem;">
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Velocidad de carga</span></li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Indexación y rastreo</span></li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Estructura del sitio web</span></li>
                            <li style="display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Core Web Vitals</span></li>
                        </ul>
                    </div>

                    <!-- H3: Linkbuilding y Autoridad de Dominio -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 40px;">
                        <h3 style="font-family: var(--font-heading); font-weight: 800; font-size: 1.75rem; color: var(--clr-accent); margin-bottom: 16px;">Linkbuilding y Autoridad de Dominio</h3>
                        <p style="font-size: 1rem; opacity: 0.9; margin-bottom: 20px;">Construimos autoridad para tu sitio web mediante estrategias de enlaces de calidad. Esto permite:</p>
                        <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.95rem;">
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Mejorar tu posicionamiento en buscadores</span></li>
                            <li style="margin-bottom: 12px; display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Aumentar la confianza de tu dominio</span></li>
                            <li style="display: flex; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-primary); margin-top: 4px;"></i><span>Competir por palabras clave más relevantes</span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Gráficas Reales -->
        <section class="container" style="padding: 120px 0; text-align: center;">
            <div style="margin-bottom: 60px;">
                <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: var(--clr-contrast);">Crecimiento Comprobado con Datos Reales</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin: 20px auto 0;">Nuestro compromiso se refleja en el tráfico orgánico sostenido y en aumento que logramos para nuestros clientes a través de estrategias SEO avanzadas.</p>
            </div>
            
            <div style="background: #fff; padding: 30px; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); display: inline-block; max-width: 100%;">
                <img src="./assets/seo_growth_chart_placeholder.png" alt="Gráfica de crecimiento orgánico en Google Search Console y Semrush" style="max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #eaeaea;">
                <p style="color: var(--clr-muted); font-size: 0.9rem; margin-top: 20px; font-style: italic;">(Captura de pantalla real de la gráfica de crecimiento de tráfico de Semrush / Google Search Console)</p>
            </div>
        </section>

        <!-- H2: ¿Por qué elegir a Futurité? Autoridad Comprobada -->
        <section style="background: rgba(45, 79, 230, 0.03); padding: 120px 0;">
            <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
                <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: var(--clr-contrast); margin-bottom: 24px;">¿Por qué elegir a Futurité? Autoridad Comprobada</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin-bottom: 60px;">Nuestro trabajo está respaldado por experiencia y resultados. No solo ejecutamos SEO, desarrollamos estrategias que impactan directamente en el crecimiento de nuestros clientes.</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; width: 100%;">
                    <div style="background: #fff; border: 1px solid var(--clr-primary); padding: 50px 40px; border-radius: 24px;">
                        <i class="fa-solid fa-calendar-check" style="font-size: 2.5rem; color: var(--clr-accent); margin-bottom: 20px;"></i>
                        <h4 style="font-size: 1.5rem; margin-bottom: 16px; color: var(--clr-contrast);">Más de 15 años de experiencia</h4>
                        <p style="color: var(--clr-muted); line-height: 1.6;">Dominando el panorama del marketing digital.</p>
                    </div>
                    <div style="background: #fff; border: 1px solid var(--clr-primary); padding: 50px 40px; border-radius: 24px;">
                        <i class="fa-solid fa-trophy" style="font-size: 2.5rem; color: var(--clr-accent); margin-bottom: 20px;"></i>
                        <h4 style="font-size: 1.5rem; margin-bottom: 16px; color: var(--clr-contrast);">Top Agencia SEO</h4>
                        <p style="color: var(--clr-muted); line-height: 1.6;">Reconocidos como una de las mejores agencias SEO en México.</p>
                    </div>
                    <div style="background: #fff; border: 1px solid var(--clr-primary); padding: 50px 40px; border-radius: 24px;">
                        <i class="fa-solid fa-chart-line" style="font-size: 2.5rem; color: var(--clr-accent); margin-bottom: 20px;"></i>
                        <h4 style="font-size: 1.5rem; margin-bottom: 16px; color: var(--clr-contrast);">Resultados de Negocio</h4>
                        <p style="color: var(--clr-muted); line-height: 1.6;">Estrategias alineadas a resultados reales comerciales.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- El Futuro del SEO: Inteligencia Artificial y GEO -->
        <section style="padding: 120px 0;">
            <div class="container">
                <div style="text-align: center; margin-bottom: 60px;">
                    <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: var(--clr-contrast);">El Futuro del SEO: Inteligencia Artificial y GEO</h2>
                    <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin: 20px auto 0;">El posicionamiento ha evolucionado. Hoy no solo se trata de Google, sino de cómo tu marca aparece en respuestas generadas por inteligencia artificial.</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px;">
                    <div style="background: var(--clr-primary); color: #fff; padding: 50px; border-radius: 24px; position: relative; overflow: hidden;">
                        <i class="fa-solid fa-robot" style="position: absolute; right: -20px; bottom: -20px; font-size: 10rem; color: #fff; opacity: 0.15; pointer-events: none;"></i>
                        <h3 style="font-size: 1.75rem; font-family: var(--font-heading); color: #fff; margin-bottom: 24px; position: relative; z-index: 2;">Generative Engine Optimization (GEO)</h3>
                        <p style="font-size: 1.1rem; line-height: 1.6; opacity: 0.9; margin-bottom: 24px; position: relative; z-index: 2;">Optimizamos tu contenido para aparecer en respuestas generadas por motores de IA. Esto incluye:</p>
                        <ul style="list-style: none; padding: 0; margin: 0; position: relative; z-index: 2;">
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Estructuración de contenido para AI Overviews</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Optimización semántica avanzada</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Creación de contenido “citable” por modelos de IA</span></li>
                        </ul>
                    </div>
                    <div style="background: var(--clr-contrast); color: #fff; padding: 50px; border-radius: 24px; position: relative; overflow: hidden;">
                        <i class="fa-solid fa-brain" style="position: absolute; right: -20px; bottom: -20px; font-size: 10rem; color: #fff; opacity: 0.05; pointer-events: none;"></i>
                        <h3 style="font-size: 1.75rem; font-family: var(--font-heading); color: #fff; margin-bottom: 24px; position: relative; z-index: 2;">Optimización de Modelos de Lenguaje (LLM SEO)</h3>
                        <p style="font-size: 1.1rem; line-height: 1.6; opacity: 0.9; margin-bottom: 24px; position: relative; z-index: 2;">Trabajamos para que tu marca sea reconocida por modelos de lenguaje como una fuente confiable. Aplicamos estrategias que permiten:</p>
                        <ul style="list-style: none; padding: 0; margin: 0; position: relative; z-index: 2;">
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Mayor visibilidad en respuestas generativas</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Posicionamiento como autoridad en tu industria</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Integración con el ecosistema del mundo digital actual</span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Casos de Éxito y Testimoniales Slider -->
        <section style="background: var(--clr-contrast); padding: 120px 0; overflow: hidden;">
            <div class="container">
                <div style="text-align: center; margin-bottom: 60px;">
                    <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: #fff;">Testimoniales y Casos de Éxito SEO</h2>
                </div>

                <!-- Testimonial Slider Wrapper -->
                <div style="display: flex; gap: 30px; overflow-x: auto; padding-bottom: 40px; scroll-snap-type: x mandatory; scrollbar-width: none;">
                    <!-- Video Card 1 -->
                    <div style="min-width: 300px; flex: 1; background: #fff; border-radius: 24px; overflow: hidden; scroll-snap-align: start;">
                        <div style="width: 100%; aspect-ratio: 9/16; background: #000; position: relative;">
                            <!-- Placeholder for video -->
                            <video src="./assets/testimonial1.mp4" controls style="width: 100%; height: 100%; object-fit: cover;"></video>
                        </div>
                        <div style="padding: 24px;">
                            <h3 style="font-size: 1.25rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 10px;">Caso de Éxito: Retailer Nacional aumenta su tráfico orgánico un 200%</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem;">Estrategia SEO integral que posicionó más de 50 palabras clave en el Top 3 de Google.</p>
                        </div>
                    </div>
                    <!-- Video Card 2 -->
                    <div style="min-width: 300px; flex: 1; background: #fff; border-radius: 24px; overflow: hidden; scroll-snap-align: start;">
                        <div style="width: 100%; aspect-ratio: 9/16; background: #000; position: relative;">
                            <!-- Placeholder for video -->
                            <video src="./assets/testimonial2.mp4" controls style="width: 100%; height: 100%; object-fit: cover;"></video>
                        </div>
                        <div style="padding: 24px;">
                            <h3 style="font-size: 1.25rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 10px;">Caso de Éxito: Clínica Médica domina el posicionamiento local y duplica sus leads</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem;">Implementación de SEO Local y contenido médico especializado (E-E-A-T).</p>
                        </div>
                    </div>
                    <!-- Video Card 3 -->
                    <div style="min-width: 300px; flex: 1; background: #fff; border-radius: 24px; overflow: hidden; scroll-snap-align: start;">
                        <div style="width: 100%; aspect-ratio: 9/16; background: #000; position: relative;">
                            <!-- Placeholder for video -->
                            <video src="./assets/testimonial3.mp4" controls style="width: 100%; height: 100%; object-fit: cover;"></video>
                        </div>
                        <div style="padding: 24px;">
                            <h3 style="font-size: 1.25rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 10px;">Caso de Éxito: SaaS B2B alcanza a tomadores de decisión mediante LLM SEO</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem;">Optimización para motores generativos que resultó en visibilidad en IA Overviews.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Cinta Animada de Servicios (Marquee) -->
        <div style="overflow: hidden; width: 100%; max-width: 100vw; padding: 40px 0; margin-top: -60px; margin-bottom: -82px; position: relative; z-index: 20; box-sizing: border-box;">
            <div style="background: var(--clr-accent); color: var(--clr-contrast); padding: 24px 0; white-space: nowrap; transform: rotate(-2deg) scale(1.05); width: 100%; position: relative; z-index: 10;">
                <div style="display: flex; width: max-content; animation: serviceMarquee 35s linear infinite;">
                    <div style="display: flex; gap: 60px; padding: 0 30px; align-items: center;">
                        <a href="agencia-de-redes-sociales.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Redes Sociales</a>
                        <a href="agencia-de-google-ads.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Google Ads</a>
                        <a href="agencia-seo.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> SEO</a>
                        <a href="index.html#apps" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> APP'S</a>
                        <a href="index.html#ecommerce" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Comercio Electrónico</a>
                        <a href="index.html#marketing-medico" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Marketing Médico</a>
                    </div>
                    <div style="display: flex; gap: 60px; padding: 0 30px; align-items: center;">
                        <a href="agencia-de-redes-sociales.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Redes Sociales</a>
                        <a href="agencia-de-google-ads.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Google Ads</a>
                        <a href="agencia-seo.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> SEO</a>
                        <a href="index.html#apps" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> APP'S</a>
                        <a href="index.html#ecommerce" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Comercio Electrónico</a>
                        <a href="index.html#marketing-medico" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Marketing Médico</a>
                    </div>
                </div>
                <style>
                    @keyframes serviceMarquee {
                        from { transform: translateX(0); }
                        to { transform: translateX(-50%); }
                    }
                </style>
            </div>
        </div>

        <!-- Preguntas Frecuentes (FAQ) -->
        <section class="faq-section" style="padding: 120px 0; background: var(--clr-base);">
            <div class="container">
                <div style="margin-bottom: 60px; text-align: center;">
                    <h2 style="font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast);">Preguntas Frecuentes sobre el Posicionamiento SEO</h2>
                </div>

                <div class="faq-accordion">
                    <!-- FAQ Item 1 -->
                    <details class="faq-item" name="faq-group-seo">
                        <summary class="faq-question"><h3 style="display:inline; font-size:inherit; font-weight:inherit; margin:0;">¿Qué es el SEO (posicionamiento web)?</h3></summary>
                        <div class="faq-answer">
                            <p>El SEO es el conjunto de estrategias que permiten mejorar la visibilidad de un sitio web en los resultados orgánicos de buscadores como Google.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 2 -->
                    <details class="faq-item" name="faq-group-seo">
                        <summary class="faq-question"><h3 style="display:inline; font-size:inherit; font-weight:inherit; margin:0;">¿Cómo funciona el posicionamiento SEO?</h3></summary>
                        <div class="faq-answer">
                            <p>Funciona optimizando distintos factores como contenido, estructura del sitio, autoridad del dominio y experiencia del usuario para mejorar el ranking en buscadores.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 3 -->
                    <details class="faq-item" name="faq-group-seo">
                        <summary class="faq-question"><h3 style="display:inline; font-size:inherit; font-weight:inherit; margin:0;">¿Cuál es la diferencia entre SEO y SEM?</h3></summary>
                        <div class="faq-answer">
                            <p>El SEO se enfoca en resultados orgánicos a mediano y largo plazo, mientras que el SEM (como Google Ads) se basa en publicidad pagada para obtener resultados inmediatos.</p>
                        </div>
                    </details>
                    
                    <!-- FAQ Item 4 -->
                    <details class="faq-item" name="faq-group-seo">
                        <summary class="faq-question"><h3 style="display:inline; font-size:inherit; font-weight:inherit; margin:0;">¿Cuánto tarda una estrategia SEO en mostrar resultados?</h3></summary>
                        <div class="faq-answer">
                            <p>Depende del mercado y la competencia, pero generalmente los resultados sólidos de una estrategia SEO profesional comienzan a notarse entre el tercer y sexto mes de ejecución continua.</p>
                        </div>
                    </details>
                </div>
            </div>
        </section>

    </main>
"""

new_html = head_content + main_content + "\n" + footer_content

# Fix the active link in the nav
new_html = new_html.replace('href="index.html#seo"', 'href="agencia-seo.html"')

with open('agencia-seo.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

