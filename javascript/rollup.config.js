import resolve from '@rollup/plugin-node-resolve';
import babel from '@rollup/plugin-babel';
import {terser} from 'rollup-plugin-terser';

// Ref: https://rollupjs.org/guide/en/#babel

export default {
  input: '', // Input .js file here
  output: {
    dir: '', // Output dir here
    format: 'es', // Change format accordingly
    plugins: [
      terser({
        mangle: false, // Do you want terser to mangle your variables?
      }),
    ],
  },
  plugins: [
    resolve(),
    babel({babelHelpers: 'bundled'}),
  ],
};
