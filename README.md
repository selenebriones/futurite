# Futurité - Minimalismo de Alto Rendimiento 🚀

Bienvenido al repositorio maestro de la nueva Landing Page de **Futurité**, una agencia enfocada en la creación y escalamiento de marcas a través de arquitectura y ecosistemas digitales de altísimo rendimiento.

## 🌌 Filosofía de Diseño

Este proyecto fue desarrollado bajo el concepto estético y funcional de **"Minimalismo de Alto Rendimiento"**, buscando mantener una velocidad de carga máxima, interfaces interactivas elegantes, y código ultra limpio sin depender de frameworks o librerías pesadas (como Tailwind o Bootstrap). Todo el esquema de diseño está montado desde cero con variables nativas, ofreciendo lujo y precisión técnica.

## 🛠 Stack Tecnológico

- **HTML5:** Estructura semántica corporativa y limpia.
- **CSS3 Puro:** Sistema robusto basado en `CSS Grid` y `Flexbox`. 
- **Animaciones Nativas (No-JS):** Menús desplegables complejos, interacciones de `hover` con sombras vectoriales, transiciones de menús de acordeón y rediseño nativo del color de los vectores.
- **Vanilla JavaScript:** Lógica ligera para el comportamiento estricto y rastreo del DOM (`script.js`).

## 📁 Estructura del Proyecto

```text
/Futurite
├── index.html           # Estructura del DOM, SEO semántico y componentes
├── style.css            # Arquitectura global de UI, Design System y Media Queries
├── script.js            # Comportamiento ligero del lado del cliente
└── /assets              # Repositorio de recursos pesados (Logos, imágenes .webp y SVGs)
```

## 🎨 Token de Diseño (CSS Variables)

El proyecto utiliza un sistema cerrado de propiedades personalizadas para garantizar consistencia del corporativo en cualquier parte del código:

- `--clr-base`: Fondo Blanco / Modos claros
- `--clr-text`: Texto predeterminado
- `--clr-primary`: Azul Eléctrico (Marca corporativa principal)
- `--clr-contrast`: Deep Space Navy (`#0F172A` o `#050a16` utilizado en el megamedio de alto impacto)
- `--clr-accent`: Verde Lima de interacción hiperactiva (`#CAFE67`)
- `--font-heading`: Tipografía principal (Títulos y botones)
- `--font-body`: Tipografía de lectura (Párrafos e UI)

## ⚡️ Componentes Clave

- **Menú Desplegable (CSS):** Estructura multi-nivel animada exclusivamente en la capa de estilos usando selectores de anidamiento.
- **Acordeón FAQ:** Optimizado para interactividad suave y táctil controlada puramente a través de jerarquía semántica.
- **Smart Footer:** Layout experimental construido en sistema Grid de `1fr 1fr 1.4fr` para ordenar módulos altamente saturados (Contacto, Legal, Enlaces Rápidos y Logos), optimizado para renderizarse responsivo en pantallas móviles.

## 📐 Reglas de Mantenimiento

Para cualquier modificación futura al portal:
1. **No inyectar estilos en-linea:** Salvo excepciones atómicas necesarias, utilizar `style.css` de manera modularizada.
2. **Priorizar el Rendimiento Web:** Todas las imágenes que entren a `/assets` deben estar prioritariamente optimizadas bajo formatos `.webp`.
3. **Respetar la semántica:** Todo Call-to-Action debe mapear al color de acento (`var(--clr-accent)`). Todos los textos oscuros de base operan bajo jerarquía visual modularizada.

---

*Diseñado para redefinir el estándar digital.*
&copy; 2026 Futurité. Todos los derechos reservados.
