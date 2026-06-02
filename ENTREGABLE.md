# Entregable: LocalRank

¡Hola! Aquí tienes la web profesional para LocalRank, diseñada y desarrollada con un enfoque total en la conversión y la verticalidad.

## 🛠️ Stack Elegido

Para asegurar la máxima velocidad, optimización SEO y escalabilidad, la web está desarrollada con **Astro** y **Tailwind CSS**.
La salida de este proyecto es 100% estática (SSG - Static Site Generation), perfecta para ser desplegada gratuitamente y con un rendimiento excelente en **Cloudflare Pages**.

No he utilizado ningún framework pesado que renderice en el cliente (cero client-side React), por lo que Google leerá cada página instantáneamente. Las interacciones esenciales (como el buscador principal) utilizan JavaScript vanilla muy ligero.

## 🎨 Decisiones de Diseño Principales

1. **UX inspirada en Booking/eDreams**:
   El buscador no es un adorno, es el núcleo de la navegación en la Home. He diseñado un hero amplio y claro donde la acción principal ("Ver oportunidades") destaca sobre todo lo demás con un fuerte contraste. Al rellenar "Sector" y "Ciudad" (que cuentan con autocompletado y listas desplegables), el usuario es redirigido directamente a la página cruzada correspondiente, sintiendo que el servicio es exclusivo para su situación.
2. **Jerarquía Visual y Limpieza**:
   He apostado por espaciados generosos (Tailwind `py-16`, `py-24`), colores que transmiten confianza (azul oscuro profundo, blanco, detalles en verde esmeralda para CTAs) y tipografía moderna y muy legible.
3. **Coherencia y Consistencia**:
   Todos los CTAs principales llevan a `/valoracion`, que es la página clave. Mismo header, footer, estilo de tarjetas y botones en todo el site.
4. **Respeto por la Lengua**:
   Se han revisado los textos para asegurar un español de España perfecto (tildes correctas, uso de '¿' y '¡', sin anglicismos innecesarios).

## 🚀 Cómo escalar a más cruces Sector × Ciudad

He generado dinámicamente un cruce para **todos los sectores y ciudades disponibles en los datos**, así que ya tienes listas **56 URLs indexables cruzadas** (8 sectores × 7 ciudades).

Para escalar aún más:
1. Simplemente abre el archivo `src/data/content.ts`.
2. Añade un nuevo sector al array `sectors` o una nueva ciudad al array `cities`.
3. Al ejecutar el comando de build (`npm run build`), Astro generará **automáticamente** las nuevas páginas individuales de ciudad/sector, además de todas las combinaciones cruzadas correspondientes para esos nuevos datos sin que tengas que programar ni una sola línea nueva de código.

## 📦 Instrucciones para Desplegar en Cloudflare Pages

1. Sube este repositorio a tu cuenta de GitHub/GitLab.
2. En tu panel de Cloudflare Pages, crea un nuevo proyecto conectándolo a tu repositorio.
3. **Framework preset**: Selecciona `Astro`.
4. **Build command**: `npm run build`
5. **Build output directory**: `dist`
6. ¡Haz clic en *Save and Deploy*!

Tu web estará funcionando al instante.
