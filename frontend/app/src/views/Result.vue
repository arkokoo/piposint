<template>
    <section class="container" style="padding-top: 8rem;">
        <div>
            <pre v-if="responseData">{{ responseData }}</pre>
        </div>
    </section>
</template>

<script>
export default {
  data() {
    return {
      responseData: null,
    };
  },
  created() {
    this.responseData = this.$route.params.data;
  },
}
</script>