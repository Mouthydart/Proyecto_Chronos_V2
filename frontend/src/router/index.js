import { createRouter, createWebHistory } from 'vue-router'
import PaginaInicio from '../views/paginaInicio.vue'
import KnowUs from '../views/knowUs.vue'
import Experiences from '../views/experiences.vue'
import ContacUs from '../views/contactUs.vue'
import FAQ from '../views/faq.vue'
import LoginView from '../views/loginView.vue'
import CreateAccount from '../views/createAccount.vue'
import ForgotPassword from '../views/forgotPassword.vue'
import ModalPassword from '../views/modalPassword.vue'
import SectionAcademy from '../views/sectionAcademy.vue'
import SectionHealth from '../views/sectionHealth.vue'
import SectionFinances from '../views/sectionFinance.vue'
import SectionLeisure from '../views/sectionLeisure.vue'
import Calendar from '../views/calendario.vue'
import CreateAcademy from '../views/createSecAca.vue'
import CreateHealth from '../views/createSecSal.vue'
import CreateFinance from '../views/createSecFin.vue'
import CreateLeisure from '../views/createSecLei.vue'
import EditAcademy from '../views/editSecAca.vue'
import EditHealth from '../views/editSecSal.vue'
import EditFinance from '../views/editSecFin.vue'
import EditLeisure from '../views/editSecLei.vue'
import UserProfile from '../views/UserProfile.vue'
import { requireAuth, redirectIfAuthenticated } from './guards.js'

const routes = [
  { path: '/', component: LoginView, beforeEnter: redirectIfAuthenticated }, // La vista de Login
  { path: '/home', component: PaginaInicio, beforeEnter: requireAuth }, // La vista de Home/Sidebar principal
  { path: '/knowUs', component: KnowUs, beforeEnter: requireAuth }, //  Conocenos
  { path: '/experiences', component: Experiences, beforeEnter: requireAuth }, // Experiencias
  { path: '/contactUs', component: ContacUs, beforeEnter: requireAuth }, // Contactanos
  { path: '/faq', component: FAQ, beforeEnter: requireAuth }, // FAQ
  { path: '/createAccount', component: CreateAccount, beforeEnter: redirectIfAuthenticated }, // La vista de Home/Sidebar principal
  { path: '/forgotPassword', component: ForgotPassword, beforeEnter: redirectIfAuthenticated }, // La vista de recuperar contraseña
  { path: '/modalPassword', component: ModalPassword, beforeEnter: requireAuth }, // La vista del modal recuperar contraseña
  { path: '/estudio', component: SectionAcademy, beforeEnter: requireAuth }, // La seccion de estudio
  { path: '/salud', component: SectionHealth, beforeEnter: requireAuth }, // La seccion de salud
  { path: '/finanzas', component: SectionFinances, beforeEnter: requireAuth }, // La seccion de finanzas
  { path: '/tiempo-libre', component: SectionLeisure, beforeEnter: requireAuth }, // La seccion de tiempo libre
  { path: '/calendario', component: Calendar, beforeEnter: requireAuth }, // La seccion de tiempo libre
  { path: '/createAcademy', component: CreateAcademy, beforeEnter: requireAuth }, // Crear registro academico
  { path: '/createHealth', component: CreateHealth, beforeEnter: requireAuth }, // Crear registro Salud
  { path: '/createFinance', component: CreateFinance, beforeEnter: requireAuth }, // Crear registro Finanzas
  { path: '/createLeisure', component: CreateLeisure, beforeEnter: requireAuth }, // Crear registro Tiempo libre
  { path: '/editAcademy/:id', name: 'EditAcademy', component: EditAcademy, beforeEnter: requireAuth },// Editar registro academico
  { path: '/editHealth/:id', name: 'EditHealth', component: EditHealth, beforeEnter: requireAuth },// Editar registro salud
  { path: '/editFinance/:id', name: 'EditFinance', component: EditFinance, beforeEnter: requireAuth },// Editar registro finanzas
  { path: '/editLeisure/:id', name: 'EditLeisure', component: EditLeisure, beforeEnter: requireAuth },// Editar registro tiempo libre
  { path: '/profile', component: UserProfile, beforeEnter: requireAuth }, // Perfil del usuario
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
