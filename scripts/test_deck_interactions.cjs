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
 setPointerCapture(id){this.capturedPointer=id;}
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
const swipeArea=new Element('span');
const doc={activeElement:null,querySelectorAll:s=>s==='.slide'?slides:s==='[data-copy]'?[copy]:[],getElementById:id=>ids[id],createElement:tag=>new Element(tag),querySelector:s=>s==='.nav-info'?swipeArea:s==='dialog[open]'&&ids['outline-dialog'].open?ids['outline-dialog']:null,addEventListener:(k,fn)=>documentHandlers[k]=fn,createRange:()=>({selectNodeContents(n){this.node=n;}})};
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
 selection.isCollapsed=true;
 const down=extra=>swipeArea.handlers.pointerdown({pointerId:1,isPrimary:true,button:0,clientX:150,clientY:50,...extra});
 const up=extra=>swipeArea.handlers.pointerup({pointerId:1,clientX:70,clientY:50,...extra});
 check(()=>{engine.goTo(0);down();up();assert.equal(engine.currentSlide(),1);});
 check(()=>{down();up({clientX:230});assert.equal(engine.currentSlide(),0);});
 check(()=>{down();up({clientX:150});assert.equal(engine.currentSlide(),0,'tap does not advance');});
 check(()=>{down();up({clientX:112});assert.equal(engine.currentSlide(),0,'short gesture does not advance');});
 check(()=>{down();up({clientX:145,clientY:180});assert.equal(engine.currentSlide(),0,'vertical scrolling does not advance');});
 check(()=>{down();up({clientY:115});assert.equal(engine.currentSlide(),0,'diagonal gesture does not advance');});
 check(()=>{down();swipeArea.handlers.pointercancel();up();assert.equal(engine.currentSlide(),0);});
 check(()=>{down();swipeArea.handlers.lostpointercapture();up();assert.equal(engine.currentSlide(),0);});
 check(()=>{down();up({pointerId:2});assert.equal(engine.currentSlide(),0);});
 check(()=>{down({isPrimary:false});up();assert.equal(engine.currentSlide(),0,'multiple fingers do not advance');});
 check(()=>{down({button:2});up();assert.equal(engine.currentSlide(),0);});
 check(()=>{down();ids['outline-dialog'].showModal();up();assert.equal(engine.currentSlide(),0);ids['outline-dialog'].close();});
 check(()=>{down();selection.isCollapsed=false;up();assert.equal(engine.currentSlide(),0,'selection is preserved');selection.isCollapsed=true;});
 check(()=>{down();up({clientX:230});assert.equal(engine.currentSlide(),0);engine.goTo(2);down();up();assert.equal(engine.currentSlide(),2,'swiping stops at deck bounds');});
 check(()=>{assert.equal(documentHandlers.pointerdown,undefined);assert.equal(prompt.handlers.pointerdown,undefined);});
 console.log(`Passed ${checks} deck interaction checks, including selection, keyboard navigation, slider, Outline, copy fallback, and scoped swiping.`);
})().catch(e=>{console.error(e);process.exitCode=1;});
