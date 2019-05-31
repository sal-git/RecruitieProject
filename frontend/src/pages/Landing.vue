<template>
   <div>
      <NavBar />
      <section class="hero is-fullheight">
         <div class="hero-body is-fullheight">
            <div class="container has-text-centered">
               <div class="columns is-vcentered">
                  <div class="column is-4 is-narrow">
                     <div class="columns is-vcentered">
                        <div class="column is-4 is-narrow">
                           <div style="position:relative;overflow:hidden">
                              <div style="width:100%;padding-bottom:100%"></div>
                              <picture>
                                 <img sizes="(max-width: 1000px) 100vw, 1000px" src="@/assets/img/human-resources.png" alt="" style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; object-fit: cover; object-position: center center; opacity: 1; transition: opacity 0.5s ease 0s;">
                              </picture>
                           </div>
                        </div>
                        <h1 class="title is-1 has-text-left-tablet"><span>Recruitie</span></h1>
                     </div>
                     <div class="has-text-left-tablet">
                        <h5 class="subtitle is-5 has-text-left-tablet"><span>A simple intuitative tool that helps you find the best candidate for any job.</span></h5>
                        <div class="columns is-centered is-vcentered">
                           <div class="column">
                              <div>
                                 <div><button class="button is-medium is-success is-rounded">Sign up</button><button class="button is-light is-medium is-rounded" href="javascript:;">Login</button></div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="column is-8 is-narrow">
                     <div style="position:relative;overflow:hidden">
                        <div style="width:100%;padding-bottom:68.4873949579832%"></div>
                        <picture>
                           <img sizes="(max-width: 1000px) 100vw, 1000px" src="https://www.psionline.com/wp-content/uploads/screenshot-placeholder-laptop.png" alt="" style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; object-fit: cover; object-position: center center; opacity: 1; transition: opacity 0.5s ease 0s;">
                        </picture>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
   </div>
</template>

<script>
    import NavBar from '../components/core/NavBar.vue'

    export default {
        name: 'LandingPage',
        components: {
            NavBar
        }
    }
</script>

<style lang="scss" scoped>

</style>