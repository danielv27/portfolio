<template>
  <div class="sticky top-0 left-0 z-30 bg-gradient-to-b  py-4 w-screen flex justify-between bg-dark-blue">
    <div class="flex ml-6">
      <a :href="logoHref">
        <img class="w-16 lg:w-20 mt-1.5 object-contain" :src="logo" alt="Logo"/>
      </a>
    </div>
    <div class="hidden lg:flex items-center gap-6 mr-14 ">
      <a
          v-for="item in navItems"
          :key="item.href"
          class="hover-underline-animation"
          :class="{selected: item.selected}"
          :href="item.href">
        {{ item.label }}
      </a>

      <a :href="resumeFileName" target="_blank">
        <div class="border p-2 transition-colors ease-in duration-900 opacity-100 hover:text-light-blue rounded">
          Resume
        </div>
      </a>
    </div>
    <div class="flex lg:hidden items-center mr-6">
      <a :href="resumeFileName" target="_blank">
        <div class="border px-3 py-1.5 text-sm transition-colors ease-in duration-900 opacity-100 hover:text-light-blue rounded">
          Resume
        </div>
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import logo from '@assets/logo.png'
import { ref, watch } from "vue";
import { useWindowScroll } from "@vueuse/core";

const { y } = useWindowScroll();

interface NavItem {
  label: string;
  href: string;
  selected: boolean;
}

const navItems = ref<NavItem[]>([
  { label: 'About', href: '#about', selected: false },
  { label: 'Experience', href: '#experience', selected: false },
  { label: 'Education', href: '#education', selected: false },
  { label: 'Open Source', href: '#projects', selected: false },
  { label: 'Contact', href: '#contact', selected: false },
]);

function updateActiveSection() {
  const threshold = window.innerHeight * 0.45;
  let activeIndex = -1;

  navItems.value.forEach((item, index) => {
    const el = document.getElementById(item.href.slice(1));
    if (!el) return;
    const rect = el.getBoundingClientRect();
    // A section is the active candidate if its top has entered the upper 45%
    // of the viewport and hasn't fully scrolled past the top yet
    if (rect.top <= threshold && rect.bottom > 0) {
      activeIndex = index; // last one wins = deepest visible section
    }
  });

  navItems.value.forEach((item, index) => {
    item.selected = index === activeIndex;
  });
}

watch(y, updateActiveSection);

const logoHref = '#main'
const resumeFileName = 'resume.pdf';

</script>
<style scoped>
.hover-underline-animation {
  display: inline-block;
  position: relative;
  padding-bottom: 2px;
}

.hover-underline-animation.selected,
.hover-underline-animation:hover {
  color: #66FCF1;
}

.hover-underline-animation::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 1px;
  bottom: 0;
  left: 0;
  background-color: #66FCF1;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation.selected::after,
.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}

</style>