<!-- eslint-disable no-console -->
<!-- eslint-disable max-len -->
<template>
  <!-- for HOME PAGE -->
  <div class="container">

    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" style='background-color:#001d64'>
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="../assets/CataML450-logos_white.png" class="d-inline-block" style='object-fit:cover;height:40px'
            alt="">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="nav-link" :class="{ active: idx == navBarSelected }" v-for="x, idx of navBarTextsBadges" :key="idx"
              :href="x[1]">{{ x[0] }}
            </a>
            <a class="nav-link" target="_blank" href='https://opencatalystproject.org/'>OCP<i
                class="fa fa-external-link"></i>
            </a>
          </div>
        </div>
      </div>
    </nav>

    <h1>Intro</h1>
    <p>This is an online tool that use pre-trained machine learning models to predict the molecular adsorption
      energy
      and force.</p>
    <video id="video" width="40%" class="center" onclick="play();">
      <source src="../assets/system.mp4" type="video/mp4" />
    </video>

    <h2>Step 1: Choose the category of your catalyst</h2>
    <p>Traditional methods all focus on training a general model across all types of catalyst. However, considering
      the fact that catalyst with similar types or combinations of certain atoms tend to have similar chemical
      characteristics, we use clustering to partition the metallic catalyst into 5 subgroups, and apply separate
      gemnet models for each group respectively.</p>
    <img src="../assets/catalyst categories.jpg" width="70%" class="center">
    <p>Category: {{ selected.text }}</p>
    <select class="form-select" aria-label="Default select example" v-model="selected">
      <option v-for="(product, index) in products" v-bind:key=index
        v-bind:value="{ id: product.id, text: product.name }">{{ product.name }}
      </option>
    </select>

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
    <label>CIF File:
        <input type="file" @change="handleFileUpload( $event )"/>
      </label>

    <!-- <h2>Step 3: Enter the formula of adsorbate</h2>
      For example, C3H8.
      <input class="form-control form-control-lg" type="text" placeholder="adsorbate">
      </br> -->

    <h2>Step 3: Predict the energy and force</h2>
    <button class="btn btn-primary" v-on:click="getPredict()">Predict</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home-page',
  data() {
    return {
      file: '',
      msg: '',
      navBarTextsBadges: [['Home', '/'], ['Help', 'help']],
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
      const formData = new FormData();
      formData.append('cif_file', this.file);
      formData.append('id', 'hi!');
      const path = 'http://localhost:5000/predict';
      console.log('getPredict');
      axios.post(
        path,
        formData,
        {
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': true,
            'Content-Type': 'multipart/form-data',
          },
        },
      ).then((response) => {
        console.log('SUCCESS!!');
        console.log(response);
      })
        .catch(() => {
          console.log('FAILURE!!');
        });
    },

    handleFileUpload(event) {
      console.log('handleFileUpload');
      // eslint-disable-next-line prefer-destructuring
      this.file = event.target.files[0];
    },
  },
};
</script>

<style>
.navbar {
  font-family: 'Josefin Sans';
  font-size: 20px;
}

.container {
  width: 70%;
  position: relative;
  top: 100px;
  font-family: 'Josefin Sans';
}

.container img {
  margin-top: 10px;
  margin-bottom: 10px;
}

.container h2 {
  margin-top: 20px;
  margin-bottom: 10px;
}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

body {
  /* background-image: url('assets/outdoor.jpg'); */
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  font-family: 'Josefin Sans';
}

p {
  font-size: 20px;
}
</style>
