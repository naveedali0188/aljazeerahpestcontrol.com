import os,json,re,shutil,sys
BASE=os.environ.get("BASE","").rstrip("/")   # e.g. /my-repo for project pages
DOM="https://aljazeerahpestcontrol.ae"
SITE=os.environ.get("SITE_URL",("https://naveedali0188.github.io"+BASE) if BASE else "https://aljazeerahpestcontrol.com").rstrip("/")
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
"en":dict(home="Home",about="About",contact="Contact",faq="FAQ",privacy="Privacy Policy",blog="Blog",loc="Locations",svc="Services",call="Call now",wa="WhatsApp",quote="Request an inspection",
 site_title="Pest Control & Cleaning in the UAE",about_desc="Learn about Al Jazeerah Pest Control LLC and its pest-control and cleaning services across the UAE.",contact_desc="Contact Al Jazeerah Pest Control by phone, WhatsApp, email or request an inspection.",faq_desc="Answers to common questions about pest-control inspections, treatment guidance and service areas.",privacy_desc="Read how this static website handles language preferences and WhatsApp contact messages.",blog_desc="Read pest-control and cleaning articles on the official Al Jazeerah Pest Control website.",
 h1="Pest control and cleaning across Dubai, Sharjah, Ajman and Abu Dhabi",sub="Book a site inspection and get a treatment plan for your home or business.",
 language="Language",nav="Main navigation",eyebrow="Al Jazeerah Pest Control LLC · UAE",local="Dubai · Sharjah · Ajman · Abu Dhabi",scroll="Scroll to explore",discover="Explore services",
 narrative="Care for the places",narrative_em="where life happens.",res_title="Residential care",res_desc="Pest-control services for homes, with a site inspection to assess the property.",commercial_title="Commercial care",commercial_desc="Pest-control services for businesses and commercial properties.",clean_title="Cleaning & property care",clean_desc="Cleaning services for homes and properties, from general cleaning to specialist care.",
 showcase="A closer look at our work",show_home_alt="Original illustration of a home and its surrounding landscape.",show_business_alt="Original illustration of a commercial building.",show_care_alt="Original illustration of property-care details.",show_home="Thoughtful care for every space",show_business="For homes and businesses",show_care="Property care, considered",
 service_intro="Explore the service and contact our team to discuss a site inspection.",service_link="Explore service",all_services="All services",footer_intro="Pest control and cleaning services for homes and businesses across the UAE.",footer_services="Services",footer_company="Company",footer_contact="Contact",footer_follow="Follow",view_map="View location on map",contact_heading="Speak with our team",
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
"ar":dict(home="الرئيسية",about="من نحن",contact="اتصل بنا",faq="الأسئلة الشائعة",privacy="سياسة الخصوصية",blog="المدونة",loc="المواقع",svc="الخدمات",call="اتصل الآن",wa="واتساب",quote="اطلب معاينة",
 site_title="مكافحة الحشرات والتنظيف في الإمارات",about_desc="تعرف على شركة الجزيرة لمكافحة الحشرات ذ.م.م وخدمات مكافحة الحشرات والتنظيف في الإمارات.",contact_desc="تواصل مع الجزيرة لمكافحة الحشرات عبر الهاتف أو واتساب أو البريد الإلكتروني، أو اطلب معاينة.",faq_desc="إجابات عن الأسئلة الشائعة حول معاينة مكافحة الحشرات وإرشادات المعالجة ومناطق الخدمة.",privacy_desc="تعرف على كيفية تعامل هذا الموقع الثابت مع تفضيلات اللغة ورسائل التواصل عبر واتساب.",blog_desc="اقرأ مقالات مكافحة الحشرات والتنظيف على الموقع الرسمي للجزيرة لمكافحة الحشرات.",
 h1="مكافحة الحشرات والتنظيف في دبي والشارقة وعجمان وأبوظبي",sub="احجز معاينة للموقع واحصل على خطة معالجة لمنزلك أو شركتك.",
 language="اللغة",nav="التنقل الرئيسي",eyebrow="الجزيرة لمكافحة الحشرات ذ.م.م · الإمارات",local="دبي · الشارقة · عجمان · أبوظبي",scroll="مرر للاستكشاف",discover="اكتشف الخدمات",
 narrative="العناية بالأماكن",narrative_em="التي تجمعنا.",res_title="العناية بالمنازل",res_desc="خدمات مكافحة الحشرات للمنازل، مع معاينة لتقييم العقار.",commercial_title="العناية بالأعمال",commercial_desc="خدمات مكافحة الحشرات للشركات والعقارات التجارية.",clean_title="التنظيف والعناية بالعقارات",clean_desc="خدمات تنظيف المنازل والعقارات، من التنظيف العام إلى العناية المتخصصة.",
 showcase="لمحة أقرب عن خدماتنا",show_home_alt="رسم أصلي لمنزل والمناظر المحيطة به.",show_business_alt="رسم أصلي لمبنى تجاري.",show_care_alt="رسم أصلي لتفاصيل العناية بالعقارات.",show_home="عناية مدروسة لكل مساحة",show_business="للمنازل والأعمال",show_care="عناية بالعقار بكل اهتمام",
 service_intro="استكشف الخدمة وتواصل مع فريقنا لمناقشة معاينة الموقع.",service_link="استكشف الخدمة",all_services="جميع الخدمات",footer_intro="خدمات مكافحة الحشرات والتنظيف للمنازل والأعمال في أنحاء الإمارات.",footer_services="الخدمات",footer_company="الشركة",footer_contact="التواصل",footer_follow="تابعونا",view_map="عرض الموقع على الخريطة",contact_heading="تواصل مع فريقنا",
 intro="تقدم شركة الجزيرة لمكافحة الحشرات ذ.م.م خدمة {n} في الإمارات. احجز معاينة وسيقوم فني بتقييم العقار وشرح المعالجة الموصى بها.",
 steps="المعاينة|يفحص الفني العقار ويحدد المشكلة.|خطة المعالجة|تحصل على خطة مناسبة للآفة والعقار.|نصائح المتابعة|تحصل على إرشادات للوقاية وما يجب فعله بعد المعالجة.",
 safe="تعتمد خطوات المعالجة والمنتج المستخدم ومدة العودة إلى المكان على نوع الآفة والعقار وملصق المنتج وتعليمات الفني.",
 locnote="نخدم {n}. مكاتبنا في دبي والشارقة.",f_name="الاسم",f_phone="الهاتف",f_msg="كيف يمكننا مساعدتك؟",f_send="إرسال عبر واتساب",f_err="يرجى إدخال الاسم ورقم هاتف صحيح.",f_ok="تم إعداد الرسالة. راجعها وأرسلها في واتساب.",
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
"zh":dict(home="首页",about="关于我们",contact="联系我们",faq="常见问题",privacy="隐私政策",blog="博客",loc="服务地区",svc="服务项目",call="立即致电",wa="WhatsApp",quote="预约现场检查",
 site_title="阿联酋害虫防治与清洁服务",about_desc="了解 Al Jazeerah Pest Control LLC 及其在阿联酋提供的害虫防治和清洁服务。",contact_desc="通过电话、WhatsApp 或电子邮件联系 Al Jazeerah Pest Control，或预约现场检查。",faq_desc="了解有关害虫防治现场检查、处理建议和服务区域的常见问题。",privacy_desc="了解此静态网站如何处理语言偏好设置及通过 WhatsApp 联系的信息。",blog_desc="在 Al Jazeerah Pest Control 官方网站阅读害虫防治与清洁相关文章。",
 h1="迪拜、沙迦、阿治曼和阿布扎比的害虫防治与清洁服务",sub="预约现场检查，为您的住宅或企业获取处理方案。",
 language="语言",nav="主导航",eyebrow="Al Jazeerah Pest Control LLC · 阿联酋",local="迪拜 · 沙迦 · 阿治曼 · 阿布扎比",scroll="向下探索",discover="探索服务",
 narrative="用心守护",narrative_em="生活的空间。",res_title="住宅服务",res_desc="面向住宅的害虫防治服务，并通过现场检查评估物业情况。",commercial_title="商业服务",commercial_desc="面向企业和商业物业的害虫防治服务。",clean_title="清洁与物业养护",clean_desc="住宅和物业清洁服务，涵盖常规清洁及专项养护。",
 showcase="服务一览",show_home_alt="原创住宅与周边景观插画。",show_business_alt="原创商业建筑插画。",show_care_alt="原创物业养护细节插画。",show_home="细致照料每一处空间",show_business="服务住宅与企业",show_care="用心养护物业",
 service_intro="了解服务详情，并联系我们讨论现场检查。",service_link="了解服务",all_services="全部服务",footer_intro="为阿联酋各地住宅和企业提供害虫防治与清洁服务。",footer_services="服务",footer_company="公司",footer_contact="联系",footer_follow="关注我们",view_map="在地图上查看位置",contact_heading="联系我们的团队",
 intro="Al Jazeerah Pest Control LLC 在阿联酋提供{n}服务。预约现场检查，技术人员将评估您的物业并说明建议的处理方式。",
 steps="现场检查|技术人员检查物业并确定问题。|处理方案|您将获得适合害虫和物业的方案。|后续建议|获得预防及处理后注意事项的指导。",
 safe="处理步骤、产品选择和重新进入时间取决于害虫种类、物业、产品标签以及技术人员的指示。",
 locnote="我们服务{n}。办公室位于迪拜和沙迦。",f_name="姓名",f_phone="电话",f_msg="需要什么帮助？",f_send="通过WhatsApp发送",f_err="请填写姓名和有效的电话号码。",f_ok="消息已准备好。请在WhatsApp中检查并发送。",
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
"ru":dict(home="Главная",about="О компании",contact="Контакты",faq="Вопросы и ответы",privacy="Политика конфиденциальности",blog="Блог",loc="Регионы",svc="Услуги",call="Позвонить",wa="WhatsApp",quote="Заказать осмотр",
 site_title="Борьба с вредителями и уборка в ОАЭ",about_desc="Об Al Jazeerah Pest Control LLC и услугах по борьбе с вредителями и уборке в ОАЭ.",contact_desc="Свяжитесь с Al Jazeerah Pest Control по телефону, в WhatsApp или по электронной почте либо закажите осмотр.",faq_desc="Ответы на вопросы об осмотре объекта, рекомендациях по обработке и районах обслуживания.",privacy_desc="Как этот статический сайт обрабатывает выбор языка и сообщения для связи через WhatsApp.",blog_desc="Читайте статьи о борьбе с вредителями и уборке на официальном сайте Al Jazeerah Pest Control.",
 h1="Борьба с вредителями и уборка в Дубае, Шардже, Аджмане и Абу-Даби",sub="Закажите осмотр объекта и получите план обработки для дома или бизнеса.",
 language="Язык",nav="Главная навигация",eyebrow="Al Jazeerah Pest Control LLC · ОАЭ",local="Дубай · Шарджа · Аджман · Абу-Даби",scroll="Листайте дальше",discover="Услуги",
 narrative="Забота о местах",narrative_em="где проходит жизнь.",res_title="Забота о доме",res_desc="Услуги по борьбе с вредителями для жилых помещений с осмотром объекта.",commercial_title="Забота о бизнесе",commercial_desc="Услуги по борьбе с вредителями для компаний и коммерческих объектов.",clean_title="Уборка и уход за объектами",clean_desc="Уборка домов и объектов: от общей уборки до специализированного ухода.",
 showcase="Ближе к нашим услугам",show_home_alt="Оригинальная иллюстрация дома и окружающего ландшафта.",show_business_alt="Оригинальная иллюстрация коммерческого здания.",show_care_alt="Оригинальная иллюстрация деталей ухода за объектом.",show_home="Внимание к каждому пространству",show_business="Для домов и бизнеса",show_care="Продуманный уход за объектом",
 service_intro="Изучите услугу и свяжитесь с командой, чтобы обсудить осмотр объекта.",service_link="Подробнее об услуге",all_services="Все услуги",footer_intro="Услуги по борьбе с вредителями и уборке для домов и бизнеса по всему ОАЭ.",footer_services="Услуги",footer_company="Компания",footer_contact="Контакты",footer_follow="Мы в соцсетях",view_map="Посмотреть на карте",contact_heading="Свяжитесь с нашей командой",
 intro="Al Jazeerah Pest Control LLC предоставляет услугу «{n}» в ОАЭ. Закажите осмотр: специалист оценит объект и объяснит рекомендуемую обработку.",
 steps="Осмотр|Специалист осматривает объект и определяет проблему.|План обработки|Вы получаете план, подходящий для вредителя и объекта.|Рекомендации|Вы получаете советы по профилактике и действиям после обработки.",
 safe="Этапы обработки, выбор препарата и время возвращения в помещение зависят от вредителя, объекта, этикетки препарата и указаний специалиста.",
 locnote="Мы работаем: {n}. Офисы находятся в Дубае и Шардже.",f_name="Имя",f_phone="Телефон",f_msg="Чем мы можем помочь?",f_send="Отправить в WhatsApp",f_err="Введите имя и корректный номер телефона.",f_ok="Сообщение подготовлено. Проверьте его и отправьте в WhatsApp.",
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
    ld=[{"@context":"https://schema.org","@type":["LocalBusiness","PestControl"],"@id":SITE+"/#organization","name":"Al Jazeerah Pest Control LLC","url":SITE+"/","email":MAIL,"telephone":"+971557207420","areaServed":[c.split("|")[0] for c in C.values()],"sameAs":["https://www.facebook.com/aljazeerahgroup786"],"hasMap":MAP},
     {"@context":"https://schema.org","@type":"WebSite","@id":SITE+"/#website","name":"Al Jazeerah Pest Control LLC","url":SITE+"/","inLanguage":{"ar":"ar","en":"en","zh":"zh-Hans","ru":"ru"}[l],"publisher":{"@id":SITE+"/#organization"}},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":full(l,q)} for i,(q,n) in enumerate(crumbs)]}]
    if p in S or p.startswith("pest-control-"): ld.append({"@context":"https://schema.org","@type":"Service","name":title,"provider":{"@type":"PestControl","name":"Al Jazeerah Pest Control LLC","telephone":"+971557207420"},"areaServed":"United Arab Emirates","url":full(l,p)})
    return f'''<!doctype html><html lang="{ {'zh':'zh-Hans'}.get(l,l)}" dir="{'rtl' if l=='ar' else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f2f2f2"><title>{title} | Al Jazeerah Pest Control</title><meta name="description" content="{desc}"><link rel="canonical" href="{full(l,p)}">{alt}<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{full(l,p)}"><link rel="icon" href="{BASE}/assets/img/favicon.webp"><link rel="stylesheet" href="{BASE}/css/style.css"><script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head>'''
def nav(l):
    t=T[l]; li=lambda p:f'<a href="{url(l,p)}">{nmx(p,l)}</a>'
    grp=lambda g:"".join(li(s) for s,v in S.items() if v[0]==g)
    return f'''<a class="skip" href="#main">{t["skip"]}</a><header class="top"><a class="brand" href="{url(l,'home')}" aria-label="Al Jazeerah Pest Control LLC — {t["home"]}"><img src="{BASE}/assets/img/logo.webp" width="192" height="55" alt="Al Jazeerah Pest Control LLC"></a>
<button class="mb" aria-expanded="false" aria-controls="nv">{t["menu"]}</button><nav id="nv" aria-label="{t["nav"]}"><a href="{url(l,'home')}">{t["home"]}</a><a href="{url(l,'about')}">{t["about"]}</a>
<details><summary>{t["svc"]}</summary><div>{grp("pest")}</div></details><details><summary>{nm("cleaning",l)}</summary><div>{grp("clean")}</div></details><details><summary>{t["loc"]}</summary><div>{"".join(li("pest-control-"+c) for c in C)}</div></details>
<a href="{url(l,'faq')}">{t["faq"]}</a><a class="nav-contact" href="{url(l,'contact')}">{t["contact"]}<span aria-hidden="true"> ↗</span></a></nav>
<div class="lang" role="group" aria-label="{t["language"]}">{"".join(f'<a href="{url(x,PAGE[0])}" hreflang="{x}" lang="{x}" data-l="{x}" aria-label="{NAME[x]}" {"aria-current=page" if x==l else ""} title="{NAME[x]}"><span aria-hidden="true">{FLAG[x]}</span><span class="lang-name">{NAME[x]}</span></a>' for x in L)}</div></header>'''
def form(l):
    t=T[l]
    return f'''<form class="qf" id="qf" novalidate data-err="{t["f_err"]}" data-ok="{t["f_ok"]}" data-wa="{WA}"><label>{t["f_name"]}<input name="n" autocomplete="name" required aria-required="true"></label><label>{t["f_phone"]}<input name="p" type="tel" autocomplete="tel" inputmode="tel" required aria-required="true"></label><label>{t["f_msg"]}<textarea name="m" rows="4"></textarea></label><button class="btn go" type="submit">{t["f_send"]}<span aria-hidden="true"> ↗</span></button><p id="fs" role="status" aria-live="polite"></p></form>'''
def body(l,p):
    t=T[l]; n=nmx(p,l); st=t["steps"].split("|")
    if p=="home":
        col=lambda slug,title,description:f'<article class="narrative-card" data-reveal><span class="index">0{1 if slug=="residential-pest-control" else 2 if slug=="commercial-pest-control" else 3}</span><h3>{title}</h3><p>{description}</p><a class="text-link" href="{url(l,slug)}">{t["service_link"]}<span aria-hidden="true"> ↗</span></a></article>'
        groups=[("pest",t["svc"]),("clean",nm("cleaning",l))]
        cards=lambda g:"".join(f'<a class="service-card" href="{url(l,s)}" data-reveal><span class="svc-icon" aria-hidden="true"><svg viewBox="0 0 40 40"><path d="M20 4 36 20 20 36 4 20 20 4Z"/><path d="M20 12v16M12 20h16"/></svg></span><span class="service-card-copy"><h3>{nm(s,l)}</h3><p>{t["service_intro"]}</p><span class="text-link">{t["service_link"]}<span aria-hidden="true"> ↗</span></span></span></a>' for s,v in S.items() if v[0]==g)
        return f'''<section class="hero"><div class="hero-inner"><p class="eyebrow"><span></span>{t["eyebrow"]}</p><div class="echo"><span aria-hidden="true">{t["h1"]}</span><span aria-hidden="true">{t["h1"]}</span><span aria-hidden="true">{t["h1"]}</span><span aria-hidden="true">{t["h1"]}</span><h1>{t["h1"]}</h1></div><p class="hero-copy">{t["sub"]}</p><div class="hero-actions"><a class="btn go" href="{url(l,'contact')}">{t["quote"]}<span aria-hidden="true"> ↗</span></a><a class="btn btn-quiet" href="tel:+971557207420">{t["call"]} · 055 720 7420</a></div><p class="hero-locations">{t["local"]}</p></div><a class="hero-scroll" href="#intro"><span aria-hidden="true">↓</span>{t["scroll"]}</a></section>
<section class="narrative section-shell" id="intro" data-reveal><p class="eyebrow">{t["svc"]} / 01</p><h2>{t["narrative"]} <em>{t["narrative_em"]}</em></h2><div class="narrative-grid">{col("residential-pest-control",t["res_title"],t["res_desc"])}{col("commercial-pest-control",t["commercial_title"],t["commercial_desc"])}{col("cleaning",t["clean_title"],t["clean_desc"])}</div></section>
<section class="showcase section-shell" aria-labelledby="showcase-title"><div class="section-heading" data-reveal><p class="eyebrow">02 / {t["about"]}</p><h2 id="showcase-title">{t["showcase"]}</h2></div><div class="gallery-grid"><figure class="gallery-landscape" data-reveal><img src="{BASE}/assets/img/editorial-home.svg" alt="{t["show_home_alt"]}" width="1200" height="760" loading="lazy" decoding="async"><figcaption>{t["show_home"]}</figcaption></figure><a class="gallery-pill" href="{url(l,'contact')}" data-reveal><img src="{BASE}/assets/img/editorial-business.svg" alt="{t["show_business_alt"]}" width="700" height="1000" loading="lazy" decoding="async"><span class="pill-cta">{t["quote"]}<span aria-hidden="true"> ↗</span></span></a><figure class="gallery-circle" data-reveal><img src="{BASE}/assets/img/editorial-care.svg" alt="{t["show_care_alt"]}" width="800" height="800" loading="lazy" decoding="async"><figcaption>{t["show_care"]}</figcaption></figure><figure class="gallery-wide" data-reveal><img src="{BASE}/assets/img/editorial-business.svg" alt="{t["show_business_alt"]}" width="1200" height="760" loading="lazy" decoding="async"><figcaption>{t["show_business"]}</figcaption></figure></div></section>
<section class="services-section section-shell" id="services"><div class="section-heading" data-reveal><p class="eyebrow">03 / {t["svc"]}</p><h2>{t["discover"]}</h2><p>{t["service_intro"]}</p></div>{"".join(f'<h3 class="service-group-title" data-reveal>{title}</h3><div class="service-grid">{cards(g)}</div>' for g,title in groups)}<div class="location-links" data-reveal><span>{t["loc"]}</span>{"".join(f'<a href="{url(l,"pest-control-"+c)}">{nm("pest-control-"+c,l)} ↗</a>' for c in C)}</div></section>
<section class="contact-band"><div><p class="eyebrow">{t["contact_heading"]}</p><h2>{t["sub"]}</h2></div><a class="btn go" href="{url(l,'contact')}">{t["quote"]}<span aria-hidden="true"> ↗</span></a></section>'''
    if p=="about": return f'<section class="page-hero section-shell" data-reveal><p class="eyebrow">{t["about"]}</p><h1>{n}</h1><p>{t["aboutp"]}</p><a class="btn go" href="{url(l,"contact")}">{t["contact"]}<span aria-hidden="true"> ↗</span></a></section>'
    if p=="privacy": return f'<section class="page-hero section-shell" data-reveal><p class="eyebrow">{t["privacy"]}</p><h1>{n}</h1><p>{t["priv"]}</p></section>'
    if p=="faq": return f'<section class="page-hero section-shell faq-page" data-reveal><p class="eyebrow">{t["faq"]}</p><h1>{n}</h1>'+"".join(f'<details class="fq"><summary>{q}<span aria-hidden="true">+</span></summary><div class="fq-answer"><p>{a}</p></div></details>' for q,a in t["kb"])+f'<p class="cta"><a class="btn go" href="{url(l,"contact")}">{t["quote"]}<span aria-hidden="true"> ↗</span></a></p></section>'
    if p=="blog": return f'<section class="page-hero section-shell" data-reveal><p class="eyebrow">{t["blog"]}</p><h1>{n}</h1><a class="btn" href="{DOM}/blog/" rel="noopener">{t["bl"]}<span aria-hidden="true"> ↗</span></a></section>'
    if p=="contact": return f'''<section class="contact-page section-shell"><div class="contact-copy" data-reveal><p class="eyebrow">{t["contact_heading"]}</p><h1>{n}</h1><ul class="contact-list"><li><span>{t["mobile"]}</span><a href="tel:+971557207420">+971 55 720 7420</a></li><li><span>{t["dubai"]}</span><a href="tel:+97144503654">+971 4 450 3654</a></li><li><span>{t["sharjah"]}</span><a href="tel:+97165358500">+971 6 535 8500</a></li><li><span>{t["email"]}</span><a href="mailto:{MAIL}">{MAIL}</a></li><li><span>{t["wa"]}</span><a href="{WA}">{t["wa"]} ↗</a></li><li><span>{t["map"]}</span><a href="{MAP}" rel="noopener">{t["view_map"]} ↗</a></li></ul></div><div data-reveal><h2>{t["ct"]}</h2>{form(l)}</div></section>'''
    extra=f'<p>{t["locnote"].format(n=nm(p,l))}</p>' if p.startswith("pest-control-") else ""
    related="".join(f'<a href="{url(l,s)}">{nm(s,l)}</a>' for s,v in S.items() if v[0]==(S[p][0] if p in S else "pest") and s!=p)[:2500]
    return f'''<section class="service-page section-shell"><div class="service-page-copy" data-reveal><p class="eyebrow">{t["svc"]}</p><h1>{n}</h1><p class="service-lead">{t["intro"].format(n=n)}</p>{extra}<ol class="steps"><li><b>{st[0]}</b><span>{st[1]}</span></li><li><b>{st[2]}</b><span>{st[3]}</span></li><li><b>{st[4]}</b><span>{st[5]}</span></li></ol><p class="note">{t["safe"]}</p><nav class="rel" aria-label="{t["svc"]}">{related}</nav></div><aside data-reveal><h2>{t["contact_heading"]}</h2>{form(l)}</aside></section>'''
def page(l,p):
    global PAGE; PAGE=(p,)
    t=T[l]; n=nmx(p,l); title=t["site_title"] if p=="home" else n
    desc=(t["sub"] if p=="home" else t[f"{p}_desc"] if p in ("about","contact","faq","privacy","blog") else t["intro"].format(n=n))[:158].replace('"',"")
    bc="" if p=="home" else f'<nav class="bc" aria-label="Breadcrumb"><a href="{url(l,"home")}">{t["home"]}</a> / {n}</nav>'
    foot=f'''<footer class="site-footer"><div class="footer-grid"><section class="footer-brand"><a href="{url(l,"home")}" aria-label="Al Jazeerah Pest Control LLC — {t["home"]}"><img src="{BASE}/assets/img/logo.webp" width="192" height="55" alt="Al Jazeerah Pest Control LLC"></a><p>{t["footer_intro"]}</p><p class="copyright">© Al Jazeerah Pest Control LLC</p></section><nav class="footer-col" aria-label="{t["footer_services"]}"><h2>{t["footer_services"]}</h2>{''.join(f'<a href="{url(l,s)}">{nm(s,l)}</a>' for s,v in list(S.items())[:6])}<a href="{url(l,"home")}#services">{t["all_services"]} ↗</a></nav><nav class="footer-col" aria-label="{t["footer_company"]}"><h2>{t["footer_company"]}</h2><a href="{url(l,"about")}">{t["about"]}</a><a href="{url(l,"faq")}">{t["faq"]}</a><a href="{url(l,"contact")}">{t["contact"]}</a><a href="{url(l,"privacy")}">{t["privacy"]}</a><a href="{url(l,"blog")}">{t["blog"]}</a><a href="{url(l,"home")}#services">{t["loc"]}</a></nav><section class="footer-col"><h2>{t["footer_contact"]}</h2><a href="tel:+971557207420">+971 55 720 7420</a><a href="tel:+97144503654">+971 4 450 3654 · {t["dubai"]}</a><a href="tel:+97165358500">+971 6 535 8500 · {t["sharjah"]}</a><a href="mailto:{MAIL}">{MAIL}</a><a href="{WA}">{t["wa"]} ↗</a><a href="{MAP}" rel="noopener">{t["view_map"]} ↗</a><h3>{t["footer_follow"]}</h3><a href="https://www.facebook.com/aljazeerahgroup786" rel="noopener">Facebook ↗</a></section></div><div class="footer-bottom"><a href="{url(l,"privacy")}">{t["privacy"]}</a><span>{t["local"]}</span></div></footer>
<div class="fab"><a href="tel:+971557207420" aria-label="{t["call"]}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h4l2 5-2.5 2a15 15 0 0 0 5.5 5.5l2-2.5 5 2v4c0 1.1-.9 2-2 2C10.2 21 3 13.8 3 5c0-1.1.9-2 2-2Z"/></svg></a><a class="w2" href="{WA}" aria-label="{t["wa"]}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11.5a8 8 0 0 1-11.8 7L4 20l1.5-4.2A8 8 0 1 1 20 11.5Z"/><path d="M9 8.5c.7 2.4 2.1 3.8 4.5 4.5l1-1 2 .8c-.2 1.7-1.3 2.4-2.7 2.1-3.8-.9-6.3-3.4-7.2-7.2-.3-1.4.4-2.5 2.1-2.7l.8 2-1 1.5Z"/></svg></a></div>
<button id="cb" class="cbtn" aria-expanded="false" aria-controls="cp">{t["chat"]}</button><div id="cp" class="cp" hidden role="dialog" aria-label="{t["chat"]}"><p class="ch">{t["chath"]}</p><div id="cl" aria-live="polite"></div><div id="cs" data-s="{t["sug"]}"></div><div class="ci"><input id="cq" placeholder="{t["ph"]}" aria-label="{t["ph"]}"><button id="cg" aria-label="{t["chat"]}">➤</button></div><a class="btn" href="{WA}">{t["wa"]}</a></div>
<script>window.KB={json.dumps(t["kb"],ensure_ascii=False)};window.UNK={json.dumps(t["unk"],ensure_ascii=False)};window.WA="{WA}"</script><script src="{BASE}/js/app.js" defer></script>'''
    html=head(l,p,title,desc)+f'<body>{nav(l)}<main id="main">{bc}{body(l,p)}</main>{foot}</body></html>'
    d=os.path.join("."+url(l,p)[len(BASE):]); os.makedirs(d,exist_ok=True); open(d+"index.html","w",encoding="utf-8").write(html)
if __name__=="__main__":
    for l in L:
        for p in PAGES: page(l,p)
    open("index.html","w",encoding="utf-8").write(f'<!doctype html><meta charset="utf-8"><title>Al Jazeerah Pest Control</title><link rel="canonical" href="{SITE}/en/"><script>var s="en";try{{s=localStorage.getItem("lang")}}catch(e){{}}if(!{json.dumps(L)}.includes(s)){{s=(navigator.language||"en").slice(0,2);if(!{json.dumps(L)}.includes(s))s="en"}}location.replace("{BASE}/"+s+"/")</script><noscript><a href="{BASE}/en/">English</a> <a href="{BASE}/ar/">العربية</a> <a href="{BASE}/zh/">中文</a> <a href="{BASE}/ru/">Русский</a></noscript>')
    missing={"en":("Page not found","This address does not match a page on our site."),"ar":("الصفحة غير موجودة","عنوان الصفحة لا يطابق صفحة على موقعنا."),"zh":("未找到页面","此网址与本网站中的页面不匹配。"),"ru":("Страница не найдена","По этому адресу на сайте нет страницы.")}
    nf_sections="".join(f'<section lang="{x}" dir="{"rtl" if x=="ar" else "ltr"}"><h2>{missing[x][0]}</h2><p>{missing[x][1]}</p><a href="{url(x,"home")}">{T[x]["home"]} ↗</a></section>' for x in L)
    nf=head("en","home","404","Page not found")+f'<body><main class="notfound-page section-shell"><p class="eyebrow">404 / {NAME["en"]}</p><div class="notfound-grid">{nf_sections}</div></main></body></html>'
    open("404.html","w",encoding="utf-8").write(nf)
    sm="".join(f'<url><loc>{full(l,p)}</loc>'+"".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{full(x,p)}"/>' for x in L)+'</url>' for l in L for p in PAGES)
    open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">{sm}</urlset>')
    open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print(len(L)*len(PAGES),"pages")
