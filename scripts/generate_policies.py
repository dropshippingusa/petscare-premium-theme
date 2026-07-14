import os

# Ensure templates directory exists
os.makedirs("templates", exist_ok=True)

# Volume 1: Master Terms of Service
terms_of_service_content = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center; margin-bottom:40px;">Volume 1: Master Terms of Service</h1>
  <div class="page-content policy-content">
    <h2>Section 1 – Introduction</h2>
    <h3>Welcome to PETS CARE USA</h3>
    <p>Welcome to PETS CARE USA. These Master Terms of Service governing your access to and use of the website, including any content, functionality, and services offered on or through petscareusa.com, represent a legally binding agreement between you and PETS CARE USA.</p>
    
    <h3>Acceptance of Terms</h3>
    <p>By accessing, browsing, or otherwise using this website, or by placing an order, you acknowledge that you have read, understood, and agree to be bound by these Terms of Service. If you do not agree to these terms, you must not access or use the website or purchase any products.</p>
    
    <h3>Scope of Agreement</h3>
    <p>These terms govern all transactions, account registrations, content submissions, and communications. This agreement supersedes all prior agreements, warranties, representations, or understandings, written or oral, regarding the subject matter herein.</p>
    
    <h3>Electronic Acceptance</h3>
    <p>You agree that your electronic assent, click-through, or use of the website constitutes a legally binding signature under the Federal Electronic Signatures in Global and National Commerce Act (E-SIGN Act) and the Uniform Electronic Transactions Act (UETA).</p>
    
    <h3>Definitions</h3>
    <ul>
      <li><strong>"Service"</strong> refers to the online ecommerce store, website, tools, and support provided by PETS CARE USA.</li>
      <li><strong>"Product"</strong> refers to any pet food, treats, toys, supplements, accessories, or other physical goods listed for sale.</li>
      <li><strong>"Supplier"</strong> refers to the independent third-party manufacturer, wholesaler, or distributor who fulfills and ships the Product.</li>
      <li><strong>"User"</strong> or <strong>"Customer"</strong> refers to any browser, registered member, or buyer accessing the Site.</li>
    </ul>
    
    <h3>Interpretation</h3>
    <p>Section headings are for convenience only and do not limit the scope or interpretation of the provisions. Singular words include the plural and vice versa.</p>
    
    <h3>Updates to Terms</h3>
    <p>We reserve the right to update, change, or replace any part of these Terms of Service by posting updates to our website. It is your responsibility to check this page periodically for changes. Your continued use of or access to the website following the posting of any changes constitutes acceptance of those changes.</p>

    <h2>Section 2 – About PETS CARE USA</h2>
    <h3>Company Overview</h3>
    <p>PETS CARE USA is an independent online retail store serving pet owners in the United States.</p>
    
    <h3>Business Model</h3>
    <p>PETS CARE USA operates as a sales intermediary and dropshipping platform. We do not maintain physical inventory, own warehouses, or operate manufacturing facilities.</p>
    
    <h3>Shopify Platform</h3>
    <p>Our store is hosted on Shopify Inc. They provide us with the online e-commerce platform that allows us to present and sell our products to you.</p>
    
    <h3>Third-Party Suppliers</h3>
    <p>All products sold on our site are sourced from and fulfilled by independent third-party suppliers who coordinate with us via the Shopify platform.</p>
    
    <h3>Independent Fulfillment Partners</h3>
    <p>Packaging, labeling, and direct-to-consumer shipping are conducted entirely by the independent suppliers or their logistics partners.</p>
    
    <h3>Merchant Responsibilities</h3>
    <p>PETS CARE USA is responsible for managing the user interface, processing transactions, coordinating order details with suppliers, and facilitating customer support inquiries.</p>
    
    <h3>Customer Responsibilities</h3>
    <p>You are responsible for determining whether a product is safe and suitable for your specific pet, verifying ingredients, and following all manufacturer guidelines.</p>

    <h2>Section 3 – Eligibility</h2>
    <h3>Minimum Age</h3>
    <p>By using this site, you represent that you are at least 18 years of age, or the age of majority in your state of residence.</p>
    
    <h3>Legal Capacity</h3>
    <p>You represent and warrant that you possess the legal authority, capacity, and rights to enter into this binding legal agreement.</p>
    
    <h3>Business Purchases</h3>
    <p>If you purchase products on behalf of a business entity, you represent that you have the authority to bind that entity to these Terms of Service.</p>
    
    <h3>Restricted Users</h3>
    <p>We reserve the right to restrict access to our services for users who have previously violated our terms, engaged in fraudulent activities, or reside in jurisdictions where our offerings are legally restricted.</p>

    <h2>Section 4 – User Accounts</h2>
    <h3>Account Registration</h3>
    <p>To access certain features, you may be required to register a user account. You agree to provide accurate, current, and complete information.</p>
    
    <h3>Password Security</h3>
    <p>You are solely responsible for maintaining the confidentiality of your account credentials. You must notify us immediately of any unauthorized use of your account.</p>
    
    <h3>Account Verification</h3>
    <p>We reserve the right to verify account details, including email addresses and shipping locations, to prevent fraud.</p>
    
    <h3>Account Suspension & Termination</h3>
    <p>We reserve the right to suspend or terminate your account at our sole discretion, without notice, for any conduct that we believe violates these Terms of Service or is harmful to other users or our business interests.</p>

    <h2>Section 5 – Orders</h2>
    <h3>Order Acceptance</h3>
    <p>The receipt of an order number or email confirmation does not constitute our acceptance of an order. We reserve the right to reject or cancel any order at any time.</p>
    
    <h3>Order Confirmation</h3>
    <p>Orders are only accepted once they have been approved and processed by our third-party suppliers for fulfillment.</p>
    
    <h3>Order Cancellation & Modification</h3>
    <p>Due to the automated nature of our supplier fulfillment networks, order modifications or cancellations are generally not possible once an order has been submitted. Please review your cart carefully before completing checkout.</p>
    
    <h3>Pricing & Inventory Errors</h3>
    <p>In the event that a product is listed at an incorrect price or with incorrect availability information due to typographical errors or supplier feeds, we reserve the right to cancel any orders placed for that product.</p>

    <h2>Section 6 – Products</h2>
    <h3>Product Descriptions & Specifications</h3>
    <p>All product specifications, details, and ingredients are provided directly by our suppliers. While we attempt to display information accurately, we do not guarantee that descriptions are complete, reliable, or error-free.</p>
    
    <h3>Product Images & Colors</h3>
    <p>We make every effort to display product images and colors as accurately as possible. However, monitor displays vary, and we cannot guarantee that colors will match the physical product exactly.</p>
    
    <h3>Manufacturer Claims & Country of Origin</h3>
    <p>All safety claims, organic certifications, vet approvals, and origin markings are made by the manufacturer/supplier. We do not independently verify these claims.</p>

    <h2>Section 7 – Pricing & Payments</h2>
    <h3>Prices & Taxes</h3>
    <p>Prices are subject to change without notice. Applicable sales taxes will be calculated and displayed during checkout based on delivery location.</p>
    
    <h3>Accepted Payment Methods</h3>
    <p>We accept payment via Shopify Payments, PayPal, Shop Pay, Apple Pay, Google Pay, and major credit cards. You authorize us to charge your selected payment method upon order submission.</p>
    
    <h3>Fraud Prevention</h3>
    <p>We employ automated fraud detection screening. Orders flagged as high-risk will be cancelled immediately to protect credit card holders.</p>

    <h2>Section 8 – Website Use & IP</h2>
    <h3>Permitted Use</h3>
    <p>You are granted a limited, non-exclusive license to access and use the website for personal, non-commercial shopping purposes.</p>
    
    <h3>Prohibited Activities</h3>
    <p>You must not use bots, spiders, or scraping tools to extract data, nor may you introduce malware, viruses, or interfere with website performance.</p>
    
    <h3>Intellectual Property</h3>
    <p>All graphics, logos, website layout, and text are the intellectual property of PETS CARE USA or our content suppliers and are protected by US copyright and trademark laws.</p>
  </div>
