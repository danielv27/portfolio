import {createApp} from 'vue'
import {MotionPlugin} from '@vueuse/motion'
import VNetworkGraph from "v-network-graph"
import './style.css'
import App from './App.vue'
import {OhVueIcon, addIcons} from "oh-vue-icons";
import 'vue3-toastify/dist/index.css';
import VueTippy from 'vue-tippy'
import 'tippy.js/dist/tippy.css'; // optional for styling

import {
    SiGithub,
    SiLinkedin,
    SiVuedotjs,
    SiReact,
    SiTypescript,
    SiTailwindcss,
    SiFlutter,
    SiDocker,
    SiLinux,
    SiAmazonaws,
    SiLaravel,
    SiDjango,
    SiFirebase,
    SiExpress,
    SiVite,
    SiWebpack,
    SiTestinglibrary,
} from "oh-vue-icons/icons/si";
import { BiBoxArrowUpRight } from "oh-vue-icons/icons/bi";

const app = createApp(App)

addIcons(
    SiGithub,
    SiLinkedin,
    SiVuedotjs,
    SiReact,
    SiTypescript,
    SiTailwindcss,
    SiFlutter,
    SiDocker,
    SiLinux,
    SiAmazonaws,
    SiLaravel,
    SiDjango,
    SiFirebase,
    SiExpress,
    SiVite,
    SiWebpack,
    SiTestinglibrary,
    BiBoxArrowUpRight,
);

app.component('VIcon', OhVueIcon);
app.use(VueTippy);
app.use(MotionPlugin);
app.use(VNetworkGraph)

app.mount('#app')