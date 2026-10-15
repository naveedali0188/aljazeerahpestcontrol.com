import os,json,re,shutil,sys
BASE=os.environ.get("BASE","").rstrip("/")   # e.g. /my-repo for project pages
DOM="https://aljazeerahpestcontrol.com"
SITE=os.environ.get("SITE_URL","https://YOUR-USER.github.io"+BASE).rstrip("/")
L=["ar","en","zh","ru"]; NAME={"ar":"العربية","en":"English","zh":"中文","ru":"Русский"}; FLAG={"ar":"🇦🇪","en":"🇬🇧","zh":"🇨🇳","ru":"🇷🇺"}
WA="https://wa.me/971557207420"; MAP="https://maps.app.goo.gl/K4xXKgWvBWNzpsRL9"; MAIL="Info@aljazeerahpestcontrol.ae"
S={ # slug: en|ar|zh|ru  (group)
"pest-control":("pest","General Pest Control|مكافحة الحشرات العامة|综合害虫防治|Общая борьба с вредителями"),
"cockroach-control":("pest","Cockroach Control|مكافحة الصراصير|蟑螂防治|Борьба с тараканами"),
"ant-control":("pest","Ant Control|مكافحة النمل|蚂蚁防治|Борьба с муравьями"),
"bed-bug-control":("pest","Bed Bug Control|مكافحة بق الفراش|臭虫防治|Борьба с клопами"),
"mosquito-control":("pest","Mosquito Control|مكافحة البعوض|蚊虫防治|Борьба с комарами"),
"termite-control":("pest","Termite Control|مكافحة النمل الأبيض|白蚁防治|Борьба с термитами"),
"rat-control":("pest","Rat Control|مكافحة الجرذان|灭鼠服务|Борьба с крысами"),
"fly-control":("pest","Fly Control|مكافحة الذباب|苍蝇防治|Борьба с мухами"),
"bird-control":("pest","Bird Control|مكافحة الطيور|驱鸟服务|Отпугивание птиц"),
"bee-control":("pest","Honey Bee Control|مكافحة نحل العسل|蜜蜂处理|Борьба с пчёлами"),
"lizard-control":("pest","Lizard Control|مكافحة السحالي|蜥蜴防治|Борьба с ящерицами"),
"snake-control":("pest","Snake Control|مكافحة الثعابين|蛇类防治|Борьба со змеями"),
"wasp-control":("pest","Wasp Control|مكافحة الدبابير|黄蜂防治|Борьба с осами"),
"cleaning":("clean","Cleaning Services|خدمات التنظيف|清洁服务|Услуги уборки"),
"general-cleaning":("clean","General Cleaning|التنظيف العام|综合清洁|Генеральная уборка"),
"villa-cleaning":("clean","Villa Cleaning|تنظيف الفلل|别墅清洁|Уборка вилл"),
"water-tank-cleaning":("clean","Water Tank Cleaning|تنظيف خزانات المياه|水箱清洗|Чистка водяных баков"),
"glass-cleaning":("clean","Glass Cleaning|تنظيف الزجاج|玻璃清洁|Мойка стёкол"),
"elevator-cleaning":("clean","Elevator Cleaning|تنظيف المصاعد|电梯清洁|Уборка лифтов"),
"paper-removal":("clean","Paper Removal|إزالة الورق|纸张清除|Удаление бумаги"),
"elevator-polishing":("clean","Elevator Polishing|تلميع المصاعد|电梯抛光|Полировка лифтов"),
"residential-pest-control":("sector","Residential Pest Control|مكافحة الحشرات للمنازل|住宅害虫防治|Борьба с вредителями в жилье"),
"commercial-pest-control":("sector","Commercial Pest Control|مكافحة الحشرات للشركات|商业害虫防治|Борьба с вредителями в бизнесе")}
C={"abu-dhabi":"Abu Dhabi|أبوظبي|阿布扎比|Абу-Даби","dubai":"Dubai|دبي|迪拜|Дубай","sharjah":"Sharjah|الشارقة|沙迦|Шарджа","ajman":"Ajman|عجمان|阿治曼|Аджман"}
LOCF={"en":"Pest Control in {}","ar":"مكافحة الحشرات في {}","zh":"{}害虫防治","ru":"Борьба с вредителями: {}"}
def nm(slug,l):
    if slug in S: return S[slug][1].split("|")[L.index(l) if False else {"en":0,"ar":1,"zh":2,"ru":3}[l]]
    if slug.startswith("pest-control-"): return LOCF[l].format(C[slug[13:]].split("|")[{"en":0,"ar":1,"zh":2,"ru":3}[l]])
    return T[l][slug]