</div>
"""

# Volume 2: Privacy Policy
privacy_policy_content = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center; margin-bottom:40px;">Volume 2: Privacy Policy</h1>
  <div class="page-content policy-content">
    <h2>Introduction</h2>
    <p>PETS CARE USA is committed to protecting your privacy. This Privacy Policy describes how we collect, use, and share your personal information when you visit or make a purchase from petscareusa.com.</p>
    
    <h2>Information We Collect</h2>
    <h3>Personal Information</h3>
    <p>We collect contact details such as your name, shipping address, billing address, email address, and phone number when you place an order or register an account.</p>
    
    <h3>Order Data</h3>
    <p>We retain transaction details, purchase history, and items ordered to facilitate processing, customer support, and returns.</p>
    
    <h3>Device & Browser Information</h3>
    <p>When you visit the site, we automatically collect details about your web browser, IP address, time zone, and pages viewed to optimize user experience.</p>
    
    <h2>Cookies & Tracking Technologies</h2>
    <p>We use cookies, web beacons, and pixels to track store activity, manage shopping carts, and serve personalized marketing advertisements. You can disable cookies in your browser settings, but some features of the site may cease to function.</p>
    
    <h2>How We Use Your Information</h2>
    <p>We use collected data to process payments, arrange shipping, fulfill orders, send order confirmations, screen for fraud, and provide you with marketing communications in accordance with your preferences.</p>
    
    <h2>Sharing Your Information</h2>
    <ul>
      <li><strong>Shopify:</strong> We share your personal data with Shopify to power our online store checkout and database systems.</li>
      <li><strong>Fulfillment Partners & Suppliers:</strong> We share order details, shipping names, and addresses with our third-party suppliers to print shipping labels and dispatch products directly.</li>
      <li><strong>Analytics & Ads:</strong> We use Google Analytics and marketing trackers to understand visitor flows and optimize promotions.</li>
    </ul>

    <h2>Your US State Privacy Rights</h2>
    <p>Under CCPA, CPRA, and other state privacy regulations, you have the right to request access to the personal data we hold, request deletion of your information, correct inaccuracies, and opt-out of the sale or sharing of your data for targeted advertising. Contact us at support@petscareusa.com to submit a request.</p>
  </div>
</div>
"""

