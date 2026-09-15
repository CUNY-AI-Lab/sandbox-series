const assert=require('node:assert/strict'),fs=require('node:fs');
const A=require('./engine.js'),s=JSON.parse(fs.readFileSync(__dirname+'/prism.json','utf8'));
const win=['go north','take prism','take screen','go south','go east','open shutter','use prism','use screen','test red light','record result'];
assert.equal(A.replay(s,win).complete,true);
assert.equal(A.replay(s,['go east','record result']).complete,false);
assert.equal(A.replay(s,['go north','take prism','take prism']).inventory.length,1);
assert.equal(A.replay(s,['go east','use prism']).events.at(-1).valid,false);
for(const command of ['constructor','__proto__','go constructor','go __proto__','unknown','take missing']) assert.equal(A.replay(s,[command]).events[0].valid,false);
assert.deepEqual(A.replay(s,win),A.replay(s,win));
assert.equal(A.replay(s,win.slice(0,-1)).complete,false);
assert.equal(A.replay(s,win.concat('close shutter')).complete,false);
assert.equal(A.create(s).commands.length,0);
assert.throws(()=>A.replay(s,Array(301).fill('look')));
const bad=JSON.parse(JSON.stringify(s));bad.rooms.study.exits.north='missing';assert.throws(()=>A.validate(bad));
const invalid=JSON.parse(JSON.stringify(s));invalid.actions[0].requires_items=['missing'];assert.throws(()=>A.validate(invalid));
const saved=JSON.parse(JSON.stringify({scenario:s,commands:win,result:{complete:false}}));assert.equal(A.replay(saved.scenario,saved.commands).complete,true);
console.log('Passed win, prerequisites, duplicate inventory, invalid/prototype commands, deterministic replay, undo replay, reset, closed-shutter state, record limits, invalid references, and untrusted saved-result checks.');

const extension = require("./aperture.json");

assert.equal(A.replay(extension, win).complete, false);
assert.equal(A.replay(extension, win.concat("narrow aperture")).complete, true);
assert.equal(A.replay(extension, ["go east", "narrow aperture"]).events.at(-1).valid, false);
console.log("Passed procedural extension completion and blocked aperture action.");
