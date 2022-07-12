<!-- eslint-disable no-console -->
<!-- eslint-disable max-len -->
<template>
    <!-- for HOME PAGE -->
    <div class="container">

        <h1>Intro</h1>
        <p>This is an online tool that use pre-trained machine learning models to predict the molecular adsorption
            energy
            and force.</p>
        <video id="video" width="40%" class="center" onclick="play();">
            <source src="../assets/system.mp4" type="video/mp4" />
        </video>

        <br>

        <h2>Step 1: Choose the category of your catalyst</h2>
        <p>Traditional methods all focus on training a general model across all types of catalyst. However, considering
            the fact that catalyst with similar types or combinations of certain atoms tend to have similar chemical
            characteristics, we use clustering to partition the metallic catalyst into 5 subgroups, and apply separate
            gemnet models for each group respectively.</p>
        <img src="../assets/catalyst categories.jpg" width="70%" class="center">
        <p>Category: {{ selected.text }}</p>
        <select class="form-select" aria-label="Default select example" v-model="selected">
            <option v-for="(product,index) in products" v-bind:key=index v-bind:value="{ id: product.id, text: product.name }">{{ product.name }}
            </option>
        </select>

        <br>

        <h2>Step 2: Upload the atom structure of catalyst</h2>
        <p>We support CIF (Crystallographic Information File) format. You can generate CIF file from <a
                href="https://materialsproject.org/materials">Material
                Project</a>. First, search
            for materials information by chemistry, composition, or property. Here we search for "Cu".
            <img src="../assets/screenshot_-1.png" width="70%" class="center">
            Then, pick the matertial you want in the matching search results. Here we pick the first one with ID mp-30.
            <img src="../assets/screenshot_0.png" width="70%" class="center">
            Export the material sturcture as CIF and upload it.
            <img src="../assets/screenshot_1.png" width="70%" class="center">
        </p>
        <input type="file" class="form-control" id="customFile" />
        <br>

        <!-- <h2>Step 3: Enter the formula of adsorbate</h2>
      For example, C3H8.
      <input class="form-control form-control-lg" type="text" placeholder="adsorbate">
      </br> -->

        <h2>Step 3: Predict the energy and force</h2>
        <button class="btn btn-primary" v-on:click="getPredict">Predict</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home-page',
  data() {
    return {
      msg: '',
      navBarTextsBadges: [['Home', 'index.html'], ['Help', 'help.html']],
      navBarSelected: 0,
      selected: '',
      products: [
        { id: 0, name: 'All (default)' },
        { id: 1, name: 'Pure metals' },
        { id: 2, name: 'Multi-metallic (1-3 metals)' },
        { id: 3, name: 'Intermetallic (ordered multimetallic)' },
        { id: 4, name: 'Overlayer (thin layers of metal applied to the surface)' },
        { id: 5, name: 'High-entropy (more than 3 metals)' },
      ],
    };
  },
  created() {
    console.log('propertyComputed will update, as this.property is now reactive.');
  },
  methods: {
    getPredict() {
      const path = 'http://localhost:5000/predict';
      console.log('getPredict');
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .then(() => {
          console.log(this.msg);
        })
        .catch((error) => {
          // eslint-disable-next-line
                    console.error(error);
        });
    },
  },
};
</script>
