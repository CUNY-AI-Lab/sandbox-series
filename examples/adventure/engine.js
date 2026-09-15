/* Deterministic text-adventure engine. No network, storage, or dynamic code. */
(function (root) {
  'use strict';
  function validate(s) {
    if (!s || typeof s !== 'object' || Array.isArray(s)) throw Error('Scenario must be an object.');
    for (const key of ['title', 'introduction', 'start']) if (typeof s[key] !== 'string' || !s[key].trim() || s[key].length > 3000) throw Error('Invalid ' + key + '.');
    if (!s.rooms || typeof s.rooms !== 'object' || Array.isArray(s.rooms)) throw Error('Rooms are required.');
    const ids = Object.keys(s.rooms);
    if (ids.length < 2 || ids.length > 12 || !ids.includes(s.start)) throw Error('Use 2–12 rooms and a valid start.');
    const items = new Set();
    for (const id of ids) {
      if (!/^[a-z][a-z0-9_-]{0,39}$/.test(id)) throw Error('Invalid room ID.');
      const r = s.rooms[id];
      if (!r || typeof r.name !== 'string' || typeof r.description !== 'string' || !r.name.trim() || !r.description.trim() || r.name.length > 100 || r.description.length > 3000) throw Error('Invalid room text.');
      if (!r.exits || typeof r.exits !== 'object' || Array.isArray(r.exits)) throw Error('Invalid exits.');
      for (const [direction, target] of Object.entries(r.exits)) if (!['north','south','east','west','up','down'].includes(direction) || !ids.includes(target)) throw Error('Invalid exit.');
      if (!Array.isArray(r.items) || r.items.length > 12) throw Error('Invalid items.');
      for (const item of r.items) {
        if (typeof item !== 'string' || !/^[a-z][a-z -]{0,39}$/.test(item) || items.has(item)) throw Error('Items need unique, plain names.');
        items.add(item);
      }
    }
    if (!Array.isArray(s.actions) || s.actions.length < 1 || s.actions.length > 30) throw Error('Use 1–30 actions.');
    const commands = new Set(), flags = new Set();
    for (const a of s.actions) {
      if (!a || typeof a.command !== 'string' || !/^[a-z][a-z -]{1,59}$/.test(a.command) || /^(go |take |look$|inventory$|help$|undo$|restart$|save$|load$|discuss$)/.test(a.command) || commands.has(a.command)) throw Error('Invalid or duplicate action command.');
      commands.add(a.command);
      if (!ids.includes(a.room) || typeof a.text !== 'string' || !a.text.trim() || a.text.length > 3000) throw Error('Invalid action.');
      for (const k of ['requires_items','requires_flags','sets_flags','clears_flags']) {
        if (!Array.isArray(a[k]) || a[k].length > 20 || a[k].some(x => typeof x !== 'string' || !/^[a-z][a-z0-9_ -]{0,39}$/.test(x))) throw Error('Invalid action condition.');
      }
      if (a.requires_items.some(x => !items.has(x))) throw Error('Action refers to an unknown item.');
      a.sets_flags.forEach(x => flags.add(x));
    }
    if (!Array.isArray(s.goal_flags) || !s.goal_flags.length || s.goal_flags.length > 20 || s.goal_flags.some(x => !flags.has(x))) throw Error('Goal needs reachable flag names.');
    for (const a of s.actions) if (a.requires_flags.concat(a.clears_flags).some(x => !flags.has(x))) throw Error('Unknown flag condition.');
    const seen = new Set([s.start]), queue = [s.start];
    while (queue.length) for (const next of Object.values(s.rooms[queue.shift()].exits)) if (!seen.has(next)) {seen.add(next); queue.push(next);}
    if (seen.size !== ids.length) throw Error('Every room must be reachable from start.');
    return s;
  }
  function create(s) {
    validate(s);
    return {room:s.start, inventory:[], flags:[], taken:[], commands:[], events:[], complete:false};
  }
  function describe(s, state) {
    const r=s.rooms[state.room], items=r.items.filter(x=>!state.taken.includes(x));
    return r.name+'\n'+r.description+'\nExits: '+Object.keys(r.exits).join(', ')+(items.length?'\nYou see: '+items.join(', '):'');
  }
  function act(s, old, input) {
    const state=JSON.parse(JSON.stringify(old));
    let command=String(input).trim().toLowerCase().replace(/\s+/g,' '), text='', valid=true;
    const aliases={n:'go north',s:'go south',e:'go east',w:'go west',u:'go up',d:'go down',i:'inventory',l:'look'};
    command=Object.hasOwn(aliases,command)?aliases[command]:command;
    if (command==='look') text=describe(s,state);
    else if (command==='inventory') text='Inventory: '+(state.inventory.join(', ')||'empty');
    else if (command==='help') {const actions=s.actions.filter(a=>a.room===state.room).map(a=>a.command);text='look · inventory · go [direction] · take [item]\nundo — reverse one move\nrestart — begin again\nsave — download play record\nload — restore saved record\ndiscuss — place record in chat'+(actions.length?'\n\nActions here: '+actions.join(', '):'');}
    else if (command.startsWith('go ')) {
      const exits=s.rooms[state.room].exits, direction=command.slice(3);
      const target=Object.hasOwn(exits,direction)?exits[direction]:null;
      if (!target) {valid=false;text='No exit in that direction.';}
      else {state.room=target;text=describe(s,state);}
    } else if (command.startsWith('take ')) {
      const item=command.slice(5);
      if (!s.rooms[state.room].items.includes(item)||state.taken.includes(item)) {valid=false;text='That item is not here.';}
      else {state.inventory.push(item);state.taken.push(item);text='Taken: '+item+'.';}
    } else {
      const a=s.actions.find(a=>a.command===command&&a.room===state.room);
      if (!a) {valid=false;text='Unknown action here. Type help to see available commands.';}
      else if (a.requires_items.some(x=>!state.inventory.includes(x))) {valid=false;text='You need: '+a.requires_items.filter(x=>!state.inventory.includes(x)).join(', ')+'.';}
      else if (a.requires_flags.some(x=>!state.flags.includes(x))) {valid=false;text='Conditions are not ready. Examine earlier observations or try another action.';}
      else {
        state.flags=state.flags.filter(x=>!a.clears_flags.includes(x));
        for (const f of a.sets_flags) if (!state.flags.includes(f)) state.flags.push(f);
        text=a.text;
      }
    }
    state.complete=s.goal_flags.every(x=>state.flags.includes(x));
    state.commands.push(command);
    state.events.push({turn:state.commands.length,command,valid,room:state.room,text,flags:[...state.flags],inventory:[...state.inventory],complete:state.complete});
    return state;
  }
  function replay(s,commands) {
    if (!Array.isArray(commands)||commands.length>300||commands.some(c=>typeof c!=='string'||c.length>120)) throw Error('Invalid play record.');
    return commands.reduce((state,c)=>act(s,state,c),create(s));
  }
  root.Adventure={validate,create,describe,act,replay};
  if (typeof module!=='undefined'&&module.exports) module.exports=root.Adventure;
})(typeof globalThis!=='undefined'?globalThis:this);
