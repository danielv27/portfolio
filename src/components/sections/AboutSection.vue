<template>
  <div class="flex bg-gradient-to-b from-dark-blue to-green justify-center h-144">
    <div id="about" class="block md:flex w-full md:w-2/3 px-4 text-left text-white mt-16 gap-12">
      <div>
        <h1 ref="headingRef" class="w-full flex text-4xl mb-4">
          About Me
        </h1>
        <section ref="contentRef">
          I'm Daniel Verner, a full-stack software engineer passionate about building reliable, well-crafted software
          across the entire stack.
          <br><br>
          With experience spanning frontend, backend, and DevOps, I enjoy working on systems end-to-end — from designing
          clean APIs and scalable services to building intuitive user interfaces. I value modular architecture,
          automated testing, and CI/CD pipelines that keep teams shipping with confidence.
          <br><br>
          I also enjoy contributing to open source projects and exploring areas like static analysis and developer
          tooling.
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