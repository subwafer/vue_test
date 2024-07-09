<template>
  <button @click="fetch_data">Refresh</button>
  <div v-if="err">{{ err_msg }}</div>
  <div v-else-if="loading">Loading...</div>
  <table v-else class="table">
    <thead>
      <tr>
        <th v-for="(value, key) in robots[0]" :key="key">{{ key }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="robot in robots" :key="robot.id">
        <td v-for="(value, key) in robot" :key="key">{{ value }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { post_request } from './utils/http_requests.js';
  import { store } from './store.js';

  const loading = ref(false); // if loading, display loading
  const err = ref(false);
  const err_msg = ref('');

  const robots = ref([]);

  const fetch_data = async function() {
    loading.value = true;
    err.value = false;
    err_msg.value = "";
    robots.value = [];
    store.jsonData = [];

    try {
            let req_config = {
                url: "/__robots",
                response_type: 'json',
                timeout: 5000,
                req_data: { user: "admin", password: "admin" }
            };

            let data = await post_request(req_config.url, req_config.response_type, req_config.timeout, req_config.req_data);

        robots.value = data;
        store.jsonData = data;

    } catch (error) {
        err.value = true;
        err_msg.value = "Failed to load data";
        console.error("Failed to load data");
    } finally {
        loading.value = false;
    }
  };

  onMounted(fetch_data);
</script>