T={ # UI strings
"en":dict(home="Home",about="About",contact="Contact",faq="FAQ",privacy="Privacy Policy",blog="Blog",loc="Locations",svc="Services",call="Call now",wa="WhatsApp",quote="Get a free quote",
 h1="Pest control and cleaning across Dubai, Sharjah, Ajman and Abu Dhabi",sub="Book a site inspection and get a treatment plan for your home or business.",
 intro="Al Jazeerah Pest Control LLC provides {n} in the UAE. Book a site inspection and a technician will assess your property and explain the recommended treatment.",
 steps="Inspection|A technician checks the property and identifies the problem.|Treatment plan|You receive a plan suited to the pest and the property.|Follow-up advice|You get guidance on prevention and what to do after treatment.",
 safe="Treatment steps, product choice and re-entry times depend on the pest, the property, the product label and the technician's instructions.",
 locnote="We serve {n}. Our offices are in Dubai and Sharjah.",f_name="Name",f_phone="Phone",f_msg="How can we help?",f_send="Send via WhatsApp",f_err="Please enter your name and a valid phone number.",f_ok="WhatsApp opened with your message. Nothing is sent until you press send there.",
 ct="Contact us",mobile="Mobile",dubai="Dubai office",sharjah="Sharjah office",email="Email",map="Find us on the map",bl="Read our articles on the main website",
 aboutp="Al Jazeerah Pest Control LLC offers pest control and cleaning services for homes and businesses in Dubai, Abu Dhabi, Sharjah and Ajman. Offices: Dubai and Sharjah.",
 priv="This website does not use cookies or trackers. The language you choose is saved in your browser only. The quote form builds a WhatsApp message on your device; we do not store form data on this site. If you message us, your details are handled by WhatsApp and our team.",
 chat="FAQ assistant",chath="Answers from our FAQ (not a live AI). For anything else, contact the team.",ph="Type your question",unk="I don't have a verified answer for that. Please contact the team on WhatsApp or by phone.",skip="Skip to content",menu="Menu",
 sug="Which areas do you serve?|Is treatment safe for pets?|How do I book an inspection?",
 kb=[("What are the signs of an infestation?","Common signs include seeing pests, droppings, nests, damage, unusual noises and allergic reactions. A site inspection confirms the cause."),
 ("Is treatment safe for people and pets?","It depends on the pest, the product label and the technician's instructions. Ask the technician before treatment whether people or pets should leave and for how long."),
 ("Which areas do you serve?","We serve Dubai, Sharjah, Ajman and Abu Dhabi. Offices are in Dubai and Sharjah."),
 ("How do I book an inspection or get a quote?","Call 055 720 7420 or message us on WhatsApp. The company advertises free site inspections; confirm details when you book."),
 ("How do I contact you?","Mobile 055 720 7420, Dubai office 04 450 3654, Sharjah office 06 535 8500, email Info@aljazeerahpestcontrol.ae.")]),
"ar":dict(home="الرئيسية",about="من نحن",contact="اتصل بنا",faq="الأسئلة الشائعة",privacy="سياسة الخصوصية",blog="المدونة",loc="المواقع",svc="الخدمات",call="اتصل الآن",wa="واتساب",quote="احصل على عرض مجاني",
 h1="مكافحة الحشرات والتنظيف في دبي والشارقة وعجمان وأبوظبي",sub="احجز معاينة للموقع واحصل على خطة معالجة لمنزلك أو شركتك.",
 intro="تقدم شركة الجزيرة لمكافحة الحشرات ذ.م.م خدمة {n} في الإمارات. احجز معاينة وسيقوم فني بتقييم العقار وشرح المعالجة الموصى بها.",
 steps="المعاينة|يفحص الفني العقار ويحدد المشكلة.|خطة المعالجة|تحصل على خطة مناسبة للآفة والعقار.|نصائح المتابعة|تحصل على إرشادات للوقاية وما يجب فعله بعد المعالجة.",
 safe="تعتمد خطوات المعالجة والمنتج المستخدم ومدة العودة إلى المكان على نوع الآفة والعقار وملصق المنتج وتعليمات الفني.",
 locnote="نخدم {n}. مكاتبنا في دبي والشارقة.",f_name="الاسم",f_phone="الهاتف",f_msg="كيف يمكننا مساعدتك؟",f_send="إرسال عبر واتساب",f_err="يرجى إدخال الاسم ورقم هاتف صحيح.",f_ok="تم فتح واتساب برسالتك. لن يُرسل شيء حتى تضغط إرسال هناك.",
 ct="تواصل معنا",mobile="الجوال",dubai="مكتب دبي",sharjah="مكتب الشارقة",email="البريد الإلكتروني",map="موقعنا على الخريطة",bl="اقرأ مقالاتنا على الموقع الرئيسي",
 aboutp="تقدم شركة الجزيرة لمكافحة الحشرات ذ.م.م خدمات مكافحة الحشرات والتنظيف للمنازل والشركات في دبي وأبوظبي والشارقة وعجمان. المكاتب: دبي والشارقة.",
 priv="لا يستخدم هذا الموقع ملفات تعريف الارتباط أو أدوات التتبع. تُحفظ اللغة التي تختارها في متصفحك فقط. يُنشئ النموذج رسالة واتساب على جهازك ولا نخزن بيانات النموذج على هذا الموقع. عند مراسلتنا تتم معالجة بياناتك عبر واتساب وفريقنا.",
 chat="مساعد الأسئلة الشائعة",chath="إجابات من الأسئلة الشائعة (ليس ذكاءً اصطناعياً مباشراً). لأي سؤال آخر تواصل مع الفريق.",ph="اكتب سؤالك",unk="ليس لدي إجابة مؤكدة. يرجى التواصل مع الفريق عبر واتساب أو الهاتف.",skip="انتقل إلى المحتوى",menu="القائمة",
 sug="ما المناطق التي تخدمونها؟|هل المعالجة آمنة للحيوانات الأليفة؟|كيف أحجز معاينة؟",
 kb=[("ما علامات وجود الآفات؟","من العلامات الشائعة رؤية الآفات أو فضلاتها أو أعشاشها أو أضرارها أو أصوات غير معتادة أو حساسية. تؤكد المعاينة السبب."),
 ("هل المعالجة آمنة للأشخاص والحيوانات الأليفة؟","يعتمد ذلك على نوع الآفة وملصق المنتج وتعليمات الفني. اسأل الفني قبل المعالجة عن ضرورة مغادرة الأشخاص أو الحيوانات ولمدة كم."),
 ("ما المناطق التي تخدمونها؟","نخدم دبي والشارقة وعجمان وأبوظبي. المكاتب في دبي والشارقة."),
 ("كيف أحجز معاينة أو أطلب عرض سعر؟","اتصل على 055 720 7420 أو راسلنا عبر واتساب. تعلن الشركة عن معاينة مجانية للموقع؛ تأكد من التفاصيل عند الحجز."),
 ("كيف أتواصل معكم؟","الجوال 055 720 7420، مكتب دبي 04 450 3654، مكتب الشارقة 06 535 8500، البريد Info@aljazeerahpestcontrol.ae.")]),
"zh":dict(home="首页",about="关于我们",contact="联系我们",faq="常见问题",privacy="隐私政策",blog="博客",loc="服务地区",svc="服务项目",call="立即致电",wa="WhatsApp",quote="获取免费报价",
 h1="迪拜、沙迦、阿治曼和阿布扎比的害虫防治与清洁服务",sub="预约现场检查，为您的住宅或企业获取处理方案。",
 intro="Al Jazeerah Pest Control LLC 在阿联酋提供{n}服务。预约现场检查，技术人员将评估您的物业并说明建议的处理方式。",
 steps="现场检查|技术人员检查物业并确定问题。|处理方案|您将获得适合害虫和物业的方案。|后续建议|获得预防及处理后注意事项的指导。",
 safe="处理步骤、产品选择和重新进入时间取决于害虫种类、物业、产品标签以及技术人员的指示。",
 locnote="我们服务{n}。办公室位于迪拜和沙迦。",f_name="姓名",f_phone="电话",f_msg="需要什么帮助？",f_send="通过WhatsApp发送",f_err="请填写姓名和有效的电话号码。",f_ok="已打开WhatsApp并填入您的信息。在那里点击发送后才会发出。",
 ct="联系我们",mobile="手机",dubai="迪拜办公室",sharjah="沙迦办公室",email="电子邮件",map="在地图上找到我们",bl="在主网站阅读我们的文章",
 aboutp="Al Jazeerah Pest Control LLC 为迪拜、阿布扎比、沙迦和阿治曼的住宅和企业提供害虫防治与清洁服务。办公室：迪拜和沙迦。",
 priv="本网站不使用Cookie或追踪器。您选择的语言仅保存在您的浏览器中。报价表单仅在您的设备上生成WhatsApp消息，本网站不存储表单数据。联系我们后，您的信息由WhatsApp和我们的团队处理。",
 chat="常见问题助手",chath="答案来自常见问题（并非实时AI）。其他问题请联系团队。",ph="输入您的问题",unk="我没有经过核实的答案，请通过WhatsApp或电话联系团队。",skip="跳到内容",menu="菜单",
 sug="你们服务哪些地区？|处理对宠物安全吗？|如何预约检查？",
 kb=[("害虫侵扰有哪些迹象？","常见迹象包括看到害虫、粪便、巢穴、损坏、异常声音和过敏反应。现场检查可确认原因。"),
 ("处理对人和宠物安全吗？","取决于害虫种类、产品标签和技术人员的指示。处理前请询问技术人员人员和宠物是否需要离开以及多长时间。"),
 ("你们服务哪些地区？","我们服务迪拜、沙迦、阿治曼和阿布扎比。办公室在迪拜和沙迦。"),
 ("如何预约检查或获取报价？","致电 055 720 7420 或通过WhatsApp联系我们。公司宣传提供免费现场检查，预约时请确认细节。"),
 ("如何联系你们？","手机 055 720 7420，迪拜办公室 04 450 3654，沙迦办公室 06 535 8500，邮箱 Info@aljazeerahpestcontrol.ae。")]),
"ru":dict(home="Главная",about="О компании",contact="Контакты",faq="Вопросы и ответы",privacy="Политика конфиденциальности",blog="Блог",loc="Регионы",svc="Услуги",call="Позвонить",wa="WhatsApp",quote="Бесплатный расчёт",
 h1="Борьба с вредителями и уборка в Дубае, Шардже, Аджмане и Абу-Даби",sub="Закажите осмотр объекта и получите план обработки для дома или бизнеса.",
 intro="Al Jazeerah Pest Control LLC предоставляет услугу «{n}» в ОАЭ. Закажите осмотр: специалист оценит объект и объяснит рекомендуемую обработку.",
 steps="Осмотр|Специалист осматривает объект и определяет проблему.|План обработки|Вы получаете план, подходящий для вредителя и объекта.|Рекомендации|Вы получаете советы по профилактике и действиям после обработки.",
 safe="Этапы обработки, выбор препарата и время возвращения в помещение зависят от вредителя, объекта, этикетки препарата и указаний специалиста.",
 locnote="Мы работаем: {n}. Офисы находятся в Дубае и Шардже.",f_name="Имя",f_phone="Телефон",f_msg="Чем мы можем помочь?",f_send="Отправить в WhatsApp",f_err="Введите имя и корректный номер телефона.",f_ok="WhatsApp открыт с вашим сообщением. Оно будет отправлено только после нажатия «Отправить» там.",
 ct="Свяжитесь с нами",mobile="Мобильный",dubai="Офис в Дубае",sharjah="Офис в Шардже",email="Эл. почта",map="Мы на карте",bl="Читайте статьи на основном сайте",
 aboutp="Al Jazeerah Pest Control LLC оказывает услуги по борьбе с вредителями и уборке для домов и бизнеса в Дубае, Абу-Даби, Шардже и Аджмане. Офисы: Дубай и Шарджа.",
 priv="Сайт не использует cookie и трекеры. Выбранный язык хранится только в вашем браузере. Форма создаёт сообщение WhatsApp на вашем устройстве; данные формы на сайте не хранятся. При обращении ваши данные обрабатываются WhatsApp и нашей командой.",
 chat="FAQ-помощник",chath="Ответы из раздела FAQ (не живой ИИ). По другим вопросам свяжитесь с командой.",ph="Введите вопрос",unk="У меня нет проверенного ответа. Свяжитесь с командой в WhatsApp или по телефону.",skip="Перейти к содержимому",menu="Меню",
 sug="В каких районах вы работаете?|Безопасна ли обработка для животных?|Как заказать осмотр?",
 kb=[("Каковы признаки заражения?","Частые признаки: вредители, помёт, гнёзда, повреждения, необычные звуки, аллергические реакции. Осмотр подтверждает причину."),
 ("Безопасна ли обработка для людей и животных?","Это зависит от вредителя, этикетки препарата и указаний специалиста. Перед обработкой уточните, нужно ли людям и животным покидать помещение и на какое время."),
 ("В каких районах вы работаете?","Мы работаем в Дубае, Шардже, Аджмане и Абу-Даби. Офисы — в Дубае и Шардже."),
 ("Как заказать осмотр или расчёт?","Позвоните по 055 720 7420 или напишите в WhatsApp. Компания заявляет бесплатный осмотр; уточните детали при заказе."),
 ("Как с вами связаться?","Мобильный 055 720 7420, офис в Дубае 04 450 3654, офис в Шардже 06 535 8500, почта Info@aljazeerahpestcontrol.ae.")])}
