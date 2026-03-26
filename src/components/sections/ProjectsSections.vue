<template>
  <div id="projects" class="projects-section pt-12 px-10 md:px-16">
    <h2 class="text-3xl font-bold mb-6">Contributions</h2>
    <div class="projects-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="(project, index) in projects" :key="index"
           class="flex flex-col project-card bg-lighter-dark-blue rounded-lg shadow-md p-6 justify-between">
        <div>
          <h3 class="text-light-blue text-xl font-semibold mb-2">{{ project.title }}</h3>
          <p class="text-gray text-gray-700">{{ project.description }}</p>
        </div>
        <div :class="`mt-8 flex ${project.link ? 'justify-between' : 'justify-end'}`" >
          <a v-show="project.link" :href="project.link" target="_blank" class="text-blue-500 hover:underline inline-block">View
            Project</a>
          <img v-if="project.image" :class="'max-w-8 rounded-md  object-contain ' + (project.imageClass ?? '')" :src="project.image" :alt="project.title"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import atLargeLogo from '@assets/atLargeReseach.png'
import astLogo from '@assets/cppast.png'
import elasticLogo from '@assets/elastic.svg'

interface Project {
  title: string;
  description: string;
  image: string;
  link?: string;
  imageClass?: string;
}

const projects: Project[] = [
  {
    title: 'TS EDSL — Continuum',
    description: 'Contributed to the Continuum project by designing and implementing a TypeScript embedded domain-specific language (EDSL) for cloud simulation configuration. Leveraged TypeScript\'s type system and VS Code snippets for a type-safe, ergonomic developer experience.',
    image: atLargeLogo,
    link: 'https://github.com/atlarge-research/continuum/tree/7ee6d908fafe9985337f42e104fec90de13357fe/input/dsl/src'
  },
  {
    title: 'AST Insight — Static Code Analysis',
    description: 'MSc thesis project: an AST-based static analysis tool for detecting and correcting security vulnerabilities in C code. Parses source files into abstract syntax trees, identifies insecure patterns, and applies automated corrections.',
    image: astLogo,
    imageClass: 'border border-dark-blue bg-white',
    link: 'https://github.com/danielv27/ast-insight'
  },
  {
    title: 'KB-Indexer — Cloud Migration',
    description: 'Migrated a monolithic research search engine to a scalable cloud application on Azure. Used Kubernetes, Helm charts, and Grafana for orchestration and monitoring. Built an API and Vue web app for interactive index management.',
    image: elasticLogo,
    imageClass: 'bg-dark-blue p-1.5',
    link: 'https://github.com/DevOps-Group20'
  },
];
</script>

<style scoped>
.projects-section {
  max-width: 1200px;
  margin: 0 auto;
}

.project-card {
  transition: transform 0.3s;
}

.project-card:hover {
  transform: scale(1.05);
}
</style>
