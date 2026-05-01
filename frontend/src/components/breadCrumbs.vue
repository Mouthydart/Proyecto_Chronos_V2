<template>
<nav class="flex" aria-label="Breadcrumb">
  <ol class="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse">

    <li class="inline-flex items-center">
      <router-link to="/" class="inline-flex items-center text-sm font-medium text-blue-600 hover:text-purple-600">
        <svg class="w-3 h-3 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z"/>
        </svg>
        Inicio
      </router-link>
    </li>
    
    <li class="rtl:rotate-180">
      <svg class="w-3 h-3 text-gray-400 mx-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
      </svg>
    </li>

   <li class="inline-flex items-center">
      <router-link to="/knowUs" class="inline-flex items-center text-sm font-medium text-blue-600 hover:text-purple-600">
        <svg class="w-3 h-3 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
        </svg>
        Conocenos
      </router-link>
    </li>

    <li>
      <router-link to="/experiences" class="flex items-center">
        <svg class="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
        </svg>
        <a href="#" class="ms-1 text-sm font-medium text-blue-600 hover:text-purple-600">
          <svg class="w-3 h-3 me-2.5 inline" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 18">
            <path d="M5 4h1a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm0 4H3v2h2v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1H6V7a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1h3Zm11-4h1a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm-1 4h-2v2h2v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1h-1V7a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v1h1Z"/>
          </svg>
          Experiencias
        </a>
      </router-link>
    </li>

    <li aria-current="page">
      <router-link to="/contactUs"class="flex items-center">
        <svg class="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
        </svg>
        <a href="#" class="ms-1 text-sm font-medium text-blue-600 hover:text-purple-600">
          <svg class="w-3 h-3 me-2.5 inline" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 16">
            <path d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"/>
            <path d="M11.241 9.817c-.36.275-.801.425-1.242.425s-.881-.15-1.242-.425L.41 2.441A2 2 0 0 0 0 3.218V15a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V3.219a2 2 0 0 0-.411-.777L11.241 9.817Z"/>
          </svg>
          Contactanos
        </a>
       </router-link>
    </li>

    <li aria-current="page">
      <router-link to="/faq" class="flex items-center">
        <svg class="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
        </svg>
        <span class="ms-1 text-sm font-medium text-blue-600 hover:text-purple-600">
          <svg class="w-3 h-3 me-2.5 inline" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
            <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z"/>
            <path d="M16 3a2 2 0 0 0-2-2h-3.328a2 2 0 0 1-1.664-.897L9.366.13a2 2 0 0 0-2.454 0l-.306.305A1.972 1.972 0 0 1 5.672 1H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h4.5v1.44a2.98 2.98 0 0 0 1.545 2.536 1 1 0 0 0 .438.106h.023c.319 0 .6-.183.74-.475l.08-.198a.63.63 0 0 1 1.058-.093l.87 1.258a1 1 0 0 0 1.5.025l.035-.043a.5.5 0 0 1 .412-.132l.711.178c.307.078.67-.19.6-.5l-.334-1.332a.5.5 0 0 1 .15-.494l.43-1.026c.289-.691.688-1.55 1.13-2.09l.135-.164c.266-.318.175-.769-.193-.993l-1.02-.635a.5.5 0 0 1-.22-.606l.162-.485a.5.5 0 0 1 .536-.341l1.164.195a.5.5 0 0 0 .546-.388l.196-1.163A2 2 0 0 0 16 9.5V3ZM7.922 17.5a.997.997 0 0 1-1.341-.749l-.025-.136.035-.19.032-.132c.071-.24.238-.415.426-.505l.394-.191.077-.037.067-.032h.003l.08-.038h.001l.142-.068a.5.5 0 0 1 .448.016l.487.234c.057.027.135.039.227.039.255 0 .432-.137.495-.311l.006-.017.064-.176.01-.025.011-.03c.01-.027.01-.059.01-.091 0-.17-.116-.299-.304-.413l-1.385-.82a1.5 1.5 0 0 1-.58-.87l-.022-.119-.011-.06-.011-.061c-.01-.068-.009-.136.002-.204.01-.068.03-.13.064-.188.034-.058.077-.11.13-.153.053-.043.116-.078.188-.103.072-.025.152-.039.239-.039.112 0 .227.021.34.062.113.04.225.1.332.179.108.08.213.175.312.285.1.11.196.23.284.364.18.267.31.57.387.893l.004.016.035.159.01.047.005.021.003.013c.002.007.002.016.002.025a.5.5 0 0 1-.413.568l-1.164.195a.5.5 0 0 0-.546.388l-.196 1.163a1 1 0 0 1-1.073.743Z"/>
          </svg>
          FAQ
        </span>
      </router-link>
    </li>
    
  </ol>
</nav>
</template>