# Volume 3: Shipping, Returns & Refunds
shipping_returns_content = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center; margin-bottom:40px;">Volume 3: Shipping, Returns & Refunds</h1>
  <div class="page-content policy-content">
    <h2>1. Shipping Policy</h2>
    <h3>Processing Times</h3>
    <p>All orders are routed immediately to our third-party suppliers. Processing times generally range from 1 to 3 business days, excluding weekends and public holidays.</p>
    
    <h3>Delivery Estimates</h3>
    <p>Standard domestic shipping within the United States takes approximately 3 to 7 business days following processing. These shipping times are estimates only, and carrier or warehouse delays may occur.</p>
    
    <h3>Split Shipments</h3>
    <p>Because we coordinate with multiple independent suppliers, items in a single order may ship from different warehouses. As a result, your products may arrive in separate packages and at slightly different times. Individual tracking links will be provided.</p>
    
    <h3>Shipping Restrictions</h3>
    <p>We ship exclusively to domestic addresses within the United States. We cannot ship to PO Boxes, APO, FPO, or DPO addresses due to carrier restrictions on pet foods and heavy shipments.</p>
    
    <h3>Address Accuracy</h3>
    <p>The buyer is responsible for providing a correct and complete shipping address. We are not liable for packages delivered to incorrect locations entered during checkout.</p>
    
    <h3>Lost or Missing Packages</h3>
    <p>If tracking indicates "Delivered" but you have not received your package, please contact the shipping carrier directly. PETS CARE USA is not responsible for packages stolen or lost after carrier delivery confirmation.</p>

    <h2>2. Returns & Refunds</h2>
    <h3>Return Eligibility Window</h3>
    <p>We accept return requests within 30 days of package delivery. To be eligible for a return, products must be unused, unopened, in their original packaging, and in the same condition as received.</p>
    
    <h3>Exempt & Non-Returnable Items</h3>
    <p>Due to safety, hygiene, and health guidelines, the following items cannot be returned:</p>
    <ul>
      <li>Open or used pet food, treats, and edible supplements.</li>
      <li>Pet grooming products, beds, or clothing that have been opened or show pet hair.</li>
      <li>Customized or personalized items.</li>
    </ul>
    
    <h3>Return Authorization Requirement</h3>
    <p><strong>Do not return products to the sender address shown on the package box.</strong> You must email support@petscareusa.com to receive a Return Merchandise Authorization (RMA) and the correct supplier warehouse return address. Unapproved returns will be rejected.</p>
    
    <h3>Damages and Defective Items</h3>
    <p>If an item arrives damaged or defective, email us immediately with high-resolution photos and details. We will file a claim with the supplier to arrange a replacement or refund at no extra cost to you.</p>
    
    <h3>Return Shipping Fees</h3>
    <p>Unless the return is a result of a supplier error, the customer is responsible for all return shipping costs.</p>
  </div>
