// node rendre.js overlay.json ut.mov [t1,t2,... for stillbilder]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { spawn } = require('child_process');
(async () => {
  const [jf, ut, only] = process.argv.slice(2); const D = JSON.parse(fs.readFileSync(jf)); const n = Math.round(D.lengde * 30);
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'overlay.html')); await p.evaluate(d => window.init(d), D); await p.waitForTimeout(500);
  if (only) { for (const t of only.split(',').map(Number)) { await p.evaluate(t => window.render(t), t);
      await p.screenshot({ path: path.join(path.dirname(jf), 'tmp', `ov_${t}.png`), omitBackground: true }); } await b.close(); return; }
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', '30', '-i', '-', '-c:v', 'qtrle', ut]);
  for (let f = 0; f < n; f++) { await p.evaluate(t => window.render(t), f / 30); const buf = await p.screenshot({ omitBackground: true });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('overlay ferdig', n);
})();
