import resolve from '@rollup/plugin-node-resolve';
import babel from '@rollup/plugin-babel';
import {terser} from 'rollup-plugin-terser';

const skippedWarnings = new Set([
  'THIS_IS_UNDEFINED',
]);

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
  /**
   * Ref: https://github.com/rollup/rollup/issues/1518#issuecomment-321875784
   * @param {Object} warning
   * @param {Function} warn
   * @returns
   */
  onwarn(warning, warn) {
    // Skip certain warnings

    // should intercept ... but doesn't in some rollup versions
    if (skippedWarnings.has(warning.code)) { return; }

    warn(warning);
  },
};
