/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/image_gallery/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["dark"],
  },
};
