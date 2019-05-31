<template>
    <div>
        <!-- <form class="" action="" method="POST"> -->
            <div class="field">
                <label class="label">Note:</label>
                <div class="control">
                    <textarea class="textarea" v-model="note" placeholder="Ex. has a lot of work with JQuery"></textarea>
                </div>
            </div>
            <div class="control is-pulled-right">
                <button v-on:click="submitNote()" class="button is-link">Submit</button>
            </div>
        <!-- </form> -->
    </div>
</template>

<script>
    import axios from 'axios'


    export default {
        name: 'NoteForm',
        props: ['id', 'noteType'],
        data() {
            return {
                note: null,
                noteType: null
                // id: 1
            }
        },
        methods: {
            submitNote() {
                // TODO once auth is created change the serializers to get the user id from token
                // TODO come back and clean it up once auth is up
                console.log(this.noteType)
                if (this.noteType == "candidate") {
                    axios
                        .post('/api/candidates-notes', {
                                "candidate": 1,
                                "user": 1,
                                "date": "2019-05-30T00:00",
                                "note": this.note
                        })
                        .catch(function (error) {
                            console.log(error);
                        })
                        .then(function (response) {
                            // TODO do it as an event 
                            this.$parent.getNotes()


                        }.bind(this))
                } else {
                    axios
                        .post('/api/leads-notes', {
                                "lead": 1,
                                "user": 1,
                                "date": "2019-05-30T00:00",
                                "note": this.note
                        })
                        .catch(function (error) {
                            console.log(error);
                        })
                        .then(function (response) {
                            // TODO do it as an event 
                            this.$parent.getNotes()


                        }.bind(this))
                }
                
            }
        }

    }
</script>

<style lang="scss" scoped>

</style>