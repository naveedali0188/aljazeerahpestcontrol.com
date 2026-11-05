/* ==========================================================================
   Al Jazeerah Pest Control LLC — interactions
   - English / Arabic localisation with RTL switching (?lang=ar + localStorage)
   - Accessible mobile navigation, FAQ accordion
   - Quote form validation with an honest mailto fallback + WhatsApp option
   - Counters and scroll reveal (both respect prefers-reduced-motion)
   ========================================================================== */
(function () {
  'use strict';

  var docEl = document.documentElement;
  docEl.classList.add('js');

  var LANG_KEY = 'aj-lang';
  var PHONE = '055 840 8005';
  var PHONE_HREF = 'tel:+971558408005';
  var WA_HREF = 'https://wa.me/971558408005';
  var MAIL = 'Info@aljazeerahpestcontrol.ae';

  /* ---------------------------------------------------------------- Arabic */
  var AR = {
    'a11y.skip': 'تخطَّ إلى المحتوى الرئيسي',
    'a11y.openMenu': 'فتح القائمة',
    'a11y.mainMenu': 'القائمة الرئيسية',
    'a11y.wa': 'تواصل عبر واتساب',
    'foot.socialAria': 'حسابات التواصل الاجتماعي',
    'foot.quickAria': 'روابط سريعة',
    'foot.servicesAria': 'الخدمات',

    'nav.home': 'الرئيسية',
    'nav.about': 'من نحن',
    'nav.pest': 'مكافحة الحشرات',
    'nav.cleaning': 'التنظيف',
    'nav.locations': 'المواقع',
    'nav.sectors': 'القطاعات',
    'nav.contact': 'اتصل بنا',
    'nav.cta': 'اتصل للحصول على عرض سعر مجاني',

    'hero.badge': 'نخدم دبي والشارقة وعجمان',
    'hero.title': 'مكافحة حشرات احترافية <em>في دبي والشارقة</em>',
    'hero.sub': 'تزيل شركة الجزيرة لمكافحة الحشرات الحشرات من المنازل والمكاتب والمنشآت التجارية، وتساعدك على منع عودتها. أخبرنا بمشكلتك واحصل على عرض سعر مجاني دون أي التزام.',
    'hero.b1': 'فنيون ذوو خبرة للمنازل والشركات',
    'hero.b2': 'معالجات للصراصير والنمل وبق الفراش والنمل الأبيض والقوارض وغيرها',
    'hero.b3': 'عرض سعر مجاني دون أي التزام',
    'hero.call': 'اتصال سريع',
    'hero.wa': 'راسلنا على واتساب',
    'hero.chip': 'عرض سعر مجاني',

    'lead.kicker': 'عرض سعر مجاني',
    'lead.title': 'اطلب عرض سعرك المجاني في خطوات قليلة',
    'lead.text': 'أرسل لنا رسالة عن عقارك، وسيتواصل معك فريقنا لمناقشة المشكلة وترتيب موعد للزيارة.',
    'lead.p1': 'مكاتب في دبي والشارقة',
    'lead.p2': 'منازل ومكاتب ومساحات تجارية',
    'lead.p3': 'مكافحة حشرات وتنظيف للمنازل والمنشآت الصناعية',
    'lead.direct': 'تفضّل التحدث؟ اتصل بنا على',

    'form.title': 'أرسل لنا بريدًا إلكترونيًا',
    'form.name': 'الاسم <span class="req" aria-hidden="true">*</span>',
    'form.phone': 'رقم الهاتف <span class="req" aria-hidden="true">*</span>',
    'form.email': 'البريد الإلكتروني <span class="req" aria-hidden="true">*</span>',
    'form.subject': 'الموضوع <span class="req" aria-hidden="true">*</span>',
    'form.message': 'الرسالة <span class="req" aria-hidden="true">*</span>',
    'form.submit': 'اطلب عرض سعر مجاني',
    'form.note': 'الحقول المعلَّمة بـ * مطلوبة. يفتح هذا النموذج تطبيق البريد الإلكتروني لديك، ولا تُحفظ بياناتك على هذا الموقع.',

    'approved.title': 'معتمدون من',
    'approved.a1': 'شعار بلدية دبي',
    'approved.a2': 'شعار بلدية الشارقة',
    'approved.a3': 'شعار الجمعية الوطنية لإدارة الآفات',

    'about.kicker': 'من نحن',
    'about.title': 'مكافحة حشرات وتنظيف عملي لكل عقار',
    'about.text': 'تحمي شركة الجزيرة لمكافحة الحشرات المنازل والمكاتب والعقارات التجارية في دبي والشارقة وعجمان. يحدد فريقنا مصدر المشكلة ويعالجه، ويوضح لك كيفية منع عودة الحشرات.',
    'about.text2': 'تحتاج تنظيفًا أيضًا؟ يغطي فريق التنظيف لدينا خزانات المياه والزجاج والمنازل والمساحات التجارية.',
    'svc.res.tag': 'المنازل',
    'svc.res.t': 'مكافحة الحشرات للمنازل',
    'svc.res.d': 'معالجات مستهدفة للشقق والفلل والمنازل، مع إرشادات واضحة لعائلتك.',
    'cta.quote': 'احصل على عرض سعر مجاني',
    'svc.com.tag': 'الشركات',
    'svc.com.t': 'مكافحة الحشرات للشركات',
    'svc.com.d': 'برامج مجدولة للمكاتب والمطاعم ومتاجر التجزئة والمستودعات.',
    'svc.prev.tag': 'أوقف تكرار الإصابة',
    'svc.prev.t': 'الوقاية من الحشرات',
    'svc.prev.d': 'فحص وسد لمنافذ دخول الحشرات إلى المكان.',
    'svc.cock.tag': 'الأكثر طلبًا',
    'svc.cock.t': 'مكافحة الصراصير',
    'svc.cock.d': 'معالجة مركّزة للمطابخ والبالوعات ومناطق تحضير الطعام.',

    'stats.kicker': 'لمحة سريعة',
    'stats.title': 'الجزيرة بالأرقام',
    'stats.text': 'معلومات مبنية على الخدمات والمواقع المذكورة في هذا الموقع، دون تقديرات.',
    'stats.s1': 'فروع في دبي والشارقة <small>دبي والشارقة</small>',
    'stats.s2': 'أنواع حشرات نعالجها',
    'stats.s3': 'خدمات تنظيف',
    'stats.s4': 'إمارات نخدمها <small>دبي والشارقة وعجمان</small>',

    'clean.kicker': 'خدمات التنظيف',
    'clean.title': 'مساحة أنظف وأكثر صحة لعائلتك وفريقك',
    'clean.text': 'تنظيف احترافي لخزانات المياه والزجاج والمنازل والعقارات التجارية، بمواعيد تناسبك.',
    'clean.c1': 'تنظيف خزانات المياه',
    'clean.c1d': 'تنظيف وفحص خزانات المياه السكنية والتجارية.',
    'clean.c2': 'تنظيف زجاج النوافذ',
    'clean.c2d': 'تنظيف الزجاج من الداخل والخارج للمنازل والمباني.',
    'clean.c3': 'تنظيف المنازل',
    'clean.c3d': 'تنظيف عميق للشقق والفلل والمنازل العائلية.',
    'clean.c4': 'تنظيف المنشآت التجارية',
    'clean.c4d': 'مكاتب ومتاجر تجزئة ومطاعم ومرافق.',

    'testi.kicker': 'شهادات العملاء',
    'testi.title': 'هذا ما يقوله عملاؤنا',
    'testi.quote': 'أنا عميل سعيد منذ ٥ سنوات. المواد المستخدمة خفيفة الرائحة لكنها فعّالة جدًا، وفريقهم لطيف أيضًا.',
    'testi.name': 'هاريسون كلارك',
    'testi.role': 'الشارقة',

    'pests.kicker': 'الحشرات التي نعالجها',
    'pests.title': 'ماذا ترى؟ نحن نعالجه.',
    'pests.text': 'من الحشرات المنزلية الشائعة إلى النمل الأبيض والثعابين، أخبرنا بما وجدته وسنوصي بالمعالجة المناسبة.',
    'p.cock': 'الصراصير',
    'p.ant': 'النمل',
    'p.bed': 'بق الفراش',
    'p.bee': 'النحل',
    'p.liz': 'الوزغ',
    'p.wasp': 'الدبابير',
    'p.mosq': 'البعوض',
    'p.snake': 'الثعابين',
    'p.term': 'النمل الأبيض',
    'p.rod': 'القوارض',
    'pests.ask': 'استفسر عن المعالجة',

    'cta.callQuote': 'اتصل للحصول على عرض سعر مجاني',
    'cta.wa': 'راسلنا على واتساب',
    'why.kicker': 'لماذا تختارنا',
    'why.title': 'لا مزيد من الاختباء للحشرات',
    'why.text': 'نعالج مصدر المشكلة وليس آثارها فقط، ونترك لك إرشادات واضحة لحماية عقارك.',
    'why.b1': 'فنيون مدربون بمعدات احترافية',
    'why.b2': 'خطط للمنازل والمكاتب وكل قطاع تجاري',
    'why.b3': 'مكاتب في دبي والشارقة، نخدم دولة الإمارات',
    'why.ctaTitle': 'جاهز للبدء؟',
    'why.ctaText': 'احصل على عرض سعر مجاني دون التزام لعقارك اليوم.',

    'loc.kicker': 'المواقع',
    'loc.title': 'زيارة مكاتبنا أو الاتصال بها',
    'loc.text': 'مكتبان يخدمان العملاء في دبي والشارقة وعجمان.',
    'loc.dubai.t': 'مكتب دبي',
    'loc.dubai.a': 'المدينة العالمية، مجموعة إنجلترا، دبي، الإمارات',
    'loc.map': 'افتح في خرائط جوجل',
    'loc.sharjah.t': 'مكتب الشارقة',
    'loc.sharjah.a': 'المنطقة الصناعية، مويلح التجارية، الشارقة، الإمارات',
    'loc.mobile.t': 'الجوال',
    'loc.mobile.d': 'اتصل بنا أو راسلنا على واتساب للحصول على عرض سعر مجاني',

    'sectors.kicker': 'القطاعات',
    'sectors.title': 'القطاعات التي نخدمها',
    'sectors.text': 'برامج مكافحة حشرات وتنظيف مصممة بما يناسب طبيعة عمل قطاعك.',
    'sec.1': 'المنازل والفلل',
    'sec.2': 'المكاتب',
    'sec.3': 'المطاعم والمقاهي',
    'sec.4': 'متاجر التجزئة',
    'sec.5': 'المستودعات',
    'sec.6': 'المرافق الصحية',
    'sec.7': 'المدارس',
    'sec.8': 'الفنادق والصالات الرياضية',

    'faq.kicker': 'الأسئلة الشائعة',
    'faq.title': 'الأسئلة الشائعة',
    'faq.q1': 'هل يستحق مكافحة الحشرات التكلفة؟',
    'faq.a1': 'في معظم المنازل والشركات، نعم. المعالجة الاحترافية تتعامل مع الإصابة من مصدرها، وعادة تكلف أقل من الأضرار التي قد تسببها حشرات مثل النمل الأبيض.',
    'faq.q2': 'كم مرة يجب أن أعالج منزلي؟',
    'faq.a2': 'تُعالج معظم المنازل في الإمارات كل شهرين إلى ثلاثة أشهر. يتوقف الجدول المناسب على نوع الحشرة ومدى الإصابة ونوع العقار.',
    'faq.q3': 'ما أكثر الحشرات شيوعًا في الإمارات؟',
    'faq.a3': 'الصراصير والنمل والنمل الأبيض والقوارض وبق الفراش هي الأكثر شيوعًا. كما نعالج البعوض والنحل والدبابير والوزغ والثعابين.',
    'faq.q4': 'ما علامات الإصابة بالحشرات؟',
    'faq.a4': 'رؤية الحشرات، أو سماع أصوات ليلًا، أو العثور على فضلات أو أعشاش، أو تلف في الممتلكات، أو لدغات غير مفسّرة أو حساسية.',
    'faq.q5': 'ما أفضل وقت في السنة لمكافحة الحشرات؟',
    'faq.a5': 'الربيع والخريف هما الأكثر فاعلية في الإمارات. وإذا رأيت حشرات، عالجها فور ملاحظتها في أي وقت من السنة.',
    'faq.q6': 'ما المناطق التي تخدمونها؟',
    'faq.a6': 'نخدم دبي والشارقة وعجمان، ولدينا مكاتب في دبي والشارقة.',
    'faq.q7': 'هل تقدمون عرض سعر مجاني؟',
    'faq.a7': 'نعم. اتصل على <a href="tel:+971558408005" dir="ltr">055 840 8005</a>، أو أرسل لنا رسالة واتساب، أو استخدم نموذج عرض السعر في هذه الصفحة. لا يوجد أي مقابل لعرض السعر.',

    'cta.kicker': 'احمِ نفسك',
    'cta.title': 'احمِ نفسك من الحشرات، لنبدأ اليوم',
    'cta.text': 'اتصل بنا أو أرسل رسالة واتساب للحصول على عرض سعر وحجز موعد.',
    'cta.book': 'احجز عرض سعر مجاني',

    'foot.about': 'تقدم شركة الجزيرة لمكافحة الحشرات خدمات مكافحة الحشرات والتنظيف للمنازل والشركات في دبي والشارقة وعجمان.',
    'foot.quick': 'روابط سريعة',
    'foot.faq': 'الأسئلة الشائعة',
    'foot.services': 'الخدمات',
    'foot.s1': 'مكافحة الحشرات العامة',
    'foot.s2': 'مكافحة الصراصير',
    'foot.s3': 'مكافحة النمل',
    'foot.s4': 'مكافحة بق الفراش',
    'foot.s5': 'مكافحة البعوض',
    'foot.s6': 'مكافحة النمل الأبيض',
    'foot.s7': 'مكافحة القوارض',
    'foot.s8': 'خدمات التنظيف',
    'foot.contact': 'تواصل معنا',
    'foot.maps': 'خرائط جوجل',
    'foot.rights': '© 2026 شركة الجزيرة لمكافحة الحشرات ذ.م.م. جميع الحقوق محفوظة.',

    'brand.alt': 'شركة الجزيرة لمكافحة الحشرات ذ.م.م',
    'hero.alt1': 'فني مكافحة حشرات يقف بجانب سيارة الخدمة',
    'hero.alt2': 'فني مكافحة حشرات بزي رسمي يحمل جهاز رش',
    'hero.alt3': 'فني ينفذ مكافحة الحشرات في فيلا',
    'stats.alt1': 'عملية مكافحة حشرات جارية',
    'stats.alt2': 'فني بمعدات حماية أثناء تنفيذ المعالجة',
    'clean.i1': 'فني ينظف خزان مياه',
    'clean.i2': 'تنظيف زجاج النوافذ في مبنى',
    'clean.i3': 'فريق تنظيف داخل منزل',
    'clean.i4': 'تنظيف مساحة تجارية',

    'err.name': 'يرجى إدخال اسمك.',
    'err.phone': 'يرجى إدخال رقم هاتف صحيح.',
    'err.email': 'يرجى إدخال بريد إلكتروني صحيح.',
    'err.subject': 'يرجى كتابة موضوع قصير.',
    'err.message': 'يرجى كتابة رسالة قصيرة.',
    'form.opening': 'يفتح تطبيق البريد الإلكتروني الآن مع بياناتك. إذا لم يفتح، اتصل على 055 840 8005 أو أرسل لنا رسالة واتساب.',
    'form.invalid': 'يرجى تصحيح الحقول المعلَّمة أدناه.'
  };

  var MESSAGES = {
    en: {
      'err.name': 'Please enter your name.',
      'err.phone': 'Please enter a valid phone number.',
      'err.email': 'Please enter a valid email address.',
      'err.subject': 'Please add a short subject.',
      'err.message': 'Please write a short message.',
      'form.opening': 'Your email app should open with your details filled in. If nothing opens, call ' + PHONE + ' or send us a WhatsApp message.',
      'form.invalid': 'Please correct the highlighted fields.'
    },
    ar: {
      'err.name': AR['err.name'],
      'err.phone': AR['err.phone'],
      'err.email': AR['err.email'],
      'err.subject': AR['err.subject'],
      'err.message': AR['err.message'],
      'form.opening': AR['form.opening'],
      'form.invalid': AR['form.invalid']
    }
  };

  var META = {
    en: {
      title: 'Al Jazeerah Pest Control LLC | Pest Control & Cleaning in Dubai & Sharjah',
      description: 'Al Jazeerah Pest Control LLC offers professional pest control and cleaning services in Dubai, Sharjah and Ajman for homes and businesses. Free quote: 055 840 8005.'
    },
    ar: {
      title: 'شركة الجزيرة لمكافحة الحشرات | مكافحة الحشرات والتنظيف في دبي والشارقة',
      description: 'تقدم شركة الجزيرة لمكافحة الحشرات خدمات مكافحة الحشرات والتنظيف للمنازل والشركات في دبي والشارقة وعجمان. عرض سعر مجاني: 055 840 8005.'
    }
  };

  /* ------------------------------------------------------------ i18n core  */
  var textNodes = [];
  var ariaNodes = [];
  var altNodes = [];

  Array.prototype.forEach.call(document.querySelectorAll('[data-i18n]'), function (el) {
    textNodes.push({ el: el, key: el.getAttribute('data-i18n'), html: el.innerHTML });
  });
  Array.prototype.forEach.call(document.querySelectorAll('[data-i18n-aria]'), function (el) {
    ariaNodes.push({ el: el, key: el.getAttribute('data-i18n-aria'), value: el.getAttribute('aria-label') || '' });
  });
  Array.prototype.forEach.call(document.querySelectorAll('[data-i18n-alt]'), function (el) {
    altNodes.push({ el: el, key: el.getAttribute('data-i18n-alt'), value: el.getAttribute('alt') || '' });
  });

  var langButtons = document.querySelectorAll('.lang-btn');
  var currentLang = 'en';

  function readLang() {
    var q;
    try { q = new URLSearchParams(window.location.search).get('lang'); } catch (e) { q = null; }
    if (q === 'ar' || q === 'en') return q;
    try {
      var saved = localStorage.getItem(LANG_KEY);
      if (saved === 'ar' || saved === 'en') return saved;
    } catch (e) { /* storage blocked */ }
    return 'en';
  }

  function applyLang(lang, options) {
    var opts = options || {};
    var isAr = lang === 'ar';
    currentLang = lang;

    textNodes.forEach(function (item) {
      var value = isAr ? AR[item.key] : null;
      item.el.innerHTML = (typeof value === 'string') ? value : item.html;
    });
    ariaNodes.forEach(function (item) {
      var label = isAr ? AR[item.key] : null;
      item.el.setAttribute('aria-label', (typeof label === 'string') ? label : item.value);
    });
    altNodes.forEach(function (item) {
      var alt = isAr ? AR[item.key] : null;
      item.el.setAttribute('alt', (typeof alt === 'string') ? alt : item.value);
    });

    docEl.lang = lang;
    docEl.dir = isAr ? 'rtl' : 'ltr';

    document.title = META[lang].title;
    var desc = document.querySelector('meta[name="description"]');
    if (desc) desc.setAttribute('content', META[lang].description);
    var ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle) ogTitle.setAttribute('content', META[lang].title);
    var ogDesc = document.querySelector('meta[property="og:description"]');
    if (ogDesc) ogDesc.setAttribute('content', META[lang].description);

    Array.prototype.forEach.call(langButtons, function (btn) {
      var active = btn.getAttribute('data-lang') === lang;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    });

    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* ignore */ }

    if (opts.updateUrl !== false) {
      try {
        var url = new URL(window.location.href);
        if (isAr) { url.searchParams.set('lang', 'ar'); } else { url.searchParams.delete('lang'); }
        window.history.replaceState(null, '', url.pathname + url.search + url.hash);
      } catch (e) { /* ignore */ }
    }
  }

  Array.prototype.forEach.call(langButtons, function (btn) {
    btn.addEventListener('click', function () {
      var lang = btn.getAttribute('data-lang');
      if (lang === currentLang) return;
      applyLang(lang);
      if (lang === 'ar') {
        /* keep the visual rhythm after a direction flip */
        window.requestAnimationFrame(function () { refreshObservers(); });
      }
    });
  });

  applyLang(readLang(), { updateUrl: false });

  /* ---------------------------------------------------------- Mobile nav   */
  var header = document.querySelector('.site-header');
  var navToggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');

  function setNav(open) {
    if (!header || !navToggle) return;
    header.classList.toggle('is-open', open);
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    navToggle.setAttribute('aria-label', open
      ? (currentLang === 'ar' ? 'إغلاق القائمة' : 'Close menu')
      : (currentLang === 'ar' ? 'فتح القائمة' : 'Open menu'));
    document.body.classList.toggle('nav-open', open);
  }

  if (navToggle) {
    navToggle.addEventListener('click', function () {
      setNav(!header.classList.contains('is-open'));
    });
  }

  if (nav) {
    nav.addEventListener('click', function (event) {
      var link = event.target.closest('a');
      if (link && link.hash) setNav(false);
    });
  }

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      if (header && header.classList.contains('is-open')) {
        setNav(false);
        navToggle.focus();
      }
    }
    if (event.key === 'Tab' && header && header.classList.contains('is-open')) {
      var focusables = header.querySelectorAll('a[href], button:not([disabled])');
      if (!focusables.length) return;
      var first = focusables[0];
      var last = focusables[focusables.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  document.addEventListener('click', function (event) {
    if (!header || !header.classList.contains('is-open')) return;
    if (!header.contains(event.target)) setNav(false);
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 980 && header && header.classList.contains('is-open')) setNav(false);
  });

  /* Sticky header shadow */
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* -------------------------------------------------------- Active nav link */
  var navLinks = nav ? Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]')) : [];
  var sections = navLinks.map(function (link) {
    return document.querySelector(link.hash);
  }).filter(Boolean);

  function setActiveLink(id) {
    navLinks.forEach(function (link) {
      var active = link.hash === '#' + id;
      link.classList.toggle('is-current', active);
      if (active) { link.setAttribute('aria-current', 'true'); }
      else { link.removeAttribute('aria-current'); }
    });
  }

  /* --------------------------------------------------------- FAQ accordion */
  var faqItems = document.querySelectorAll('.faq__item');
  Array.prototype.forEach.call(faqItems, function (item) {
    item.addEventListener('toggle', function () {
      if (!item.open) return;
      Array.prototype.forEach.call(faqItems, function (other) {
        if (other !== item && other.open) other.open = false;
      });
    });
  });

  /* ---------------------------------------------------------------- Reveal */
  /* A simple rect check on scroll is used instead of IntersectionObserver so
     content can never stay hidden if an observer callback is missed. */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var counters = Array.prototype.slice.call(document.querySelectorAll('[data-count]'));

  function inView(el, ratio) {
    var rect = el.getBoundingClientRect();
    var vh = window.innerHeight || docEl.clientHeight;
    return rect.top < vh * ratio && rect.bottom > 0;
  }

  function revealPass() {
    var i;
    for (i = revealEls.length - 1; i >= 0; i--) {
      if (inView(revealEls[i], 0.94)) {
        revealEls[i].classList.add('is-visible');
        revealEls.splice(i, 1);
      }
    }
    for (i = counters.length - 1; i >= 0; i--) {
      if (inView(counters[i], 0.98)) {
        runCounter(counters[i]);
        counters.splice(i, 1);
      }
    }
  }

  /* Throttled with a timestamp rather than requestAnimationFrame so the pass
     still runs in environments where animation frames are throttled. */
  var lastRevealPass = 0;
  function onRevealScroll() {
    var now = Date.now();
    if (now - lastRevealPass < 90) return;
    lastRevealPass = now;
    revealPass();
  }

  if (reduceMotion.matches) {
    Array.prototype.forEach.call(revealEls, function (el) { el.classList.add('is-visible'); });
    revealEls = [];
    Array.prototype.forEach.call(counters, function (el) { el.textContent = el.getAttribute('data-count'); });
    counters = [];
  } else {
    window.addEventListener('scroll', onRevealScroll, { passive: true });
    window.addEventListener('resize', onRevealScroll);
    window.addEventListener('load', onRevealScroll);
    revealPass();
  }

  /* -------------------------------------------------------------- Counters */

  function runCounter(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    if (isNaN(target)) return;
    if (reduceMotion.matches) {
      el.textContent = String(target);
      return;
    }
    var duration = 1100;
    var start = Date.now();
    el.textContent = '0';
    function step() {
      var progress = Math.min((Date.now() - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = String(Math.round(target * eased));
      if (progress < 1) window.setTimeout(step, 40);
      else el.textContent = String(target);
    }
    window.setTimeout(step, 40);
  }

  /* -------------------------------------------------- Section spy (nav) */
  if ('IntersectionObserver' in window && sections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) setActiveLink(entry.target.id);
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    sections.forEach(function (section) { spy.observe(section); });
  }

  function refreshObservers() {
    revealPass();
  }

  /* ------------------------------------------------------------ Quote form */
  var form = document.getElementById('quote-form');
  var status = document.getElementById('form-status');
  var statusDefault = status ? status.innerHTML : '';

  if (form) {
    var fields = [
      { id: 'f-name', error: 'e-name', message: 'err.name', validate: function (v) { return v.trim().length >= 2; } },
      { id: 'f-phone', error: 'e-phone', message: 'err.phone', validate: function (v) { return /^[+()\d][\d\s\-()]{5,}$/.test(v.trim()); } },
      { id: 'f-email', error: 'e-email', message: 'err.email', validate: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); } },
      { id: 'f-subject', error: 'e-subject', message: 'err.subject', validate: function (v) { return v.trim().length >= 3; } },
      { id: 'f-message', error: 'e-message', message: 'err.message', validate: function (v) { return v.trim().length >= 10; } }
    ];

    var setStatus = function (message, kind, allowHtml) {
      if (!status) return;
      status.classList.remove('is-success', 'is-error');
      if (kind) status.classList.add(kind);
      if (message) {
        if (allowHtml) status.innerHTML = message;
        else status.textContent = message;
      } else {
        status.innerHTML = statusDefault;
      }
    };

    var validateField = function (field) {
      var input = document.getElementById(field.id);
      var errorEl = document.getElementById(field.error);
      if (!input) return true;
      var valid = field.validate(input.value);
      input.setAttribute('aria-invalid', valid ? 'false' : 'true');
      if (errorEl) errorEl.textContent = valid ? '' : MESSAGES[currentLang][field.message];
      return valid;
    };

    fields.forEach(function (field) {
      var input = document.getElementById(field.id);
      if (!input) return;
      input.addEventListener('blur', function () {
        if (input.value.trim() === '') return;
        validateField(field);
      });
      input.addEventListener('input', function () {
        if (input.getAttribute('aria-invalid') === 'true') validateField(field);
      });
    });

    form.addEventListener('submit', function (event) {
      event.preventDefault();

      var invalid = [];
      fields.forEach(function (field) {
        if (!validateField(field)) invalid.push(field);
      });

      if (invalid.length) {
        setStatus(MESSAGES[currentLang]['form.invalid'], 'is-error', false);
        var firstInput = document.getElementById(invalid[0].id);
        if (firstInput) firstInput.focus();
        return;
      }

      var value = function (id) {
        var el = document.getElementById(id);
        return el ? el.value.trim() : '';
      };

      var subject = 'Quote request: ' + value('f-subject');
      var body = [
        'Name: ' + value('f-name'),
        'Phone: ' + value('f-phone'),
        'Email: ' + value('f-email'),
        '',
        value('f-message')
      ].join('\n');

      var mailto = 'mailto:' + MAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      var waText = encodeURIComponent('Quote request (' + value('f-subject') + ')\n' + value('f-name') + ' — ' + value('f-phone') + '\n' + value('f-message'));

      setStatus(
        MESSAGES[currentLang]['form.opening'] +
        ' <a href="' + WA_HREF + '?text=' + waText + '" target="_blank" rel="noopener">WhatsApp</a>',
        'is-success',
        true
      );

      window.location.href = mailto;
    });

    /* Re-render messages that were produced before the language changed:
       the status note and any visible field errors. */
    Array.prototype.forEach.call(langButtons, function (btn) {
      btn.addEventListener('click', function () {
        if (status) {
          status.classList.remove('is-success', 'is-error');
          statusDefault = status.innerHTML;
        }
        fields.forEach(function (field) {
          var input = document.getElementById(field.id);
          if (input && input.getAttribute('aria-invalid') === 'true') validateField(field);
        });
      });
    });
  }
})();
