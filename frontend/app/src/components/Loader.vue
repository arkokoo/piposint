<template>
    <div class="loader-container" v-if="isLoading">
        <span class="loader"></span>
  </div>
</template>

<script>
export default {
    props: {
        isLoading: {
            type: Boolean,
            default: false
        }
    }
}
</script>

<style lang="scss" scoped>
@import url(./styles/loader.scss);
</style>