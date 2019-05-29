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
    </div>
</template>

<script>
    export default {
        name: "CandidateView",
        props: ['candidate']
    }
</script>

<style lang="scss" scoped>

</style>