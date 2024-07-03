async function fetchHandler(url, vueContext) {
    vueContext.error.code = null;
    vueContext.error.message = '';
    try {
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        // SI on est deja dans result, on remplace les données
        if (vueContext.$route.name === 'Result') {
            vueContext.$router.replace({ name: 'Result', params: { data: btoa(encodeURIComponent(JSON.stringify(data))) } });
        }
        else {
            vueContext.$router.push({ name: 'Result', params: { data: btoa(encodeURIComponent(JSON.stringify(data))) } });
        }
      } else {
        vueContext.error.code = response.status;
        vueContext.error.message = response.statusText;
      }
    } catch (err) {
      vueContext.error.code = 500;
      console.error(err);
      vueContext.error.message = 'Internal server error';
    }
  }
  
  export { fetchHandler };