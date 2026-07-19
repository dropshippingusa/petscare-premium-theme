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
      // InitiateCheckout Event Binding
      document.addEventListener('click', e => {
        if (e.target.closest('[href="/checkout"]') || e.target.closest('.cart-checkout-btn')) {
          document.dispatchEvent(new CustomEvent('petsCare:initiateCheckout', {
            detail: { currency: 'USD' }
          }));
        }
      });
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

    /** Re-fetch cart state and re-render the drawer & full page */
    async refresh() {
      try {
        const r = await fetch(window.location.pathname + window.location.search, { cache: 'no-store' });
        const htmlText = await r.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlText, 'text/html');

        const newLines = doc.getElementById('cart-drawer-lines');
        const oldLines = document.getElementById('cart-drawer-lines');
        if (newLines && oldLines) {
          oldLines.innerHTML = newLines.innerHTML;
        }

        const newFooter = doc.getElementById('cart-drawer-footer');
        const oldFooter = document.getElementById('cart-drawer-footer');
        if (newFooter && oldFooter) {
          oldFooter.innerHTML = newFooter.innerHTML;
          oldFooter.hidden = newFooter.hasAttribute('hidden') || newFooter.style.display === 'none';
        }

        const newShipping = doc.getElementById('shipping-bar');
        const oldShipping = document.getElementById('shipping-bar');
        if (newShipping && oldShipping) {
          oldShipping.innerHTML = newShipping.innerHTML;
        }

        const cartJsonRequest = await fetch('/cart.js');
        const cart = await cartJsonRequest.json();
        this._updateCount(cart.item_count);

        const oldCartPage = document.getElementById('cart-page-container');
        const newCartPage = doc.getElementById('cart-page-container');
        if (oldCartPage && newCartPage) {
          oldCartPage.innerHTML = newCartPage.innerHTML;
        }
      } catch(e) {
        console.error('[PetsCare] cart.refresh failed, reloading page', e);
        window.location.reload();
      }
    },

    async updateNote(note) {
      try {
        await fetch('/cart/update.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ note })
        });
        PetsCare.utils.showToast('Note updated!');
      } catch(e) { console.error('[PetsCare] updateNote failed', e); }
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
            <p>Your cart is empty</p>
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
      const deliveryEst = PetsCare.utils.getDeliveryEstimateString();
      bar.innerHTML = `<p class="shipping-bar__text shipping-bar__text--done">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
        You've unlocked <strong>FREE shipping!</strong>
      </p>
      <p class="shipping-bar__text" style="color:var(--green);font-weight:700;margin-top:6px;margin-bottom:0">${deliveryEst}</p>`;
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
        
        // Dispatch AddToCart Event
        document.dispatchEvent(new CustomEvent('petsCare:addToCart', {
          detail: { items, currency: 'USD' }
        }));

        PetsCare.utils.showToast('Added to cart!');
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

      // Dispatch Search Event
      document.dispatchEvent(new CustomEvent('petsCare:search', {
        detail: { query: q }
      }));

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

  /* ─── HEADER SCROLL & ANNOUNCEMENT BAR ──────────────────────────────────── */
  header: {
    init() {
      const header = document.querySelector('.site-header-wrapper');
      if (header) {
        const isProductPage = document.body.classList.contains('template-product');
        if (isProductPage) {
          header.classList.add('is-sticky');
        }

        // Set initial header height for content padding offset
        const setInitialHeight = () => {
          document.documentElement.style.setProperty('--header-initial-h', `${header.offsetHeight}px`);
        };
        setInitialHeight();
        setTimeout(setInitialHeight, 100);

        // Update heights for other sticky elements (like the PDP gallery)
        const updateHeights = () => {
          document.documentElement.style.setProperty('--header-h', `${header.offsetHeight}px`);
        };
        updateHeights();

        // Scroll tracking logic - always sticky, compact on scroll down
        const onScroll = () => {
          const currentScrollY = window.scrollY;
          header.classList.toggle('is-scrolled', currentScrollY > 10);

          if (!isProductPage) {
            if (currentScrollY > 50) {
              header.classList.add('is-sticky');
            } else {
              header.classList.remove('is-sticky');
            }
          }
          updateHeights();
        };

        window.addEventListener('scroll', onScroll, { passive: true });
        window.addEventListener('resize', () => {
          setInitialHeight();
          updateHeights();
        });
        onScroll();
      }
      this._initAnnouncementTicker();
    },
    _initAnnouncementTicker() {
      const ticker = document.getElementById('announcement-bar-ticker');
      if (!ticker) return;
      const slides = ticker.querySelectorAll('.announcement-slide');
      if (slides.length <= 1) return;
      let activeIdx = 0;
      setInterval(() => {
        const activeSlide = slides[activeIdx];
        activeSlide.style.opacity = '0';
        activeSlide.style.transition = 'opacity 300ms ease';
        setTimeout(() => {
          activeSlide.style.display = 'none';
          activeSlide.classList.remove('is-active');
          activeIdx = (activeIdx + 1) % slides.length;
          
          const nextSlide = slides[activeIdx];
          nextSlide.style.display = 'block';
          nextSlide.classList.add('is-active');
          nextSlide.offsetHeight; // trigger reflow
          nextSlide.style.opacity = '1';
          nextSlide.style.transition = 'opacity 300ms ease';
        }, 300);
      }, 4000);
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
          if (document.getElementById('wishlist-grid')) {
            this.renderPage();
          }
        });
      });

      if (document.getElementById('wishlist-grid')) {
        this.renderPage();
      }
    },
    async renderPage() {
      const grid = document.getElementById('wishlist-grid');
      const empty = document.getElementById('wishlist-empty');
      const loading = document.getElementById('wishlist-loading');
      if (!grid) return;

      const list = this.get();
      if (list.length === 0) {
        if (loading) loading.style.display = 'none';
        if (empty) empty.style.display = 'block';
        grid.style.display = 'none';
        return;
      }

      if (loading) loading.style.display = 'block';
      if (empty) empty.style.display = 'none';
      grid.style.display = 'none';

      const q = list.map(id => `id:${id}`).join(' OR ');
      try {
        const url = `/search?view=recently-viewed&type=product&q=${encodeURIComponent(q)}`;
        const r = await fetch(url);
        const html = await r.text();
        if (html && html.trim().length > 10) {
          grid.innerHTML = html;
          if (loading) loading.style.display = 'none';
          grid.style.display = 'grid';
          this.init(); // rebind buttons
        } else {
          if (loading) loading.style.display = 'none';
          if (empty) empty.style.display = 'block';
        }
      } catch(e) {
        console.error('[PetsCare] renderWishlist failed', e);
        if (loading) loading.style.display = 'none';
        if (empty) empty.style.display = 'block';
      }
    }
  },

  /* ─── COLLECTION FILTERS ────────────────────────────────────────────────── */
  filters: {
    init() {
      const form = document.getElementById('CollectionFiltersForm');
      if (!form) return;
      // Auto-submit checkboxes
      form.querySelectorAll('input[type="checkbox"]').forEach(el => {
        el.addEventListener('change', () => {
          this._applyFilters(form);
        });
      });
    },

    _applyFilters(form) {
      const url = new URL(window.location.href);
      // Collect checked tags
      const tags = [...form.querySelectorAll('input[name="filter_tag"]:checked')].map(el => el.value);
      const availability = form.querySelector('input[name="available"]:checked');
      const priceMin = form.querySelector('#price-min')?.value;
      const priceMax = form.querySelector('#price-max')?.value;
      // Build tag URL path: /collections/handle/tag1+tag2
      const basePath = window.location.pathname.split('/').filter(p => !p.startsWith('tag')).join('/');
      let newPath = basePath;
      if (tags.length) newPath = newPath.replace(/\/$/, '') + '/' + tags.join('+');
      // Query params for price, availability
      url.pathname = newPath;
      if (availability) url.searchParams.set('available', 'true');
      else url.searchParams.delete('available');
      if (priceMin) url.searchParams.set('price_min', priceMin);
      else url.searchParams.delete('price_min');
      if (priceMax) url.searchParams.set('price_max', priceMax);
      else url.searchParams.delete('price_max');
      window.location.href = url.toString();
    },

    sort(value) {
      const url = new URL(window.location.href);
      url.searchParams.set('sort_by', value);
      window.location.href = url.toString();
    },

    openMobile() {
      const sidebar = document.getElementById('collection-sidebar');
      const backdrop = document.getElementById('sidebar-backdrop');
      if (sidebar) sidebar.classList.add('is-open');
      if (backdrop) backdrop.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    },

    closeMobile() {
      const sidebar = document.getElementById('collection-sidebar');
      const backdrop = document.getElementById('sidebar-backdrop');
      if (sidebar) sidebar.classList.remove('is-open');
      if (backdrop) backdrop.classList.remove('is-open');
      document.body.style.overflow = '';
    },

    toggleGroup(btn) {
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', isExpanded ? 'false' : 'true');
    }
  },

  /* ─── PDP ───────────────────────────────────────────────────────────────── */
  pdp: {
    init() {
      this._initGallery();
      this._initVariants();
      this._initQtyControls();
      this._initTabs();
      this._initStickyAtc();
      this._initFbt();
      this._initProductFormSubmit();
      this._initDeliveryEstimator();
      this._trackRecentlyViewed();
      this._initDescriptionToggle();
      this._initLightbox();

      // Dispatch ViewContent Event on initial load
      const data = window.PetsCareProductData;
      if (data) {
        document.dispatchEvent(new CustomEvent('petsCare:viewContent', {
          detail: {
            id: data.id,
            title: data.title,
            price: data.price / 100,
            currency: 'USD'
          }
        }));
      }
    },

    /* Gallery: thumbnail → main image swap */
    _initGallery() {
      const thumbs = document.querySelectorAll('.pdp-thumb');
      const mainImg = document.getElementById('pdp-main-img');
      if (!thumbs.length || !mainImg) return;

      thumbs.forEach(thumb => {
        thumb.addEventListener('click', () => {
          thumbs.forEach(t => t.classList.remove('is-active'));
          thumb.classList.add('is-active');
          const newSrc = thumb.dataset.src;
          if (newSrc && mainImg.src !== newSrc) {
            // Set both src and srcset to force browsers (especially mobile) to update instantly
            mainImg.src = newSrc;
            mainImg.srcset = newSrc;
          }
        });
      });
    },

    _initLightbox() {
      const modal = document.getElementById('pdp-gallery-modal');
      const mainGalleryImg = document.getElementById('pdp-main-img');
      const closeBtn = document.getElementById('pdp-gallery-modal-close');
      const prevBtn = document.getElementById('pdp-gallery-modal-prev');
      const nextBtn = document.getElementById('pdp-gallery-modal-next');
      const modalImg = document.getElementById('pdp-gallery-modal-img');
      const modalThumbs = document.querySelectorAll('.pdp-gallery-modal__thumb');
      const triggerMore = document.querySelector('.pdp-thumb--more');

      if (!modal || !mainGalleryImg) return;

      let currentIdx = 0;

      const openModal = (idx = 0) => {
        currentIdx = idx;
        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        updateModalSlide();
      };

      const closeModal = () => {
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      };

      const updateModalSlide = () => {
        modalThumbs.forEach((thumb, index) => {
          if (index === currentIdx) {
            thumb.classList.add('is-active');
            modalImg.src = thumb.dataset.src;
            thumb.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
          } else {
            thumb.classList.remove('is-active');
          }
        });
      };

      mainGalleryImg.style.cursor = 'zoom-in';
      mainGalleryImg.addEventListener('click', () => {
        const activeThumb = document.querySelector('.pdp-thumb.is-active');
        let startIdx = 0;
        if (activeThumb) {
          const thumbsArray = Array.from(document.querySelectorAll('.pdp-thumb'));
          startIdx = thumbsArray.indexOf(activeThumb);
        }
        openModal(startIdx >= 0 ? startIdx : 0);
      });

      if (triggerMore) {
        triggerMore.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          openModal(4);
        });
      }

      closeBtn.addEventListener('click', closeModal);
      modal.addEventListener('click', (e) => {
        if (e.target === modal || e.target.classList.contains('pdp-gallery-modal__container')) {
          closeModal();
        }
      });

      prevBtn.addEventListener('click', () => {
        currentIdx = currentIdx === 0 ? modalThumbs.length - 1 : currentIdx - 1;
        updateModalSlide();
      });

      nextBtn.addEventListener('click', () => {
        currentIdx = currentIdx === modalThumbs.length - 1 ? 0 : currentIdx + 1;
        updateModalSlide();
      });

      modalThumbs.forEach(thumb => {
        thumb.addEventListener('click', () => {
          currentIdx = parseInt(thumb.dataset.index);
          updateModalSlide();
        });
      });

      document.addEventListener('keydown', (e) => {
        if (!modal.classList.contains('is-open')) return;
        if (e.key === 'Escape') {
          closeModal();
        } else if (e.key === 'ArrowLeft') {
          prevBtn.click();
        } else if (e.key === 'ArrowRight') {
          nextBtn.click();
        }
      });
    },

    _initDescriptionToggle() {
      const wrapper = document.getElementById('pdp-desc-wrapper');
      const content = document.getElementById('pdp-desc-content');
      const toggleBtn = document.getElementById('pdp-desc-toggle');
      const fade = document.getElementById('pdp-desc-fade');
      if (!wrapper || !content || !toggleBtn) return;

      const limit = 220;
      if (content.scrollHeight > limit) {
        toggleBtn.style.display = 'inline-flex';
      } else {
        if (fade) fade.style.display = 'none';
      }

      toggleBtn.addEventListener('click', () => {
        const isExpanded = wrapper.classList.toggle('is-expanded');
        toggleBtn.textContent = isExpanded ? 'See Less' : 'See More';
      });
    },

    _initDeliveryEstimator() {
      const el = document.getElementById('pdp-delivery-estimator');
      if (el) el.textContent = PetsCare.utils.getDeliveryEstimateString();
    },

    _trackRecentlyViewed() {
      const data = window.PetsCareProductData;
      if (!data || !data.id) return;
      let list = [];
      try {
        list = JSON.parse(localStorage.getItem('pc_recently_viewed') || '[]');
      } catch(e) {}
      list = list.filter(id => id !== data.id);
      list.unshift(data.id);
      list = list.slice(0, 6);
      localStorage.setItem('pc_recently_viewed', JSON.stringify(list));
    },

    async _renderRecentlyViewed() {
      const grid = document.getElementById('recently-viewed-grid');
      const section = document.getElementById('recently-viewed-section');
      if (!grid || !section) return;

      let list = [];
      try {
        list = JSON.parse(localStorage.getItem('pc_recently_viewed') || '[]');
      } catch(e) {}

      // Exclude current product if on a PDP
      const currentData = window.PetsCareProductData;
      if (currentData && currentData.id) {
        list = list.filter(id => id !== currentData.id);
      }

      if (list.length === 0) return;

      const q = list.map(id => `id:${id}`).join(' OR ');
      try {
        const url = `/search?view=recently-viewed&type=product&q=${encodeURIComponent(q)}`;
        const r = await fetch(url);
        const html = await r.text();
        if (html && html.trim().length > 10) {
          grid.innerHTML = html;
          section.classList.remove('hidden');
          // Re-trigger wishlist bindings
          if (PetsCare.wishlist && typeof PetsCare.wishlist.init === 'function') {
            PetsCare.wishlist.init();
          }
          // Re-trigger custom reviews rating badges
          if (PetsCare.reviews && typeof PetsCare.reviews.initProductCards === 'function') {
            PetsCare.reviews.initProductCards();
          }
        }
      } catch(e) { console.error('[PetsCare] renderRecentlyViewed failed', e); }
    },

    /* Variant selection — pill click → find matching variant → update price, ATC */
    _initVariants() {
      const data = window.PetsCareProductData;
      if (!data) return;

      // Initialize Buy Now redirect logic
      document.querySelectorAll('.pdp-buy-now-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          const form = btn.closest('form');
          if (form) {
            let returnInput = form.querySelector('input[name="return_to"]');
            if (!returnInput) {
              returnInput = document.createElement('input');
              returnInput.type = 'hidden';
              returnInput.name = 'return_to';
              returnInput.value = '/checkout';
              form.appendChild(returnInput);
            }
            form.submit();
          }
        });
      });

      const pillGroups = document.querySelectorAll('.variant-pills');
      const variantIdInput = document.getElementById('pdp-variant-id');
      const priceEl = document.getElementById('pdp-price');
      const compareEl = document.getElementById('pdp-compare');
      const discountEl = document.getElementById('pdp-discount');
      const atcBtn = document.getElementById('pdp-atc-btn');
      const stickyPrice = document.getElementById('pdp-sticky-price');

      // Track selected options
      const selectedOptions = {};
      document.querySelectorAll('.variant-pill.is-selected').forEach(pill => {
        selectedOptions[pill.dataset.optionPosition] = pill.dataset.value;
      });

      pillGroups.forEach(group => {
        group.querySelectorAll('.variant-pill').forEach(pill => {
          pill.addEventListener('click', () => {
            if (pill.classList.contains('is-unavailable')) return;

            // Update selected state in this group
            group.querySelectorAll('.variant-pill').forEach(p => p.classList.remove('is-selected'));
            pill.classList.add('is-selected');

            // Update selected label
            const pos = pill.dataset.optionPosition;
            selectedOptions[pos] = pill.dataset.value;
            const labelSpan = document.getElementById('selected-' + pos);
            if (labelSpan) labelSpan.textContent = pill.dataset.value;

            // Find matching variant
            const matchedVariant = data.variants.find(v => {
              return v.options.every((opt, i) => {
                const optPos = String(i + 1);
                return !selectedOptions[optPos] || selectedOptions[optPos] === opt;
              });
            });

            if (matchedVariant) {
              // Update hidden input
              if (variantIdInput) variantIdInput.value = matchedVariant.id;

              // Update price display
              if (priceEl) priceEl.textContent = PetsCare.utils.formatMoney(matchedVariant.price);
              if (stickyPrice) stickyPrice.textContent = PetsCare.utils.formatMoney(matchedVariant.price);

              const qtyInput = document.getElementById('pdp-qty');
              if (qtyInput) {
                qtyInput.dataset.price = matchedVariant.price;
              }

              // Update compare/discount
              if (matchedVariant.compare_at_price > matchedVariant.price) {
                const pct = Math.round((matchedVariant.compare_at_price - matchedVariant.price) / matchedVariant.compare_at_price * 100);
                if (compareEl) { compareEl.textContent = PetsCare.utils.formatMoney(matchedVariant.compare_at_price); compareEl.style.display = ''; }
                if (discountEl) { discountEl.textContent = `-${pct}%`; discountEl.style.display = ''; }
              } else {
                if (compareEl) compareEl.style.display = 'none';
                if (discountEl) discountEl.style.display = 'none';
              }

              // Update shipping progress bar dynamically
              const shippingBar = document.getElementById('pdp-shipping-bar');
              if (shippingBar) {
                const barText = shippingBar.querySelector('.pdp-shipping-bar__text');
                if (barText) barText.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right:4px;color:var(--green)"><polyline points="20 6 9 17 4 12"/></svg>This item qualifies for <strong>FREE shipping!</strong>`;
                const barFill = document.getElementById('pdp-shipping-bar-fill');
                if (barFill) barFill.style.display = 'none';
              }

              // Update variant image in gallery
              const mediaId = (matchedVariant.featured_media && matchedVariant.featured_media.id) || 
                              (matchedVariant.featured_image && matchedVariant.featured_image.id);
              let foundThumb = null;
              if (mediaId) {
                const targetMediaId = String(mediaId);
                foundThumb = Array.from(document.querySelectorAll('.pdp-thumb')).find(thumb => {
                  return thumb.dataset.mediaId === targetMediaId;
                });
              }

              // Fallback: Match by option value (e.g., option value matches alt text or filename)
              if (!foundThumb && matchedVariant.options) {
                const thumbs = Array.from(document.querySelectorAll('.pdp-thumb'));
                const sortedOptions = [...matchedVariant.options].sort((a, b) => b.length - a.length);
                
                for (const val of sortedOptions) {
                  if (!val || val.toLowerCase() === 'default title') continue;
                  const normalizedVal = val.trim().toLowerCase();
                  
                  foundThumb = thumbs.find(thumb => {
                    const img = thumb.querySelector('img');
                    const alt = (img?.getAttribute('alt') || '').toLowerCase();
                    const src = (thumb.dataset.src || '').toLowerCase();
                    
                    const altWords = alt.split(/[^a-z0-9]+/);
                    const srcWords = src.split(/[^a-z0-9]+/);
                    return altWords.includes(normalizedVal) || srcWords.includes(normalizedVal) || alt.includes(normalizedVal);
                  });
                  if (foundThumb) break;
                }
              }

              if (foundThumb) {
                foundThumb.click();
              }

              // Update ATC state
              if (atcBtn) {
                atcBtn.disabled = !matchedVariant.available;
                atcBtn.innerHTML = matchedVariant.available
                  ? `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 002 1.61h9.72a2 2 0 002-1.61L23 6H6"/></svg>Add to Cart`
                  : 'Sold Out';
              }

              // Update Buy Now state
              const buyNowBtns = document.querySelectorAll('.pdp-buy-now-btn');
              const currentQty = parseInt(document.getElementById('pdp-qty')?.value, 10) || 1;
              buyNowBtns.forEach(btn => {
                btn.disabled = !matchedVariant.available;
                if (matchedVariant.available) {
                  btn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="none" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> <span class="buy-now-label">Buy at ${PetsCare.utils.formatMoney(matchedVariant.price * currentQty)}</span>`;
                } else {
                  btn.innerHTML = 'Sold Out';
                }
              });

              const qtyInputEvent = document.getElementById('pdp-qty');
              if (qtyInputEvent) {
                qtyInputEvent.dispatchEvent(new Event('input'));
              }

              // Update URL without reload
              const url = new URL(window.location.href);
              url.searchParams.set('variant', matchedVariant.id);
              history.replaceState({}, '', url.toString());

              // Dispatch ViewContent Event on variant switch
              document.dispatchEvent(new CustomEvent('petsCare:viewContent', {
                detail: {
                  id: matchedVariant.id,
                  title: data.title,
                  price: matchedVariant.price / 100,
                  compare_price: matchedVariant.compare_at_price ? matchedVariant.compare_at_price / 100 : null,
                  variant_title: matchedVariant.title,
                  currency: 'USD'
                }
              }));

              // Mobile only: Scroll up to gallery view on variant change
              if (window.innerWidth <= 1023) {
                const gallery = document.querySelector('.pdp-gallery') || document.querySelector('.pdp-gallery__images');
                if (gallery) {
                  const headerOffset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-h')) || 68;
                  const elementPosition = gallery.getBoundingClientRect().top;
                  const offsetPosition = elementPosition + (window.scrollY || window.pageYOffset) - headerOffset - 15;
                  window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                  });
                }
              }
            }
          });
        });
      });
    },

    /* Quantity +/− buttons */
    _initQtyControls() {
      const qtyInput = document.getElementById('pdp-qty');
      if (!qtyInput) return;

      const subtotalEl = document.getElementById('pdp-qty-subtotal');
      const subtotalValEl = document.getElementById('pdp-qty-subtotal-val');
      const buyNowBtns = document.querySelectorAll('.pdp-buy-now-btn');

      const updatePrices = () => {
        const qty = parseInt(qtyInput.value, 10) || 1;
        const price = parseInt(qtyInput.dataset.price, 10) || 0;
        const total = price * qty;

        // 1. Update inline subtotal display
        if (qty > 1 && total > 0) {
          if (subtotalValEl) subtotalValEl.textContent = PetsCare.utils.formatMoney(total);
          if (subtotalEl) subtotalEl.style.display = 'block';
        } else {
          if (subtotalEl) subtotalEl.style.display = 'none';
        }

        // 2. Update Buy Now button label
        buyNowBtns.forEach(btn => {
          if (!btn.disabled && btn.querySelector('.buy-now-label')) {
            const labelEl = btn.querySelector('.buy-now-label');
            if (labelEl) labelEl.textContent = `Buy at ${PetsCare.utils.formatMoney(total)}`;
          }
        });
      };

      // Watch for quantity clicks
      document.querySelectorAll('[data-qty-change]').forEach(btn => {
        btn.addEventListener('click', () => {
          const delta = parseInt(btn.dataset.qtyChange, 10);
          const current = parseInt(qtyInput.value, 10) || 1;
          const next = Math.max(1, current + delta);
          qtyInput.value = next;
          // Trigger update
          updatePrices();
        });
      });

      // Watch for manual typing changes
      qtyInput.addEventListener('input', updatePrices);
      qtyInput.addEventListener('change', updatePrices);

      // Initial run on page load
      updatePrices();
    },

    /* Tab switching */
    _initTabs() {
      const tabBtns = document.querySelectorAll('.pdp-tab-btn');
      tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          // Deactivate all
          tabBtns.forEach(b => { b.classList.remove('is-active'); b.setAttribute('aria-selected', 'false'); });
          document.querySelectorAll('.pdp-tab-panel').forEach(panel => { panel.classList.remove('is-active'); panel.hidden = true; });
          // Activate clicked
          btn.classList.add('is-active');
          btn.setAttribute('aria-selected', 'true');
          const target = document.getElementById(btn.dataset.tab);
          if (target) { target.classList.add('is-active'); target.hidden = false; }
        });
      });
    },

    /* Sticky ATC bar — shows when main ATC scrolls out of viewport */
    _initStickyAtc() {
      const mainAtc = document.getElementById('pdp-atc-btn-desktop') || document.getElementById('pdp-atc-btn');
      const stickyBar = document.getElementById('pdp-sticky-atc');
      if (!mainAtc || !stickyBar) return;

      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          stickyBar.classList.toggle('is-visible', !entry.isIntersecting);
          stickyBar.setAttribute('aria-hidden', String(entry.isIntersecting));
        });
      }, { threshold: 0, rootMargin: '-80px 0px 0px 0px' });
      observer.observe(mainAtc);
    },

    /* Frequently Bought Together — checkbox total calculation + bundle add */
    _initFbt() {
      const form = document.getElementById('fbt-form');
      const totalEl = document.getElementById('fbt-total');
      if (!form || !totalEl) return;

      const updateTotal = () => {
        let total = 0;
        form.querySelectorAll('.fbt-item__check').forEach(cb => {
          if (cb.checked) total += parseInt(cb.dataset.price, 10) || 0;
        });
        totalEl.textContent = PetsCare.utils.formatMoney(total);
      };

      form.querySelectorAll('.fbt-item__check:not(:disabled)').forEach(cb => {
        cb.addEventListener('change', updateTotal);
      });
      updateTotal();

      form.addEventListener('submit', async e => {
        e.preventDefault();
        const items = [];
        form.querySelectorAll('.fbt-item__check:checked').forEach(cb => {
          if (cb.dataset.variantId) {
            items.push({ id: parseInt(cb.dataset.variantId, 10), quantity: 1 });
          }
        });
        if (items.length) await PetsCare.cart.add(items, true);
      });
    },

    /* AJAX Interception for the main Product Form */
    _initProductFormSubmit() {
      const forms = document.querySelectorAll('form[action*="/cart/add"]');
      forms.forEach(form => {
        if (form.id === 'fbt-form') return; // Handled by FBT listener

        form.addEventListener('submit', async e => {
          // If native submit triggered by Buy Now, do not prevent default
          if (e.submitter && e.submitter.classList.contains('pdp-buy-now-btn')) {
            return;
          }
          
          e.preventDefault();

          const variantInput = form.querySelector('[name="id"]');
          const qtyInput = form.querySelector('[name="quantity"]');
          if (!variantInput) return;

          const variantId = parseInt(variantInput.value, 10);
          const quantity = qtyInput ? parseInt(qtyInput.value, 10) || 1 : 1;

          if (variantId) {
            const items = [{ id: variantId, quantity: quantity }];
            // Add to cart and display toast WITHOUT opening the cart drawer
            await PetsCare.cart.add(items, false);
          }
        });
      });
    }
  },

  /* ─── UTILITIES ─────────────────────────────────────────────────────────── */
  utils: {
    formatMoney(cents) {
      return '$' + (cents / 100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },

    getDeliveryEstimateString() {
      const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      const addBusinessDays = (date, daysToAdd) => {
        let cnt = 0;
        let tmpDate = new Date(date.getTime());
        while (cnt < daysToAdd) {
          tmpDate.setDate(tmpDate.getDate() + 1);
          if (tmpDate.getDay() !== 0) cnt++;
        }
        return tmpDate;
      };
      const start = addBusinessDays(new Date(), 3);
      const end = addBusinessDays(new Date(), 5);
      return `Arrives: ${days[start.getDay()]}, ${months[start.getMonth()]} ${start.getDate()} – ${days[end.getDay()]}, ${months[end.getMonth()]} ${end.getDate()}`;
    },

    showToast(msg, isError = false) {
      const toast = document.getElementById('cart-toast');
      const msgEl = document.getElementById('cart-toast-msg');
      if (!toast || !msgEl) return;
      msgEl.textContent = msg;
      toast.style.background = isError ? '#DC2626' : '';
      toast.classList.add('is-visible');
      setTimeout(() => toast.classList.remove('is-visible'), 3000);
    },

    centerActiveScrollItem(container, activeItem, behavior = 'auto') {
      if (!container || !activeItem) return;
      const containerWidth = container.clientWidth;
      const activeWidth = activeItem.offsetWidth;
      const activeLeft = activeItem.offsetLeft;
      
      // Calculate scroll target to center activeItem in viewport
      const scrollTarget = activeLeft - (containerWidth / 2) + (activeWidth / 2);
      
      if (behavior === 'smooth') {
        container.scrollTo({ left: scrollTarget, behavior: 'smooth' });
      } else {
        container.scrollLeft = scrollTarget;
      }
    }
  },

  /* ─── SCROLL MENU CENTERING ─────────────────────────────────────────────── */
  initScrollMenuCentering() {
    const runCentering = () => {
      // 1. Header main navigation
      const headerNav = document.querySelector('.header-nav');
      if (headerNav) {
        const activeLink = headerNav.querySelector('.header-nav__link.is-active');
        if (activeLink) {
          this.utils.centerActiveScrollItem(headerNav, activeLink, 'auto');
        }
      }
      
      // 2. Tabbed product carousel (homepage)
      document.querySelectorAll('.tab-buttons').forEach(container => {
        const activeTab = container.querySelector('.tab-btn.active');
        if (activeTab) {
          this.utils.centerActiveScrollItem(container, activeTab, 'auto');
        }
      });

      // 3. PDP tabs nav
      document.querySelectorAll('.pdp-tabs__nav').forEach(container => {
        const activeTab = container.querySelector('.pdp-tab-btn.is-active');
        if (activeTab) {
          this.utils.centerActiveScrollItem(container, activeTab, 'auto');
        }
      });

      // 4. PDP variant pills
      document.querySelectorAll('.variant-pills').forEach(container => {
        const activePill = container.querySelector('.variant-pill.is-selected');
        if (activePill) {
          this.utils.centerActiveScrollItem(container, activePill, 'auto');
        }
      });
    };

    // Run centering immediately and on window loads/resizes
    runCentering();
    window.addEventListener('load', runCentering);
    window.addEventListener('resize', runCentering);
    setTimeout(runCentering, 100);
    setTimeout(runCentering, 300);
    setTimeout(runCentering, 600);

    // Dynamic centering on click/interaction (smooth scroll)
    document.addEventListener('click', e => {
      // Tabbed carousel tabs
      const tabBtn = e.target.closest('.tab-btn');
      if (tabBtn) {
        const container = tabBtn.closest('.tab-buttons');
        if (container) {
          setTimeout(() => this.utils.centerActiveScrollItem(container, tabBtn, 'smooth'), 50);
        }
      }
      
      // PDP tabs
      const pdpTabBtn = e.target.closest('.pdp-tab-btn');
      if (pdpTabBtn) {
        const container = pdpTabBtn.closest('.pdp-tabs__nav');
        if (container) {
          setTimeout(() => this.utils.centerActiveScrollItem(container, pdpTabBtn, 'smooth'), 50);
        }
      }

      // PDP variant pills
      const pill = e.target.closest('.variant-pill');
      if (pill) {
        const container = pill.closest('.variant-pills');
        if (container) {
          setTimeout(() => this.utils.centerActiveScrollItem(container, pill, 'smooth'), 50);
        }
      }
    });
  },

  /* ─── CUSTOM REVIEWS ENGINE ─────────────────────────────────────────────── */
  reviews: {
    NAMES: [
      "Sarah Mitchell", "David Kowalski", "Jennifer Larson", "Robert Patterson", "Amanda Simmons",
      "Michael Barnes", "Jessica Torres", "John Davidson", "Emily Walters", "Ashley Hughes",
      "James Parker", "Megan Fields", "Brian Garrett", "Rachel Vasquez", "Matthew Norton",
      "Laura Lambert", "Daniel Shaw", "Nicole Dixon", "Christopher Bradley", "Heather Arnold",
      "Andrew Tucker", "Elizabeth Moore", "William Rivera", "Melissa Jenkins", "Kevin Campbell",
      "Stephanie Ortega", "Thomas Fletcher", "Rebecca Kline", "Justin Palmer", "Samantha Ellis",
      "Ryan Long", "Courtney Murray", "Jeffrey Drake", "Amber Wells", "Nicholas Greene",
      "Danielle Ross", "Timothy Hayes", "Tiffany Stevens", "Jonathan Collins", "Michelle Boyd",
      "Gary Mason", "Linda Ford", "Karen Evans", "Patricia Turner", "Barbara James",
      "Susan Lawson", "Sandra Reed", "Christine Wheeler", "Scott Graham", "Kimberly Warren",
      "Mark Spencer", "Dorothy Peterson", "Joseph Chapman", "Nancy Hudson", "George Carpenter",
      "Carol Reyes", "Kenneth Cooper", "Helen Bennett", "Frank Morris", "Sharon Young",
      "Ronald Rivera", "Maria Brooks", "Edward Price", "Dorothy Bell", "Brian Sanders",
      "Angela Griffin", "Joshua Perry", "Diane Foster", "Larry Powell", "Janet Butler",
      "Raymond Barnes", "Deborah Richardson", "Jerry Ward", "Virginia Cox", "Harold Jenkins",
      "Carolyn Bailey", "Philip Wood", "Kathleen Torres", "Russell Alexander", "Anna Scott"
    ],

    TITLES_5: [
      "Absolutely love this!", "My dog is obsessed!", "Best purchase this year", "Highly recommend to every pet owner",
      "Exceeded all expectations", "5 stars, no question", "Will buy again and again",
      "My cat won't leave it alone!", "Perfect from day one", "So worth the price",
      "Better than I expected", "My fur baby approves", "Amazing quality for the price",
      "Shipped fast, works great", "Outstanding product", "Couldn't be happier!"
    ],

    TEXTS_5: [
      "My pup absolutely adores this. The quality is exceptional and it's already held up to weeks of heavy play. Shipping was surprisingly fast too — arrived two days ahead of schedule. This will definitely be a repeat purchase for us.",
      "I bought this on a whim and I'm so glad I did. My cat was hesitant at first, like she always is with new things, but within 20 minutes she was completely hooked. The build quality is solid and it feels very premium.",
      "We've tried so many similar products and nothing came close to this. The material is thick, well-made, and everything about it feels intentional. My golden retriever has been using it daily for a month and it still looks brand new.",
      "Honestly shocked by how good this is. I was expecting something decent for the price but this is genuinely high quality. Fast delivery, great packaging, and my dogs are both obsessed. Ordered a second one the same week.",
      "My vet actually recommended I look for something like this and I'm really glad I found it here. The quality is exactly what she described — safe materials, well-constructed, and easy to clean. My senior lab loves it.",
      "Very impressed with everything about this. The product arrived exactly as shown, looked premium straight out of the box, and works perfectly. My husky has very high standards and this passed her inspection immediately.",
      "Wow. This is exactly what I've been looking for. My picky cat usually rejects anything new within a day, but she's been using this every single day since it arrived. Great quality and worth every penny.",
      "Fast shipping, premium packaging, and the product itself is just fantastic. Everything about this purchase felt trustworthy and professional. My beagle went crazy for it. Already bought one for my sister's dog too.",
      "I've been buying pet products online for years and this is genuinely one of the best purchases I've ever made. My dogs fight over it! Sturdy, safe, and they clearly love it. Highly, highly recommend.",
      "Outstanding. The quality is leagues above anything I've found at my local pet store. My rescue pup — who is usually super anxious with new things — took to it immediately, which tells me it's something special.",
      "Ordered this after reading reviews and it absolutely lived up to the hype. My two cats share it now, which is a miracle because they never agree on anything. The materials feel durable and the colors are true to the photos.",
      "This is exactly what every pet owner needs. Simple, effective, and incredibly well made. I've had mine for 6 weeks now and it shows zero signs of wear. Five stars without any hesitation.",
      "My rescue dog is extremely particular — she's rejected every toy and accessory I've tried except this. She's been using it every single day. I'm blown away by the quality for this price point. Absolutely a must-have.",
      "Quick delivery, solid packaging, and the product is seriously impressive. My tabby cat claimed it within minutes. The craftsmanship is noticeably higher quality than the cheaper options I've tried before.",
      "Couldn't be happier. I was a little skeptical ordering from a new store but the experience was flawless — updates along the way, arrived perfectly packed, and my dog approved immediately. 10/10 would recommend.",
      "This product is everything the listing promises and then some. Great for my older dog who needed something gentle but durable. The quality is obvious from the moment you take it out of the box.",
    ],

    TITLES_4: [
      "Really good overall", "Happy with this purchase", "Solid and dependable", "Good quality, minor niggles",
      "Works well for my pets", "Decent value for money", "Would recommend to others",
      "Pretty happy with it", "Good buy", "Not perfect but close"
    ],

    TEXTS_4: [
      "Overall a very solid product. My dog took to it well and the quality is noticeably better than the cheaper alternatives. Shipping took about 5 days which was fine. I'd buy this again without much hesitation.",
      "Good product, happy with the purchase. It took my cat a couple of days to warm up to it but now she uses it regularly. The build quality is solid — no complaints on that front. Would be 5 stars if shipping were faster.",
      "Really pleased with this. The quality is good and it does exactly what I needed it to. Minor thing — the packaging could be a bit sturdier — but the product itself is great and my pets both love it.",
      "Works well for what it is. My labrador has been using it every day and it's holding up nicely. Good value for the price. I'd recommend it to other dog owners, especially those looking for something reliable.",
      "Solid purchase. My cat was curious about it from day one and has been using it consistently. The materials feel durable. I gave it 4 stars rather than 5 only because the sizing ran slightly different than expected, but it still works great.",
      "Pretty happy with this overall. Good quality materials, arrived quickly, and my pets enjoy using it. It's not quite as flashy as some photos suggested, but it works exactly as described and does the job well.",
      "A good buy. My two dogs seem to enjoy it and the quality is decent for the price. I've had cheaper versions of similar products and this is definitely a step up. Would recommend to anyone looking for something reliable.",
      "Happy with the purchase. My rescue dog was initially nervous around it but warmed up after about a week. Now she seeks it out on her own, which is a great sign. The product feels well-made and sturdy.",
    ],

    TITLES_3: [
      "It's okay for the price", "Decent, but expected more", "Average — not bad, not great",
      "Fine but has a few issues", "Works, just not perfect"
    ],

    TEXTS_3: [
      "It's okay. The quality is decent but I was expecting something a bit more premium based on the product photos. My dog uses it occasionally but doesn't seem particularly excited by it. Might try a different option next time.",
      "Average product overall. It does what it's supposed to do, but the build quality feels a little flimsy in parts. My cat has been using it but she doesn't seem especially impressed. For the price, it's passable.",
      "Arrived on time and is functional, but it didn't really wow me or my pet. The material is fine — nothing special. My dog showed interest for the first day or two but has since moved on to other things. It's fine.",
    ],

    init() {
      // 1. Initialize ratings on any product cards in collection page
      this.initProductCards();

      // 2. Initialize product page widgets
      const widget = document.getElementById('pdp-custom-reviews');
      if (widget) {
        this.initPDPWidget(widget);
      }

      // 3. Compute global review aggregate and inject into hero eyebrow
      this.updateHeroSocialProof();
    },

    updateHeroSocialProof() {
      const eyebrow = document.querySelector('.hero__eyebrow');
      if (!eyebrow) return;

      // Sum up reviews from all product card badges visible on this page
      const badges = document.querySelectorAll('.card-custom-rating-badge[data-product-id]');
      let totalReviewCount = 0;
      let totalWeightedRating = 0;
      const seen = new Set();

      badges.forEach(badge => {
        const pid = badge.dataset.productId;
        if (!pid || seen.has(pid)) return;
        seen.add(pid);
        const data = this.getReviewsData(pid);
        totalReviewCount += data.totalReviews;
        totalWeightedRating += data.averageRating * data.totalReviews;
      });

      // If no cards on page (e.g. homepage without product sections loaded yet),
      // fall back to a believable aggregated number derived from a fixed seed
      if (totalReviewCount < 100) {
        // Simulate a store-level aggregate: ~8,400 reviews across all products
        totalReviewCount = 8427;
        totalWeightedRating = 8427 * 4.6;
      }

      const globalAvg = totalReviewCount > 0 ? (totalWeightedRating / totalReviewCount).toFixed(1) : "4.6";
      const reviewCountDisplay = totalReviewCount >= 1000
        ? `${(totalReviewCount / 1000).toFixed(1)}k`
        : `${totalReviewCount}`;

      eyebrow.innerHTML = `
        <span class="hero-eyebrow__stars">★★★★★</span>
        <span class="hero-eyebrow__avg">${globalAvg}</span>
        <span class="hero-eyebrow__text">· Loved by ${reviewCountDisplay}+ pet parents</span>
      `;
      eyebrow.classList.add('hero__eyebrow--social-proof');
    },

    getReviewsData(productId) {
      const idStr = String(productId);
      let hash = 0;
      for (let i = 0; i < idStr.length; i++) {
        hash = idStr.charCodeAt(i) + ((hash << 5) - hash);
      }
      const seed = Math.abs(hash);
      
      const seedRandom = (s) => {
        const x = Math.sin(s) * 10000;
        return x - Math.floor(x);
      };

      // Determine star rating target
      // 70% of products: 4.7 stars
      // 15% of products: 4.5 stars
      // 15% of products: 4.0 stars
      const targetPercent = seed % 100;
      let targetRating = 4.7;
      if (targetPercent >= 70 && targetPercent < 85) {
        targetRating = 4.5;
      } else if (targetPercent >= 85) {
        targetRating = 4.0;
      }

      // Determine review count: between 10 and 500 reviews
      const countRand = seedRandom(seed);
      const totalReviews = Math.floor(10 + Math.pow(countRand, 2) * 490);

      // Generate seed reviews
      const reviews = [];
      let totalStars = 0;

      for (let i = 0; i < totalReviews; i++) {
        const itemSeed = seed + i * 17;
        const rand = seedRandom(itemSeed);
        
        let rating = 5;
        if (targetRating === 4.7) {
          if (rand < 0.76) rating = 5;
          else if (rand < 0.94) rating = 4;
          else if (rand < 0.98) rating = 3;
          else if (rand < 0.99) rating = 2;
          else rating = 1;
        } else if (targetRating === 4.5) {
          if (rand < 0.62) rating = 5;
          else if (rand < 0.88) rating = 4;
          else if (rand < 0.96) rating = 3;
          else if (rand < 0.99) rating = 2;
          else rating = 1;
        } else { // 4.0 target
          if (rand < 0.40) rating = 5;
          else if (rand < 0.75) rating = 4;
          else if (rand < 0.90) rating = 3;
          else if (rand < 0.97) rating = 2;
          else rating = 1;
        }

        totalStars += rating;

        // Date between 3 months ago (90 days) and today
        const daysAgo = Math.floor(seedRandom(itemSeed + 5) * 90);
        const date = new Date();
        date.setDate(date.getDate() - daysAgo);

        // Reviewer Name
        const nameIdx = Math.floor(seedRandom(itemSeed + 3) * this.NAMES.length);
        const name = this.NAMES[nameIdx];

        // Title and Text based on Rating
        let title = "";
        let text = "";
        if (rating === 5) {
          title = this.TITLES_5[Math.floor(seedRandom(itemSeed + 7) * this.TITLES_5.length)];
          text = this.TEXTS_5[Math.floor(seedRandom(itemSeed + 9) * this.TEXTS_5.length)];
        } else if (rating === 4) {
          title = this.TITLES_4[Math.floor(seedRandom(itemSeed + 7) * this.TITLES_4.length)];
          text = this.TEXTS_4[Math.floor(seedRandom(itemSeed + 9) * this.TEXTS_4.length)];
        } else {
          title = this.TITLES_3[Math.floor(seedRandom(itemSeed + 7) * this.TITLES_3.length)];
          text = this.TEXTS_3[Math.floor(seedRandom(itemSeed + 9) * this.TEXTS_3.length)];
        }

        reviews.push({
          name: name,
          rating: rating,
          title: title,
          text: text,
          date: date.getTime()
        });
      }

      // Merge user reviews from localStorage
      const storageKey = `pdp-user-reviews-${productId}`;
      const localReviewsStr = localStorage.getItem(storageKey);
      if (localReviewsStr) {
        try {
          const localReviews = JSON.parse(localReviewsStr);
          localReviews.forEach(r => {
            reviews.unshift(r); // Add user reviews to the start of the list
            totalStars += r.rating;
          });
        } catch(e) { console.error("Failed to parse local reviews", e); }
      }

      // Sort reviews by date descending
      reviews.sort((a, b) => b.date - a.date);

      const averageRating = reviews.length > 0 ? (totalStars / reviews.length).toFixed(1) : "0.0";

      return {
        reviews: reviews,
        averageRating: parseFloat(averageRating),
        totalReviews: reviews.length
      };
    },

    initProductCards() {
      document.querySelectorAll('.card-custom-rating-badge').forEach(badge => {
        const productId = badge.dataset.productId;
        if (!productId) return;

        const data = this.getReviewsData(productId);
        
        const starsEl = badge.querySelector('.product-card__stars');
        if (starsEl) {
          starsEl.innerHTML = this.renderStarsHtml(data.averageRating);
        }
        
        const scoreEl = badge.querySelector('span:not(.product-card__stars)');
        if (scoreEl) {
          scoreEl.textContent = `${data.averageRating} (${data.totalReviews})`;
        }
        
        badge.style.display = 'flex'; // show badge
      });
    },

    initPDPWidget(widget) {
      const productId = widget.dataset.productId;
      if (!productId) return;

      const data = this.getReviewsData(productId);

      const pdpBadge = document.getElementById('pdp-custom-rating-badge');
      if (pdpBadge) {
        const starsEl = document.getElementById('pdp-stars-badge');
        const scoreEl = document.getElementById('pdp-rating-score-badge');
        const countEl = document.getElementById('pdp-review-count-badge');
        
        if (starsEl) starsEl.innerHTML = this.renderStarsHtml(data.averageRating);
        if (scoreEl) scoreEl.textContent = data.averageRating;
        if (countEl) countEl.textContent = `(${data.totalReviews} reviews)`;

        pdpBadge.style.display = 'flex';

        // Add smooth scroll click to reviews tab
        pdpBadge.addEventListener('click', e => {
          e.preventDefault();
          const tabBtn = document.getElementById('tab-btn-reviews');
          if (tabBtn) {
            tabBtn.click();
            tabBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        });
      }

      // Populate the trust badge in the PDP header (above star rating)
      const headerTrustBadge = document.getElementById('pdp-trust-badge');
      if (headerTrustBadge) {
        const avgR = data.averageRating;
        let badgeClass, badgeLabel;
        if (avgR >= 4.8) {
          badgeClass = 'reviews-trust-badge--top';
          badgeLabel = 'TOP RATED';
        } else if (avgR >= 4.5) {
          badgeClass = 'reviews-trust-badge--high';
          badgeLabel = 'HIGHLY RATED';
        } else {
          badgeClass = 'reviews-trust-badge--trusted';
          badgeLabel = 'TRUSTED';
        }
        headerTrustBadge.innerHTML = `
          <span class="reviews-trust-badge reviews-trust-badge--header ${badgeClass}">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
            ${badgeLabel}
          </span>`;
        headerTrustBadge.style.display = 'block';
      }

      this.renderWidgetHtml(widget, data, productId);
    },

    renderStarsHtml(rating) {
      const fullStars = Math.floor(rating);
      const halfStar = rating % 1 >= 0.4 && rating % 1 <= 0.8 ? 1 : 0;
      const emptyStars = 5 - fullStars - halfStar;
      
      let html = "";
      for (let i = 0; i < fullStars; i++) html += "★";
      if (halfStar) html += "☆";
      for (let i = 0; i < emptyStars; i++) html += "☆";
      return html;
    },

    renderWidgetHtml(widget, data, productId) {
      const counts = { 5: 0, 4: 0, 3: 0, 2: 0, 1: 0 };
      data.reviews.forEach(r => {
        if (counts[r.rating] !== undefined) counts[r.rating]++;
      });

      const pct = (stars) => {
        if (data.totalReviews === 0) return 0;
        return Math.round((counts[stars] / data.totalReviews) * 100);
      };

      const productTitle = widget.dataset.productTitle || "";

      let html = `
        <div class="reviews-dashboard">
          <div class="reviews-summary">
            <div class="reviews-summary__score-box">
              <div class="reviews-summary__score">${data.averageRating}</div>
              <div class="reviews-summary__stars">${this.renderStarsHtml(data.averageRating)}</div>
              <div class="reviews-summary__count">Based on ${data.totalReviews} reviews</div>
            </div>
            
            <div class="reviews-summary__distribution">
              ${[5, 4, 3, 2, 1].map(stars => `
                <div class="distribution-row">
                  <span class="distribution-row__label">${stars} ★</span>
                  <div class="distribution-row__bar-bg">
                    <div class="distribution-row__bar-fill" style="width: ${pct(stars)}%"></div>
                  </div>
                  <span class="distribution-row__pct">${pct(stars)}%</span>
                </div>
              `).join('')}
            </div>
            
            <div class="reviews-summary__action">
              <button type="button" class="btn btn--primary" id="btn-write-review">Write a Review</button>
            </div>
          </div>

          <!-- Write Review Form Container -->
          <div class="review-form-container" id="review-form-container" style="display:none;">
            <form id="custom-review-form" class="review-form">
              <h3 class="review-form__title">Write a review for ${productTitle}</h3>
              
              <div class="review-form__row">
                <label for="review-author" class="review-form__label">Your Name <span class="required">*</span></label>
                <input type="text" id="review-author" class="review-form__input" placeholder="Enter your name" required>
              </div>

              <div class="review-form__row">
                <label class="review-form__label">Rating <span class="required">*</span></label>
                <div class="star-rating-select" id="star-rating-select" role="radiogroup" aria-label="Rating selection">
                  <button type="button" class="star-select-btn" data-rating="1" aria-label="1 star">★</button>
                  <button type="button" class="star-select-btn" data-rating="2" aria-label="2 stars">★</button>
                  <button type="button" class="star-select-btn" data-rating="3" aria-label="3 stars">★</button>
                  <button type="button" class="star-select-btn" data-rating="4" aria-label="4 stars">★</button>
                  <button type="button" class="star-select-btn" data-rating="5" aria-label="5 stars">★</button>
                </div>
                <input type="hidden" id="review-rating-value" value="5" required>
              </div>

              <div class="review-form__row">
                <label for="review-title" class="review-form__label">Review Title <span class="required">*</span></label>
                <input type="text" id="review-title" class="review-form__input" placeholder="e.g. Highly recommend!" required>
              </div>

              <div class="review-form__row">
                <label for="review-body" class="review-form__label">Review Description <span class="required">*</span></label>
                <textarea id="review-body" class="review-form__textarea" rows="4" placeholder="Share your experience with this product..." required></textarea>
              </div>

              <div class="review-form__buttons">
                <button type="button" class="btn btn--secondary" id="btn-cancel-review">Cancel</button>
                <button type="submit" class="btn btn--primary">Submit Review</button>
              </div>
            </form>
          </div>

          <!-- Reviews List -->
          <div class="reviews-list" id="reviews-list-container"></div>
        </div>
      `;

      widget.innerHTML = html;

      const writeBtn = widget.querySelector('#btn-write-review');
      const cancelBtn = widget.querySelector('#btn-cancel-review');
      const formContainer = widget.querySelector('#review-form-container');
      const form = widget.querySelector('#custom-review-form');
      const starSelectBtns = widget.querySelectorAll('.star-select-btn');
      const ratingValueInput = widget.querySelector('#review-rating-value');

      if (writeBtn && formContainer) {
        writeBtn.addEventListener('click', () => {
          formContainer.style.display = formContainer.style.display === 'none' ? 'block' : 'none';
          if (formContainer.style.display === 'block') {
            formContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
        });
      }

      if (cancelBtn && formContainer) {
        cancelBtn.addEventListener('click', () => {
          formContainer.style.display = 'none';
          form.reset();
          this.updateStarRatingSelect(starSelectBtns, 5);
        });
      }

      starSelectBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const rating = parseInt(btn.dataset.rating, 10);
          ratingValueInput.value = rating;
          this.updateStarRatingSelect(starSelectBtns, rating);
        });
      });

      this.updateStarRatingSelect(starSelectBtns, 5);

      if (form) {
        form.addEventListener('submit', e => {
          e.preventDefault();
          
          const name = form.querySelector('#review-author').value.trim();
          const rating = parseInt(ratingValueInput.value, 10);
          const title = form.querySelector('#review-title').value.trim();
          const text = form.querySelector('#review-body').value.trim();
          
          if (!name || !rating || !title || !text) {
            alert("All fields marked with * are compulsory.");
            return;
          }

          const newReview = {
            name: name,
            rating: rating,
            title: title,
            text: text,
            date: Date.now()
          };

          const storageKey = `pdp-user-reviews-${productId}`;
          const existing = localStorage.getItem(storageKey);
          let userReviews = [];
          if (existing) {
            try { userReviews = JSON.parse(existing); } catch(err) {}
          }
          userReviews.unshift(newReview);
          localStorage.setItem(storageKey, JSON.stringify(userReviews));

          PetsCare.utils.showToast("Review submitted successfully!");

          formContainer.style.display = 'none';
          form.reset();
          this.updateStarRatingSelect(starSelectBtns, 5);

          this.initPDPWidget(widget);
        });
      }

      this.renderReviewsPage(widget, data.reviews, 1);
    },

    updateStarRatingSelect(btns, rating) {
      btns.forEach(btn => {
        const btnRating = parseInt(btn.dataset.rating, 10);
        if (btnRating <= rating) {
          btn.classList.add('selected');
        } else {
          btn.classList.remove('selected');
        }
      });
    },

    renderReviewsPage(widget, reviews, pageNumber) {
      const listContainer = widget.querySelector('#reviews-list-container');
      if (!listContainer) return;

      const pageSize = 8;
      const totalPages = Math.ceil(reviews.length / pageSize);
      const startIndex = (pageNumber - 1) * pageSize;
      const endIndex = Math.min(startIndex + pageSize, reviews.length);
      const pageReviews = reviews.slice(startIndex, endIndex);

      const formatDate = (timestamp) => {
        const date = new Date(timestamp);
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return date.toLocaleDateString('en-US', options);
      };

      let html = "";
      if (reviews.length === 0) {
        html = `<p class="reviews-empty">No reviews yet. Be the first to write a review!</p>`;
      } else {
        html = `
          <div class="reviews-list__items">
            ${pageReviews.map(r => `
              <div class="review-item">
                <div class="review-item__head">
                  <div class="review-item__meta">
                    <span class="review-item__stars">${this.renderStarsHtml(r.rating)}</span>
                    <span class="review-item__author">${r.name}</span>
                    <span class="review-item__verified"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-right:2px;color:var(--green)"><polyline points="20 6 9 17 4 12"/></svg>Verified Buyer</span>
                  </div>
                  <span class="review-item__date">${formatDate(r.date)}</span>
                </div>
                <h4 class="review-item__title">${r.title}</h4>
                <p class="review-item__text">${r.text}</p>
              </div>
            `).join('')}
          </div>

          ${(() => {
            if (totalPages <= 1) return '';
            
            let startPage = Math.max(1, pageNumber - 1);
            let endPage = Math.min(totalPages, startPage + 2);
            startPage = Math.max(1, endPage - 2);

            const buttons = [];
            
            // Previous button
            if (pageNumber > 1) {
              buttons.push(`
                <button type="button" class="reviews-pagination__page-btn reviews-pagination__page-btn--prev" data-page="${pageNumber - 1}">
                  Previous
                </button>
              `);
            }
            
            // Page buttons
            for (let p = startPage; p <= endPage; p++) {
              buttons.push(`
                <button type="button" class="reviews-pagination__page-btn ${p === pageNumber ? 'active' : ''}" data-page="${p}">
                  ${p}
                </button>
              `);
            }
            
            // Next button
            if (pageNumber < totalPages) {
              buttons.push(`
                <button type="button" class="reviews-pagination__page-btn reviews-pagination__page-btn--next" data-page="${pageNumber + 1}">
                  Next
                </button>
              `);
            }
            
            return `
              <div class="reviews-pagination">
                ${buttons.join('')}
              </div>
            `;
          })()}
        `;
      }

      listContainer.innerHTML = html;

      listContainer.querySelectorAll('.reviews-pagination__page-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const p = parseInt(btn.dataset.page, 10);
          this.renderReviewsPage(widget, reviews, p);
          widget.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });
      });
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

    // Render recently viewed grid on any page if container is active
    if (document.getElementById('recently-viewed-section')) {
      this.pdp._renderRecentlyViewed();
    }

    // PDP only
    if (document.querySelector('.pdp-layout')) this.pdp.init();

    // Initialize scroll menu centering
    this.initScrollMenuCentering();

    // Initialize custom reviews engine
    this.reviews.init();
  }
};

document.addEventListener('DOMContentLoaded', () => PetsCare.init());
