<template>
  <ul v-if="store.jsonData.length > 0" class="list-group">
    <li v-for="robot in store.jsonData" :key="robot.id" class="list-group-item p-2 mb-2 d-flex flex-column justify-content-center align-items-center">
        <p v-for="(value, key) in robot" :key="key">
            {{ key }} -> {{ value }}
        </p>
    </li>
  </ul>
  <div v-else>Loading...</div>
</template>

<script setup>
  import { store } from './store.js';
</script>
