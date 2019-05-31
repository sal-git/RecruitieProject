<template>
    <div>
        <section class="hero is-primary">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        {{ lead.title }}
                    </h1>
                    <h2 class="subtitle">
                         {{ lead.desc }} - {{ lead.location }}
                    </h2>
                </div>
            </div>
        </section>
        <br>
        <section>
            <NoteForm />
        </section>
        <br>
        <br>
        <section>
            <LeadNotes :rows="rowNotes" />
        </section>
    </div>
</template>

<script>
    import LeadNotes from './NoteList.vue';
    import NoteForm from './notes/NoteForm.vue';
    import axios from 'axios'


    export default {
        name: "LeadView",
        props: ['lead', ],
        data(){
            return {
                rowNotes: []
            }
        },
        components: {
            LeadNotes,
            NoteForm
        },
        mounted() {
            this.getNotes()
            // this.$on('refresh-notes', function (child) {
            //     console.log('getting dispatched')
            // })
        },
        methods: {
            getNotes() {
                axios
                    .get('/api/leads-notes', { crossdomain: true })
                    .then(response => {this.rowNotes = response.data})
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>