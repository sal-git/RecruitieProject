<template>
    <div>
        <NavBar />
        <div class="columns">
            <aside class="column is-2 aside hero is-fullheight">
                <button v-on:click="candidateLaunch" class="button is-primary">Add Candidate</button>
                <button v-on:click="leadLaunch" class="button is-primary">Add Lead</button>
            </aside>
            <div class="column is-4 messages hero is-fullheight">
                <div class="tabs is-centered">
                    <ul>
                        <li :class="[ activeTab === 'candidates' ? 'is-active' : '' ]"><a @click="activeTab='candidates'">Candidates</a></li>
                        <li :class="[ activeTab === 'leads' ? 'is-active' : '' ]"><a @click="activeTab='leads'">Leads</a></li>
                    </ul>
                </div>
                <LeadList v-if="activeTab ==='leads'"/>
                <CandidateList v-if="activeTab ==='candidates'"/>
            </div>
            <div class="column is-6 message hero is-fullheight">
                <CandidateView :candidate="candidate" v-if="activeTab ==='candidates'"/>
                <LeadView :lead="lead" v-if="activeTab ==='leads'" />
            </div>
        </div>

        <div class="modal" v-bind:class="{'is-active':isActiveCandidate}">
             <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                <p class="modal-card-title">Add Candidate</p>
                <button class="delete" aria-label="close"></button>
                </header>
                <section class="modal-card-body">
                    
                </section>
                <footer class="modal-card-foot">
                <button class="button is-success">Save changes</button>
                <button @click="close" class="button">Cancel</button>
                </footer>
            </div>
        </div>

        <div class="modal" v-bind:class="{'is-active':isActiveLead}">
            <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                <p class="modal-card-title">Add Lead</p>
                <button class="delete" aria-label="close"></button>
                </header>
                <section class="modal-card-body">
                    
                </section>
                <footer class="modal-card-foot">
                <button class="button is-success">Save changes</button>
                <button @click="close" class="button">Cancel</button>
                </footer>
            </div>
        </div>

    </div>
</template>

<script>
    import NavBar from '../components/NavBar.vue'
    import NewCandidateModal from '../components/NewCandidateModal.vue'
    import LeadView from '../components/LeadView.vue'
    import CandidateView from '../components/CandidateView.vue'
    import LeadList from '../components/LeadList'
    import CandidateList from '../components/CandidateList'
    import axios from 'axios'

    export default {
        name: 'DashboardPage',
        data: function() {
            return {
                activeTab: "leads",
                isActiveCandidate: false,
                isActiveLead: false,
                candidates: [
                    {
                        id: 1,
                        name: "Stephen",
                        location: "Brownsville, TX",
                        salary: 40000
                    },
                    {
                        id: 2,
                        name: "Samantha",
                        location: "Brownsville, TX",
                        salary: 80000
                    },
                    {
                        id: 3,
                        name: "Brendan",
                        location: "Austin, TX",
                        salary: 1140000
                    },
                ],
                candidate: null,
                lead: null
            }
        },
        methods: {
            candidateLaunch: function(){
                this.isActiveCandidate = true;
            },
            leadLaunch: function(){
                this.isActiveLead = true;
            },
            close: function() {
                this.isActiveCandidate = false;
                this.isActiveLead = false;
            },
            getCandidateInfo: function(id) {
                console.log("retrieving candidate info")
                
            },
            getLeadInfo: function(id){

            },
            constructCandidateView(id){
                axios
                    .get('http://127.0.0.1:8000/api/candidates/'+id, { crossdomain: true })
                    .then(response => {this.candidate = response.data})
            },
            constructLeadView(id){
                axios
                    .get('http://127.0.0.1:8000/api/leads/'+id, { crossdomain: true })
                    .then(response => {this.lead = response.data})
            }
        },
        components: {
            NavBar,
            NewCandidateModal,
            LeadView,
            CandidateView,
            LeadList,
            CandidateList
        },
        created: function() {
            // TODO proper setup
            // axios
            //     .get('http://127.0.0.1:8000/api/leads')
            //     .then(response => {console.log(response.data)})
            
        }
    }
</script>

