import { createApp } from 'vue';

import 'bootstrap/dist/css/bootstrap.min.css';

import robot_table from './robot_table.vue';
const robot_table_comp = createApp(robot_table);
robot_table_comp.mount('#test');

import robot_list from './robot_list.vue';
const robot_list_comp = createApp(robot_list);
robot_list_comp.mount('#test2');

