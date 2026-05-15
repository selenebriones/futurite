import re

with open('desarrollo-aplicaciones-moviles.html', 'r') as f:
    html = f.read()

# Update title and meta description
html = re.sub(r'<title>.*?</title>', '<title>Desarrollo de Aplicaciones Móviles en Monterrey | Futurité</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Agencia de Desarrollo de Aplicaciones Móviles en Monterrey. Apps Nativas, Híbridas, Web Apps y Software a la Medida. 1 Año de Garantía.">', html)

# Update Schema Markup JSON-LD FAQPage
faq_schema = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "¿Cuánto cuesta desarrollar una aplicación móvil?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "El costo depende de múltiples factores como complejidad, funcionalidades, integraciones y plataformas. Cada proyecto se cotiza de forma personalizada para asegurar que cumpla con tus objetivos."
        }
      },{
        "@type": "Question",
        "name": "¿Cuánto tiempo tarda en programarse una app?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "El tiempo varía según el alcance del proyecto. En general, un desarrollo puede tomar desde algunas semanas hasta varios meses, dependiendo de la complejidad."
        }
      },{
        "@type": "Question",
        "name": "¿Ustedes publican la app en la App Store y Google Play?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sí. Nos encargamos del proceso de publicación, configuración y cumplimiento de lineamientos en ambas plataformas."
        }
      },{
        "@type": "Question",
        "name": "¿Qué incluye el año de garantía en el desarrollo?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Incluye soporte técnico, corrección de errores y acompañamiento posterior al lanzamiento para asegurar el correcto funcionamiento de la aplicación."
        }
      }]
    }
    </script>
