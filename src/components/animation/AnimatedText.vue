<template>
  <div class="flex flex-wrap">
  <span
      v-for="word in textArray"
      ref="wordArrayRef"
      class="whitespace-nowrap"
  >{{ word }}&nbsp;</span>
  </div>
</template>

<script setup lang="ts">

import {computed, onMounted, ref} from "vue";
import {useMotion} from "@vueuse/motion";

interface Props {
  text: string;
  delay: number;
  timeBetween: number
}

const props = withDefaults(defineProps<Props>(), {
  text: '',
  delay: 0,
  timeBetween: 100
})
const textArray = computed(() => props.text.split(' '));

const wordArrayRef = ref<HTMLSpanElement[]>();

onMounted(() => wordArrayRef.value?.forEach((spanTag, index) => {
  useMotion(spanTag, {
    initial: {
      opacity: 0,
      y: 100
    },
    enter: {
      opacity: 1,
      y: 0,
      transition: {
        delay: props.delay + props.timeBetween * (index + 1),
        type: 'spring',
        stiffness: 150,
        damping: 25,
        mass: 0.5,
      }
    },
  })
}));

</script>