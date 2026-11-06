const { chromium } = require('playwright'); const fs = require('fs'); const { spawn } = require('child_process');
(async () => {
  const D = JSON.parse(fs.readFileSync('overlay.json')); const n = Math.round(D.lengde * 30);
  const only = process.argv[2] ? process.argv[2].split(',').map(Number) : null;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + process.cwd() + '/overlay.html'); await p.evaluate(d => window.init(d), D); await p.waitForTimeout(500);
  if (only) { for (const t of only) { await p.evaluate(t => window.render(t), t); await p.screenshot({ path: `ov_${t}.png`, omitBackground: true }); } await b.close(); return; }
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', '30', '-i', '-', '-c:v', 'qtrle', 'overlay.mov']);
  for (let f = 0; f < n; f++) { await p.evaluate(t => window.render(t), f / 30); const buf = await p.screenshot({ omitBackground: true }); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('overlay ferdig', n);
})();
