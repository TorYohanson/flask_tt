var faviconCanvas = document.createElement('canvas');
faviconCanvas.width = 16;
faviconCanvas.height = 16;
var faviconContext = faviconCanvas.getContext('2d');
faviconContext.lineWidth = 2;

faviconContext.strokeStyle = "#01bBC2";
faviconContext.beginPath();
faviconContext.arc(8,8,6, 0 * Math.PI, 2 * Math.PI);
faviconContext.stroke();

faviconContext.lineCap = 'round';
faviconContext.strokeStyle = '#f1be32';
faviconContext.beginPath();
faviconContext.moveTo(2, 2);
faviconContext.lineTo(14, 14);
faviconContext.moveTo(14, 2);
faviconContext.lineTo(2, 14);
faviconContext.stroke();

var link = document.createElement('link');
link.type = 'image/x-icon';
link.rel = 'shortcut icon';
link.href = faviconCanvas.toDataURL("image/x-icon");
document.getElementsByTagName('head')[0].appendChild(link);