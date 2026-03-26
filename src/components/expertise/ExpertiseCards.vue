<template>
  <div class="flex flex-col items-center mt-8">
    <h1 ref="headingRef" class="text-4xl mb-6">Expertise</h1>
    <div v-if="smallScreen" class="grid md:gap-14 md:grid-cols-2">
      <ExpertiseCard
          ref="cardsRef"
          v-for="card in cards"
          :key="card.title + 'mobile'"
          class="mb-8 "
          v-bind="card"/>
    </div>
    <Flicking v-else ref="flicking" class="w-[66vw] hover:cursor-grab active:cursor-grabbing"
              :options="{defaultIndex: 1, circular: true, panelsPerView}" :plugins="plugins">
      <ExpertiseCard ref="cardsRef" v-for="(card, index) in cards" :key="card.title" v-bind="card"
                     @click="goToCard(index)"/>
    </Flicking>
  </div>
</template>
<script setup lang="ts">
import {type ComponentPublicInstance, computed, onMounted, type Ref, ref} from "vue";
import {useMotion} from "@vueuse/motion";
import Flicking from "@egjs/vue3-flicking";
import {AutoPlay, Perspective} from "@egjs/flicking-plugins";
import {useWindowSize} from "@vueuse/core";
import ExpertiseCard from "@components/expertise/ExpertiseCard.vue";

interface Props {
  delay: number;
}

const {width} = useWindowSize();
const smallScreen = computed(() => width.value <= 1340);

const panelsPerView = computed(() => {
  if (width.value <= 500) return 1;
  if (width.value <= 1000) return 2;
  return 3;
});

const backEndCard: CardData = {
  title: 'Backend',
  content: 'Design scalable APIs and services with a focus on reliability, security, and clean architecture.',
  icons: [
    {
      name: 'si-laravel',
      tooltip: 'Laravel'
    },
    {
      name: 'si-django',
      tooltip: 'Django'
    },
    {
      name: 'si-firebase',
      tooltip: 'Firebase'
    },
    {
      name: 'si-express',
      tooltip: 'Express'
    }
  ]
};
const frontEndCard: CardData = {
  title: 'Frontend',
  content: 'Build responsive, performant interfaces with modern frameworks and component-driven architecture.',
  icons: [
    {
      name: 'si-vuedotjs',
      tooltip: 'Vue.js'
    },
    {
      name: 'si-react',
      tooltip: 'React'
    },
    {
      name: 'si-typescript',
      tooltip: 'TypeScript'
    },
    {
      name: 'si-tailwindcss',
      tooltip: 'TailwindCSS'
    },
  ]
};
const devOpsCard: CardData = {
  title: 'DevOps',
  content: 'Automate deployments with CI/CD pipelines, containerization, and cloud infrastructure.',
  icons: [
    {
      name: 'si-docker',
      tooltip: 'Docker'
    },
    {
      name: 'si-linux',
      tooltip: 'Linux'
    },
    {
      name: 'si-amazonaws',
      tooltip: 'Amazon AWS'
    },
    {
      name: 'si-github',
      tooltip: 'GitHub Actions'
    },
  ]
};
const testingCard: CardData = {
  title: 'Testing & QA',
  content: 'Maintain quality through unit, integration, and end-to-end testing strategies.',
  icons: [
    {
      name: 'si-vite',
      tooltip: 'Vitest'
    },
    {
      name: 'si-webpack',
      tooltip: 'Webpack'
    },
    {
      name: 'si-testinglibrary',
      tooltip: 'Testing Library'
    }
  ]
};

const cards: Ref<CardData[]> = computed(() => [
  backEndCard,
  frontEndCard,
  devOpsCard,
  testingCard,
]);


const props = defineProps<Props>();

const headingRef = ref();

interface Icon {
  name: string;
  tooltip: string;
}

interface CardData {
  title: string;
  content: string;
  icons: Icon[]
}


const cardsRef = ref();
const flicking = ref<ComponentPublicInstance<Flicking>>();

useMotionCustom(headingRef, 0);

onMounted(() => {
  cardsRef.value.forEach(function (card: CardData, i: number) {
    useMotionCustom(card, 300 + 300 * i);
  });
})

function useMotionCustom(element: any, delay: number, opacity = 1) {
  useMotion(element, {
    initial: {
      opacity: 0,
      y: 10,
    },
    enter: {
      opacity,
      y: 0,
      transition: {
        delay: props.delay + delay
      }
    }
  })
}

const perspectivePlugin = new Perspective({rotate: 0.5});
const autoPlayPlugin = new AutoPlay({
  duration: 6000,
  direction: "NEXT",
  stopOnHover: true,
  animationDuration: 700,
});

const plugins = ref<any[]>([
  perspectivePlugin,
  autoPlayPlugin
]);

function goToCard(index: number) {
  flicking.value?.moveTo(index);
}

</script>