const fs = require("fs");

const srcPath = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition_overlay.html";
let html = fs.readFileSync(srcPath, "utf-8");

html = html.replace(
  `  #bg-plate {`,
  `  #bg-plate { display: none !important;`
);

html = html.replace(
  `  #cinematic-vignette {`,
  `  #cinematic-vignette { display: none !important;`
);

fs.writeFileSync(srcPath, html);
console.log("Hidden #bg-plate and #cinematic-vignette in composition_overlay.html!");
