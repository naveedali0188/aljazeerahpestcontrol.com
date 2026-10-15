(() => {
  const $ = (selector, parent = document) => parent.querySelector(selector);
  const mb = $(".mb");
  const nav = $("#nv");
  const closeMenu = (restoreFocus = false) => {
    if (!mb || !nav) return;
    nav.classList.remove("open");
    mb.setAttribute("aria-expanded", "false");
    if (restoreFocus) mb.focus();
  };

  if (mb && nav) {
    mb.addEventListener("click", () => {
      const open = mb.getAttribute("aria-expanded") !== "true";
      mb.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("open", open);
    });
    nav.addEventListener("click", event => {
      if (event.target instanceof Element && event.target.closest("a")) closeMenu();
    });
    document.addEventListener("click", event => {
      if (!(event.target instanceof Node)) return;
      if (!nav.contains(event.target) && !mb.contains(event.target)) closeMenu();
    });
  }

  document.querySelectorAll(".lang a").forEach(link => {
    link.addEventListener("click", () => {
      try { localStorage.setItem("lang", link.dataset.l || "en"); } catch { /* Language links still work without storage. */ }
      document.documentElement.classList.add("language-switching");
    });
  });

  const form = $("#qf");
  if (form) {
    form.addEventListener("submit", event => {
      event.preventDefault();
      const name = form.elements.namedItem("n").value.trim();
      const phone = form.elements.namedItem("p").value.trim();
      const message = form.elements.namedItem("m").value.trim().slice(0, 500);
      const status = $("#fs");
      const digits = phone.replace(/\D/g, "");
      if (!name || digits.length < 7 || digits.length > 15) {
        status.textContent = form.dataset.err;
        form.elements.namedItem(!name ? "n" : "p").focus();
        return;
      }
      const text = [name, phone, message].filter(Boolean).join(" | ");
      const link = document.createElement("a");
      link.href = `${form.dataset.wa}?text=${encodeURIComponent(text)}`;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.hidden = true;
      document.body.append(link);
      link.click();
      link.remove();
      status.textContent = form.dataset.ok;
      form.reset();
    });
  }

  const chatButton = $("#cb");
  const chatPanel = $("#cp");
  const chatInput = $("#cq");
  const chatLog = $("#cl");
  const suggestions = $("#cs");
  if (chatButton && chatPanel && chatInput && chatLog && suggestions) {
    const closeChat = (restoreFocus = false) => {
      chatPanel.hidden = true;
      chatButton.setAttribute("aria-expanded", "false");
      if (restoreFocus) chatButton.focus();
    };
    chatButton.addEventListener("click", () => {
      chatPanel.hidden = !chatPanel.hidden;
      chatButton.setAttribute("aria-expanded", String(!chatPanel.hidden));
      if (!chatPanel.hidden) chatInput.focus();
    });

    const tokens = text => {
      const words = text.toLowerCase().match(/[\p{L}\p{N}]+/gu) || [];
      const result = [];
      words.forEach(word => {
        if (/[\u4e00-\u9fff]/u.test(word)) [...word].forEach(char => result.push(char));
        else if (word.length > 2) result.push(word.slice(0, 5));
      });
      return result;
    };
    const appendMessage = (text, className) => {
      const item = document.createElement("p");
      item.textContent = text;
      if (className) item.className = className;
      chatLog.append(item);
      chatLog.scrollTop = chatLog.scrollHeight;
      return item;
    };
    const answer = question => {
      if (!question.trim()) return;
      appendMessage(question, "u");
      const questionTokens = new Set(tokens(question));
      let bestAnswer;
      let bestScore = 0;
      (window.KB || []).forEach(([prompt, response]) => {
        const score = tokens(`${prompt} ${response}`).filter(token => questionTokens.has(token)).length;
        if (score > bestScore) {
          bestAnswer = response;
          bestScore = score;
        }
      });
      appendMessage(bestScore >= 2 ? bestAnswer : window.UNK || "");
    };
    $("#cg")?.addEventListener("click", () => {
      answer(chatInput.value);
      chatInput.value = "";
      chatInput.focus();
    });
    chatInput.addEventListener("keydown", event => {
      if (event.key === "Enter") {
        event.preventDefault();
        $("#cg")?.click();
      }
    });
    (suggestions.dataset.s || "").split("|").filter(Boolean).forEach(question => {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = question;
      button.addEventListener("click", () => answer(question));
      suggestions.append(button);
    });
    document.addEventListener("keydown", event => {
      if (event.key === "Escape" && !chatPanel.hidden) closeChat(true);
      else if (event.key === "Escape" && mb?.getAttribute("aria-expanded") === "true") closeMenu(true);
    });
  }

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reducedMotion && "IntersectionObserver" in window) {
    document.body.classList.add("has-motion");
    const reveal = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          reveal.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -30px 0px" });
    document.querySelectorAll("[data-reveal]").forEach(element => reveal.observe(element));
  }
})();
