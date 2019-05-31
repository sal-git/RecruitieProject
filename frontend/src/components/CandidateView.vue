<template>
    <div>
        <section class="hero is-primary">
            <div class="hero-body">
                <div class="container">
                <h1 class="title">
                    {{ candidate.first_name }} {{ candidate.last_name}}
                </h1>
                <h2 class="subtitle">
                    {{ candidate.location }}
                </h2>
                </div>
            </div>
        </section>
        <br>
        <br>
        <section>
            <div class="control">
                <div class="tags has-addons">
                    <span class="tag is-dark">LANG</span>
                    <span class="tag is-info">PYTHON</span>
                </div>
            </div>
            <div class="control">
                <div class="tags has-addons">
                    <span class="tag is-dark">LANG</span>
                    <span class="tag is-info">JAVA</span>
                </div>
            </div>
            <div class="control">
                <div class="tags has-addons">
                    <span class="tag is-dark">LANG</span>
                    <span class="tag is-info">C++</span>
                </div>
            </div>
        </section>
        <br>
        <br>
        <section>
            <NoteForm noteType="candidate" />
        </section>
        <br>
        <br>
        <section>
            <CandidateNotes :rows="rowNotes" />
        </section>
    </div>
</template>

<script>
    import CandidateNotes from './NoteList.vue';
    import NoteForm from './notes/NoteForm.vue';
    import axios from 'axios'

    export default {
        name: "CandidateView",
        props: ['candidate'],
        data() {
            return {
                rowNotes: []
            }
        },
        components: {
            CandidateNotes,
            NoteForm
        },
        mounted() {
            this.getNotes()
        },
        methods: {
            getNotes() {
                axios
                    .get('/api/candidates-notes', { crossdomain: true })
                    .then(response => {this.rowNotes = response.data})
            }
        }
        
    }
</script>

<style lang="scss" scoped>

</style>