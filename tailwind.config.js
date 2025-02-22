/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}","./node_modules/tw-elements/dist/js/**/*.js",      'node_modules/preline/dist/*.js',],
  theme: {
    extend: { fontFamily: {
      Montserrat: ['Montserrat', "sans-serif"], 
     }},
  },
  plugins: [      require('tailwindcss'),
  require('autoprefixer')
],
}