for l in L: T[l].update({k:v for k,v in {"pest":"","clean":""}.items()})
for l in L: T[l]["pestg"]=T[l]["svc"]
PAGES=["home","about","contact","faq","privacy","blog"]+list(S)+["pest-control-"+c for c in C]
def url(l,p): return f"{BASE}/{l}/" + ("" if p=="home" else p+"/")
def full(l,p): return SITE+url(l,p)[len(BASE):]
def nmx(p,l): return T[l]["home"] if p=="home" else nm(p,l)
def head(l,p,title,desc):
    alt="".join(f'<link rel="alternate" hreflang="{x}" href="{full(x,p)}">' for x in L)+f'<link rel="alternate" hreflang="x-default" href="{full("en",p)}">'
    crumbs=[("home",T[l]["home"])]+([(p,title)] if p!="home" else [])
    ld=[{"@context":"https://schema.org","@type":["LocalBusiness","PestControl"],"name":"Al Jazeerah Pest Control LLC","url":DOM+"/","email":MAIL,"telephone":"+971557207420","areaServed":[c.split("|")[0] for c in C.values()],"sameAs":["https://www.facebook.com/aljazeerahpestcontroldubaisharjah","https://www.instagram.com/aljazeerahpestcontrol/","https://www.linkedin.com/company/al-jazeerah-pest-control/"],"hasMap":MAP},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":full(l,q)} for i,(q,n) in enumerate(crumbs)]}]
    if p in S or p.startswith("pest-control-"): ld.append({"@context":"https://schema.org","@type":"Service","name":title,"provider":{"@type":"PestControl","name":"Al Jazeerah Pest Control LLC","telephone":"+971557207420"},"areaServed":"United Arab Emirates","url":full(l,p)})
    return f'''<!doctype html><html lang="{ {'zh':'zh-Hans'}.get(l,l)}" dir="{'rtl' if l=='ar' else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Al Jazeerah Pest Control</title><meta name="description" content="{desc}"><link rel="canonical" href="{full(l,p)}">{alt}<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{full(l,p)}"><link rel="icon" href="{BASE}/assets/img/icon.svg"><link rel="stylesheet" href="{BASE}/css/style.css"><script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head>'''
def nav(l):
    t=T[l]; li=lambda p:f'<a href="{url(l,p)}">{nmx(p,l)}</a>'
    grp=lambda g:"".join(li(s) for s,v in S.items() if v[0]==g)
    return f'''<a class="skip" href="#main">{t["skip"]}</a><header class="top"><a class="brand" href="{url(l,'home')}"><img src="{BASE}/assets/img/icon.svg" width="36" height="36" alt=""><span>Al Jazeerah<small>Pest Control LLC</small></span></a>
<button class="mb" aria-expanded="false" aria-controls="nv">{t["menu"]}</button><nav id="nv" aria-label="Main"><a href="{url(l,'home')}">{t["home"]}</a><a href="{url(l,'about')}">{t["about"]}</a>
<details><summary>{t["svc"]}</summary><div>{grp("pest")}</div></details><details><summary>{nm("cleaning",l)}</summary><div>{grp("clean")}</div></details><details><summary>{t["loc"]}</summary><div>{"".join(li("pest-control-"+c) for c in C)}</div></details>
<a href="{url(l,'faq')}">{t["faq"]}</a><a href="{url(l,'contact')}">{t["contact"]}</a></nav>
<div class="lang" role="group" aria-label="Language">{"".join(f'<a href="{url(x,PAGE[0])}" hreflang="{x}" lang="{x}" data-l="{x}" {"aria-current=page" if x==l else ""} title="{NAME[x]}"><span aria-hidden="true">{FLAG[x]}</span> {NAME[x]}</a>' for x in L)}</div></header>'''
def form(l):
    t=T[l]
    return f'''<form class="qf" id="qf" novalidate data-err="{t["f_err"]}" data-ok="{t["f_ok"]}" data-wa="{WA}"><label>{t["f_name"]}<input name="n" autocomplete="name" required></label><label>{t["f_phone"]}<input name="p" type="tel" autocomplete="tel" required></label><label>{t["f_msg"]}<textarea name="m" rows="3"></textarea></label><button class="btn go" type="submit">{t["f_send"]}</button><p id="fs" role="status"></p></form>'''
def body(l,p):
    t=T[l]; n=nmx(p,l); st=t["steps"].split("|")
    if p=="home":
        cards=lambda g:"".join(f'<a class="card" href="{url(l,s)}"><h3>{nm(s,l)}</h3></a>' for s,v in S.items() if v[0]==g)
        return f'''<section class="hero"><div class="hw"><h1>{t["h1"]}</h1><p>{t["sub"]}</p><p class="cta"><a class="btn go" href="{url(l,'contact')}">{t["quote"]}</a><a class="btn" href="tel:+971557207420">{t["call"]}: 055 720 7420</a><a class="btn" href="{WA}">{t["wa"]}</a></p></div><svg class="ring" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="30"/><circle cx="100" cy="100" r="30"/><circle cx="100" cy="100" r="30"/><path d="M100 62l32 12v24c0 22-14 36-32 44-18-8-32-22-32-44V74z"/></svg></section>
<section class="w"><h2>{t["svc"]}</h2><div class="grid">{cards("pest")}</div><h2>{nm("cleaning",l)}</h2><div class="grid">{cards("clean")}</div><h2>{t["loc"]}</h2><div class="grid">{"".join(f'<a class="card" href="{url(l,"pest-control-"+c)}"><h3>{nm("pest-control-"+c,l)}</h3></a>' for c in C)}</div><div class="grid">{cards("sector")}</div></section>'''
    if p=="about": return f'<section class="w"><h1>{n}</h1><p>{t["aboutp"]}</p></section>'
    if p=="privacy": return f'<section class="w"><h1>{n}</h1><p>{t["priv"]}</p></section>'
    if p=="faq": return f'<section class="w"><h1>{n}</h1>'+"".join(f'<details class="fq"><summary>{q}</summary><p>{a}</p></details>' for q,a in t["kb"])+f'<p class="cta"><a class="btn go" href="{url(l,"contact")}">{t["quote"]}</a></p></section>'
    if p=="blog": return f'<section class="w"><h1>{n}</h1><p><a class="btn" href="{DOM}/blog/" rel="noopener">{t["bl"]}</a></p></section>'
    if p=="contact": return f'''<section class="w two"><div><h1>{n}</h1><ul class="cl"><li>{t["mobile"]}: <a href="tel:+971557207420">055 720 7420</a></li><li>{t["dubai"]}: <a href="tel:+97144503654">04 450 3654</a></li><li>{t["sharjah"]}: <a href="tel:+97165358500">06 535 8500</a></li><li>{t["email"]}: <a href="mailto:{MAIL}?subject=Pest%20Control%20Free%20Quote">{MAIL}</a></li><li><a href="{WA}">{t["wa"]}</a></li><li><a href="{MAP}" rel="noopener">{t["map"]}</a></li></ul></div><div>{form(l)}</div></section>'''
    extra=f'<p>{t["locnote"].format(n=nm(p,l))}</p>' if p.startswith("pest-control-") else ""
    related="".join(f'<a href="{url(l,s)}">{nm(s,l)}</a>' for s,v in S.items() if v[0]==(S[p][0] if p in S else "pest") and s!=p)[:2500]
    return f'''<section class="w two"><div><h1>{n}</h1><p>{t["intro"].format(n=n)}</p>{extra}<ol class="steps"><li><b>{st[0]}</b> {st[1]}</li><li><b>{st[2]}</b> {st[3]}</li><li><b>{st[4]}</b> {st[5]}</li></ol><p class="note">{t["safe"]}</p><nav class="rel" aria-label="Related">{related}</nav></div><aside>{form(l)}</aside></section>'''
def page(l,p):
    global PAGE; PAGE=(p,)
    t=T[l]; n=nmx(p,l); desc=(t["sub"] if p=="home" else t["intro"].format(n=n))[:158].replace('"',"")
    bc="" if p=="home" else f'<nav class="bc" aria-label="Breadcrumb"><a href="{url(l,"home")}">{t["home"]}</a> / {n}</nav>'
    foot=f'''<footer><p>© Al Jazeerah Pest Control LLC · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="tel:+971557207420">055 720 7420</a> · <a href="{url(l,'privacy')}">{t["privacy"]}</a> · <a href="{url(l,'blog')}">{t["blog"]}</a></p></footer>
<div class="fab"><a href="tel:+971557207420" aria-label="{t["call"]}">📞</a><a class="w2" href="{WA}" aria-label="{t["wa"]}">💬</a></div>
<button id="cb" class="cbtn">{t["chat"]}</button><div id="cp" class="cp" hidden role="dialog" aria-label="{t["chat"]}"><p class="ch">{t["chath"]}</p><div id="cl" aria-live="polite"></div><div id="cs" data-s="{t["sug"]}"></div><div class="ci"><input id="cq" placeholder="{t["ph"]}" aria-label="{t["ph"]}"><button id="cg">➤</button></div><a class="btn" href="{WA}">{t["wa"]}</a></div>
<script>window.KB={json.dumps(t["kb"],ensure_ascii=False)};window.UNK={json.dumps(t["unk"],ensure_ascii=False)};window.WA="{WA}"</script><script src="{BASE}/js/app.js" defer></script>'''
    html=head(l,p,n,desc)+f'<body>{nav(l)}<main id="main">{bc}{body(l,p)}</main>{foot}</body></html>'
    d=os.path.join("."+url(l,p)[len(BASE):]); os.makedirs(d,exist_ok=True); open(d+"index.html","w",encoding="utf-8").write(html)
if __name__=="__main__":
    for l in L:
        for p in PAGES: page(l,p)
    open("index.html","w",encoding="utf-8").write(f'<!doctype html><meta charset="utf-8"><title>Al Jazeerah Pest Control</title><link rel="canonical" href="{SITE}/en/"><script>var s="en";try{{s=localStorage.getItem("lang")}}catch(e){{}}if(!{json.dumps(L)}.includes(s)){{s=(navigator.language||"en").slice(0,2);if(!{json.dumps(L)}.includes(s))s="en"}}location.replace("{BASE}/"+s+"/")</script><noscript><a href="{BASE}/en/">English</a> <a href="{BASE}/ar/">العربية</a> <a href="{BASE}/zh/">中文</a> <a href="{BASE}/ru/">Русский</a></noscript>')
    nf=head("en","home","404","Page not found")+f'<body><main class="w"><h1>404</h1><p>Page not found.</p><p>{" ".join(f"<a href={BASE}/{x}/>{NAME[x]}</a>" for x in L)}</p></main></body></html>'
    open("404.html","w",encoding="utf-8").write(nf)
    sm="".join(f'<url><loc>{full(l,p)}</loc>'+"".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{full(x,p)}"/>' for x in L)+'</url>' for l in L for p in PAGES)
    open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">{sm}</urlset>')
    open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print(len(L)*len(PAGES),"pages")
