import Vue from 'vue'
import VueRouter from 'vue-router'

import ExampleComponent from '@/components/ExampleComponent.vue'
import DashboardPage from '@/pages/Dashboard.vue'
import LandingPage from '@/pages/Landing.vue'


const routes = [
  {path: '/dashboard', component: DashboardPage},
  {path: '/', component: LandingPage}
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})


export default router
