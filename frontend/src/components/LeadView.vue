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
    </div>
</template>

<script>
    export default {
        name: "LeadView",
        props: ['lead']

    }
</script>

<style lang="scss" scoped>

</style>