<template>
  <div id="intro" class="self-center my-10 md:my-20 md:mx-8 xl:mx-32 px-4 md:px-0 overflow-hidden">
    <img class="absolute w-144 top-28 left-0 lg:top-40 lg:left-10" :src="squiggleSVG" alt="squiggle">
    <div class="flex flex-col xl:flex-row gap-10 lg:gap-40 items-center w-full">
      <RotateOnHover class="z-10 md:ml-3">
        <img ref="profileImgRef" :src="profilePicture" alt="profile"
          class="max-w-80 lg:max-w-96 rounded-full border-2 border-green shadow-2xl" />
      </RotateOnHover>
      <div class="text-left ml-3 min-w-0 w-full">
        <div class="text-xl md:text-4xl mb-2 break-words">
          <AnimatedText class="text-3xl lg:text-4xl mb-2" text="Hi, I'm Daniel," :delay="400" :time-between="180" />
          <AnimatedText text="A Full-Stack Software Engineer" :delay="1100" :time-between="240" />
        </div>
        <div ref="descriptionRef" class="text-gray text-md md:text-lg lg:mr-20">
          Welcome to my portfolio! Here you'll find my work, skills,
          and experience as a <span class="text-light-blue">full-stack software engineer</span>. I enjoy building
          reliable systems across the entire stack, from scalable backend services and clean APIs
          to performant, polished <span class="text-light-blue">user interfaces</span>.
        </div>
      </div>
    </div>
    <ExpertiseCards class="mt-24" :delay="3200" />
  </div>
</template>
<script setup>
import AnimatedText from "@components/animation/AnimatedText.vue";
import { computed, ref } from "vue";
import { useMotion } from "@vueuse/motion";
import profilePicture from "@assets/profile-blue-bg.png"
import ExpertiseCards from "@components/expertise/ExpertiseCards.vue";
import squiggleSVG from "@assets/squigglesAndDots.svg"
import RotateOnHover from "@components/animation/RotateOnHover.vue";


const descriptionRef = ref();

useMotion(descriptionRef, {
  initial: {
    opacity: 0,
    y: 5,
  },
  enter: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 500,
      delay: 2600,
    }
  },
});

</script>