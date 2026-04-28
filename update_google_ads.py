import re

with open('agencia-de-google-ads.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Agencia de Google Ads en Monterrey | Futurité</title>',
    content
)
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Agencia de Google Ads en Monterrey: Maximiza tu ROAS con Expertos Certificados. Generamos más leads, ventas y mejor retorno de inversión.">',
    content
)

# New Main Content
main_new = """<!-- Main Content Wrapper (White Background) -->
    <main style="background-color: var(--clr-base); border-radius: 40px; margin-top: -40px; position: relative; z-index: 10; box-shadow: 0 -20px 40px rgba(0,0,0,0.05); padding-top: 80px;">

        <!-- Hero Section -->
        <section class="hero-section" style="padding: 100px 0 60px 0; background: var(--clr-base);">
            <div class="container" style="text-align: center; max-width: 900px; margin: 0 auto;">
                <span style="display: inline-block; padding: 8px 16px; background: rgba(45, 79, 230, 0.1); color: var(--clr-primary); font-weight: 700; border-radius: 100px; margin-bottom: 24px; font-size: 0.9rem; letter-spacing: 1px; text-transform: uppercase;">Agencia Google Partner</span>
                <h1 style="font-size: clamp(3rem, 6vw, 5rem); font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); line-height: 1.1; letter-spacing: -1.5px; margin-bottom: 24px;">
                    Agencia de Google Ads en Monterrey: <br><span style="color: var(--clr-primary);">Maximiza tu ROAS</span> con Expertos Certificados
                </h1>
                <p style="font-size: 1.25rem; color: var(--clr-muted); line-height: 1.6; max-width: 750px; margin: 0 auto 40px;">
                    En Futurité diseñamos y gestionamos campañas de Google Ads enfocadas en resultados reales: más leads, más ventas y mejor retorno de inversión. No se trata solo de aparecer en Google, sino de hacerlo con una estrategia que convierta cada clic en una oportunidad de negocio. Optimizamos cada campaña con base en datos, comportamiento del usuario y objetivos comerciales claros.
                </p>
                <a href="#contacto" class="btn btn-primary" style="padding: 18px 36px; font-size: 1.1rem;">
                    Quiero una estrategia para mi negocio <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i>
                </a>
            </div>
        </section>

        <!-- Trust Badges (Logos) -->
        <section style="padding: 40px 0; border-bottom: 1px solid #f0f0f0;">
            <div class="container">
                <p style="text-align: center; font-size: 0.9rem; font-weight: 700; color: var(--clr-muted); margin-bottom: 30px; letter-spacing: 1px; text-transform: uppercase;">Certificados por y trabajando con las mejores plataformas</p>
                <div style="display: flex; justify-content: center; align-items: center; gap: 60px; flex-wrap: wrap; opacity: 0.6; filter: grayscale(100%); transition: var(--transition-fast);">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" style="height: 35px; object-fit: contain;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/1024px-Google_%22G%22_logo.svg.png" alt="Google Partner" style="height: 35px; object-fit: contain;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Google_Analytics_Logo_2015.svg/1200px-Google_Analytics_Logo_2015.svg.png" alt="Google Analytics 4" style="height: 35px; object-fit: contain;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Google_Tag_Manager_Logo.svg/1024px-Google_Tag_Manager_Logo.svg.png" alt="Google Tag Manager" style="height: 35px; object-fit: contain;">
                </div>
            </div>
        </section>

        <!-- Campañas de Performance -->
        <section style="padding: 120px 0;">
            <div class="container">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;">
                    <div>
                        <h2 style="font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px; font-size: clamp(2.5rem, 4vw, 3.5rem); line-height: 1.1;">Campañas de Performance que <span style="color: var(--clr-primary);">Multiplican tu Inversión</span></h2>
                        <p style="font-size: 1.1rem; color: var(--clr-muted); margin-bottom: 30px; line-height: 1.6;">Invertir en Google Ads sin una estrategia clara puede significar perder dinero. Nuestro enfoque está diseñado para maximizar cada peso invertido.</p>
                        
                        <h4 style="font-size: 1.2rem; font-weight: 700; color: var(--clr-contrast); margin-bottom: 16px;">Trabajamos con campañas orientadas a performance:</h4>
                        <ul style="list-style: none; padding: 0; margin-bottom: 30px; color: var(--clr-text);">
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-check" style="color: var(--clr-accent);"></i><span>Generación de leads calificados</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-check" style="color: var(--clr-accent);"></i><span>Incremento en ventas online</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-check" style="color: var(--clr-accent);"></i><span>Captación de tráfico con alta intención de compra</span></li>
                        </ul>
                        
                        <h4 style="font-size: 1.2rem; font-weight: 700; color: var(--clr-contrast); margin-bottom: 16px;">Optimizamos continuamente métricas clave como:</h4>
                        <ul style="list-style: none; padding: 0; margin-bottom: 0; color: var(--clr-text);">
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-trend-down" style="color: var(--clr-accent);"></i><span>Costo por clic (CPC)</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-trend-down" style="color: var(--clr-accent);"></i><span>Costo por adquisición (CPA)</span></li>
                            <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-trend-up" style="color: var(--clr-accent);"></i><span>Retorno sobre la inversión (ROAS)</span></li>
                        </ul>
                    </div>
                    <div>
                        <!-- Placeholder for relevant image -->
                        <div style="background: var(--clr-contrast); border-radius: 32px; padding: 60px; color: #fff; text-align: center; box-shadow: var(--shadow-float);">
                            <h3 style="font-size: 3rem; color: var(--clr-accent); font-family: var(--font-heading); margin-bottom: 16px;">+40%</h3>
                            <p style="font-size: 1.2rem; margin-bottom: 40px; opacity: 0.9;">Reducción promedio en el Costo de Adquisición (CPA) de nuestros clientes en los primeros 3 meses.</p>
                            <h3 style="font-size: 3rem; color: var(--clr-accent); font-family: var(--font-heading); margin-bottom: 16px;">250%</h3>
                            <p style="font-size: 1.2rem; margin-bottom: 0; opacity: 0.9;">Incremento sostenido en el ROAS utilizando algoritmos de Performance Max.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ¿Qué tipo de campañas gestionamos? (Using Methodology layout) -->
        <section style="padding: 120px 0; margin-bottom: 100px;">
            <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 80px; align-items: start;">
                
                <!-- Left Column -->
                <div style="position: sticky; top: 120px;">
                    <span style="display: block; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; color: var(--clr-primary); margin-bottom: 16px; text-transform: uppercase;">Servicios Especializados</span>
                    <h2 style="font-size: clamp(2.9rem, 5vw, 4.6rem); font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px; line-height: 1.1; letter-spacing: -1px;">¿Qué tipo de campañas <br><span style="color: var(--clr-primary);">gestionamos?</span></h2>
                    <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 500px; line-height: 1.6;">No todas las campañas funcionan igual. Elegimos y optimizamos los formatos adecuados según tu negocio, mercado y objetivos de facturación.</p>
                </div>
                
                <!-- Right Column -->
                <div style="display: flex; flex-direction: column;">
                    <!-- Step 1 -->
                    <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1; margin-top: -10px;">01</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Red de Búsqueda</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin-bottom: 12px;">Aparece en los primeros resultados cuando tus clientes buscan activamente tus productos o servicios.</p>
                            <ul style="font-size: 0.85rem; color: var(--clr-text); padding-left: 20px;">
                                <li>Investigación de keywords con intención de compra</li>
                                <li>Anuncios optimizados para conversión</li>
                                <li>Estrategias de puja basadas en datos</li>
                            </ul>
                        </div>
                    </div>
                    <!-- Step 2 -->
                    <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 30px; border-bottom: 1px solid #e5e7eb; padding-bottom: 40px; margin-bottom: 40px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1; margin-top: -10px;">02</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Performance Max y Shopping</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin-bottom: 12px;">Campañas automatizadas impulsadas por inteligencia artificial que permiten alcanzar a tus clientes en múltiples canales.</p>
                            <ul style="font-size: 0.85rem; color: var(--clr-text); padding-left: 20px;">
                                <li>Google Shopping para eCommerce</li>
                                <li>Anuncios en YouTube, Display, Gmail y Discover</li>
                                <li>Optimización automática basada en conversiones</li>
                            </ul>
                        </div>
                    </div>
                    <!-- Step 3 -->
                    <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 30px; padding-bottom: 10px;">
                        <div style="font-size: 5.5rem; font-weight: 900; color: var(--clr-accent); font-family: var(--font-heading); line-height: 1; margin-top: -10px;">03</div>
                        <div style="text-align: left; max-width: 320px;">
                            <h3 style="font-size: 1.2rem; font-family: var(--font-heading); color: var(--clr-contrast); margin-bottom: 8px;">Remarketing y Display</h3>
                            <p style="color: var(--clr-muted); font-size: 0.95rem; line-height: 1.5; margin-bottom: 12px;">Impactamos nuevamente a usuarios que ya interactuaron con tu marca para aumentar la probabilidad de conversión.</p>
                            <ul style="font-size: 0.85rem; color: var(--clr-text); padding-left: 20px;">
                                <li>Estrategias de remarketing dinámico</li>
                                <li>Segmentación por comportamiento</li>
                                <li>Creativos adaptados al embudo de ventas</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Nuestra Metodología Analítica (Cards layout) -->
        <section style="background: var(--clr-contrast); padding: 120px 0; margin-bottom: 100px;">
            <div class="container" style="color: #fff; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; margin-bottom: 24px; color: #fff;">Nuestra Metodología Analítica</h2>
                <p style="font-size: 1.1rem; opacity: 0.9; max-width: 700px; margin-bottom: 60px; line-height: 1.6;">Cada decisión que tomamos está respaldada por datos duros y analítica avanzada. No trabajamos con suposiciones ni corazonadas.</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px; width: 100%; text-align: center;">
                    <!-- Card 1 -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); padding: 50px 40px; border-radius: 24px; transition: transform var(--transition-fast);">
                        <div style="width: 70px; height: 70px; background: rgba(202, 254, 103, 0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 30px; font-size: 2rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-chart-pie"></i>
                        </div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 16px; color: #fff;">Auditoría y Setup en GA4</h4>
                        <p style="opacity: 0.8; font-size: 1.05rem; line-height: 1.6; margin-bottom: 20px;">Configuramos correctamente la medición desde el primer día para garantizar precisión absoluta.</p>
                        <ul style="font-size: 0.9rem; text-align: left; opacity: 0.9; padding-left: 20px;">
                            <li style="margin-bottom: 8px;">Google Analytics 4 (GA4) y Tag Manager</li>
                            <li style="margin-bottom: 8px;">Configuración de eventos y conversiones</li>
                            <li>Integraciones directas con CRM</li>
                        </ul>
                    </div>
                    <!-- Card 2 -->
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--clr-primary); padding: 50px 40px; border-radius: 24px; transition: transform var(--transition-fast);">
                        <div style="width: 70px; height: 70px; background: rgba(202, 254, 103, 0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 30px; font-size: 2rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-arrow-trend-up"></i>
                        </div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 16px; color: #fff;">Optimización del Costo por Lead</h4>
                        <p style="opacity: 0.8; font-size: 1.05rem; line-height: 1.6; margin-bottom: 20px;">Una campaña de Ads nunca se deja sola. Nuestro equipo monitorea y mejora el performance semanalmente.</p>
                        <ul style="font-size: 0.9rem; text-align: left; opacity: 0.9; padding-left: 20px;">
                            <li style="margin-bottom: 8px;">Análisis de datos en tiempo real</li>
                            <li style="margin-bottom: 8px;">Ajustes en segmentación, creativos y pujas</li>
                            <li>Escalamiento agresivo de campañas rentables</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- ¿Por qué elegir a Futurité? -->
        <section style="padding: 0 0 100px 0;">
            <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
                <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px;">¿Por qué elegir a Futurité como tu Agencia Google Partner?</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 800px; margin-bottom: 40px; line-height: 1.6;">Elegir una agencia de Google Ads implica confiar en quién gestiona tu inversión publicitaria. Nos convertimos en un aliado estratégico dentro de tu crecimiento digital, no solo en un proveedor de campañas.</p>
                <div style="display: flex; gap: 40px; flex-wrap: wrap; justify-content: center;">
                    <div style="width: 250px;">
                        <i class="fa-solid fa-bullseye" style="font-size: 2rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--clr-contrast); margin-bottom: 12px;">Estrategia B2B y B2C</h4>
                        <p style="font-size: 0.95rem; color: var(--clr-muted);">Enfoque estratégico orientado a resultados y KPIs claros.</p>
                    </div>
                    <div style="width: 250px;">
                        <i class="fa-solid fa-magnifying-glass-chart" style="font-size: 2rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--clr-contrast); margin-bottom: 12px;">Transparencia Total</h4>
                        <p style="font-size: 0.95rem; color: var(--clr-muted);">Acceso a dashboards y reportes de métricas en todo momento.</p>
                    </div>
                    <div style="width: 250px;">
                        <i class="fa-solid fa-certificate" style="font-size: 2rem; color: var(--clr-primary); margin-bottom: 16px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--clr-contrast); margin-bottom: 12px;">Equipo Certificado</h4>
                        <p style="font-size: 0.95rem; color: var(--clr-muted);">Especialistas validados por Google y en constante capacitación.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Preguntas Frecuentes (FAQ) -->
        <section class="faq-section" style="padding: 0 0 80px 0; background: var(--clr-base);">
            <div class="container">
                <div style="margin-bottom: 60px; text-align: center;">
                    <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast);">Preguntas Frecuentes sobre Inversión en Google Ads</h2>
                </div>

                <div class="faq-accordion">
                    <!-- FAQ Item 1 -->
                    <details class="faq-item" name="faq-group-ads">
                        <summary class="faq-question">¿Cuál es el presupuesto mínimo recomendado para iniciar?</summary>
                        <div class="faq-answer">
                            <p>Depende en gran medida de tu industria, competencia y objetivos de ventas. Sin embargo, recomendamos iniciar con una inversión diaria que permita generar datos suficientes (clics e interacciones) para optimizar las campañas de forma efectiva utilizando el aprendizaje automático de Google.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 2 -->
                    <details class="faq-item" name="faq-group-ads">
                        <summary class="faq-question">¿En cuánto tiempo empezaré a ver prospectos o ventas?</summary>
                        <div class="faq-answer">
                            <p>A diferencia del SEO, las campañas de Google Ads pueden generar resultados desde los primeros días de activación. Sin embargo, la optimización real para alcanzar el mejor Costo Por Lead (CPL) ocurre conforme se recopilan datos. Generalmente, los resultados más estables y escalables se observan a partir de la tercera semana.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 3 -->
                    <details class="faq-item" name="faq-group-ads">
                        <summary class="faq-question">¿Ustedes me entregan reportes de los resultados?</summary>
                        <div class="faq-answer">
                            <p>Sí, la transparencia es clave en nuestra metodología. Entregamos reportes periódicos y habilitamos un dashboard en tiempo real (Looker Studio) con métricas críticas como conversiones generadas, costo por lead (CPA), inversión consumida, y rendimiento general de las campañas y grupos de anuncios.</p>
                        </div>
                    </details>
                </div>
            </div>
        </section>

    </main>"""

content = re.sub(
    r'<!-- Main Content Wrapper \(White Background\) -->.*?</main>',
    main_new,
    content,
    flags=re.DOTALL
)

with open('agencia-de-google-ads.html', 'w', encoding='utf-8') as f:
    f.write(content)
