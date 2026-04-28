/**
 * Futurité 2026 - Interactive Scripts
 */

document.addEventListener('DOMContentLoaded', () => {

    /* --- 1. Reveal Animations on Scroll --- */
    const revealElements = document.querySelectorAll('[data-reveal]');
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));

    /* --- 2. Number Counter Animation --- */
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // The lower the slower

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const updateCount = () => {
                    const target = +counter.getAttribute('data-target');
                    const count = +counter.innerText;
                    
                    // Lower inc to slow and higher to speed up
                    const inc = target / speed;

                    if (count < target) {
                        counter.innerText = Math.ceil(count + inc);
                        setTimeout(updateCount, 20);
                    } else {
                        counter.innerText = target;
                    }
                };
                updateCount();
                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => counterObserver.observe(counter));

    /* --- 3. Marquee Duplication for Infinite Loop --- */
    const marqueeTrack = document.querySelector('.marquee-track');
    const marqueeContent = document.querySelector('.marquee-content');
    
    if (marqueeTrack && marqueeContent) {
        // Clone the content twice to ensure there's enough material to loop flawlessly
        const clone1 = marqueeContent.cloneNode(true);
        const clone2 = marqueeContent.cloneNode(true);
        
        marqueeTrack.appendChild(clone1);
        marqueeTrack.appendChild(clone2);
    }

    /* --- 4. Navbar Blur on Scroll --- */
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.05)';
        } else {
            navbar.style.boxShadow = 'none';
        }
    });
    /* --- 5. Mobile Menu Toggle --- */
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
        
        // Auto-close menu when a link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileMenuBtn.querySelector('i').classList.add('fa-bars');
                mobileMenuBtn.querySelector('i').classList.remove('fa-xmark');
            });
        });
    }

    /* --- 6. Contact Form Submission --- */
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerText;
            submitBtn.innerText = "Enviando...";
            submitBtn.disabled = true;

            const payload = {
                nombre: document.getElementById('formNombre').value,
                apellidos: document.getElementById('formApellidos').value,
                correo: document.getElementById('formCorreo').value,
                telefono: document.getElementById('formTelefono').value,
                empresa: document.getElementById('formEmpresa').value,
                mensaje: document.getElementById('formMensaje').value,
                origen: "https://futurite.mx/"
            };

            try {
                const response = await fetch("https://n8n.ongoing.mx/webhook/aa97f360-8b05-45cc-98d4-8f576cd710c8", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "futurite": "Huo0lpaw."
                    },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    alert("¡Mensaje enviado con éxito!");
                    contactForm.reset();
                } else {
                    alert("Ocurrió un error al enviar el mensaje. Por favor intenta de nuevo.");
                }
            } catch (error) {
                console.error("Error al enviar el formulario:", error);
                alert("Error de conexión. Por favor intenta de nuevo más tarde.");
            } finally {
                submitBtn.innerText = originalBtnText;
                submitBtn.disabled = false;
            }
        });
    }
});
