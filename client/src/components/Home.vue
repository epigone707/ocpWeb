<!-- eslint-disable no-console -->
<!-- eslint-disable max-len -->
<template>
  <!-- for HOME PAGE -->
  <div class="container">

    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" style='background-color:#001d64'>
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="../assets/CataML450-logos_white.png" class="d-inline-block" style='object-fit:cover;height:50px'
            alt="">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="nav-link" :class="{ active: idx == navBarSelected }" v-for="x, idx of navBarTextsBadges"
              :key="idx" :href="x[1]">{{ x[0] }}
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
      energy, relaxed energy and per-atom forces.</p>
    <video id="video" width="40%" class="center" onclick="play();">
      <source src="../assets/system.mp4" type="video/mp4" />
    </video>

    <h2>Step 1: Choose the category of your catalyst</h2>
    <p>Traditional methods focus on training a general model across all types of catalyst. However, considering
      the fact that catalyst with similar types or combinations of certain atoms tend to have similar chemical
      characteristics, we use clustering to partition the metallic catalyst into 2 subgroups, and apply separate
      gemnet models for each group respectively.</p>
    <!-- <img src="../assets/catalyst categories.jpg" width="70%" class="center"> -->
    <p>Category: {{ selected.text }}</p>
    <select class="form-select" aria-label="Default select example" v-model="selected">
      <option v-for="(product, index) in products" v-bind:key=index
        v-bind:value="{ id: product.id, text: product.name }">{{ product.name }}
      </option>
    </select>

    <h2>Step 2: Upload the atoms structure of catalyst</h2>
    <p>We support <a
        href="https://web.archive.org/web/20190811094343/https://libatoms.github.io/QUIP/io.html#extendedxyz">extended
        XYZ (a.k.a. extxyz) format</a>. Extended XYZ format is an enhanced version of the <a
        href="http://en.wikipedia.org/wiki/XYZ_file_format">basic XYZ format</a>
      that allows extra columns to be present in the file for additonal per-atom properties as
      well as standardising the format of the comment line to include the
      cell lattice and other per-frame parameters.</p>
    <p>It's easiest to describe the format with an example. Below is a extxyz file example, which is a valid input to
      our back-end
      ML models. Don't worry, we will teach you the meaning of each line
      so that you can design the catalyst and adsorbate molecules on your own!
    </p>
    <pre><code>71
