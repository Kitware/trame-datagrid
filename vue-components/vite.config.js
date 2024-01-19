export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "trame_datagrid",
      formats: ["umd"],
      fileName: "trame_datagrid",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../trame_datagrid/module/serve",
    assetsDir: ".",
  },
};
