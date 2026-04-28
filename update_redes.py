import re

with open('agencia-de-redes-sociales.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = re.sub(
    r'<title>.*?</title>', 
    '<title>Agencia de Redes Sociales en Monterrey | Futurité</title>', 
    content
)

# Replace meta description
content = re.sub(
    r'<meta name="description"\s+content="[^"]*">',
    '<meta name="description" content="Agencia de Redes Sociales en Monterrey. Estrategias que generan ventas reales, contenido viral y campañas de performance (ROAS) en Meta, TikTok y LinkedIn.">',
    content
)

# Replace H1 Section
h1_section_new = """    <!-- H1 Header Section -->
    <section class="nosotros-header"
        style="position: relative; padding: 450px 0 100px; text-align: center; background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100%); color: var(--clr-base); overflow: hidden;">
        <div class="container" style="position: relative; z-index: 2;">
            <span
                style="display: block; font-size: 1.25rem; color: var(--clr-primary); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 16px;">Social Media Performance</span>
            <h1
                style="font-size: clamp(3rem, 5vw, 4rem); font-family: var(--font-heading); font-weight: 800; letter-spacing: -2px; margin-bottom: 0; line-height: 1.1; color: var(--clr-contrast);">
                Agencia de Redes Sociales en Monterrey:<br><span style="color: var(--clr-primary);">Estrategias que Generan Ventas Reales</span></h1>
        </div>
    </section>"""

content = re.sub(
    r'<!-- H1 Header Section -->.*?</section>' , 
    h1_section_new, 
    content, 
    flags=re.DOTALL
)

