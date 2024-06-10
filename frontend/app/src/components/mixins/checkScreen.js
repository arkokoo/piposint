export default {
  data() {
    return {
      windowWidth: null,
      mobileNav: false,
      mobile: true,
    };
  },
  created() {
    window.addEventListener('resize', this.checkScreen);
    this.checkScreen();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreen);
  },
  methods: {
    checkScreen() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth <= 826) {
        this.mobile = true;
        return;
      } else {
        this.mobile = false;
        this.mobileNav = false;
        return;
      }
    },
  },
};