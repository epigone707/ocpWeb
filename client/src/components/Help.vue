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
            <a class="nav-link" :class="{active:idx==navBarSelected}" v-for="x,idx of navBarTextsBadges"
              :key="idx" :href="x[1]" >{{x[0]}}
            </a>
             <a class="nav-link" target="_blank"
              href='https://opencatalystproject.org/'>OCP<i
                class="fa fa-external-link"></i>
            </a>
          </div>
        </div>
      </div>
    </nav>

        <h1>Source Code</h1>
        <p>Below two links are our project's repos.</p>
        <li><a href="https://github.com/epigone707/ocpWeb">This website</a></li>
        <li><a href="https://github.com/PeterQiu0516/Catalyst-Rational-Design-through-AI">Machine Learning Model (adapted from gemnet)</a></li>

    </div>
</template>

<script>
export default {
  name: 'Help-page',
  data() {
    return {
      navBarTextsBadges: [['Home', '/'], ['Help', 'help']],
      navBarSelected: 1,
      selected: '',
    };
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

.container img{
    margin-top: 10px;
    margin-bottom: 10px;
}

.container h2{
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
