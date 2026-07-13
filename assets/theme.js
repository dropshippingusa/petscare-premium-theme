/* Core Theme JavaScript */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile nav toggle
  const hamburger = document.getElementById('hamburger');
  const mainNav = document.getElementById('main-nav');
  if (hamburger && mainNav) {
    hamburger.addEventListener('click', () => {
      mainNav.classList.toggle('open');
    });
  }

  // Cart Drawer open/close
  const cartIcon = document.getElementById('cart-icon-trigger');
  const cartDrawer = document.getElementById('cart-drawer');
  const cartClose = document.getElementById('cart-drawer-close');
  const cartOverlay = document.getElementById('cart-drawer-overlay');

  if (cartIcon && cartDrawer && cartClose && cartOverlay) {
    cartIcon.addEventListener('click', (e) => {
      e.preventDefault();
      openCartDrawer();
    });

    cartClose.addEventListener('click', closeCartDrawer);
    cartOverlay.addEventListener('click', closeCartDrawer);
  }
});

function openCartDrawer() {
  document.getElementById('cart-drawer').classList.add('open');
  document.getElementById('cart-drawer-overlay').classList.add('open');
  fetchCartData();
}

function closeCartDrawer() {
  document.getElementById('cart-drawer').classList.remove('open');
  document.getElementById('cart-drawer-overlay').classList.remove('open');
}

// AJAX Add to Cart
function ajaxAddToCart(variantId, quantity = 1) {
  const formData = {
    'items': [{
      'id': variantId,
      'quantity': quantity
    }]
  };

  fetch('/cart/add.js', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
    // Show toast
    const toast = document.getElementById('cart-toast');
    if (toast) {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3000);
    }
    // Refresh cart drawer
    openCartDrawer();
  })
  .catch((error) => {
    console.error('Error adding to cart:', error);
  });
}

// Fetch Cart Data and update Drawer
function fetchCartData() {
  fetch('/cart.js')
  .then(response => response.json())
  .then(cart => {
    // Update count in header and drawer
    document.getElementById('header-cart-count').textContent = cart.item_count;
    document.getElementById('drawer-cart-count').textContent = cart.item_count;
    
    // Update subtotal
    const subtotalFormatted = Shopify.formatMoney(cart.total_price, "${{amount}}");
    document.getElementById('drawer-cart-subtotal').textContent = subtotalFormatted;

    // Free shipping threshold ($60.00 = 6000 cents)
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

    // Load Cart Items
    const itemsContainer = document.getElementById('cart-drawer-items');
    if (cart.item_count === 0) {
      itemsContainer.innerHTML = '<div class="cart-empty-msg">Your cart is currently empty.</div>';
    } else {
      let itemsHtml = '';
      cart.items.forEach(item => {
        const priceFormatted = Shopify.formatMoney(item.price, "${{amount}}");
        itemsHtml += `
          <div class="cart-item" style="display:flex; gap:12px; margin-bottom:16px; align-items:center; border-bottom:1px solid #f1f5f9; padding-bottom:12px;">
            <img src="${item.image}" alt="${item.title}" style="width:70px; height:70px; object-fit:cover; border-radius:12px;">
            <div style="flex:1;">
              <h4 style="font-size:0.9rem; margin-bottom:4px;">${item.product_title}</h4>
              <p style="font-size:0.75rem; color:#64748b; margin-bottom:6px;">${item.variant_title || ''}</p>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.85rem; font-weight:700; color:#f97316;">${priceFormatted}</span>
                <span style="font-size:0.8rem; color:#64748b;">Qty: ${item.quantity}</span>
              </div>
            </div>
          </div>
        `;
      });
      itemsContainer.innerHTML = itemsHtml;
    }
  });
}

// Simple Currency formatter helper
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