# Replace main block
main_new = """    <!-- Main Content Wrapper (White Background) -->
    <main
        style="background-color: var(--clr-base); border-radius: 0; padding: 60px 0 100px; box-shadow: 0 -20px 40px rgba(0,0,0,0.1);">

        <!-- Intro Content -->
        <section class="container" style="margin-top: 40px; margin-bottom: 80px;">
            <div style="max-width: 800px; margin: 0 auto; text-align: center; font-size: 1.25rem; line-height: 1.8; color: var(--clr-muted);">
                <p>En Futurité ayudamos a empresas a crecer en el mundo digital a través de estrategias de marketing digital enfocadas en resultados medibles. No solo gestionamos redes sociales: diseñamos sistemas que convierten tu presencia digital en leads, clientes y crecimiento sostenible.</p>
                <p style="margin-top: 24px;">Trabajamos con marcas que buscan escalar su negocio mediante contenido estratégico, campañas optimizadas y una ejecución alineada a objetivos comerciales reales.</p>
            </div>
        </section>

        <!-- Más allá de los Likes -->
        <section class="container" style="margin-bottom: 100px;">
            <div style="background: rgba(202, 254, 103, 0.1); border-radius: 32px; padding: 60px; display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 60px; align-items: center;">
                <div>
                    <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px; line-height: 1.2;">Más allá de los Likes:<br><span style="color: var(--clr-primary);">Enamoramos a tu audiencia y aumentamos tu ROAS</span></h2>
                    <p style="color: var(--clr-muted); font-size: 1.1rem; line-height: 1.7; margin-bottom: 24px;">Publicar por publicar no genera resultados. Hoy, las redes sociales deben funcionar como un canal de adquisición de clientes.</p>
                    <p style="color: var(--clr-muted); font-size: 1.1rem; line-height: 1.7; margin-bottom: 24px;">En nuestra agencia de marketing digital, transformamos tus redes en un activo estratégico:</p>
                    <ul style="list-style: none; padding: 0; margin: 0 0 32px 0;">
                        <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-primary); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Atraemos a la audiencia correcta</span></li>
                        <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-primary); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Generamos interés con contenido relevante</span></li>
                        <li style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 16px;"><i class="fa-solid fa-check" style="color: var(--clr-primary); margin-top: 6px;"></i><span style="color: var(--clr-muted); font-size: 1.1rem;">Convertimos interacciones en oportunidades de negocio</span></li>
                    </ul>
                    <p style="color: var(--clr-muted); font-size: 1.1rem; line-height: 1.7; font-weight: 600;">Nuestro enfoque combina creatividad, análisis de datos y optimización constante para mejorar tu retorno de inversión en cada campaña.</p>
                </div>
                <div style="position: relative;">
                    <div style="width: 100%; aspect-ratio: 1/1; background: url('https://images.unsplash.com/photo-1611162617474-5b21e879e113?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80') center/cover; border-radius: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.15);"></div>
                    <div style="position: absolute; bottom: -30px; right: -30px; background: var(--clr-primary); color: #fff; padding: 24px; border-radius: 20px; box-shadow: 0 10px 30px rgba(45, 79, 230, 0.3);">
                        <i class="fa-solid fa-rocket" style="font-size: 2.5rem;"></i>
                    </div>
                </div>
            </div>
        </section>

        <!-- Dominamos los Algoritmos -->
        <section class="container" style="margin-bottom: 100px;">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px;">Dominamos los Algoritmos Actuales<br>(Meta, TikTok, LinkedIn)</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 700px; margin: 0 auto;">El crecimiento en redes sociales depende de entender cómo funcionan los algoritmos modernos y cómo interactúan los usuarios con el contenido.</p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 40px; margin-bottom: 60px;">
                <!-- Platform 1 -->
                <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); text-align: center; transition: transform 0.3s ease;">
                    <div style="width: 70px; height: 70px; background: rgba(0,0,0,0.05); border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; color: var(--clr-contrast); font-size: 2rem;">
                        <i class="fa-brands fa-tiktok"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">TikTok</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Contenido enfocado en descubrimiento y alcance orgánico masivo.</p>
                </div>
                <!-- Platform 2 -->
                <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); text-align: center; transition: transform 0.3s ease;">
                    <div style="width: 70px; height: 70px; background: rgba(0,0,0,0.05); border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; color: #E1306C; font-size: 2rem;">
                        <i class="fa-brands fa-instagram"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">Instagram Reels</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Engagement profundo y posicionamiento de marca visualmente atractivo.</p>
                </div>
                <!-- Platform 3 -->
                <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); text-align: center; transition: transform 0.3s ease;">
                    <div style="width: 70px; height: 70px; background: rgba(0,0,0,0.05); border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; color: #0077B5; font-size: 2rem;">
                        <i class="fa-brands fa-linkedin-in"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">LinkedIn</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Generación de leads B2B y networking profesional de alto nivel.</p>
                </div>
                <!-- Platform 4 -->
                <div style="background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); text-align: center; transition: transform 0.3s ease;">
                    <div style="width: 70px; height: 70px; background: rgba(0,0,0,0.05); border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; color: #1877F2; font-size: 2rem;">
                        <i class="fa-brands fa-meta"></i>
                    </div>
                    <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 16px;">Meta Ads</h3>
                    <p style="color: var(--clr-muted); line-height: 1.6;">Conversión, remarketing y escalabilidad precisa de tus campañas.</p>
                </div>
            </div>

            <!-- Two Sub-sections -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px;">
                <div style="background: var(--clr-primary); color: #fff; padding: 50px; border-radius: 24px; position: relative; overflow: hidden;">
                    <i class="fa-solid fa-chart-pie" style="position: absolute; right: -20px; bottom: -20px; font-size: 10rem; color: #fff; opacity: 0.15; pointer-events: none;"></i>
                    <h3 style="font-size: 1.75rem; font-family: var(--font-heading); margin-bottom: 24px; position: relative; z-index: 2;">Campañas de Performance</h3>
                    <p style="font-size: 1.1rem; line-height: 1.6; opacity: 0.9; margin-bottom: 24px; position: relative; z-index: 2;">Diseñamos campañas orientadas a resultados concretos: leads, ventas o tráfico cualificado. Optimizamos continuamente variables clave como segmentación, creativos y presupuesto para mejorar métricas como:</p>
                    <ul style="list-style: none; padding: 0; margin: 0; position: relative; z-index: 2;">
                        <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Costo por adquisición (CPA)</span></li>
                        <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Retorno sobre inversión (ROAS)</span></li>
                        <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Tasa de conversión</span></li>
                    </ul>
                </div>
                <div style="background: var(--clr-contrast); color: #fff; padding: 50px; border-radius: 24px; position: relative; overflow: hidden;">
                    <i class="fa-solid fa-pen-nib" style="position: absolute; right: -20px; bottom: -20px; font-size: 10rem; color: #fff; opacity: 0.05; pointer-events: none;"></i>
                    <h3 style="font-size: 1.75rem; font-family: var(--font-heading); margin-bottom: 24px; position: relative; z-index: 2;">Estrategias Orgánicas y Creación de Contenido</h3>
                    <p style="font-size: 1.1rem; line-height: 1.6; opacity: 0.9; margin-bottom: 24px; position: relative; z-index: 2;">El contenido orgánico es clave para construir confianza y posicionar tu marca en redes sociales. Creamos contenido alineado a tu audiencia y objetivos:</p>
                    <ul style="list-style: none; padding: 0; margin: 0; position: relative; z-index: 2;">
                        <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Publicaciones estratégicas</span></li>
                        <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Videos cortos adaptados a formatos actuales</span></li>
                        <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-arrow-right" style="color: var(--clr-accent);"></i><span>Copy optimizado para engagement</span></li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Casos de Exito -->
        <section style="background: rgba(45, 79, 230, 0.03); padding: 100px 0; margin-bottom: 100px;">
            <div class="container">
                <div style="text-align: center; margin-bottom: 60px;">
                    <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px;">Casos de Éxito: Marcas que confían en Futurité</h2>
                    <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 700px; margin: 0 auto;">Trabajamos con empresas que buscan resultados medibles dentro de su estrategia digital. Nuestro enfoque se basa en datos, ejecución constante y mejora continua.</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px; text-align: center;">
                    <div style="background: #fff; padding: 50px 30px; border-radius: 24px; box-shadow: 0 15px 40px rgba(0,0,0,0.05);">
                        <span style="display: block; font-size: 4rem; font-weight: 900; color: var(--clr-primary); margin-bottom: 16px;">300%</span>
                        <h3 style="font-size: 1.25rem; color: var(--clr-contrast); margin-bottom: 16px;">Incremento del ROAS</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Multiplicamos el retorno de inversión de campañas e-commerce mediante segmentación avanzada.</p>
                    </div>
                    <div style="background: #fff; padding: 50px 30px; border-radius: 24px; box-shadow: 0 15px 40px rgba(0,0,0,0.05);">
                        <span style="display: block; font-size: 4rem; font-weight: 900; color: var(--clr-primary); margin-bottom: 16px;">45%</span>
                        <h3 style="font-size: 1.25rem; color: var(--clr-contrast); margin-bottom: 16px;">Reducción de Costo por Lead</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Optimizamos las rutas de conversión y los creativos B2B para captar prospectos de mayor calidad a menor precio.</p>
                    </div>
                    <div style="background: #fff; padding: 50px 30px; border-radius: 24px; box-shadow: 0 15px 40px rgba(0,0,0,0.05);">
                        <span style="display: block; font-size: 4rem; font-weight: 900; color: var(--clr-primary); margin-bottom: 16px;">10x</span>
                        <h3 style="font-size: 1.25rem; color: var(--clr-contrast); margin-bottom: 16px;">Aumento en Tráfico Orgánico</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Disparamos el alcance de marca gracias a formatos de video vertical (Reels y TikToks) diseñados para el algoritmo.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Metodología en 5 pasos -->
        <section class="container" style="margin-bottom: 100px;">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast); margin-bottom: 24px;">Nuestra Metodología de Trabajo en 5 Pasos</h2>
                <p style="font-size: 1.1rem; color: var(--clr-muted); max-width: 700px; margin: 0 auto;">Nuestro proceso está diseñado para garantizar claridad, control y resultados desde el inicio.</p>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 30px; max-width: 800px; margin: 0 auto;">
                <!-- Step 1 -->
                <div style="display: flex; align-items: flex-start; gap: 30px; background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <div style="width: 60px; height: 60px; flex-shrink: 0; background: var(--clr-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: var(--clr-contrast);">1</div>
                    <div>
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 12px;">Auditoría y Análisis de Marca</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Evaluamos tu presencia actual, analizamos a la competencia y detectamos áreas de oportunidad dentro del mercado para definir el punto de partida.</p>
                    </div>
                </div>
                <!-- Step 2 -->
                <div style="display: flex; align-items: flex-start; gap: 30px; background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <div style="width: 60px; height: 60px; flex-shrink: 0; background: var(--clr-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: var(--clr-contrast);">2</div>
                    <div>
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 12px;">Estrategia de Comunicación</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Definimos el mensaje central, el tono de voz de la marca y el enfoque estratégico que conectará de manera auténtica con tu audiencia objetivo.</p>
                    </div>
                </div>
                <!-- Step 3 -->
                <div style="display: flex; align-items: flex-start; gap: 30px; background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <div style="width: 60px; height: 60px; flex-shrink: 0; background: var(--clr-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: var(--clr-contrast);">3</div>
                    <div>
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 12px;">Producción Creativa (Diseño y Video)</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Desarrollamos contenido visual y creativo de alto impacto, nativamente adaptado a los formatos de cada plataforma (Stories, Reels, Carruseles).</p>
                    </div>
                </div>
                <!-- Step 4 -->
                <div style="display: flex; align-items: flex-start; gap: 30px; background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <div style="width: 60px; height: 60px; flex-shrink: 0; background: var(--clr-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: var(--clr-contrast);">4</div>
                    <div>
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 12px;">Pauta y Distribución Estratégica</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Lanzamos campañas de anuncios pagados (Ads) rigurosamente segmentadas y optimizadas para maximizar el alcance y detonar conversiones.</p>
                    </div>
                </div>
                <!-- Step 5 -->
                <div style="display: flex; align-items: flex-start; gap: 30px; background: #fff; padding: 40px; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <div style="width: 60px; height: 60px; flex-shrink: 0; background: var(--clr-accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: var(--clr-contrast);">5</div>
                    <div>
                        <h3 style="font-size: 1.5rem; color: var(--clr-contrast); margin-bottom: 12px;">Analítica y Optimización Continua</h3>
                        <p style="color: var(--clr-muted); line-height: 1.6; margin: 0;">Medimos los resultados mediante dashboards en tiempo real y ajustamos la estrategia proactivamente para escalar el rendimiento y el ROAS mes a mes.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ¿Por qué elegirnos? -->
        <section class="container" style="margin-bottom: 100px;">
            <div style="background: var(--clr-contrast); border-radius: 32px; padding: 80px 60px; color: #fff; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; margin-bottom: 24px; color: #fff;">¿Por qué elegirnos como tu equipo de Social Media?</h2>
                <p style="font-size: 1.1rem; opacity: 0.9; max-width: 700px; margin-bottom: 60px; line-height: 1.6;">Elegir una agencia de marketing digital implica confiar en un equipo que entienda tu negocio y se enfoque en resultados. Nos integramos como un aliado estratégico dentro de tu empresa para impulsar tu crecimiento en el entorno digital.</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; width: 100%;">
                    <div>
                        <div style="width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-chess-knight"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px;">Estrategias Personalizadas</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6;">No usamos plantillas genéricas, construimos a tu medida.</p>
                    </div>
                    <div>
                        <div style="width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-chart-line"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px;">Métricas Reales</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6;">Nos enfocamos en leads y ventas, no solo en interacciones vanidosas.</p>
                    </div>
                    <div>
                        <div style="width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-database"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px;">Decisiones con Datos</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6;">Optimización constante basada en analítica web y performance.</p>
                    </div>
                    <div>
                        <div style="width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.5rem; color: var(--clr-accent);">
                            <i class="fa-solid fa-comments"></i>
                        </div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 12px;">Comunicación Clara</h4>
                        <p style="opacity: 0.8; font-size: 1rem; line-height: 1.6;">Reportes transparentes y seguimiento continuo de cada campaña.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Preguntas Frecuentes (FAQ) -->
        <section class="faq-section" style="padding: 0 0 40px 0; background: var(--clr-base);">
            <div class="container">
                <div style="margin-bottom: 60px; text-align: center;">
                    <h2 style="font-size: 2.5rem; font-family: var(--font-heading); font-weight: 800; color: var(--clr-contrast);">Preguntas Frecuentes sobre el Manejo de Redes Sociales</h2>
                </div>

                <div class="faq-accordion">
                    <!-- FAQ Item 1 -->
                    <details class="faq-item" name="faq-group-rrss">
                        <summary class="faq-question">¿En qué redes sociales debería estar mi negocio?</summary>
                        <div class="faq-answer">
                            <p>Depende de tu industria, público objetivo y objetivos comerciales. Analizamos tu mercado para definir las plataformas que generarán mayor retorno dentro de tu estrategia de marketing digital, asegurando no desperdiciar recursos en canales irrelevantes.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 2 -->
                    <details class="faq-item" name="faq-group-rrss">
                        <summary class="faq-question">¿Ustedes crean los diseños y videos para las campañas?</summary>
                        <div class="faq-answer">
                            <p>Sí. Nos encargamos de la producción integral de contenido visual de alta calidad, incluyendo diseño gráfico profesional y edición de video dinámico (Reels, TikToks), adaptado específicamente a los formatos nativos de cada red social y objetivo de campaña.</p>
                        </div>
                    </details>

                    <!-- FAQ Item 3 -->
                    <details class="faq-item" name="faq-group-rrss">
                        <summary class="faq-question">¿Cuál es la diferencia entre pauta y contenido orgánico?</summary>
                        <div class="faq-answer">
                            <p>El contenido orgánico construye presencia de marca a largo plazo, confianza y comunidad. La pauta (publicidad pagada) permite acelerar resultados, alcanzar nuevas audiencias hiper-segmentadas y generar conversiones directas de forma más rápida. Ambos trabajan juntos dentro de una estrategia integral de marketing digital para un crecimiento escalable.</p>
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

with open('agencia-de-redes-sociales.html', 'w', encoding='utf-8') as f:
    f.write(content)