</div>
"""

# Volume 4: Legal Protection
legal_protection_content = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center; margin-bottom:40px;">Volume 4: Legal Protection</h1>
  <div class="page-content policy-content">
    <h2>1. Disclaimer of Warranties</h2>
    <p>THE WEBSITE AND ALL PRODUCTS SOLD THROUGH IT ARE PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS, WITHOUT REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED.</p>
    <p>TO THE FULL EXTENT PERMITTED BY LAW, PETS CARE USA DISCLAIMS ALL IMPLIED WARRANTIES, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, COURSE OF DEALING, AND TRADE USAGE.</p>
    <p>MANUFACTURERS ARE SOLELY RESPONSIBLE FOR DEFECTS, SAFETY COMPLIANCE, AND PRODUCT QUALITY. WE MAKE NO WARRANTY THAT THE PRODUCTS WILL MEET YOUR REQUIREMENTS OR EXPECTATIONS.</p>

    <h2>2. Limitation of Liability</h2>
    <p>IN NO EVENT SHALL PETS CARE USA, OUR DIRECTORS, OFFICERS, EMPLOYEES, AFFILIATES, AGENTS, CONTRACTORS, OR SUPPLIERS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, PUNITIVE, OR EXEMPLARY DAMAGES OF ANY KIND.</p>
    <p>THIS INCLUDES, WITHOUT LIMITATION, DAMAGES FOR LOSS OF PROFITS, LOSS OF SAVINGS, LOSS OF DATA, REPLACEMENT COSTS, OR ANY SIMILAR LOSSES, WHETHER BASED IN CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY, OR OTHERWISE, ARISING FROM YOUR USE OF THE SERVICE OR ANY PRODUCTS PROCURED THROUGH THE SITE.</p>
    <p>OUR MAXIMUM AGGREGATE LIABILITY FOR ANY CLAIM ARISING OUT OF A PRODUCT PURCHASE SHALL BE STRICTLY CAPPED AT THE ACTUAL AMOUNT PAID BY YOU FOR THAT SPECIFIC ORDER.</p>

    <h2>3. Indemnification</h2>
    <p>You agree to indemnify, defend, and hold harmless PETS CARE USA, our affiliates, officers, directors, employees, and suppliers from and against any and all claims, liabilities, damages, losses, costs, and expenses (including legal fees) arising out of or related to:</p>
    <ul>
      <li>Your misuse of any product purchased from our website;</li>
      <li>Your violation of these Terms of Service or any applicable law;</li>
      <li>Any injury, damage, or adverse reaction caused by a product when not used in strict accordance with manufacturer instructions.</li>
    </ul>

    <h2>4. Dispute Resolution (Arbitration & Class Action Waiver)</h2>
    <h3>Mandatory Binding Arbitration</h3>
    <p>Any dispute, controversy, or claim arising out of or relating to your use of this site or purchase of products shall be resolved exclusively through final and binding arbitration administered by the American Arbitration Association (AAA) under its Consumer Arbitration Rules.</p>
    
    <h3>Class Action Waiver</h3>
    <p>YOU AGREE THAT ANY ARBITRATION SHALL BE CONDUCTED IN YOUR INDIVIDUAL CAPACITY ONLY, AND NOT AS A CLASS ACTION OR REPRESENTATIVE PROCEEDING. YOU WAIVE THE RIGHT TO PARTICIPATE IN A CLASS ACTION LAWSUIT OR CLASS-WIDE ARBITRATION.</p>
    
    <h3>Jury Trial Waiver</h3>
    <p>THE PARTIES MUTUALLY WAIVE THEIR CONSTITUTIONAL RIGHT TO A JURY TRIAL FOR ANY CLAIMS SUBJECT TO THIS AGREEMENT.</p>

    <h2>5. Force Majeure</h2>
    <p>PETS CARE USA shall not be held liable or responsible for any failure to perform, or delay in performance of, our obligations caused by events beyond our reasonable control, including natural disasters, pandemics, war, terrorism, government regulations, carrier strikes, power failures, or supplier disruptions.</p>
  </div>
</div>
"""

