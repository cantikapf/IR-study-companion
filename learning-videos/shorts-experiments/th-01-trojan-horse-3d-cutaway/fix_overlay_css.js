const fs = require("fs");

const srcPath = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition_overlay.html";
let html = fs.readFileSync(srcPath, "utf-8");

html = html.replace(
  `  html, body {
    margin: 0;
    padding: 0;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    background-color: #050811;
    font-family: 'Space Grotesk', -apple-system, sans-serif;
  }`,
  `  html, body {
    margin: 0;
    padding: 0;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    background: transparent !important;
    background-color: transparent !important;
    font-family: 'Space Grotesk', -apple-system, sans-serif;
  }`
);

html = html.replace(
  `  #vignette {`,
  `  #vignette { display: none !important;`
);

fs.writeFileSync(srcPath, html);
console.log("Updated composition_overlay.html styling!");