"""
html = re.sub(r'<script type="application/ld\+json">\s*{\s*"@context":\s*"https://schema.org",\s*"@type":\s*"FAQPage".*?</script>', faq_schema.strip(), html, flags=re.DOTALL)

# Now we need to replace the content of `<main>` and `<header class="nosotros-header">`.
# Actually, the header is right before main. Let's replace from `<section class="nosotros-header"` down to `</main>`.

# Wait, `nosotros-header` is:
# <section class="nosotros-header" style="...">
#    ...
# </section>
# <main ...>
# ...
# </main>

new_content = """
    <!-- H1 Header Section -->
    <section class="nosotros-header" style="position: relative; padding: 450px 0 100px; text-align: center; background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100%); color: var(--clr-base); overflow: hidden;">
        <div class="container" style="position: relative; z-index: 2;">
            <span style="display: block; font-size: 1.25rem; color: var(--clr-primary); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px;">Software y Móvil</span>
            <h1 style="font-size: clamp(3rem, 5vw, 4rem); font-family: var(--font-heading); font-weight: 800; letter-spacing: -2px; margin-bottom: 0; line-height: 1.1; color: var(--clr-contrast);">
                Desarrollo de Aplicaciones Móviles en Monterrey</h1>
        </div>
    </section>

    <!-- Main Content Wrapper (White Background) -->
    <main style="background-color: var(--clr-base); border-radius: 0; padding: 60px 0 0; position: relative; z-index: 10;">

        <!-- Green Banner Container (Trust Badge 1 Año Garantía) -->
        <div class="container" style="margin-top: -110px; margin-bottom: 80px; position: relative; z-index: 10;">
            <div style="background-color: var(--clr-accent); color: var(--clr-contrast); padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(202, 254, 103, 0.2);">
                <p style="font-size: 1.5rem; font-weight: 600; margin: 0;">Transformamos tu idea en una App con UX de primer nivel y 1 Año de Garantía</p>
            </div>
        </div>

        <!-- Intro Content -->
        <section class="container" style="margin-top: 40px; margin-bottom: 80px;">
            <div style="text-align: justify; font-size: 1.25rem; line-height: 1.8; color: var(--clr-muted);">
                <p>En Futurité desarrollamos aplicaciones móviles a la medida que combinan tecnología, experiencia de usuario y estrategia digital para impulsar el crecimiento de tu empresa.</p>
                <p style="margin-top: 24px;">Convertimos ideas en soluciones funcionales, escalables y enfocadas en resultados reales dentro del mundo digital. Desarrollar una app no es solo programar, es crear una experiencia que funcione para tu negocio y tus usuarios.</p>
                <p style="margin-top: 24px;">En nuestra agencia de marketing digital trabajamos cada proyecto con un enfoque integral:</p>
                <ul style="list-style: none; padding: 0; margin: 24px 0 0 0;">
                    <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-accent); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Diseño centrado en el usuario (UX/UI)</span></li>
                    <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-accent); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Desarrollo escalable y seguro</span></li>
                    <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-accent); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Integración con sistemas y plataformas</span></li>
                    <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-accent); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Optimización para rendimiento y crecimiento</span></li>
                </ul>
                <p style="margin-top: 24px; font-weight: 600; color: var(--clr-contrast);">Además, todos nuestros desarrollos incluyen 1 año de garantía, asegurando estabilidad, soporte y confianza en cada proyecto.</p>
            </div>
        </section>

        <!-- Tipos de Apps -->
        <section style="background: rgba(45, 79, 230, 0.03); padding: 120px 0;">
            <div class="container">
                <div style="text-align: center; margin-bottom: 60px;">
                    <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: var(--clr-contrast); margin-bottom: 24px;">Tipos de Aplicaciones que Desarrollamos a la Medida</h2>
                    <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin: 0 auto;">Cada negocio requiere una solución distinta. Por eso desarrollamos diferentes tipos de aplicaciones según tus objetivos.</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; margin-bottom: 60px;">
                    <!-- App Nativa -->
                    <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">Aplicaciones Nativas</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin-bottom: 24px;">Desarrollamos aplicaciones móviles nativas para máximo rendimiento y experiencia. Ideales para proyectos que requieren alto desempeño y escalabilidad.</p>
                        <h4 style="font-size: 1rem; color: var(--clr-contrast); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">Tecnologías:</h4>
                        <ul style="list-style: none; padding: 0; margin: 0;">
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-brands fa-apple" style="color: var(--clr-primary);"></i><span>Swift (iOS)</span></li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-brands fa-android" style="color: var(--clr-primary);"></i><span>Kotlin (Android)</span></li>
                        </ul>
                    </div>
                    <!-- App Híbrida -->
                    <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">Aplicaciones Híbridas y Multiplataforma</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin-bottom: 24px;">Creamos aplicaciones que funcionan en múltiples sistemas operativos con una sola base de código. Reducen tiempos y costos de desarrollo.</p>
                        <h4 style="font-size: 1rem; color: var(--clr-contrast); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">Tecnologías:</h4>
                        <ul style="list-style: none; padding: 0; margin: 0;">
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-solid fa-code" style="color: var(--clr-primary);"></i><span>Flutter</span></li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-brands fa-react" style="color: var(--clr-primary);"></i><span>React Native</span></li>
                        </ul>
                    </div>
                    <!-- Web Apps -->
                    <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">Web Apps y Sistemas Empresariales</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin-bottom: 24px;">Soluciones web robustas que funcionan como aplicaciones dentro de entornos empresariales, ideales para automatización de procesos internos.</p>
                        <h4 style="font-size: 1rem; color: var(--clr-contrast); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px;">Tecnologías:</h4>
                        <ul style="list-style: none; padding: 0; margin: 0;">
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-brands fa-node-js" style="color: var(--clr-primary);"></i><span>Node.js, Laravel</span></li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-solid fa-database" style="color: var(--clr-primary);"></i><span>SQL / NoSQL</span></li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 10px;"><i class="fa-brands fa-aws" style="color: var(--clr-primary);"></i><span>AWS / Firebase</span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Modulos -->
        <section class="container" style="padding: 120px 0; text-align: center;">
            <div style="margin-bottom: 60px;">
                <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 2.5rem; color: var(--clr-contrast);">Módulos Integrables para tu Empresa</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin: 20px auto 0;">Nuestras aplicaciones pueden integrarse con distintos sistemas para potenciar su funcionalidad. Cada app se desarrolla pensando en el crecimiento de tu negocio.</p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; text-align: center;">
                <div style="background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
                    <i class="fa-solid fa-credit-card" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                    <h3 style="font-size: 1.1rem; color: var(--clr-contrast);">Sistemas de Pago</h3>
                </div>
                <div style="background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
                    <i class="fa-solid fa-users-cog" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                    <h3 style="font-size: 1.1rem; color: var(--clr-contrast);">Integración con CRM</h3>
                </div>
                <div style="background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
                    <i class="fa-solid fa-chart-line" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                    <h3 style="font-size: 1.1rem; color: var(--clr-contrast);">Paneles Admin</h3>
                </div>
                <div style="background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
                    <i class="fa-solid fa-bell" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                    <h3 style="font-size: 1.1rem; color: var(--clr-contrast);">Notificaciones Push</h3>
                </div>
                <div style="background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
                    <i class="fa-solid fa-map-location-dot" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                    <h3 style="font-size: 1.1rem; color: var(--clr-contrast);">Geolocalización</h3>
                </div>
                <div style="background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eaeaea;">
                    <i class="fa-solid fa-robot" style="font-size: 2.5rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                    <h3 style="font-size: 1.1rem; color: var(--clr-contrast);">Automatización</h3>
                </div>
            </div>
        </section>

        <!-- Metodología en 6 pasos -->
        <section style="padding: 120px 0; margin-bottom: 100px;">
            <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 80px; align-items: start;">
                
                <!-- Left Column -->
                <div style="position: sticky; top: 120px;">
                    <span style="display: block; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; color: var(--clr-primary); margin-bottom: 16px; text-transform: uppercase;">Nuestro Proceso</span>
                    <h2 style="font-size: clamp(3rem, 5vw, 4.5rem); font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px; line-height: 1.1; letter-spacing: -1px;">
                        Proceso de Desarrollo <br><span style="color: var(--clr-primary);">en 6 Pasos.</span>
                    </h2>
                    <p style="color: var(--clr-muted); font-size: 1.1rem; line-height: 1.6; max-width: 90%;">Trabajamos con una metodología estructurada que garantiza claridad, control y resultados.</p>
                </div>
                
                <!-- Right Column (Ordered List of Steps) -->
                <ol style="display: flex; flex-direction: column; list-style: none; padding: 0; margin: 0;">
                    <!-- Step 1 -->
                    <li style="display: flex; align-items: center; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1;">01</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Análisis y definición del proyecto</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Evaluamos tus necesidades, objetivos y alcance del desarrollo.</p>
                        </div>
                    </li>
                    <!-- Step 2 -->
                    <li style="display: flex; align-items: center; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1;">02</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Arquitectura y experiencia de usuario (UX/UI)</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Diseñamos la estructura y navegación de la aplicación.</p>
                        </div>
                    </li>
                    <!-- Step 3 -->
                    <li style="display: flex; align-items: center; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1;">03</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Desarrollo y programación</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Construimos la app utilizando tecnologías modernas y buenas prácticas.</p>
                        </div>
                    </li>
                    <!-- Step 4 -->
                    <li style="display: flex; align-items: center; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1;">04</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Prototipos y validación</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Probamos funcionalidades antes del lanzamiento.</p>
                        </div>
                    </li>
                    <!-- Step 5 -->
                    <li style="display: flex; align-items: center; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1;">05</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Pruebas y QA</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Aseguramos estabilidad, rendimiento y seguridad.</p>
                        </div>
                    </li>
                    <!-- Step 6 -->
                    <li style="display: flex; align-items: center; justify-content: space-between; gap: 30px; padding-bottom: 10px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1;">06</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Lanzamiento y soporte (Hypercare)</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Publicamos la aplicación y damos seguimiento para asegurar su funcionamiento.</p>
                        </div>
                    </li>
                </ol>
            </div>
        </section>

        <!-- Cinta Animada de Servicios (Marquee) -->
        <div style="overflow: hidden; width: 100%; max-width: 100vw; padding: 40px 0; margin-top: -60px; margin-bottom: -82px; position: relative; z-index: 20; box-sizing: border-box;">
            <div style="background: var(--clr-accent); color: var(--clr-contrast); padding: 24px 0; white-space: nowrap; transform: rotate(-2deg) scale(1.05); width: 100%; position: relative; z-index: 10;">
                <div style="display: flex; width: max-content; animation: serviceMarquee 35s linear infinite;">
                    <div style="display: flex; gap: 60px; padding: 0 30px; align-items: center;">
                        <a href="desarrollo-aplicaciones-moviles.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> APP'S</a>
                        <a href="agencia-de-redes-sociales.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Redes Sociales</a>
                        <a href="agencia-de-google-ads.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Google Ads</a>
                        <a href="agencia-seo.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> SEO</a>
                        <a href="index.html#ecommerce" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Comercio Electrónico</a>
                        <a href="index.html#marketing-medico" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Marketing Médico</a>
                    </div>
                    <div style="display: flex; gap: 60px; padding: 0 30px; align-items: center;">
                        <a href="desarrollo-aplicaciones-moviles.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> APP'S</a>
                        <a href="agencia-de-redes-sociales.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Redes Sociales</a>
                        <a href="agencia-de-google-ads.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> Google Ads</a>
                        <a href="agencia-seo.html" style="font-size: 1.5rem; font-weight: 800; text-transform: uppercase; font-family: var(--font-heading); text-decoration: none; color: inherit; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'"><i class="fa-solid fa-star" style="font-size: 1rem; margin-right: 15px;"></i> SEO</a>
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

        <!-- ¿Por qué elegir a Futurité? Autoridad Comprobada -->
        <section style="background: var(--clr-contrast); padding: 120px 0;">
            <div class="container" style="color: #fff; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <h2 style="font-family: var(--font-heading); font-weight: 800; margin-bottom: 24px; color: #fff;">¿Por qué elegir a Futurité para tu App?</h2>
                <p style="font-size: 1.1rem; opacity: 0.9; max-width: 700px; margin-bottom: 60px; line-height: 1.6;">Nuestra diferencia principal es que somos una agencia de marketing digital con un brazo de desarrollo (TI) in-house. Esto nos permite crear aplicaciones no solo funcionales, sino escalables comercialmente.</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; width: 100%; text-align: center;">
                    <!-- Card 1 -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); padding: 40px 30px; border-radius: 24px; transition: transform var(--transition-fast);">
                        <div style="width: 50px; height: 50px; background: rgba(202, 254, 103, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-code"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px; color: #fff;">Equipo In-House</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6; margin: 0;">Programadores y diseñadores UX expertos bajo un mismo techo.</p>
                    </div>
                    <!-- Card 2 -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); padding: 40px 30px; border-radius: 24px; transition: transform var(--transition-fast);">
                        <div style="width: 50px; height: 50px; background: rgba(202, 254, 103, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px; color: #fff;">1 Año de Garantía</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6; margin: 0;">Seguridad y soporte para que tu aplicación nunca falle.</p>
                    </div>
                    <!-- Card 3 -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); padding: 40px 30px; border-radius: 24px; transition: transform var(--transition-fast);">
                        <div style="width: 50px; height: 50px; background: rgba(202, 254, 103, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-mobile-screen-button"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px; color: #fff;">Stack Moderno</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6; margin: 0;">Usamos Flutter, React Native, Swift y Kotlin reales.</p>
                    </div>
                    <!-- Card 4 -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); padding: 40px 30px; border-radius: 24px; transition: transform var(--transition-fast);">
                        <div style="width: 50px; height: 50px; background: rgba(202, 254, 103, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-rocket"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px; color: #fff;">Enfoque Comercial</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6; margin: 0;">No solo creamos tu app, te ayudamos a impulsarla en el mercado.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Preguntas Frecuentes (FAQ) -->
        <section class="faq-section" style="padding: 120px 0; background: var(--clr-base);">
            <div class="container">
                <div style="margin-bottom: 60px; text-align: center;">
                    <h2 style="font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast);">Preguntas Frecuentes sobre el Desarrollo de Apps</h2>
                </div>

                <div class="faq-accordion">
                    <!-- FAQ Item 1 -->
                    <details class="faq-item" name="faq-group-apps">
                        <summary class="faq-question">¿Cuánto cuesta desarrollar una aplicación móvil?</summary>
                        <div class="faq-answer">
                            <p>El costo depende de múltiples factores como complejidad, funcionalidades, integraciones y plataformas. Cada proyecto se cotiza de forma personalizada para asegurar que cumpla con tus objetivos.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 2 -->
                    <details class="faq-item" name="faq-group-apps">
                        <summary class="faq-question">¿Cuánto tiempo tarda en programarse una app?</summary>
                        <div class="faq-answer">
                            <p>El tiempo varía según el alcance del proyecto. En general, un desarrollo puede tomar desde algunas semanas hasta varios meses, dependiendo de la complejidad.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 3 -->
                    <details class="faq-item" name="faq-group-apps">
                        <summary class="faq-question">¿Ustedes publican la app en la App Store y Google Play?</summary>
                        <div class="faq-answer">
                            <p>Sí. Nos encargamos del proceso de publicación, configuración y cumplimiento de lineamientos en ambas plataformas.</p>
                        </div>
                    </details>
                    
                    <!-- FAQ Item 4 -->
                    <details class="faq-item" name="faq-group-apps">
                        <summary class="faq-question">¿Qué incluye el año de garantía en el desarrollo?</summary>
                        <div class="faq-answer">
                            <p>Incluye soporte técnico, corrección de errores y acompañamiento posterior al lanzamiento para asegurar el correcto funcionamiento de la aplicación.</p>
                        </div>
                    </details>
                </div>
            </div>
        </section>

    </main>
"""

# replace between <!-- H1 Header Section --> and </main>
html = re.sub(r'<!-- H1 Header Section -->.*?</main>', new_content.strip() + '\n\n    </main>', html, flags=re.DOTALL)

with open('desarrollo-aplicaciones-moviles.html', 'w') as f:
    f.write(html)
