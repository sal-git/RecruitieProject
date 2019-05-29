<template>
    <div>
        <div v-for="lead in leads" class="card" v-bind:key="lead.id" v-on:click="getLeadInfo(lead.id)">
            <div class="card-content">
                <div class="lead-card-header">
                    <span class="lead-card-from"><small>{{ lead.location }}</small></span>
                    <span class="lead-card-timestamp"></span>
                    <span class="lead-card-attachment"><i class="fa fa-paperclip"></i></span>
                </div>
                <div class="lead-card-subject">
                    <span class="lead-card-subject"><strong id="fake-subject-1">{{ lead.title }}</strong></span>
                </div>
                <div class="lead-card-snippet">
                    <p id="fake-snippet-1">{{ lead.desc }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'


    export default {
        name: 'LeadList',
        data() {
            return {
                leads: null
            }
        },
        mounted() {
            axios
                .get('http://127.0.0.1:8000/api/leads', { crossdomain: true })
                .then(response => {this.leads = response.data})
        },
        methods: {
            getLeadInfo: function(id) {
                //perhaps do events, but this component will only be used in this context
                this.$parent.constructLeadView(id);
                
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>