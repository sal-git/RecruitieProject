<template>
    <div>
        <div v-for="candidate in candidates" class="card" v-bind:key="candidate.id" v-on:click="getCandidateInfo(candidate.id)">
            <div class="card-content">
                <div class="candidate-card-header">
                    <span class="candidate-card-from"><small>{{ candidate.location }}</small></span>
                </div>
                <div class="candidate-card-subject">
                    <span class="candidate-card-subject"><strong id="fake-subject-1">{{ candidate.first_name }} {{ candidate.last_name }}</strong></span>
                </div>
                <div class="candidate-card-snippet">
                    <p id="fake-snippet-1">Years of Exp: {{ candidate.years_of_exp }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'CandidateList',
        data() {
            return {
                candidates: null
            }
        },
        mounted() {
            axios
                .get('http://127.0.0.1:8000/api/candidates', { crossdomain: true })
                .then(response => {this.candidates = response.data})
        },
        methods: {
            getCandidateInfo: function(id) {
                //perhaps do events, but this component will only be used in this context
                this.$parent.constructCandidateView(id);
                
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>