<template>
  <div class="flex w-[95vw] md:w-1/2 relative">
    <ul class="w-1/12 min-w-28 timeline timeline-vertical text-white">
      <li v-for="(entry, index) in entries" :key="index"
        class="entry transition ease-in-out delay-75 bg-blue-500 active:text-dark-blue hover:scale-110 duration-300"
        :class="{ 'text-dark-blue': currentIndex === index }" @mouseenter="setIndex(index)">
        <hr v-if="index !== 0" />
        <div class="timeline-start">{{ entry.date }}</div>
        <div class="timeline-middle">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
              clip-rule="evenodd" />
          </svg>
        </div>
        <hr v-if="index !== entries.length - 1" />
      </li>
    </ul>
    <Transition :duration="550" name="nested">
      <div ref="cardRef" v-show="show"
        class="absolute mt-5 ml-20 px-6 pt-4 md:pt-14 w-[calc(100%-5rem)] h-full bg-dark-blue rounded-b-4xl rounded-r-4xl">
        <div class="inner h-full flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-2 md:mb-6">
              <h1 class="text-2xl">{{ currentEntry.title }}</h1>
              <a v-if="currentEntry.link" :href="currentEntry.link" target="_blank"
                class="text-light-blue opacity-60 hover:opacity-100 transition-opacity">
                <VIcon name="bi-box-arrow-up-right" scale="1.2" />
              </a>
            </div>
            <div v-html="currentEntry.content"></div>
          </div>
          <img class="self-end" :class="currentEntry.iconStyles" :src="currentEntry.icon" :alt="currentEntry.title">
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import vuSvg from '@assets/vu.svg';
import dongItSvg from '@assets/dongIT.svg'
import myLogo from '@assets/logo.png'
import capisoftLogo from '@assets/capiscoft-white.png'
import myParcelLogo from '@assets/myparcel-logo.svg'
import { computed, onMounted, ref, watch } from 'vue';
import { useWindowScroll } from "@vueuse/core";
import { isInViewport } from "@utils/viewPort.js";

const show = ref(false);
const setShow = (value: boolean) => (show.value = value);

const cardRef = ref();
const { y } = useWindowScroll();

onMounted(() => {
  watch(y, () => setShow(isInViewport(cardRef.value)));
})

const currentIndex = ref<number>(0);
const setIndex = (index: number) => (currentIndex.value = index);

interface Entry {
  date: string;
  title: string;
  content: string;
  icon: string;
  iconStyles?: string;
  link?: string;
}

const listStyle = "list-disc ml-3.5"
const entries: Entry[] = [
  {
    date: 'Jan 2025',
    title: 'Software Engineer, MyParcel',
    content: `
         <ul class="${listStyle}">
            <li>Built and maintained microservices powering a European e-commerce shipping platform</li>
            <li>Collaborated with stakeholders and clients to refine features and requirements</li>
            <li>Took active part in system design, CI/CD pipelines, and full-stack delivery</li>
        </ul>`,
    icon: myParcelLogo,
    iconStyles: 'h-8 w-auto mb-4 mr-1',
    link: 'https://www.myparcel.com'
  },
  {
    date: 'Aug 2023',
    title: 'Software Engineer, DongIT',
    content: `
         <ul class="${listStyle}">
            <li>Full-stack role across both frontend (Vue) and backend services</li>
            <li>Containerized services with Docker for reliable deployments</li>
            <li>Set up CI/CD pipelines to streamline testing and releases</li>
        </ul>`,
    icon: dongItSvg,
    iconStyles: 'max-h-16 mb-1',
    link: 'https://www.dongit.nl'
  },
  {
    date: 'Nov 2022',
    title: 'Software Engineer, Capisoft B.V.',
    content: `
      <ul class="${listStyle}">
        <li>Lead role managing project delivery and technical direction</li>
        <li>Owned full-stack integration between backend APIs and client apps</li>
        <li>Drove testing, deployment, and code quality standards</li>
      </ul>`,
    icon: capisoftLogo,
    iconStyles: 'max-h-10 mb-4',
    link: 'https://www.capisoft.nl'
  },
  {
    date: 'Feb 2022',
    title: 'Software Engineer, DBV Software Solutions',
    content: `
      <ul class="${listStyle}">
        <li>Freelance studio delivering cross-platform apps for mobile, desktop, and web</li>
        <li>Shipped production apps with React Native, Flutter, and Firebase</li>
      </ul>`,
    icon: myLogo,
    iconStyles: 'max-h-16 pb-5'
  },
  {
    date: 'Sep 2021',
    title: 'Teaching Assistant, Vrije Universiteit Amsterdam',
    content: `
      <p>Mentored CS and AI students in small groups, teaching core programming concepts and problem-solving skills.</p>`,
    icon: vuSvg,
    iconStyles: 'max-h-20 mb-1 max-w-32',
    link: 'https://www.vu.nl'
  },
];

const currentEntry = computed(() => entries[currentIndex.value]);
</script>

<style scoped>
li {
  height: 90px;
}
</style>
