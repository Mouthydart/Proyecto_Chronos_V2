<template>
  <div class="w-full min-h-screen relative flex flex-col items-center pt-8">
    <breadCrumbs class="absolute top-0 left-0 p-4" />

    <div
      class="mt-16 mb-16 inline-block text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300"
    >
      Chronos
    </div>

    <div class="text-center w-full">
      <h1 class="text-3xl md:text-4xl font-bold text-gray-800">
        Lo que dicen nuestros usuarios
      </h1>
      <p class="text-sm md:text-base text-gray-500 mt-4 mb-16">
        Únete a miles de estudiantes que transformaron la gestión de su tiempo con
        nosotros.
      </p>

      <div class="relative w-full max-w-screen-xl mx-auto flex justify-center items-center mt-16 px-4">
        
        <button
          @click="goPrev"
          :disabled="totalPages <= 1"
          class="absolute left-4 md:-left-16 lg:-left-20 z-10 p-3 rounded-full bg-white shadow-lg hover:bg-gray-100 transition-colors duration-200 focus:outline-none disabled:opacity-50"
          aria-label="Página anterior de testimonios"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 text-gray-700"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>

        <div 
            class="flex flex-nowrap justify-center gap-25 text-left transition-transform duration-500 ease-in-out "
        >
          <div
            v-for="(testimonial, index) in visibleTestimonials"
            :key="currentPage * ITEMS_PER_PAGE + index"
            class="w-80 flex-shrink-0 flex flex-col items-start border border-gray-200 p-6 rounded-xl bg-gray-50 shadow-xl hover:shadow-xl "
          >
            <svg
              width="44"
              height="40"
              viewBox="0 0 44 40"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M33.172 5.469q2.555 0 4.547 1.547a7.4 7.4 0 0 1 2.695 4.007q.47 1.711.469 3.61 0 2.883-1.125 5.86a22.8 22.8 0 0 1-3.094 5.577 33 33 0 0 1-4.57 4.922A35 35 0 0 1 26.539 35l-3.398-3.398q5.296-4.243 7.218-6.563 1.946-2.32 2.016-4.617-2.86-.329-4.781-2.461-1.923-2.133-1.922-4.992 0-3.117 2.18-5.297 2.202-2.203 5.32-2.203m-20.625 0q2.555 0 4.547 1.547a7.4 7.4 0 0 1 2.695 4.007q.47 1.711.469 3.61 0 2.883-1.125 5.86a22.8 22.8 0 0 1-3.094 5.577 33 33 0 0 1-4.57 4.922A35 35 0 0 1 5.914 35l-3.398-3.398q5.296-4.243 7.218-6.563 1.946-2.32 2.016-4.617-2.86-.329-4.781-2.461-1.922-2.133-1.922-4.992 0-3.117 2.18-5.297 2.202-2.203 5.32-2.203"
                fill="#2563EB"
              />
            </svg>

            <div class="flex items-center justify-center mt-3 gap-1">
              <svg
                v-for="star in 5"
                :key="'star-' + (currentPage * ITEMS_PER_PAGE + index) + star"
                width="16"
                height="15"
                viewBox="0 0 16 15"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M7.524.464a.5.5 0 0 1 .952 0l1.432 4.41a.5.5 0 0 0 .476.345h4.637a.5.5 0 0 1 .294.904L11.563 8.85a.5.5 0 0 0-.181.559l1.433 4.41a.5.5 0 0 1-.77.559L8.294 11.65a.5.5 0 0 0-.588 0l-3.751 2.726a.5.5 0 0 1-.77-.56l1.433-4.41a.5.5 0 0 0-.181-.558L.685 6.123A.5.5 0 0 1 .98 5.22h4.637a.5.5 0 0 0 .476-.346z"
                  :fill="star <= testimonial.rating ? '#FF532E' : '#D1D5DB'"
                />
              </svg>
            </div>

            <p class="text-sm mt-3 text-gray-500">
              {{ testimonial.quote }}
            </p>
            <div class="flex items-center gap-3 mt-4">
              <img
                class="h-12 w12 rounded-full object-cover"
                :src="testimonial.authorImage"
                :alt="testimonial.authorName"
              />
              <div>
                <h2 class="text-lg text-gray-900 font-medium">
                  {{ testimonial.authorName }}
                </h2>
                <p class="text-sm text-gray-500">
                  {{ testimonial.authorTitle }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <button
          @click="goNext"
          :disabled="totalPages <= 1"
          class="absolute right-4 md:-right-16 lg:-right-20 z-10 p-3 rounded-full bg-white shadow-lg hover:bg-gray-100 transition-colors duration-200 focus:outline-none disabled:opacity-50"
          aria-label="Página siguiente de testimonios"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 text-gray-700"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M9 5l7 7-7 7"
            />
          </svg>
        </button>
      </div>
      
      <div class="flex justify-center mt-8 gap-2">
        <span
          v-for="(page, index) in totalPages"
          :key="'dot-' + index"
          @click="currentPage = index"
          :class="{
            'bg-blue-600': index === currentPage,
            'bg-gray-300 hover:bg-gray-400': index !== currentPage,
          }"
          class="h-3 w-3 rounded-full cursor-pointer transition-colors duration-300"
          :aria-label="'Ir a la página ' + (index + 1)"
        ></span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import breadCrumbs from '../components/breadCrumbs.vue';


