/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/todo_app/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["dark"],
  },
};