Lattice="9.18446134 0.0 0.0 0.0 22.63986204 -4.15391219 0.0 0.0 29.07738533" Properties=species:S:1:pos:R:3:move_mask:L:1:tags:I:1 pbc="T T T"
Ca       0.00000000       1.59977838      13.75983413  F        0
Ca       0.00000000      12.91970940       9.60592198  F        0
Ca       2.29611534       4.05467998      11.68287816  F        0
Ca       2.29611534      15.37461100      11.68287812  F        0
Ca       0.00000000       7.25974389      11.68287791  F        0
Ca       0.00000000      18.57967491       7.52896576  F        0
Ca       2.29611534       9.71464549       9.60592194  F        0
Ca       2.29611534      21.03457651       9.60592190  F        0
Ca       9.17763995       1.59095314      17.69283799  T        1
Ca       0.00000000      12.91970940      13.75983409  F        0
Ca       2.29611534       4.05467998      15.83679027  F        0
Ca       2.29066491      15.28372395      15.68350401  T        1
Ca       9.18348026       7.34652543      15.63808273  T        1
Ca       0.00000000      18.57967491      11.68287816  F        0
Ca       2.29611534       9.71464549      13.75983405  F        0
Ca       2.54997008      20.99736767      13.92455556  T        1
Ca       4.59223067       1.59977838      13.75983413  F        0
Ca       4.59223067      12.91970940       9.60592198  F        0
Ca       6.88834601       4.05467998      11.68287816  F        0
Ca       6.88834601      15.37461100      11.68287812  F        0
Ca       4.59223067       7.25974389      11.68287791  F        0
Ca       4.59223067      18.57967491       7.52896576  F        0
Ca       6.88834601       9.71464549       9.60592194  F        0
Ca       6.88834601      21.03457651       9.60592190  F        0
Ca       4.58193103       1.46827135      17.85365541  T        1
Ca       4.59223067      12.91970940      13.75983409  F        0
Ca       6.88834601       4.05467998      15.83679027  F        0
Ca       6.88545014      15.25889504      15.65682260  T        1
Ca       4.59315922       7.34715006      15.63644330  T        1
Ca       4.59223067      18.57967491      11.68287816  F        0
Ca       6.88834601       9.71464549      13.75983405  F        0
Ca       6.61873210      21.03855048      13.78417394  T        1
Cu       2.29611534       0.77843498      11.68287816  F        0
Cu       2.29611534      12.09836600      11.68287812  F        0
Cu       2.29611534       6.43840049       9.60592194  F        0
Cu       2.29611534      17.75833151       9.60592190  F        0
Cu       2.29611534       0.77843498      15.83679027  F        0
Cu       2.29701918      12.15035075      15.62754869  T        1
Cu       2.29611534       6.43840049      13.75983405  F        0
Cu       2.32833957      17.85936620      13.98529752  T        1
Cu       6.88834601       0.77843498      11.68287816  F        0
Cu       6.88834601      12.09836600      11.68287812  F        0
Cu       6.88834601       6.43840049       9.60592194  F        0
Cu       6.88834601      17.75833151       9.60592190  F        0
Cu       6.88834601       0.77843498      15.83679027  F        0
Cu       6.88928190      12.13354857      15.62561480  T        1
Cu       6.88834601       6.43840049      13.75983405  F        0
Cu       6.87812517      17.71723110      13.65923797  T        1
Ag       0.00000000       4.88703790       9.60592198  F        0
Ag       0.00000000      16.20696892       9.60592194  F        0
Ag       0.00000000      10.54700341      11.68287787  F        0
Ag       0.00000000      21.86693443       7.52896572  F        0
Ag       0.00000000       4.88703790      13.75983409  F        0
Ag       0.01753167      16.23838218      13.82017581  T        1
Ag       0.00680367      10.61766016      15.85136871  T        1
Ag       0.00000000      21.86693443      11.68287812  F        0
Ag       4.59223067       4.88703790       9.60592198  F        0
Ag       4.59223067      16.20696892       9.60592194  F        0
Ag       4.59223067      10.54700341      11.68287787  F        0
Ag       4.59223067      21.86693443       7.52896572  F        0
Ag       4.59223067       4.88703790      13.75983409  F        0
Ag       4.57866733      16.22220623      13.82969226  T        1
Ag       4.58642150      10.61732735      15.85150247  T        1
Ag       4.59223067      21.86693443      11.68287812  F        0
C        1.30185946      19.36114296      16.43787420  T        2
C        2.36653517      18.99328301      15.66234078  T        2
H        1.39650304      19.70137209      17.48632911  T        2
H        0.26855034      19.29583420      16.06379907  T        2
H        4.62397042      22.04645541      15.86336363  T        2
H        3.34254960      19.08643970      16.18832954  T        2
O        4.61136328      22.03688418      14.88235297  T        2</code></pre>
    <p>The first line is the number of atoms. In the example, "71" means there're totally 71 atoms in the catalyst
      molecule and adsobate molecule.</p>
    <p>The second line is a series of
      key/value pairs. The keys should be strings and values can be
      integers, reals, bools (denoted by <code>T</code> and <code>F</code> for true and false)
      or strings. Quotes are required if a value contains any spaces (like
      <code>Lattice</code> above).
    </p>

    <p>There are two mandatory parameters: <code>Lattice</code> and <code>Properties</code>.</p>
    <p>
      <code>Lattice</code> is a Cartesian 3x3 matrix representation of the cell
      vectors, with each vector stored as a column and the 9 values listed in
      Fortran column-major order, i.e. in the form :
    </p>
    <pre><code>Lattice=&quot;R1x R1y R1z R2x R2y R2z R3x R3y R3z&quot;</code></pre>
    <p>
      where <code>R1x R1y R1z</code> are the Cartesian x-, y- and z-components of the
      first lattice vector, <code>R2x R2y R2z</code> those of the second
      lattice vector and <code>R3x R3y R3z</code> are those of the
      third lattice vector.</p>

    <p>
      The list of properties in the file is described by the <code>Properties</code>
      parameter, which should take the form of a series of colon separated
      triplets giving the name, format (<code>S</code> for string, <code>R</code> for real number, <code>L</code> for
      bool, <code>I</code> for integer) and
      number of columns of each property. For example:</p>
    <pre><code>Properties=species:S:1:pos:R:3:move_mask:L:1:tags:I:1 pbc="T T T"</code></pre>
    <p>
      indicates the first column represents atomic species, the next three
      columns represent atomic positions, the next one column defines whether you want to mask the atom, and the
      last column is an single integer called <code>tags</code>. If the atom is in the catalyst and below surface,
      <code>tags</code> should be set to 0. If the atom is on the catalyst surface, set to 1. If the atom is adsorbate,
      set to 2. Since we only want the predicted forces for surface atoms (<code>tags=1</code>) and adsorbate atoms
      (<code>tags=2</code>), we set their
      <code>move_mask</code> to be <code>T</code> (True).
    </p>
    <p>According to <a href="https://github.com/Open-Catalyst-Project/ocp">OCP instructions</a>, we don't need
      to care about <code>pbc</code>, just simply set it to <code>"T T T"</code>.

    </p>
    <p>
      With this property definition, the line :
    </p>
    <pre><code>Ca       0.00000000       1.59977838      13.75983413  F        0</code></pre>
    <p>
      would describe a calcium atom at position (0.00000000, 1.59977838, 13.75983413) and it is under the catalyst
      surface.</p>
    <p>To give you a better understanding of the structure of this catalyst+adsorbate example, here is a visualization
      generated by <a href="https://wiki.fysik.dtu.dk/ase/ase/visualize/visualize.html">ase gui</a>. The four small white
      atoms are H atoms. The two small grey atoms are C atoms. The red atom is O atom.</p>
    <img src="../assets/71Ca.png" class="center" style='object-fit:cover;' alt="">
    <img src="../assets/71Ca_view.png" class="center" style='object-fit:cover;' alt="">
    <br>
    <p>Now you can create a txt file, type in your catalyst and adsorbate data as above, and change the
      file extension from txt to extxyz.</p>
    <p>Uploud your extxyz file:</p>
    <label>
      <input type="file" @change="handleFileUpload($event)" />
    </label>

    <h2>Step 3: Predict the energy and forcea</h2>
    <p>Please be patient, it may take 1-2 minutes to generate the results. Note that we will only show the forces result
      of those atoms that you set <code>move_mask</code> to be <code>T</code></p>
    <button class="btn btn-primary" v-on:click="getPredict()">Predict</button>
    <p>{{ results.text }}</p>
    <div v-if="results.MAE_energy != 'N/A'">
      <p>
        Relaxed Energy: {{ results.energy }} (Unit: eV)
      </p>
      <p>Per-atom Forces: (Unite: eV/å)</p>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Atom Index</th>
            <th>Force(x direction)</th>
            <th>Force(y direction)</th>
            <th>Force(z direction)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in results.force" :key="i">
            <th scope="row">{{ i }}</th>
            <td>{{ item[0] }}</td>
            <td>{{ item[1] }}</td>
            <td>{{ item[2] }}</td>
          </tr>
        </tbody>
      </table>
      <p>
        MAE: {{ results.MAE }} (Unit: eV)
      </p>
      <p>Visualization:</p>
      <img :src="results.img_1" alt=""/>

    </div>

    <br>
    <br>
    <br>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home-page',

  data() {
    return {
      results: {
        text: 'Click the "predict" button to show the result.',
        energy: 'N/A',
        force: [['N/A', 'N/A', 'N/A']],
        img_1: '',
        MAE: 'N/A',
      },
      file: '',
      msg: '',
      navBarTextsBadges: [['Home', '/'], ['Help', 'help']],
      navBarSelected: 0,
      selected: '',
      products: [
        { id: 0, name: 'All (default)' },
        { id: 1, name: 'Metallic' },
        { id: 2, name: 'Non-metallic' },
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
      this.results.energy = 'Loading...';
      this.results.force = ['Loading...'];
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
        this.results.text = 'Predicted Results:';
        this.results.energy = response.data.energy;
        this.results.force = response.data.force;
        this.results.img_1 = response.data.img_1;
      })
        .catch((error) => {
          console.log('FAILURE!!');
          console.log(error);
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

pre code {
  background-color: #eee;
  display: block;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 15px;
  padding-right: 15px;
  border-radius: 5px;
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