<style lang="scss" scoped>
    html,body {
    font-family: 'Open Sans', serif;
    font-size: 14px;
    line-height: 1.5;
    height: 100%;
    background-color: #fff;
    }
    .nav.is-dark {
    background-color: #232B2D;
    color: #F6F7F7;
    }
    .nav.is-dark .nav-item a, .nav.is-dark a.nav-item {
        color: #F6F7F7;
    }
    .nav.is-dark .nav-item a.button.is-default {
        color: #F6F7F7;
        background-color: transparent;
        border-width: 2px;
    }
    .nav.menu {
    border-bottom: 1px solid #e1e1e1;
    }
    .nav.menu .nav-item .icon-btn {
    border: 3px solid #B7C6C9;
    border-radius: 90px;
    padding: 5px 7px;
    color: #B7C6C9;
    }
    .nav.menu .nav-item.is-active .icon-btn {
    color: #2EB398;
    border: 3px solid #2EB398;
    }
    .nav.menu .nav-item .icon-btn .fa {
    font-size: 20px;
    color: #B7C6C9;
    }
    .nav.menu .nav-item.is-active .icon-btn .fa {
    color: #2EB398;
    }
    .aside {
    display:block;
    background-color: #F9F9F9;
    border-right: 1px solid #DEDEDE;
    }
    .messages {
    display:block;
    background-color: #fff;
    border-right: 1px solid #DEDEDE;
    }
    .message {
    display:block;
    background-color: #fff;
    }
    .aside .compose {
    height: 95px;
    margin:0 -10px;
    padding: 25px 30px;
    }
    .aside .compose .button {
    color: #F6F7F7;
    }
    .aside .compose .button .compose {
    font-size: 14px;
    font-weight: 700;
    }
    .aside .main {
    padding: 40px;
    color: #6F7B7E;
    }
    .aside .title {
    color: #6F7B7E;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    }
    .aside .main .item {
    display: block;
    padding: 10px 0;
    color: #6F7B7E;
    }
    .aside .main .item.active {
    background-color: #F1F1F1;
    margin: 0 -50px;
    padding-left: 50px;
    }
    .aside .main .item:active,.aside .main .item:hover {
    background-color: #F2F2F2;
    margin: 0 -50px;
    padding-left: 50px;
    }
    .aside .main .icon {
    font-size: 19px;
    padding-right: 30px;
    color: #A0A0A0;
    }
    .aside .main .name {
    font-size: 15px;
    color: #5D5D5D;
    font-weight: 500;
    }
    .messages {
    padding: 40px 20px;
    }
    .message {
    padding: 40px 20px;
    }
    .messages .action-buttons {
    padding: 0;
    margin-top: -20px;
    }
    .message .action-buttons {
    padding: 0;
    margin-top: -5px;
    }
    .action-buttons .control.is-grouped {
    display: inline-block;
    margin-right: 30px;
    }
    .action-buttons .control.is-grouped:last-child {
    margin-right: 0;
    }
    .action-buttons .control.is-grouped .button:first-child {
    border-radius: 5px 0 0 5px;
    }
    .action-buttons .control.is-grouped .button:last-child {
    border-radius: 0 5px 5px 0;
    }
    .action-buttons .control.is-grouped .button {
    margin-right: -5px;
    border-radius: 0;
    }
    .pg {
    display: inline-block;
    top:10px;
    }
    .action-buttons .pg .title {
    display: block;
    margin-top: 0;
    padding-top: 0;
    margin-bottom: 3px;
    font-size:12px;
    color: #AAAAA;
    }
    .action-buttons .pg a{
    font-size:12px;
    color: #AAAAAA;
    text-decoration: none;
    }
    .is-grouped .button {
    background-image: linear-gradient(#F8F8F8, #F1F1F1);
    }
    .is-grouped .button .fa {
    font-size: 15px;
    color: #AAAAAA;
    }
    .inbox-messages {
    margin-top:60px;
    }
    .message-preview {
    margin-top: 60px;
    }
    .inbox-messages .card {
    width: 100%;
    }
    .inbox-messages strong {
    color: #5D5D5D;
    }
    .inbox-messages .msg-check {
    padding: 0 20px;
    }
    .inbox-messages .msg-subject {
    padding: 10px 0;
    color: #5D5D5D;
    }
    .inbox-messages .msg-attachment {
    float:right;
    }
    .inbox-messages .msg-snippet {
    padding: 5px 20px 0px 5px;
    }
    .inbox-messages .msg-subject .fa {
    font-size: 14px;
    padding:3px 0;
    }
    .inbox-messages .msg-timestamp {
    float: right;
    padding: 0 20px;
    color: #5D5D5D;
    }
    .message-preview .avatar {
    display: inline-block;
    }
    .message-preview .top .address {
    display: inline-block;
    padding: 0 20px;
    }
    .avatar img {
    width: 40px;
    border-radius: 50px;
    border: 2px solid #999;
    padding: 2px;
    }
    .address .name {
    font-size: 16px;
    font-weight: bold;
    }
    .address .email {
    font-weight: bold;
    color: #B6C7D1;
    }
    .card.active {
    background-color:#F5F5F5;
    }
</style>