(()=>{const $=s=>document.querySelector(s);
const mb=$(".mb"),nv=$("#nv");mb.onclick=()=>{const o=nv.classList.toggle("open");mb.setAttribute("aria-expanded",o)};
document.querySelectorAll(".lang a").forEach(a=>a.addEventListener("click",()=>{try{localStorage.setItem("lang",a.dataset.l)}catch(e){}}));
const f=$("#qf");if(f)f.onsubmit=e=>{e.preventDefault();const n=f.n.value.trim(),p=f.p.value.trim(),s=$("#fs");
if(!n||!/^[+\d][\d\s()-]{6,}$/.test(p)){s.textContent=f.dataset.err;return}
const m=`${n} | ${p}\n${f.m.value.trim().slice(0,500)}`;window.open(f.dataset.wa+"?text="+encodeURIComponent(m),"_blank","noopener");s.textContent=f.dataset.ok};
const cp=$("#cp"),cl=$("#cl"),cq=$("#cq");$("#cb").onclick=()=>{cp.hidden=!cp.hidden;if(!cp.hidden)cq.focus()};
const tok=t=>{const w=t.toLowerCase().match(/[\p{L}\p{N}]+/gu)||[];const o=[];w.forEach(x=>/[\u4e00-\u9fff]/.test(x)?[...x].forEach(c=>o.push(c)):x.length>2&&o.push(x.slice(0,5)));return o};
const add=(t,c)=>{const p=document.createElement("p");p.textContent=t;if(c)p.className=c;cl.append(p);cl.scrollTop=1e9;return p};
const ask=q=>{if(!q.trim())return;add(q,"u");const qt=new Set(tok(q));let b=null,bs=0;KB.forEach(([k,a])=>{const s=tok(k+" "+a).filter(x=>qt.has(x)).length;if(s>bs){bs=s;b=a}});
const r=add("…");const reduce=matchMedia("(prefers-reduced-motion:reduce)").matches;setTimeout(()=>{r.textContent=bs>=2?b:UNK},reduce?0:500)};
$("#cg").onclick=()=>{ask(cq.value);cq.value=""};cq.onkeydown=e=>{if(e.key==="Enter")$("#cg").click()};
$("#cs").dataset.s.split("|").forEach(s=>{const b=document.createElement("button");b.textContent=s;b.onclick=()=>ask(s);$("#cs").append(b)})})();
