<template>
<!-- for testing -->
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping-pong',
  data() {
    return {
      msg: '',
    };
  },
  created() {
    console.log('propertyComputed will update, as this.property is now reactive.');
    this.getMessage();
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      console.log('getMessage');
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
