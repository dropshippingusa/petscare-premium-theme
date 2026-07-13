/* Enterprise Shopify Theme Operations */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Hamburger Menu
  const hamburger = document.getElementById('hamburger');
  const mainNav = document.getElementById('main-nav');
  if (hamburger && mainNav) {
    hamburger.addEventListener('click', () => {
      mainNav.classList.toggle('open');
    });
  }

  // Cart Drawer open/close triggers
  const cartTriggers = [
    document.getElementById('cart-icon-trigger'),
    document.getElementById('mobile-cart-trigger')
  ];
  const cartDrawer = document.getElementById('cart-drawer');
  const cartClose = document.getElementById('cart-drawer-close');
  const cartOverlay = document.getElementById('cart-drawer-overlay');
  
  cartTriggers.forEach(btn => {
    if (btn) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openCartDrawer();
      });
    }
  });

  if (cartClose) cartClose.addEventListener('click', closeCartDrawer);
  if (cartOverlay) cartOverlay.addEventListener('click', closeCartDrawer);

  // Predictive Autocomplete Search Input Handler
  const searchInput = document.getElementById('search-input');
  const searchResultsBox = document.getElementById('predictive-search-box');

  if (searchInput && searchResultsBox) {
    searchInput.addEventListener('input', debounce((e) => {
      const query = e.target.value.trim();
      if (query.length < 2) {
        searchResultsBox.classList.remove('active');
        return;
      }
      
      searchResultsBox.innerHTML = '<div class="predictive-search-loading">Searching suggestions...</div>';
      searchResultsBox.classList.add('active');

      fetch(`/search/suggest.json?q=${encodeURIComponent(query)}&resources[type]=product,collection&resources[limit]=5`)
      .then(response => response.json())
      .then(suggestions => {
        const products = suggestions.resources.results.products || [];
        const collections = suggestions.resources.results.collections || [];

        if (products.length === 0 && collections.length === 0) {
          searchResultsBox.innerHTML = '<div class="predictive-search-loading">No results found</div>';
          return;
        }

        let html = '';
        
        // Show matching collections/categories
        if (collections.length > 0) {
          html += '<div style="padding:8px 16px; font-size:0.75rem; font-weight:700; text-transform:uppercase; color:#878787; border-bottom:1px solid #f1f5f9;">Collections</div>';
          collections.forEach(col => {
            html += `
              <a href="${col.url}" class="predictive-search-item">
                <span style="font-size:1.1rem; margin-right:8px;">📁</span>
                <div><h4>${col.title}</h4></div>
              </a>
            `;
          });
        }

        // Show matching products
        if (products.length > 0) {
          html += '<div style="padding:8px 16px; font-size:0.75rem; font-weight:700; text-transform:uppercase; color:#878787; border-bottom:1px solid #f1f5f9;">Products</div>';
          products.forEach(prod => {
            html += `
              <a href="${prod.url}" class="predictive-search-item">
                <img src="${prod.image}" alt="${prod.title}">
                <div style="flex:1;">
                  <h4>${prod.title}</h4>
                  <p>$${(prod.price / 100.0).toFixed(2)}</p>
                </div>
              </a>
            `;
          });
        }

        searchResultsBox.innerHTML = html;
      })
      .catch(err => {
        console.error('Predictive Search error:', err);
      });
    }, 300));

    // Hide search panel when clicking outside
    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !searchResultsBox.contains(e.target)) {
        searchResultsBox.classList.remove('active');
      }
    });
  }
});

function openCartDrawer() {
  const drawer = document.getElementById('cart-drawer');
  const overlay = document.getElementById('cart-drawer-overlay');
  if (drawer && overlay) {
    drawer.classList.add('open');
    overlay.classList.add('open');
    fetchCartData();
  }
}

function closeCartDrawer() {
  const drawer = document.getElementById('cart-drawer');
  const overlay = document.getElementById('cart-drawer-overlay');
  if (drawer && overlay) {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
  }
}

// Debounce helper
function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

// AJAX Add to Cart Form
function ajaxAddToCartForm(form) {
  const formData = new FormData(form);
  
  fetch('/cart/add.js', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    const toast = document.getElementById('cart-toast');
    if (toast) {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3000);
    }
    openCartDrawer();
  })
  .catch(error => {
    console.error('Error adding item to cart:', error);
  });
}

