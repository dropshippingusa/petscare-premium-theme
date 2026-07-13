/**
 * PetsCare.com — Theme JavaScript
 * Shopify-Native: Uses /search/suggest.json, /cart/add.js, /cart/change.js
 * No external dependencies. Vanilla JS only.
 */

'use strict';

const PetsCare = {

  /* ─── CART ─────────────────────────────────────────────────────────────── */
  cart: {
    drawer: null,
    countEls: [],

    init() {
      this.drawer = document.getElementById('cart-drawer');
      this.countEls = document.querySelectorAll('#cart-count, #mobile-cart-badge');
      document.querySelectorAll('[data-open-cart]').forEach(el =>
        el.addEventListener('click', e => { e.preventDefault(); this.open(); })
      );
    },

    open() {
      if (!this.drawer) return;
      this.drawer.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      this.refresh();
    },

    close() {
      if (!this.drawer) return;
      this.drawer.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    },

    /** Re-fetch cart state and re-render the drawer */
    async refresh() {
      try {
        const r = await fetch('/cart.js');
        const cart = await r.json();
        this._renderLines(cart);
        this._updateCount(cart.item_count);
        this._updateShippingBar(cart.total_price);
      } catch(e) { console.error('[PetsCare] cart.refresh failed', e); }
    },

    _renderLines(cart) {
      const el = document.getElementById('cart-drawer-lines');
      const footer = document.getElementById('cart-drawer-footer');
      const countLabel = document.getElementById('cart-count-label');
      if (countLabel) countLabel.textContent = `(${cart.item_count})`;

      if (!el) return;

      if (cart.item_count === 0) {
        el.innerHTML = `
          <div class="cart-empty">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#D1D5DB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/>
              <line x1="3" y1="6" x2="21" y2="6"/>
              <path d="M16 10a4 4 0 01-8 0"/>
            </svg>
            <p>Your bag is empty</p>
            <a href="/collections/all" class="btn btn--primary btn--sm" onclick="PetsCare.cart.close()">Start Shopping</a>
          </div>`;
        if (footer) footer.hidden = true;
        return;
      }

      if (footer) footer.hidden = false;

      el.innerHTML = cart.items.map(item => {
        const variant = item.variant_title && item.variant_title !== 'Default Title'
          ? `<p class="cart-item__variant">${item.variant_title}</p>` : '';
        return `
          <div class="cart-item" data-key="${item.key}">
            <a href="${item.url}">
              <img src="${item.image}" alt="${item.title}" width="80" height="80" class="cart-item__img" loading="lazy">
            </a>
            <div class="cart-item__info">
              <a href="${item.url}" class="cart-item__title">${item.product_title}</a>
              ${variant}
              <div class="cart-item__bottom">
                <div class="cart-item__qty-control">
                  <button class="cart-item__qty-btn" onclick="PetsCare.cart.change('${item.key}', ${item.quantity - 1})" aria-label="Decrease quantity">−</button>
                  <span class="cart-item__qty-val">${item.quantity}</span>
                  <button class="cart-item__qty-btn" onclick="PetsCare.cart.change('${item.key}', ${item.quantity + 1})" aria-label="Increase quantity">+</button>
                </div>
                <span class="cart-item__price">${PetsCare.utils.formatMoney(item.final_line_price)}</span>
              </div>
            </div>
            <button class="cart-item__remove icon-btn" onclick="PetsCare.cart.change('${item.key}', 0)" aria-label="Remove item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
              </svg>
            </button>
          </div>`;
      }).join('');

      // Update subtotal
      const subtotalEl = document.getElementById('cart-subtotal-amount');
      if (subtotalEl) subtotalEl.textContent = PetsCare.utils.formatMoney(cart.total_price);
    },

    _updateCount(count) {
      const badge = document.getElementById('header-cart-count');
      const mobileBadge = document.getElementById('mobile-cart-badge');
      if (badge) {
        badge.textContent = count;
        badge.hidden = count === 0;
      }
      if (mobileBadge) {
        mobileBadge.textContent = count;
        mobileBadge.hidden = count === 0;
      }
    },

    _updateShippingBar(totalPrice) {
      const bar = document.getElementById('shipping-bar');
      if (!bar) return;
      const threshold = 4900; // $49.00 in cents
      const remaining = threshold - totalPrice;
      if (remaining <= 0) {
        bar.innerHTML = `<p class="shipping-bar__text shipping-bar__text--done">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          You've unlocked <strong>FREE shipping!</strong>
        </p>`;
      } else {
        const pct = Math.min((totalPrice / threshold) * 100, 100);
        bar.innerHTML = `
          <p class="shipping-bar__text">Add <strong>${PetsCare.utils.formatMoney(remaining)}</strong> more for FREE shipping</p>
          <div class="shipping-bar__track">
            <div class="shipping-bar__fill" style="width:${pct}%"></div>
          </div>`;
      }
    },

    /** Add one or more items to cart */
    async add(items, openDrawer = true) {
      try {
        const r = await fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ items })
        });
        if (!r.ok) throw new Error(await r.text());
        PetsCare.utils.showToast('Added to bag!');
        if (openDrawer) this.open();
        else this.refresh();
      } catch(e) {
        console.error('[PetsCare] cart.add failed', e);
        PetsCare.utils.showToast('Could not add item — try again', true);
      }
    },

    /** Update line item quantity (0 = remove) */
    async change(key, quantity) {
      try {
        await fetch('/cart/change.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: key, quantity })
        });
        this.refresh();
      } catch(e) { console.error('[PetsCare] cart.change failed', e); }
    }
  },

  /* ─── SEARCH ────────────────────────────────────────────────────────────── */
  search: {
    overlay: null,
    input: null,
    resultsEl: null,
    _debounceTimer: null,
    _abortCtrl: null,

    init() {
      this.overlay = document.getElementById('search-overlay');
      this.input = document.getElementById('search-input');
      this.resultsEl = document.getElementById('search-results');

      if (!this.overlay || !this.input) return;

      this.input.addEventListener('input', () => {
        clearTimeout(this._debounceTimer);
        this._debounceTimer = setTimeout(() => this._query(this.input.value.trim()), 280);
      });

      // Open on header search icon click
      document.querySelectorAll('[data-open-search]').forEach(el =>
        el.addEventListener('click', e => { e.preventDefault(); this.open(); })
      );

      // Close on Escape
      document.addEventListener('keydown', e => {
        if (e.key === 'Escape') { this.close(); PetsCare.cart.close(); }
      });
    },

    open() {
      if (!this.overlay) return;
      this.overlay.classList.add('is-open');
      this.overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      setTimeout(() => this.input?.focus(), 320);
    },

    close() {
      if (!this.overlay) return;
      this.overlay.classList.remove('is-open');
      this.overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    },

    async _query(q) {
      if (!q || q.length < 2) {
        this.resultsEl.innerHTML = '';
        return;
      }

      // Abort previous in-flight request
      if (this._abortCtrl) this._abortCtrl.abort();
      this._abortCtrl = new AbortController();

      this.resultsEl.innerHTML = `<div class="search-loading">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        Searching…
      </div>`;

      try {
        const url = `/search/suggest.json?q=${encodeURIComponent(q)}&resources[type]=product,collection,article&resources[limit]=6`;
        const r = await fetch(url, { signal: this._abortCtrl.signal });
        const data = await r.json();
        this._renderResults(data.resources?.results || {}, q);
      } catch(e) {
        if (e.name !== 'AbortError') {
          this.resultsEl.innerHTML = '<p class="text-muted" style="padding:16px">No results found.</p>';
        }
      }
    },

    _renderResults(results, q) {
      const products = results.products || [];
      const collections = results.collections || [];
      let html = '';

      if (products.length) {
        html += `<p class="search-results__label">Products</p>
          <div class="search-results__grid">
          ${products.map(p => {
            const price = p.price ? PetsCare.utils.formatMoney(p.price * 100) : '';
            const comparePrice = (p.compare_at_price_min && p.compare_at_price_min > p.price)
              ? PetsCare.utils.formatMoney(p.compare_at_price_min * 100) : '';
            return `<a href="${p.url}" class="search-result-item" onclick="PetsCare.search.close()">
              <img src="${p.featured_image?.url || ''}" alt="${p.title}" class="search-result-item__img" loading="lazy">
              <div>
                <p class="search-result-item__title">${p.title}</p>
                <div style="display:flex;align-items:baseline;gap:6px">
                  <span class="search-result-item__price">${price}</span>
                  ${comparePrice ? `<span class="search-result-item__compare">${comparePrice}</span>` : ''}
                </div>
              </div>
            </a>`;
          }).join('')}
          </div>`;
      }

      if (collections.length) {
        html += `<p class="search-results__label" style="margin-top:20px">Collections</p>
          ${collections.map(c => `
            <a href="${c.url}" class="search-result-item" onclick="PetsCare.search.close()">
              <div class="search-result-item__img" style="background:var(--bg-subtle);display:flex;align-items:center;justify-content:center">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#9CA3AF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/></svg>
              </div>
              <div><p class="search-result-item__title">${c.title}</p></div>
            </a>`).join('')}`;
      }

      if (!html) {
        html = `<p class="text-muted" style="padding:16px">No results for "<strong>${q}</strong>". <a href="/search?q=${encodeURIComponent(q)}&type=product" style="color:var(--primary)">View all results</a></p>`;
      } else {
        html += `<div style="padding:16px 8px;border-top:1px solid var(--border);margin-top:12px">
          <a href="/search?q=${encodeURIComponent(q)}&type=product" style="font-size:14px;font-weight:600;color:var(--primary)">
            View all results for "${q}" →
          </a>
        </div>`;
      }

      this.resultsEl.innerHTML = html;
    }
  },

  /* ─── MEGA MENU ─────────────────────────────────────────────────────────── */
  megaMenu: {
    init() {
      const triggers = document.querySelectorAll('[data-mega-trigger]');
      const menus = document.querySelectorAll('[data-mega-menu]');
      let closeTimer;

      triggers.forEach(trigger => {
        const targetId = trigger.dataset.megaTrigger;
        const menu = document.querySelector(`[data-mega-menu="${targetId}"]`);
        if (!menu) return;

        trigger.addEventListener('mouseenter', () => {
          clearTimeout(closeTimer);
          menus.forEach(m => m.classList.remove('is-open'));
          menu.classList.add('is-open');
        });
        trigger.addEventListener('focus', () => {
          menus.forEach(m => m.classList.remove('is-open'));
          menu.classList.add('is-open');
        });
        menu.addEventListener('mouseenter', () => clearTimeout(closeTimer));
        menu.addEventListener('mouseleave', () => {
          closeTimer = setTimeout(() => menu.classList.remove('is-open'), 150);
        });
        trigger.addEventListener('mouseleave', () => {
          closeTimer = setTimeout(() => menu.classList.remove('is-open'), 150);
        });
      });

      // Close on outside click
      document.addEventListener('click', e => {
        if (!e.target.closest('[data-mega-trigger]') && !e.target.closest('[data-mega-menu]')) {
          menus.forEach(m => m.classList.remove('is-open'));
        }
      });
    }
  },

  /* ─── HEADER SCROLL ─────────────────────────────────────────────────────── */
  header: {
    init() {
      const header = document.querySelector('.site-header');
      if (!header) return;
      const onScroll = () => {
        header.classList.toggle('is-scrolled', window.scrollY > 10);
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  },

  /* ─── COUNTDOWN TIMER ───────────────────────────────────────────────────── */
  countdown: {
    init() {
      const timers = document.querySelectorAll('[data-countdown]');
      timers.forEach(el => {
        const endTime = parseInt(el.dataset.countdown, 10);
        this._tick(el, endTime);
        setInterval(() => this._tick(el, endTime), 1000);
      });
    },
    _tick(el, endTime) {
      const now = Date.now();
      let diff = Math.max(0, endTime - now);
      const h = Math.floor(diff / 3600000); diff -= h * 3600000;
      const m = Math.floor(diff / 60000); diff -= m * 60000;
      const s = Math.floor(diff / 1000);
      const pad = n => String(n).padStart(2, '0');
      const hEl = el.querySelector('[data-unit="h"]');
      const mEl = el.querySelector('[data-unit="m"]');
      const sEl = el.querySelector('[data-unit="s"]');
      if (hEl) hEl.textContent = pad(h);
      if (mEl) mEl.textContent = pad(m);
      if (sEl) sEl.textContent = pad(s);
    }
  },

  /* ─── PDP INTERACTIONS ──────────────────────────────────────────────────── */
  pdp: {
    init() {
      this._initGallery();
      this._initVariants();
      this._initQty();
      this._initTabs();
      this._initFbt();
    },

    _initGallery() {
      const mainImg = document.getElementById('pdp-main-img');
      const thumbs = document.querySelectorAll('.pdp-thumb');
      if (!mainImg || !thumbs.length) return;
      thumbs.forEach(thumb => {
        thumb.addEventListener('click', () => {
          thumbs.forEach(t => t.classList.remove('is-active'));
          thumb.classList.add('is-active');
          const src = thumb.dataset.src;
          if (src) {
            mainImg.style.opacity = '0';
            setTimeout(() => { mainImg.src = src; mainImg.style.opacity = '1'; }, 180);
          }
        });
      });
    },

    _initVariants() {
      const pills = document.querySelectorAll('.variant-pill');
      const priceEl = document.getElementById('pdp-price');
      const comparePriceEl = document.getElementById('pdp-compare-price');
      const variantInput = document.getElementById('pdp-variant-id');

      pills.forEach(pill => {
        pill.addEventListener('click', () => {
          // Deselect siblings in same option group
          const group = pill.closest('.variant-pills');
          group?.querySelectorAll('.variant-pill').forEach(p => p.classList.remove('is-selected'));
          pill.classList.add('is-selected');

          // Update selected display text
          const label = pill.closest('.variant-group')?.querySelector('.variant-group__label span');
          if (label) label.textContent = pill.dataset.value;

          // If variant id provided, update hidden input and prices
          const variantId = pill.dataset.variantId;
          const price = pill.dataset.price;
          const comparePrice = pill.dataset.comparePrice;

          if (variantInput && variantId) variantInput.value = variantId;
          if (priceEl && price) priceEl.textContent = PetsCare.utils.formatMoney(parseInt(price));
          if (comparePriceEl) {
            if (comparePrice && parseInt(comparePrice) > parseInt(price)) {
              comparePriceEl.textContent = PetsCare.utils.formatMoney(parseInt(comparePrice));
              comparePriceEl.hidden = false;
            } else {
              comparePriceEl.hidden = true;
            }
          }
        });
      });
    },

    _initQty() {
      const input = document.getElementById('pdp-qty');
      document.querySelectorAll('[data-qty-change]').forEach(btn => {
        btn.addEventListener('click', () => {
          if (!input) return;
          const delta = parseInt(btn.dataset.qtyChange);
          const val = Math.max(1, (parseInt(input.value) || 1) + delta);
          input.value = val;
        });
      });
    },

    _initTabs() {
      const btns = document.querySelectorAll('.pdp-tab-btn');
      const panels = document.querySelectorAll('.pdp-tab-panel');
      btns.forEach(btn => {
        btn.addEventListener('click', () => {
          btns.forEach(b => b.classList.remove('is-active'));
          panels.forEach(p => p.classList.remove('is-active'));
          btn.classList.add('is-active');
          const panel = document.getElementById(btn.dataset.tab);
          if (panel) panel.classList.add('is-active');
        });
      });
    },

    _initFbt() {
      const fbtForm = document.getElementById('fbt-form');
      if (!fbtForm) return;
      const totalEl = document.getElementById('fbt-total');

      const recalc = () => {
        let total = 0;
        fbtForm.querySelectorAll('.fbt-item__check:checked').forEach(cb => {
          total += parseInt(cb.dataset.price || 0);
        });
        if (totalEl) totalEl.textContent = PetsCare.utils.formatMoney(total);
      };

      fbtForm.querySelectorAll('.fbt-item__check').forEach(cb => cb.addEventListener('change', recalc));
      recalc();

      fbtForm.addEventListener('submit', async e => {
        e.preventDefault();
        const items = [];
        fbtForm.querySelectorAll('.fbt-item__check:checked').forEach(cb => {
          if (cb.dataset.variantId) items.push({ id: parseInt(cb.dataset.variantId), quantity: 1 });
        });
        if (items.length) await PetsCare.cart.add(items);
      });
    }
  },

  /* ─── WISHLIST (localStorage — session, no app needed) ──────────────────── */
  wishlist: {
    _key: 'pc_wishlist',
    get() { try { return JSON.parse(localStorage.getItem(this._key) || '[]'); } catch { return []; } },
    toggle(id) {
      let list = this.get();
      const idx = list.indexOf(id);
      if (idx > -1) list.splice(idx, 1);
      else list.push(id);
      localStorage.setItem(this._key, JSON.stringify(list));
      return idx === -1;
    },
    has(id) { return this.get().includes(id); },
    init() {
      document.querySelectorAll('[data-wishlist-toggle]').forEach(btn => {
        const id = btn.dataset.wishlistToggle;
        if (this.has(id)) btn.classList.add('is-wishlisted');
        btn.addEventListener('click', e => {
          e.preventDefault();
          const added = this.toggle(id);
          btn.classList.toggle('is-wishlisted', added);
          PetsCare.utils.showToast(added ? 'Added to wishlist' : 'Removed from wishlist');
        });
      });
    }
  },

  /* ─── COLLECTION FILTERS ────────────────────────────────────────────────── */
  filters: {
    init() {
      const form = document.getElementById('CollectionFiltersForm');
      if (!form) return;
      // Auto-submit on change (Shopify URL-based filtering)
      form.querySelectorAll('input[type="checkbox"], select').forEach(el => {
        el.addEventListener('change', () => form.submit());
      });
      // Mobile filter toggle
      const toggleBtn = document.getElementById('filter-toggle');
      const sidebar = document.querySelector('.collection-sidebar');
      if (toggleBtn && sidebar) {
        toggleBtn.addEventListener('click', () => sidebar.classList.toggle('is-open'));
      }
    }
  },

  /* ─── UTILITIES ─────────────────────────────────────────────────────────── */
  utils: {
    formatMoney(cents) {
      return '$' + (cents / 100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },

    showToast(msg, isError = false) {
      const toast = document.getElementById('cart-toast');
      const msgEl = document.getElementById('cart-toast-msg');
      if (!toast || !msgEl) return;
      msgEl.textContent = msg;
      toast.style.background = isError ? '#DC2626' : '';
      toast.classList.add('is-visible');
      setTimeout(() => toast.classList.remove('is-visible'), 3000);
    }
  },

  /* ─── BOOTSTRAP ─────────────────────────────────────────────────────────── */
  init() {
    this.header.init();
    this.cart.init();
    this.search.init();
    this.megaMenu.init();
    this.countdown.init();
    this.wishlist.init();
    this.filters.init();
    // PDP only
    if (document.querySelector('.pdp-layout')) this.pdp.init();
  }
};

document.addEventListener('DOMContentLoaded', () => PetsCare.init());
