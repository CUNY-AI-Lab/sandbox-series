'use strict';
// Execute the real deck engine against a minimal DOM, then test input behavior.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
class Element {
 constructor(tag='div'){this.tagName=tag;this.children=[];this.attrs={};this.dataset={};this.handlers={};this.textContent='';this.classes=new Set();this.classList={toggle:(c,on)=>on?this.classes.add(c):this.classes.delete(c)};}
 append(...xs){for(const x of xs){x.parent=this;this.children.push(x);}}
 setAttribute(k,v){this.attrs[k]=String(v);} removeAttribute(k){delete this.attrs[k];} getAttribute(k){return this.attrs[k];}
 addEventListener(k,fn){this.handlers[k]=fn;} focus(){doc.activeElement=this;}
 contains(el){return el===this||this.children.some(c=>c.contains(el));}
 querySelectorAll(selector){return this.children.flatMap(c=>[...(selector==='button'&&c.tagName==='button'?[c]:[]),...c.querySelectorAll(selector)]);}
 closest(selector){let el=this;while(el){if(selector.split(',').some(s=>s===el.tagName||(s==='.prompt-block'&&el.classes.has('prompt-block'))||(s==='[contenteditable="true"]'&&el.attrs.contenteditable==='true')))return el;el=el.parent;}return null;}
 showModal(){this.open=true;} close(){this.open=false;}
}
const ids=Object.fromEntries(['slide-progress','slide-announcer','outline-dialog','outline-list','nav-total','nav-current','arrow-prev','arrow-next','overview-button','close-outline'].map(x=>[x,new Element(x.includes('button')||x.startsWith('arrow')?'button':'div')]));
const slides=Array.from({length:3},(_,i)=>{const s=new Element('section');s.dataset.title='Slide '+(i+1);s.setAttribute('aria-label','Slide '+(i+1));return s;});
const prompt=new Element('pre');prompt.classes.add('prompt-block');prompt.textContent='Exact prompt\nwith original spacing.';ids.prompt=prompt;slides[0].append(prompt);
const copy=new Element('button');copy.dataset.copy='prompt';copy.textContent='Copy prompt';slides[0].append(copy);
const selection={isCollapsed:true,removeAllRanges(){this.isCollapsed=true;},addRange(range){this.isCollapsed=false;this.node=range.node;}};
const documentHandlers={},windowHandlers={};let clipboardText='';
const doc={activeElement:null,querySelectorAll:s=>s==='.slide'?slides:s==='[data-copy]'?[copy]:[],getElementById:id=>ids[id],createElement:tag=>new Element(tag),querySelector:s=>s==='dialog[open]'&&ids['outline-dialog'].open?ids['outline-dialog']:null,addEventListener:(k,fn)=>documentHandlers[k]=fn,createRange:()=>({selectNodeContents(n){this.node=n;}})};
const context={document:doc,window:{getSelection:()=>selection,addEventListener:(k,fn)=>windowHandlers[k]=fn},location:{hash:'#1'},history:{replaceState(_s,_t,hash){context.location.hash=hash;}},navigator:{clipboard:{writeText:async text=>{clipboardText=text;}}},setTimeout:()=>{},console};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../js/deck-engine.js'),'utf8'),context);
const engine=context.window.deckEngine;
function key(name,extra={}){const e={key:name,target:new Element('div'),preventDefault(){this.prevented=true;},...extra};documentHandlers.keydown(e);return e;}
let checks=0;function check(fn){fn();checks++;}
(async()=>{
 check(()=>assert.equal(engine.totalSlides(),3));
 check(()=>{key('ArrowRight');assert.equal(engine.currentSlide(),1);assert.equal(ids['slide-progress'].value,2);});
 check(()=>{key('End');key('ArrowRight');assert.equal(engine.currentSlide(),2);});
 check(()=>{key('Home');key('ArrowLeft');assert.equal(engine.currentSlide(),0);});
 for(const k of ['ArrowRight','ArrowLeft','PageDown','PageUp','Home','End',' '])check(()=>{engine.goTo(1);selection.isCollapsed=false;key(k);assert.equal(engine.currentSlide(),1,k);selection.isCollapsed=true;});
 for(const modifier of ['shiftKey','altKey','ctrlKey','metaKey'])check(()=>{engine.goTo(1);key('ArrowRight',{[modifier]:true});assert.equal(engine.currentSlide(),1,modifier);});
 for(const tag of ['input','textarea','select'])check(()=>{engine.goTo(1);key('ArrowRight',{target:new Element(tag)});assert.equal(engine.currentSlide(),1,tag);});
 check(()=>{const el=new Element();el.attrs.contenteditable='true';key('End',{target:el});assert.equal(engine.currentSlide(),1);});
 check(()=>{key('Escape');assert.equal(ids['outline-dialog'].open,true);key('ArrowRight');assert.equal(engine.currentSlide(),1);ids['outline-dialog'].close();});
 for(const k of [' ','Home','End','ArrowDown'])check(()=>{engine.goTo(0);key(k,{target:prompt});assert.equal(engine.currentSlide(),0,k);});
 for(const tag of ['a','button'])check(()=>{engine.goTo(0);key(' ',{target:new Element(tag)});assert.equal(engine.currentSlide(),0,tag);});
 check(()=>{ids['slide-progress'].value='3';ids['slide-progress'].handlers.input();assert.equal(engine.currentSlide(),2);});
 check(()=>{ids['outline-list'].querySelectorAll('button')[1].handlers.click();assert.equal(engine.currentSlide(),1);assert.equal(doc.activeElement,ids['overview-button']);});
 await copy.handlers.click();check(()=>{assert.equal(clipboardText,prompt.textContent);assert.equal(ids['slide-announcer'].textContent,'Prompt copied');});
 context.navigator.clipboard=undefined;await copy.handlers.click();check(()=>{assert.equal(selection.node,prompt);assert.equal(selection.isCollapsed,false);});
 check(()=>{const before=engine.currentSlide();key('ArrowRight');assert.equal(engine.currentSlide(),before);});
 console.log(`Passed ${checks} deck interaction checks, including selection, modifiers, editable fields, slider, Outline, copy, and copy fallback.`);
})().catch(e=>{console.error(e);process.exitCode=1;});
