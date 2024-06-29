<template>
  <div class="flex flex-col items-center mx-20 mt-8">
    <h1 ref="headingRef" class="text-4xl mb-6">Expertise</h1>
    <ExpertiseCard
        v-if="mobile"
        v-for="card in cards"
        :key="card.title"
        class="mb-8"
        v-bind="card" />
    <Flicking v-else ref="flicking" class="w-[66vw]" :options="{defaultIndex: 1, circular: true, panelsPerView}" :plugins="plugins">
      <ExpertiseCard ref="cardsRef" v-for="(card, index) in cards" :key="card.title" v-bind="card" @click="goToCard(index)" />
    </Flicking>
  </div>
</template>
<script setup lang="ts">
import {type ComponentPublicInstance, computed, onMounted, ref} from "vue";
import {useMotion} from "@vueuse/motion";
import Flicking from "@egjs/vue3-flicking";
import {AutoPlay, Perspective} from "@egjs/flicking-plugins";
import {useWindowSize} from "@vueuse/core";
import ExpertiseCard from "@components/expertise/ExpertiseCard.vue";

interface Props {
  delay: number;
}

const {width} = useWindowSize();
const mobile = computed(() => width.value <= 500);

const panelsPerView = computed(() => {
  if(width.value <= 500) return 1;
  if(width.value <= 1000) return 2;
  return 3;
})

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

const cards: CardData[] = [
  {
    title: 'Backend',
    content: 'Design and implement robust server-side logic. Ensuring databases and APIs are efficient, scalable and secure forming the backbone for reliable applications.',
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
  },
  {
    title: 'Frontend',
    content: 'Create engaging, responsive interfaces by optimizing user experience and performance, ensuring seamless and visually appealing applications.',
    icons: [
      {
        name: 'si-vuedotjs',
        tooltip: 'VueJs'
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
      {
        name: 'si-flutter',
        tooltip: 'Flutter'
      },
    ]
  },
  {
    title: 'DevOps',
    content: 'Streamlining deployment with CI/CD practices and containerization. Utilizing DevOps practices to ensure efficient operations, infrastructure maintenance and seamless development and deployment workflows.',
    icons: [
      {
        name: 'si-docker',
        tooltip: 'Container Orchestration'
      },
      {
        name: 'si-linux',
        tooltip: 'Monolithic Deployment'
      },
      {
        name: 'si-amazonaws',
        tooltip: 'Amazon AWS'
      },
      {
        name: 'si-github',
        tooltip: 'Github Actions (CI/CD)'
      },
    ]
  },
  {
    title: 'Testing & Quality Assurance',
    content: 'Ensuring software reliability through comprehensive testing strategies. This includes implementing unit, component and end-to-end tests to maintain high standards of quality and stability.',
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
  },
];

const cardsRef = ref();
const flicking = ref<ComponentPublicInstance<Flicking>>();

useMotionCustom(headingRef, 0);

onMounted(() => {
  useMotionCustom(cardsRef.value[0], 300);
  useMotionCustom(cardsRef.value[1], 600);
  useMotionCustom(cardsRef.value[2], 900);
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