const testimonials = ref([
    {
        quote: "Chronos transformó mi caos académico en orden. Antes perdía horas planificando, ahora es automático. ¡Mis notas han mejorado notablemente!",
        authorName: "Donald Jackman",
        authorTitle: "Estudiante de Ingeniería",
        rating: 5,
        authorImage: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=100",
    },
    {
        quote: "La herramienta es intuitiva y el diseño es limpio. Pude integrarla a mi rutina de estudio desde el primer día. Lo mejor es el seguimiento de progreso.",
        authorName: "Richard Nelson",
        authorTitle: "Estudiante de Arquitectura",
        rating: 4,
        authorImage: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?q=80&w=100",
    },
    {
        quote: "Como madre universitaria, cada minuto cuenta. Chronos me permite balancear mis estudios con la vida familiar sin sentir que sacrifico mi tiempo. ¡Muy recomendable!",
        authorName: "Martha Giraldo",
        authorTitle: "Estudiante de Posgrado",
        rating: 5,
        authorImage: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=100&h=100&auto=format&fit=crop",
    },
    {
        quote: "¡Simplemente lo mejor para organizar mis entregas! El sistema de alertas me salvó de reprobar mi materia más difícil.",
        authorName: "Samuel Pérez",
        authorTitle: "Estudiante de Diseño Gráfico",
        rating: 5,
        authorImage: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=100&h=100&auto=format&fit=crop",
    },
    {
        quote: "La curva de aprendizaje es casi nula, y los resultados son inmediatos. Finalmente tengo una visión clara de mi carga académica semanal.",
        authorName: "Laura Montes",
        authorTitle: "Estudiante de Medicina",
        rating: 4,
        authorImage: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=100&h=100&auto=format&fit=crop",
    },
]);

const ITEMS_PER_PAGE = 3;
const currentPage = ref(0);

const totalPages = computed(() => Math.ceil(testimonials.value.length / ITEMS_PER_PAGE));

const visibleTestimonials = computed(() => {
    const start = currentPage.value * ITEMS_PER_PAGE;
    const end = start + ITEMS_PER_PAGE;
    return testimonials.value.slice(start, end);
});

const goPrev = () => {
    currentPage.value = (currentPage.value - 1 + totalPages.value) % totalPages.value;
};

const goNext = () => {
    currentPage.value = (currentPage.value + 1) % totalPages.value;
};
</script>