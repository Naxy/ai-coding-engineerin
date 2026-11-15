<script setup lang="ts">
import { computed, ref } from "vue";
const quantity = ref(2);
const unitPrice = ref(12.5);
const total = computed(() => quantity.value * unitPrice.value);
</script>

<template>
  <main>
    <label>Quantity <input v-model.number="quantity" type="number" min="0" /></label>
    <p>Total: {{ total.toFixed(2) }}</p>
  </main>
</template>