// Fetch Cart Calculations
function fetchCartData() {
  fetch('/cart.js')
  .then(response => response.json())
  .then(cart => {
    document.getElementById('header-cart-count').textContent = cart.item_count;
    const bottomCount = document.getElementById('bottom-cart-count');
    if (bottomCount) bottomCount.textContent = cart.item_count;
    document.getElementById('drawer-cart-count').textContent = cart.item_count;
    
    const subtotalFormatted = Shopify.formatMoney(cart.total_price, "${{amount}}");
    document.getElementById('drawer-cart-subtotal').textContent = subtotalFormatted;

    const threshold = 6000;
    const progressText = document.getElementById('shipping-progress-text');
    const progressBar = document.getElementById('shipping-progress-bar');
    
    if (progressText && progressBar) {
      if (cart.total_price >= threshold) {
        progressText.textContent = "🎉 You've unlocked FREE shipping!";
        progressBar.style.width = "100%";
      } else {
        const remaining = threshold - cart.total_price;
        const remainingFormatted = Shopify.formatMoney(remaining, "${{amount}}");
        progressText.textContent = `Spend ${remainingFormatted} more for FREE shipping!`;
        const percentage = (cart.total_price / threshold) * 100;
        progressBar.style.width = `${percentage}%`;
      }
    }

    const itemsContainer = document.getElementById('cart-drawer-items');
    if (!itemsContainer) return;

    if (cart.item_count === 0) {
      itemsContainer.innerHTML = '<div class="cart-empty-msg">Your cart is currently empty.</div>';
    } else {
      let itemsHtml = '';
      cart.items.forEach(item => {
        const priceFormatted = Shopify.formatMoney(item.price, "${{amount}}");
        itemsHtml += `
          <div class="cart-item" style="display:flex; gap:12px; margin-bottom:16px; align-items:center; border-bottom:1px solid #f1f5f9; padding-bottom:12px;">
            <img src="${item.image}" alt="${item.title}" style="width:65px; height:65px; object-fit:cover; border-radius:4px; border:1px solid #e0e0e0;">
            <div style="flex:1;">
              <h4 style="font-size:0.85rem; font-weight:600; margin-bottom:2px; color:#212121;">${item.product_title}</h4>
              <p style="font-size:0.72rem; color:#878787; margin-bottom:4px;">${item.variant_title || ''}</p>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.85rem; font-weight:700; color:#f97316;">${priceFormatted}</span>
                <span style="font-size:0.75rem; color:#878787;">Qty: ${item.quantity}</span>
              </div>
            </div>
          </div>
        `;
      });
      itemsContainer.innerHTML = itemsHtml;
    }
  });
}

// Mobile sidebar filters trigger
window.toggleSidebarFilter = function() {
  const sidebar = document.getElementById('collection-sidebar');
  if (sidebar) sidebar.classList.toggle('open');
};

// AJAX Collection Filtering (No page reload grid update)
window.ajaxFilterCollection = function() {
  const form = document.getElementById('collection-filter-form');
  const sortBy = document.getElementById('sort-by').value;
  
  if (!form) return;

  const formData = new FormData(form);
  const params = new URLSearchParams(formData);
  
  // Append sort parameter
  if (sortBy) {
    params.set('sort_by', sortBy);
  }

  const queryUrl = `${window.location.pathname}?${params.toString()}`;
  
  // Update browser URL
  window.history.pushState({ path: queryUrl }, '', queryUrl);

  const gridContainer = document.getElementById('collection-product-grid');
  if (gridContainer) {
    gridContainer.style.opacity = '0.5'; // loading opacity indicator
  }

  fetch(queryUrl)
  .then(response => response.text())
  .then(htmlString => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlString, 'text/html');
    
    // Swap products grid content
    const newGrid = doc.getElementById('collection-product-grid');
    if (gridContainer && newGrid) {
      gridContainer.innerHTML = newGrid.innerHTML;
      gridContainer.style.opacity = '1';
    }

    // Update count labels
    const newCount = doc.getElementById('ajax-product-count');
    const currentCount = document.getElementById('ajax-product-count');
    if (currentCount && newCount) {
      currentCount.textContent = newCount.textContent;
    }
  })
  .catch(err => {
    console.error('AJAX Filter error:', err);
    if (gridContainer) gridContainer.style.opacity = '1';
  });
};

// Shopify formatMoney Helper
if (typeof Shopify === 'undefined') {
  var Shopify = {};
}
Shopify.formatMoney = function(cents, format) {
  if (typeof cents == 'string') { cents = cents.replace('.',''); }
  var value = '';
  var placeholderRegex = /\{\{\s*(\w+)\s*\}\}/;
  var formatString = format || '${{amount}}';

  function defaultOption(opt, def) {
     return (typeof opt == 'undefined' ? def : opt);
  }

  function formatWithDelimiters(number, precision, thousands, decimal) {
    precision = defaultOption(precision, 2);
    thousands = defaultOption(thousands, ',');
    decimal   = defaultOption(decimal, '.');

    if (isNaN(number) || number == null) { return 0; }

    number = (number/100.0).toFixed(precision);

    var parts   = number.split('.'),
        dollars = parts[0].replace(/(\d)(?=(\d\d\d)+(?!\d))/g, '$1' + thousands),
        cents   = parts[1] ? (decimal + parts[1]) : '';

    return dollars + cents;
  }

  switch(formatString.match(placeholderRegex)[1]) {
    case 'amount':
      value = formatWithDelimiters(cents, 2);
      break;
    case 'amount_no_decimals':
      value = formatWithDelimiters(cents, 0);
      break;
    case 'amount_with_comma_separator':
      value = formatWithDelimiters(cents, 2, '.', ',');
      break;
    case 'amount_no_decimals_with_comma_separator':
      value = formatWithDelimiters(cents, 0, '.', ',');
      break;
  }

  return formatString.replace(placeholderRegex, value);
};