# Volume 5: Compliance
compliance_content = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center; margin-bottom:40px;">Volume 5: Compliance & Accessibility</h1>
  <div class="page-content policy-content">
    <h2>1. DMCA Copyright Policy</h2>
    <p>PETS CARE USA respects intellectual property rights. If you believe that any image, description, or content on our website infringes your copyright, please submit a formal DMCA notice to support@petscareusa.com containing:</p>
    <ul>
      <li>A physical or electronic signature of the copyright owner;</li>
      <li>Identification of the copyrighted work claimed to have been infringed;</li>
      <li>Identification of the infringing material and its exact URL;</li>
      <li>Your contact details (address, phone, email);</li>
      <li>A statement that you have a good faith belief that the use is unauthorized.</li>
    </ul>

    <h2>2. Accessibility (ADA Commitment)</h2>
    <p>We strive to make our website accessible to individuals with disabilities. We continuously audit our user interface to align with Web Content Accessibility Guidelines (WCAG 2.1). If you encounter any barriers or need assistance, email us at support@petscareusa.com, and we will assist you.</p>

    <h2>3. Cookies & Marketing Compliance</h2>
    <h3>Email & SMS Communications</h3>
    <p>By entering your contact details at checkout or subscribing, you consent to receive order updates and occasional marketing communications. You can opt-out of marketing emails at any time by clicking the "Unsubscribe" link, or reply "STOP" to SMS messages.</p>

    <h2>4. Reviews Policy</h2>
    <p>All reviews published on our website are submitted by verified buyers or imported directly from supplier feeds. We moderating reviews to filter out spam, offensive language, or irrelevant content, but we do not filter or alter reviews solely because they contain negative feedback.</p>

    <h2>5. U.S. State Privacy Addendums</h2>
    <p>We comply with state-specific data protection regulations including California (CCPA/CPRA), Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), and Texas (TDPSA). We do not sell pet owner information to third-party data brokers.</p>
  </div>
</div>
"""

# Volume 6: Supplier Transparency & Appendices
supplier_transparency_content = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center; margin-bottom:40px;">Supplier Transparency & Appendices</h1>
  <div class="page-content policy-content">
    <h2>Third-Party Supplier Transparency Policy</h2>
    <p>At PETS CARE USA, transparency is key to building trust with pet owners. This transparency policy outlines how products are sourced and fulfilled:</p>
    <ul>
      <li><strong>Retail Intermediary:</strong> PETS CARE USA acts as an online retail storefront. We display products, collect payments, and manage customer service.</li>
      <li><strong>Independent Fulfillment:</strong> When you purchase an item, the order details are securely transmitted to an independent supplier. The supplier is responsible for retrieving the product, packaging it, and shipping it directly to your door.</li>
      <li><strong>Quality Control Responsibility:</strong> Product quality, raw ingredients, and manufacturing standards are controlled exclusively by the third-party manufacturers. PETS CARE USA relies on manufacturer statements and does not independently test ingredients.</li>
    </ul>

    <h2>Health & Safety Vet Disclaimer</h2>
    <p><strong>WARNING:</strong> The information and products displayed on petscareusa.com are not intended to substitute professional veterinary advice, diagnosis, or treatment. Always consult a licensed veterinarian before changing your pet's diet, starting new supplements, or using health products.</p>

    <h2>FDA Disclaimer</h2>
    <p>Product claims and supplements listed on this site have not been evaluated by the Food and Drug Administration (FDA) unless explicitly stated. Products are not intended to diagnose, treat, cure, or prevent any veterinary disease.</p>

    <h2>Enterprise Appendices</h2>
    <h3>1. Glossary of Terms</h3>
    <ul>
      <li><strong>Site/Website:</strong> petscareusa.com</li>
      <li><strong>RMA:</strong> Return Merchandise Authorization</li>
      <li><strong>Suppliers:</strong> Independent merchant fulfillment partners</li>
    </ul>

    <h3>2. Customer DMCA Notice Template</h3>
    <p>To file an infringement claim, copy and email the template located in our Compliance section directly to support@petscareusa.com.</p>
    
    <h3>3. Return Merchandise Authorization (RMA) Process</h3>
    <p>1. Email support@petscareusa.com with order number and pictures of items. <br>
       2. Receive RMA number and designated supplier address. <br>
       3. Ship item and email tracking number. <br>
       4. Refund is issued after supplier inspects and approves the item.</p>

    <h3>4. Policy Revision Log</h3>
    <p>July 14, 2026: Restructured all site policies for enhanced dropshipping mediator liability protection.</p>
  </div>
</div>
"""

# Write files to templates directory
with open("templates/page.terms-of-service.liquid", "w", encoding="utf-8") as f:
    f.write(terms_of_service_content)

with open("templates/page.privacy-policy.liquid", "w", encoding="utf-8") as f:
    f.write(privacy_policy_content)

with open("templates/page.shipping-returns.liquid", "w", encoding="utf-8") as f:
    f.write(shipping_returns_content)

with open("templates/page.legal-protection.liquid", "w", encoding="utf-8") as f:
    f.write(legal_protection_content)

with open("templates/page.compliance.liquid", "w", encoding="utf-8") as f:
    f.write(compliance_content)

with open("templates/page.supplier-transparency.liquid", "w", encoding="utf-8") as f:
    f.write(supplier_transparency_content)

print("Policy templates created successfully.")
