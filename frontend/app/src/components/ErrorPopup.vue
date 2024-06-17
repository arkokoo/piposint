<template>
    <div class="error-popup" v-if="error.code !== null">
    <div class="error-popup-content">
      <h2>{{ error.code }}</h2>
      <p>{{ error.message }}</p>
      <div class="error-delete" @click="error = { code: null, message: '' }">
          <X />
        </div>
    </div>
  </div>
</template>

<script setup>
    import { X } from 'lucide-vue-next';
</script>

<script>
    export default {
        props: {
            error: {
                type: Object,
                default: {
                    code: null,
                    message: ''
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import url(./styles/error_popup.scss);
</style>