<template>
  <div class="education-section my-auto pt-12 h-[80vh] md:h-[65vh] px-4 md:px-32 bg-gradient-to-b from-light-blue to-dark-blue">
    <div id="education">
      <h2 class="text-3xl font-bold mb-6">Education</h2>
      <div class="education-cards grid grid-cols-1 md:grid-cols-2 gap-6">
        <div v-for="(education, index) in educations" :key="index"
             class="education-card bg-dark-blue rounded-lg shadow-md p-6">
          <div class="flex gap-8 justify-between items-center">
            <div>
              <h3 class="text-xl font-semibold mb-2">{{ education.degree }}</h3>
              <p class="text-gray-700">{{ education.institution }}</p>
              <p class="text-gray-500">{{ education.period }}</p>
            </div>
            <img :class="education.logoStyle" :src="education.logo" :alt="education.institution + ' logo'">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import vuLogo from '@assets/vu.svg'
import uvaLogo from '@assets/uva.svg'

const educations = [
  {
    degree: 'MSc Software Engineering',
    institution: 'University of Amsterdam',
    period: 'Sep 2023 — Aug 2024',
    logo: uvaLogo,
    logoStyle: 'max-w-20 max-h-20 mt-2'
  },
  {
    degree: 'BSc Computer Science, Cum Laude',
    institution: 'Vrije Universiteit Amsterdam',
    period: 'Sep 2020 — Aug 2023',
    logo: vuLogo,
    logoStyle: 'max-w-32 max-h-32 pt-1'
  }
];
</script>

<style scoped>

.education-card {
  transition: transform 0.3s;
}

.education-card:hover {
  transform: scale(1.05);
}
</style>
