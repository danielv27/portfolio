<template>
  <div class="flex bg-gradient-to-b from-dark-blue to-green justify-center h-144">
    <div id="about" class="block md:flex w-full md:w-2/3 px-4 text-left text-white mt-16 gap-12">
      <div class=" mt-14">
        <h1 ref="headingRef" class="w-full flex text-4xl mb-4">
          About Me
        </h1>
        <section ref="contentRef">
          I'm Daniel Verner, a software engineer based in Amsterdam. I focus on backend and platform work: business-critical
          integrations, APIs, containerized services, CI/CD systems, and internal developer tooling.
          <br><br>
          I enjoy owning systems from implementation through deployment and operations. My full-stack background helps me
          collaborate across product boundaries, and I apply secure coding practices with operational risks in mind. I value
          clear architecture, automated testing, and delivery workflows that help teams ship confidently.
        </section>
      </div>
      <img ref="stackImgRef" class="w-48 hidden md:block object-contain self-start" :src="Stack" alt="stack" />
    </div>
  </div>
</template>
<script setup lang="ts">
import Stack from '@assets/stack-expanded.png'
import { ref } from "vue";
import { useMotion } from "@vueuse/motion";
import { useWindowSize } from "@vueuse/core";

const headingRef = ref();
const contentRef = ref();
const stackImgRef = ref();

function useMotionCustom(element: any, delay: number) {
  useMotion(element, {
    initial: {
      opacity: 0,
      y: 10,
    },
    visibleOnce: {
      opacity: 1,
      y: 0,
      transition: {
        delay,
        duration: 500,
      }
    }
  })
}

const { width } = useWindowSize();
if (width.value >= 1000) {
  useMotionCustom(headingRef, 300);
  useMotionCustom(contentRef, 600);
  useMotionCustom(stackImgRef, 1000);
}









</script>
