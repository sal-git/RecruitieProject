<template>
    <div>
        <vue-good-table
            :columns="columns"
            :rows="rows"/>
    </div>
</template>

<script>
    import 'vue-good-table/dist/vue-good-table.css';
    import { VueGoodTable } from 'vue-good-table';
    import axios from 'axios'

    
    export default {
        name: 'NoteList',
        props: ['rows'],
        data(){
            return {
                columns: [
                    {
                        label: 'Note',
                        field: 'note',
                    },
                    {
                        label: 'Date',
                        field: 'date',
                        type: 'date',
                        dateInputFormat: 'YYYY-MM-DD',
                        dateOutputFormat: 'MMM Do YY',
                    },
                ],
                // rows: this.rows,
            };
        },
        components: {
            VueGoodTable,
        },
        mounted() {
            
        },
    }
</script>

<style lang="scss" scoped>

</style>