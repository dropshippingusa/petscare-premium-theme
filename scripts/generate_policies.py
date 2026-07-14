import os

os.makedirs("snippets", exist_ok=True)

# ─── VOLUME 1: TERMS OF SERVICE ─────────────────────────────────────────────
tos = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center;margin-bottom:40px;">TERMS OF SERVICE</h1>
  <div class="page-content policy-content">
    <p><strong>PETS CARE USA</strong> | Website: petscareusa.com | Effective Date: July 14, 2026 | Last Updated: July 14, 2026</p>
    <p>PLEASE READ THESE TERMS OF SERVICE ("AGREEMENT," "TERMS," OR "TOS") CAREFULLY BEFORE USING THE WEBSITE LOCATED AT PETSCAREUSA.COM. BY ACCESSING, BROWSING, REGISTERING AN ACCOUNT, OR PLACING AN ORDER THROUGH THIS WEBSITE, YOU ACKNOWLEDGE THAT YOU HAVE READ, UNDERSTOOD, AND AGREE TO BE LEGALLY BOUND BY ALL TERMS, CONDITIONS, AND POLICIES CONTAINED HEREIN. IF YOU DO NOT AGREE TO THESE TERMS IN THEIR ENTIRETY, YOU MUST IMMEDIATELY CEASE ALL USE OF THIS WEBSITE.</p>

    <h2>SECTION 1 – INTRODUCTION AND ACCEPTANCE OF TERMS</h2>
    <h3>1.1 Introduction</h3>
    <p>Welcome to PETS CARE USA. These Terms of Service constitute a legally binding agreement between you ("User," "Customer," "Buyer," or "You") and PETS CARE USA ("Company," "We," "Us," or "Our"), the operator of the online retail storefront located at petscareusa.com. This Agreement governs your access to and use of the Website, including all content, features, services, and products available through the Website.</p>
    <h3>1.2 Electronic Acceptance</h3>
    <p>Your use of this Website, creation of an account, or placement of an order constitutes your electronic signature and acceptance of these Terms of Service. This electronic acceptance is legally binding to the same extent as a physical signature under the Electronic Signatures in Global and National Commerce Act (15 U.S.C. § 7001, et seq.) ("E-SIGN Act") and the Uniform Electronic Transactions Act ("UETA") as adopted in applicable states.</p>
    <h3>1.3 Modifications to Terms</h3>
    <p>PETS CARE USA reserves the right, at its sole discretion, to amend, modify, update, or replace any part of these Terms of Service at any time without prior notice. Such modifications shall become effective immediately upon posting to the Website. Your continued access to or use of the Website after any modifications constitutes your irrevocable acceptance of such modified Terms.</p>
    <h3>1.4 Incorporation of Additional Policies</h3>
    <p>These Terms of Service incorporate by reference the following additional policies, each of which is expressly made part of this Agreement: Privacy Policy; Shipping and Returns Policy; Legal Protection and Liability Policy; Compliance Policy; and Supplier Transparency Policy.</p>

    <h2>SECTION 2 – DEFINITIONS</h2>
    <ul>
      <li><strong>"Agreement"</strong> means these Terms of Service, as amended, together with all documents incorporated herein by reference.</li>
      <li><strong>"Company," "PETS CARE USA," "We," "Us," or "Our"</strong> refers to the operator of the Website, an independent ecommerce marketplace and online retail storefront.</li>
      <li><strong>"Customer," "User," "Buyer," or "You"</strong> means any individual or entity who accesses, browses, registers on, or places orders through the Website.</li>
      <li><strong>"Marketplace"</strong> refers to the online ecommerce platform operated by the Company through which third-party Suppliers list and fulfill products.</li>
      <li><strong>"Order"</strong> means any purchase transaction initiated by a Customer on the Website.</li>
      <li><strong>"Product" or "Products"</strong> means any item listed for sale on the Website, including pet food, treats, supplements, toys, accessories, grooming products, health products, and related goods.</li>
      <li><strong>"Shopify"</strong> refers to Shopify Inc., the third-party technology company whose platform hosts and powers the Website's ecommerce infrastructure.</li>
      <li><strong>"Supplier," "Manufacturer," "Vendor," or "Fulfillment Partner"</strong> means any independent third-party manufacturer, supplier, distributor, wholesaler, or fulfillment company who sources, manufactures, packages, labels, warehouses, and ships Products directly to Customers.</li>
      <li><strong>"User Content"</strong> means any information, text, images, reviews, ratings, or other materials submitted by Users to the Website.</li>
      <li><strong>"Website" or "Site"</strong> means petscareusa.com and all associated subdomains, pages, features, and services.</li>
    </ul>

    <h2>SECTION 3 – MARKETPLACE STATUS AND BUSINESS MODEL</h2>
    <h3>3.1 Independent Ecommerce Marketplace</h3>
    <p>PETS CARE USA operates solely as an independent online ecommerce marketplace and sales intermediary. The Company acts as a transaction facilitator and customer service coordinator, providing a digital retail storefront through which independent Suppliers list and sell Products directly to Customers.</p>
    <h3>3.2 What PETS CARE USA Is Not</h3>
    <p>PETS CARE USA IS NOT, and does not represent itself to be, any of the following: a manufacturer, co-manufacturer, or product developer; a product designer, formulator, or ingredient supplier; an importer, exporter, or customs broker; a laboratory, testing agency, or quality inspector; a veterinarian, veterinary clinic, or animal health professional; a pharmacy, compounding pharmacy, or medical provider; a certification authority or regulatory compliance agency; a warehouse operator, fulfillment center, or logistics provider; a shipping carrier or freight forwarder; a packaging company or labeling company; or an insurer or warranty provider.</p>
    <h3>3.3 Supplier Fulfillment Model</h3>
    <p>All Products listed on the Website are sourced, manufactured, formulated, packaged, labeled, stored, inspected, quality-controlled, certified, and shipped directly by independent third-party Suppliers. PETS CARE USA does not manufacture, formulate, modify, inspect, certify, independently test, warehouse, package, relabel, or otherwise physically handle any Product unless expressly stated in a specific product listing.</p>
    <h3>3.4 Shopify Platform</h3>
    <p>The Website operates on Shopify's ecommerce infrastructure. Shopify Inc. provides technology services including payment processing, data storage, and platform hosting. Shopify is an independent third-party service provider and is not an operator, owner, agent, or representative of PETS CARE USA. Use of the Website is subject to Shopify's Terms of Service and Privacy Policy in addition to this Agreement.</p>
    <h3>3.5 No Agency Relationship with Suppliers</h3>
    <p>Nothing in this Agreement shall be construed as creating an agency, partnership, joint venture, franchise, or employment relationship between PETS CARE USA and any Supplier. Suppliers are independent contractors. PETS CARE USA does not control, direct, supervise, or manage the manufacturing, production, packaging, labeling, inspection, testing, storage, or shipping operations of any Supplier.</p>

    <h2>SECTION 4 – ELIGIBILITY</h2>
    <h3>4.1 Age Requirement</h3>
    <p>The Website is intended for use by individuals who are at least eighteen (18) years of age, or the age of majority in their jurisdiction of residence, whichever is greater. By accessing the Website or placing an Order, you represent and warrant that you meet this minimum age requirement.</p>
    <h3>4.2 Legal Capacity</h3>
    <p>By using the Website, you represent and warrant that you have the full legal right, power, and authority to enter into this Agreement, and that doing so does not violate any applicable law or any other agreement to which you are a party.</p>
    <h3>4.3 Geographic Eligibility</h3>
    <p>The Website is intended for use by residents of the contiguous United States. PETS CARE USA makes no representation that the Website, Products, or services are appropriate or available for use in other locations. Users who access the Website from outside the United States do so at their own risk and are responsible for compliance with local laws.</p>
    <h3>4.4 Prohibited Users</h3>
    <p>PETS CARE USA reserves the right, at its sole discretion, to deny access to the Website or refuse service to any person or entity, including without limitation those who have previously violated this Agreement, engaged in fraudulent activity, or abused the returns or chargeback process.</p>

    <h2>SECTION 5 – USER ACCOUNTS</h2>
    <h3>5.1 Account Registration</h3>
    <p>Certain features of the Website may require you to register for a user account. When registering, you agree to provide accurate, current, complete, and truthful information and to promptly update your account information whenever it becomes inaccurate or outdated.</p>
    <h3>5.2 Account Security</h3>
    <p>You are solely responsible for maintaining the confidentiality of your account credentials, including your username and password. You are fully responsible for all activities that occur under your account, whether or not authorized by you. You must immediately notify PETS CARE USA at support@petscareusa.com of any unauthorized access to or use of your account.</p>
    <h3>5.3 Account Suspension and Termination</h3>
    <p>PETS CARE USA reserves the right to suspend, restrict, or permanently terminate your account, in its sole discretion, without prior notice, if we believe you have violated these Terms, engaged in fraudulent conduct, filed improper chargebacks, or engaged in conduct harmful to other users, Suppliers, or the Company.</p>

    <h2>SECTION 6 – ORDERS AND ORDER PROCESSING</h2>
    <h3>6.1 Order Placement</h3>
    <p>By submitting an Order on the Website, you make an offer to purchase Products subject to these Terms. PETS CARE USA reserves the right to accept or reject any Order, in whole or in part, for any reason, including but not limited to product unavailability, pricing errors, suspected fraud, or restrictions imposed by Suppliers.</p>
    <h3>6.2 Order Confirmation</h3>
    <p>Receipt of an order confirmation email does not constitute final acceptance of your Order. Orders are accepted only upon successful transmission of your order to the applicable Supplier and confirmation of payment authorization. PETS CARE USA reserves the right to cancel confirmed Orders prior to shipment.</p>
    <h3>6.3 Order Cancellation</h3>
    <p>Due to the automated and time-sensitive nature of the Supplier fulfillment process, orders typically cannot be modified or cancelled once submitted. If you wish to cancel an Order, you must contact support@petscareusa.com immediately. Cancellation is only possible if the Order has not yet been transmitted to or accepted by the Supplier. PETS CARE USA makes no guarantee that cancellation requests can be accommodated.</p>
    <h3>6.4 Pricing Errors</h3>
    <p>In the event a Product is listed at an incorrect price due to typographical errors, system errors, or Supplier data feed errors, PETS CARE USA reserves the right to cancel any Orders placed at the incorrect price and to refund any amounts charged.</p>

    <h2>SECTION 7 – PAYMENTS</h2>
    <h3>7.1 Accepted Payment Methods</h3>
    <p>PETS CARE USA accepts payment through Shopify Payments, PayPal, Shop Pay, Apple Pay, Google Pay, and major credit and debit cards including Visa, Mastercard, American Express, and Discover. By submitting payment information, you authorize PETS CARE USA to charge the designated payment method for the full Order amount, including applicable taxes and shipping fees.</p>
    <h3>7.2 Payment Processing</h3>
    <p>Payment processing is handled by Shopify Payments and third-party payment processors. PETS CARE USA does not directly store full credit card numbers. Payment processors maintain their own privacy and security policies, and PETS CARE USA is not responsible for the practices of third-party payment processors.</p>
    <h3>7.3 Sales Tax</h3>
    <p>Applicable sales tax is calculated based on the delivery destination and applicable state and local tax laws. Tax rates are subject to change. You are responsible for all applicable taxes associated with your Order.</p>
    <h3>7.4 Chargebacks</h3>
    <p>If you initiate a chargeback with your payment provider without first contacting PETS CARE USA through our official support channels and allowing a reasonable period for resolution, PETS CARE USA reserves the right to dispute the chargeback and to suspend or terminate your account. Filing a chargeback for a valid, delivered Order may constitute fraud.</p>

    <h2>SECTION 8 – PRODUCTS AND PRODUCT INFORMATION</h2>
    <h3>8.1 Product Listings</h3>
    <p>PETS CARE USA lists Products on the Website based on information provided by independent Suppliers. The Company does not independently create, author, or verify product listings, descriptions, specifications, images, ingredient lists, certifications, or any other information associated with Products.</p>
    <h3>8.2 Product Information Disclaimer</h3>
    <p>ALL PRODUCT INFORMATION DISPLAYED ON THE WEBSITE, INCLUDING BUT NOT LIMITED TO DESCRIPTIONS, IMAGES, INGREDIENTS, SPECIFICATIONS, DIMENSIONS, CERTIFICATIONS, REGULATORY CLAIMS, VETERINARY STATEMENTS, AND PERFORMANCE CLAIMS, ORIGINATES SOLELY FROM INDEPENDENT MANUFACTURERS OR SUPPLIERS. PETS CARE USA REPUBLISHES SUCH INFORMATION SOLELY FOR CUSTOMER CONVENIENCE AND DOES NOT INDEPENDENTLY VERIFY THE ACCURACY, COMPLETENESS, LEGALITY, SAFETY, RELIABILITY, EFFECTIVENESS, MERCHANTABILITY, OR SUITABILITY OF ANY MANUFACTURER-PROVIDED INFORMATION.</p>
    <h3>8.3 Supplier Changes to Products</h3>
    <p>Suppliers may, without notice to PETS CARE USA or Customers, change product ingredients, formulations, packaging, labeling, colors, dimensions, warnings, certifications, instructions, manufacturing locations, and country of origin. PETS CARE USA is not responsible for discrepancies between Website listings and actual products resulting from undisclosed Supplier changes.</p>

    <h2>SECTION 9 – PRODUCT SUITABILITY AND CUSTOMER RESPONSIBILITY</h2>
    <h3>9.1 Customer's Sole Responsibility for Suitability</h3>
    <p>CUSTOMERS ARE SOLELY AND ENTIRELY RESPONSIBLE FOR DETERMINING WHETHER ANY PRODUCT IS APPROPRIATE, SUITABLE, AND SAFE FOR THEIR PARTICULAR PET. PETS CARE USA CANNOT EVALUATE SUITABILITY FOR ANY INDIVIDUAL ANIMAL AND DOES NOT PROVIDE PRODUCT RECOMMENDATIONS FOR SPECIFIC PETS.</p>
    <h3>9.2 Factors Affecting Suitability</h3>
    <p>Product suitability depends on numerous factors including: species, breed, genetic lineage; age and developmental stage; size, weight, and body condition; known or unknown allergies and sensitivities; current medications and potential interactions; existing medical conditions; dietary requirements; prior veterinary recommendations; and level of supervision during product use.</p>
    <h3>9.3 Veterinary Consultation Required</h3>
    <p>CUSTOMERS SHOULD CONSULT A LICENSED VETERINARIAN BEFORE USING ANY PRODUCT INTENDED FOR INGESTION, INCLUDING FOOD, TREATS, SUPPLEMENTS, VITAMINS, MINERALS, PROBIOTICS, AND HERBAL PRODUCTS, AS WELL AS TOPICAL GROOMING PRODUCTS, HEALTH PRODUCTS, AND ANY PRODUCT AFFECTING ANIMAL HEALTH OR BEHAVIOR.</p>

    <h2>SECTION 10 – VETERINARY AND PROFESSIONAL ADVICE DISCLAIMER</h2>
    <h3>10.1 No Veterinary Advice</h3>
    <p>NOTHING CONTAINED ON THIS WEBSITE, IN ANY PRODUCT LISTING, IN ANY MARKETING COMMUNICATION, IN ANY EMAIL, OR IN ANY CUSTOMER SERVICE INTERACTION CONSTITUTES VETERINARY ADVICE, MEDICAL ADVICE, PROFESSIONAL DIAGNOSIS, TREATMENT, PRESCRIPTION, BEHAVIORAL GUIDANCE, NUTRITIONAL COUNSEL, OR ANY OTHER FORM OF PROFESSIONAL CONSULTATION.</p>
    <h3>10.2 Emergency Situations</h3>
    <p>If your animal is experiencing a health emergency, contact a licensed veterinarian or emergency veterinary clinic immediately. Do not delay professional veterinary care in reliance on any Website content.</p>

    <h2>SECTION 11 – MARKETPLACE DISCLAIMER</h2>
    <h3>11.1 Marketplace Role Reaffirmed</h3>
    <p>PETS CARE USA ACTS SOLELY AS AN INDEPENDENT ECOMMERCE MARKETPLACE AND SALES INTERMEDIARY. THE COMPANY DOES NOT MANUFACTURE, FORMULATE, INSPECT, CERTIFY, WAREHOUSE, PACKAGE, RELABEL, MODIFY, INSTALL, REPAIR, ENDORSE, RECOMMEND, OR GUARANTEE ANY PRODUCTS SOLD THROUGH THE WEBSITE.</p>
    <h3>11.2 Supplier Sole Responsibility</h3>
    <p>Responsibility for the following remains solely with the applicable Supplier or manufacturer, except where applicable law provides otherwise: manufacturing and production; ingredients, formulation, and composition; labeling and packaging; independent testing and quality control; regulatory compliance and certifications; product recalls and safety notices; express and implied warranties; product safety and performance; instructions for use and warnings; country of origin disclosures; nutritional accuracy; and veterinary claims and health representations.</p>

    <h2>SECTION 12 – WARRANTY DISCLAIMER</h2>
    <h3>12.1 Disclaimer of All Warranties</h3>
    <p>TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, THE WEBSITE AND ALL PRODUCTS AND SERVICES PROVIDED THROUGH THE WEBSITE ARE PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS, WITHOUT ANY REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED. PETS CARE USA EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, TITLE, ACCURACY, COMPLETENESS, AND RELIABILITY.</p>
    <h3>12.2 No Independent Product Warranty</h3>
    <p>PETS CARE USA PROVIDES NO INDEPENDENT PRODUCT WARRANTY OF ANY KIND. ANY WARRANTY APPLICABLE TO A PRODUCT IS SOLELY THE WARRANTY, IF ANY, OFFERED BY THE MANUFACTURER OR SUPPLIER OF THAT PRODUCT. PETS CARE USA IS NOT A PARTY TO ANY MANUFACTURER WARRANTY AND HAS NO OBLIGATION TO HONOR, ADMINISTER, OR ENFORCE SUCH WARRANTIES.</p>

    <h2>SECTION 13 – PRODUCT LIABILITY DISCLAIMER</h2>
    <h3>13.1 No Product Liability for Marketplace Intermediary</h3>
    <p>BECAUSE PETS CARE USA DOES NOT MANUFACTURE, FORMULATE, INSPECT, TEST, PACKAGE, OR PHYSICALLY HANDLE PRODUCTS, ANY CLAIM ARISING FROM A PRODUCT DEFECT, LABELING ERROR, CONTAMINATION, INGREDIENT ISSUE, ALLERGIC REACTION, OR SIMILAR PRODUCT-RELATED HARM IS PROPERLY DIRECTED AT THE APPLICABLE SUPPLIER OR MANUFACTURER, NOT AT PETS CARE USA. TO THE MAXIMUM EXTENT PERMITTED BY LAW, PETS CARE USA SHALL NOT BE LIABLE FOR ANY SUCH CLAIM.</p>

    <h2>SECTION 14 – LIMITATION OF LIABILITY</h2>
    <h3>14.1 General Limitation</h3>
    <p>TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL PETS CARE USA, ITS OFFICERS, DIRECTORS, EMPLOYEES, AGENTS, CONTRACTORS, AFFILIATES, LICENSORS, SUCCESSORS, OR ASSIGNS BE LIABLE TO ANY CUSTOMER OR THIRD PARTY FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, PUNITIVE, EXEMPLARY, OR ENHANCED DAMAGES OF ANY KIND, INCLUDING WITHOUT LIMITATION DAMAGES FOR: manufacturing defects or labeling errors; allergic reactions or adverse reactions; pet injury, illness, or death; loss of profits, revenue, savings, or business opportunities; loss or corruption of data; business interruption; emotional distress; shipping delays or carrier errors; supplier errors or failures; product recalls; or unauthorized access to your account or data.</p>
    <h3>14.2 Maximum Aggregate Liability</h3>
    <p>IN ALL EVENTS, PETS CARE USA'S MAXIMUM AGGREGATE LIABILITY ARISING OUT OF OR RELATING TO ANY SINGLE ORDER OR CLAIM SHALL BE STRICTLY LIMITED TO THE ACTUAL AMOUNT PAID BY THE CUSTOMER FOR THE SPECIFIC ORDER GIVING RISE TO THE CLAIM, NOT TO EXCEED ONE HUNDRED DOLLARS ($100.00), REGARDLESS OF THE FORM OF ACTION OR THE BASIS OF THE CLAIM.</p>
    <h3>14.3 Basis of Bargain</h3>
    <p>YOU ACKNOWLEDGE AND AGREE THAT PETS CARE USA HAS OFFERED PRODUCTS AND SERVICES ON THE WEBSITE IN RELIANCE UPON THE WARRANTY DISCLAIMERS AND LIMITATIONS OF LIABILITY SET FORTH IN THIS AGREEMENT, AND THAT SUCH DISCLAIMERS AND LIMITATIONS CONSTITUTE AN ESSENTIAL ELEMENT OF THE BASIS OF THE BARGAIN BETWEEN THE PARTIES.</p>

    <h2>SECTION 15 – ASSUMPTION OF RISK</h2>
    <p>BY PURCHASING ANY PRODUCT THROUGH THIS WEBSITE, YOU VOLUNTARILY ASSUME ALL RISKS ASSOCIATED WITH PURCHASING, RECEIVING, HANDLING, STORING, INTRODUCING, ADMINISTERING, AND USING THE PRODUCT WITH YOUR PET OR IN YOUR HOUSEHOLD. SUCH RISKS INCLUDE BUT ARE NOT LIMITED TO ALLERGIC REACTIONS, ADVERSE REACTIONS, INJURY, ILLNESS, DEATH, PROPERTY DAMAGE, AND FINANCIAL LOSS. YOU ACKNOWLEDGE THAT BOTH KNOWN AND UNKNOWN RISKS EXIST IN CONNECTION WITH THE USE OF PET PRODUCTS AND EXPRESSLY ASSUME RESPONSIBILITY FOR ALL SUCH RISKS.</p>

    <h2>SECTION 16 – INDEMNIFICATION</h2>
    <p>You agree to indemnify, defend, and hold harmless PETS CARE USA, its officers, directors, employees, agents, contractors, Suppliers, and affiliates from and against any and all claims, demands, causes of action, suits, proceedings, liabilities, obligations, losses, damages, costs, and expenses (including reasonable attorneys' fees and court costs) arising out of or relating to: your use of or access to the Website; your violation of any provision of this Agreement; your violation of any applicable law, rule, or regulation; your misuse of any Product purchased through the Website; your failure to consult a veterinarian regarding Product suitability; any User Content you submit; your infringement of any third-party intellectual property rights; or any injury or damage caused by your negligence or willful misconduct.</p>

    <h2>SECTION 17 – SHIPPING AND DELIVERY</h2>
    <p>All Products are shipped directly by Suppliers. PETS CARE USA does not warehouse, pick, pack, or ship Products. Shipping timelines, carrier selection, and packaging are determined by the applicable Supplier. Delivery estimates are provided by Suppliers and are not guaranteed. Orders containing Products from multiple Suppliers may ship separately. Customers are solely responsible for providing a complete and accurate shipping address. For complete details, see the Shipping and Returns Policy.</p>

    <h2>SECTION 18 – RETURNS AND REFUNDS</h2>
    <p>Please refer to our Shipping and Returns Policy for complete information regarding return eligibility, procedures, timelines, non-returnable items, and refund processing. The Shipping and Returns Policy is incorporated herein by reference.</p>

    <h2>SECTION 19 – INTELLECTUAL PROPERTY</h2>
    <h3>19.1 Website Content Ownership</h3>
    <p>The Website, including all design elements, graphics, logos, layouts, software, code, and original text, is owned by or licensed to PETS CARE USA and is protected by United States copyright, trademark, and other intellectual property laws. PETS CARE USA grants you a limited, revocable, non-exclusive, non-transferable license to access and use the Website solely for personal, non-commercial shopping purposes.</p>
    <h3>19.2 User-Submitted Content</h3>
    <p>By submitting reviews, ratings, photos, or other content to the Website, you grant PETS CARE USA a non-exclusive, royalty-free, perpetual, irrevocable, worldwide license to use, reproduce, modify, publish, and display such content in connection with the Website and its marketing activities.</p>

    <h2>SECTION 20 – USER CONDUCT</h2>
    <p>You agree not to engage in the following prohibited activities: submitting false, misleading, or fraudulent orders or information; impersonating any person or entity; using the Website for any unlawful purpose; circumventing any security or access control measures; introducing malware or disruptive code; reselling Products commercially without authorization; submitting false or malicious product reviews; abusing customer service or return processes; or engaging in any conduct that damages PETS CARE USA's reputation.</p>

    <h2>SECTION 21 – PRODUCT RECALLS</h2>
    <p>Manufacturers and Suppliers are solely responsible for initiating, administering, and funding any product recalls. PETS CARE USA may assist in communicating recall notices to affected Customers but has no obligation to administer or fund recall programs and bears no liability arising from product recalls initiated by Suppliers or regulatory authorities.</p>

    <h2>SECTION 22 – REGULATORY DISCLAIMERS</h2>
    <p>All claims of compliance with FDA, AAFCO, USDA, FTC, EPA, CPSC, ASTM, Proposition 65, or any state regulatory standards originate from Suppliers and are not independently verified by PETS CARE USA. PETS CARE USA does not certify regulatory compliance for any Product.</p>

    <h2>SECTION 23 – DISPUTE RESOLUTION</h2>
    <h3>23.1 Informal Resolution</h3>
    <p>Before initiating formal dispute resolution, you agree to contact PETS CARE USA at support@petscareusa.com and provide a detailed written description of your dispute. You agree to allow thirty (30) days for good-faith resolution before initiating arbitration.</p>
    <h3>23.2 Mandatory Binding Arbitration</h3>
    <p>ANY DISPUTE, CLAIM, OR CONTROVERSY ARISING OUT OF OR RELATING TO THIS AGREEMENT, YOUR USE OF THE WEBSITE, OR ANY PRODUCT PURCHASED THROUGH THE WEBSITE SHALL BE RESOLVED EXCLUSIVELY BY FINAL AND BINDING INDIVIDUAL ARBITRATION ADMINISTERED BY THE AMERICAN ARBITRATION ASSOCIATION ("AAA") PURSUANT TO ITS CONSUMER ARBITRATION RULES, TO THE EXTENT PERMITTED BY APPLICABLE LAW. THE ARBITRATOR'S DECISION SHALL BE FINAL, BINDING, AND NON-APPEALABLE EXCEPT ON GROUNDS SPECIFIED IN THE FEDERAL ARBITRATION ACT (9 U.S.C. § 1, ET SEQ.).</p>
    <h3>23.3 Class Action Waiver</h3>
    <p>YOU AND PETS CARE USA EACH AGREE THAT ANY DISPUTE RESOLUTION PROCEEDING SHALL BE CONDUCTED ONLY IN YOUR INDIVIDUAL CAPACITY AND NOT AS A CLASS ACTION, COLLECTIVE ACTION, CONSOLIDATED ACTION, OR REPRESENTATIVE PROCEEDING OF ANY KIND. YOU EXPRESSLY WAIVE YOUR RIGHT TO PARTICIPATE IN ANY CLASS ACTION LAWSUIT OR CLASS-WIDE ARBITRATION PROCEEDING AGAINST PETS CARE USA.</p>
    <h3>23.4 Jury Trial Waiver</h3>
    <p>TO THE EXTENT PERMITTED BY LAW, BOTH YOU AND PETS CARE USA VOLUNTARILY AND KNOWINGLY WAIVE ANY RIGHT TO A JURY TRIAL IN CONNECTION WITH ANY DISPUTE ARISING UNDER OR RELATING TO THIS AGREEMENT.</p>
    <h3>23.5 Time Limitation on Claims</h3>
    <p>Any claim or cause of action arising out of or related to this Agreement or the Website must be filed within one (1) year after such claim or cause of action arose, or be forever barred, to the extent permitted by applicable law.</p>

    <h2>SECTION 24 – GOVERNING LAW</h2>
    <p>This Agreement shall be governed by and construed in accordance with the laws of the United States and the State of Delaware, without regard to conflict of law principles. For any dispute not subject to arbitration, you consent to exclusive personal jurisdiction and venue in the state and federal courts located in Delaware.</p>

    <h2>SECTION 25 – FORCE MAJEURE</h2>
    <p>PETS CARE USA shall not be liable or responsible for any delay, failure, or inability to perform its obligations caused directly or indirectly by events beyond its reasonable control, including natural disasters, pandemics, acts of God, war, terrorism, governmental actions, labor disputes, power failures, internet outages, supply chain disruptions, Supplier failures, or carrier disruptions.</p>

    <h2>SECTION 26 – GENERAL PROVISIONS</h2>
    <h3>26.1 Severability</h3>
    <p>If any provision of this Agreement is found to be invalid, illegal, or unenforceable, such provision shall be modified to the minimum extent necessary, and the remaining provisions shall remain in full force and effect.</p>
    <h3>26.2 Entire Agreement</h3>
    <p>This Agreement, together with all policies incorporated herein by reference, constitutes the entire agreement between you and PETS CARE USA with respect to the subject matter hereof, and supersedes all prior or contemporaneous oral or written agreements, understandings, representations, and warranties.</p>
    <h3>26.3 Contact Information</h3>
    <p>PETS CARE USA | Customer Support: support@petscareusa.com | Website: petscareusa.com</p>
  </div>
</div>"""

# ─── VOLUME 2: PRIVACY POLICY ────────────────────────────────────────────────
privacy = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center;margin-bottom:40px;">PRIVACY POLICY</h1>
  <div class="page-content policy-content">
    <p><strong>PETS CARE USA</strong> | Website: petscareusa.com | Effective Date: July 14, 2026 | Last Updated: July 14, 2026</p>
    <p>This Privacy Policy ("Policy") describes how PETS CARE USA ("Company," "We," "Us," or "Our") collects, uses, discloses, retains, and protects personal information when you visit or interact with our Website at petscareusa.com, create an account, place an order, or otherwise engage with our services. By using the Website, you acknowledge that you have read and understood this Policy and consent to the collection and use of your information as described herein.</p>

    <h2>SECTION 1 – INFORMATION WE COLLECT</h2>
    <h3>1.1 Information You Provide Directly</h3>
    <p>We collect personal information that you voluntarily provide to us, including when you: register for an account (name, email address, password); place an order (name, billing address, shipping address, email, phone number); contact customer support; subscribe to marketing communications; submit product reviews or ratings; or participate in promotions or surveys.</p>
    <h3>1.2 Information Collected Automatically</h3>
    <p>When you visit the Website, we automatically collect certain technical and usage information through cookies, web beacons, log files, and similar tracking technologies, including: IP address and approximate geographic location; browser type, version, and language settings; device type, operating system, and device identifiers; pages visited, links clicked, and navigation patterns; referring URLs and exit pages; date and time of Website visits; search queries conducted on the Website; and products viewed, added to cart, or purchased.</p>
    <h3>1.3 Order and Transaction Data</h3>
    <p>We collect and retain information about your transactions, including order numbers, products purchased, prices paid, payment method type, order status, shipping information, and communication history related to your orders.</p>
    <h3>1.4 Information from Third Parties</h3>
    <p>We may receive information about you from third-party sources, including advertising platforms, analytics providers, payment processors, fraud detection services, and social media platforms, in accordance with their respective privacy policies.</p>

    <h2>SECTION 2 – COOKIES AND TRACKING TECHNOLOGIES</h2>
    <h3>2.1 Types of Cookies Used</h3>
    <p><strong>Strictly Necessary Cookies:</strong> Required for core Website functionality including shopping cart management, session authentication, and checkout processing. These cannot be disabled without impairing Website functionality.</p>
    <p><strong>Performance and Analytics Cookies:</strong> Used to understand how visitors interact with the Website, identify popular pages, and measure traffic sources. We use Google Analytics and similar tools for this purpose.</p>
    <p><strong>Functional Cookies:</strong> Enable personalization features such as saved preferences, wishlist retention, and localization.</p>
    <p><strong>Advertising and Targeting Cookies:</strong> Used by advertising partners including Meta (Facebook) Pixel, Google Ads, TikTok Pixel, and Pinterest Tag to deliver relevant advertising and measure campaign effectiveness.</p>
    <h3>2.2 Managing Cookies</h3>
    <p>You may disable or restrict cookies through your browser settings. However, disabling certain cookies may impair Website functionality. Note that even if you opt out of advertising cookies, you may still see generic advertisements.</p>
    <h3>2.3 Web Beacons and Pixels</h3>
    <p>We use web beacons and tracking pixels in our emails and on our Website to track email open rates, click-through rates, and Website activity to understand the effectiveness of our communications and marketing campaigns.</p>

    <h2>SECTION 3 – HOW WE USE YOUR INFORMATION</h2>
    <h3>3.1 Order Fulfillment and Customer Service</h3>
    <p>To process, fulfill, and deliver your orders; communicate order confirmations, shipping updates, and delivery notifications; respond to your inquiries, complaints, and support requests; process returns, refunds, and exchanges; and send order-related administrative communications.</p>
    <h3>3.2 Marketing and Communications</h3>
    <p>To send promotional emails, discount codes, and newsletters (with your consent); send SMS messages for order updates and marketing (with your express consent where required); personalize advertising across third-party platforms; and conduct Website optimization.</p>
    <h3>3.3 Legal, Safety, and Security</h3>
    <p>To detect, prevent, and investigate fraud, abuse, or security incidents; comply with applicable laws, regulations, and court orders; enforce our Terms of Service and other policies; and protect the rights and safety of users and third parties.</p>

    <h2>SECTION 4 – SHARING YOUR INFORMATION</h2>
    <h3>4.1 Shopify</h3>
    <p>Our Website is hosted on Shopify's ecommerce platform. We share customer and order data with Shopify Inc. as necessary to operate the Website, process payments, manage accounts, and deliver services. Shopify's processing of your personal information is governed by Shopify's Privacy Policy.</p>
    <h3>4.2 Suppliers and Fulfillment Partners</h3>
    <p>We share your order information, including your name, shipping address, email address, and phone number, with the applicable Supplier solely for the purpose of processing and shipping your order. Suppliers are not authorized to use your information for any other purpose.</p>
    <h3>4.3 Payment Processors</h3>
    <p>Payment information is processed by Shopify Payments and third-party payment processors including PayPal and others. These processors receive only the information necessary to complete your transaction and are bound by their own privacy policies and PCI-DSS security standards.</p>
    <h3>4.4 Analytics and Advertising Providers</h3>
    <p>We use Google Analytics to analyze Website traffic and user behavior. We also share data with advertising platforms including Meta Platforms Inc. (Facebook/Instagram), TikTok, Pinterest, and Google Ads for targeted advertising purposes.</p>
    <h3>4.5 Legal Disclosures</h3>
    <p>We may disclose your personal information if required by law, subpoena, court order, or other legal process, or if we believe disclosure is necessary to protect our rights, prevent fraud, protect user safety, or comply with applicable regulations.</p>
    <h3>4.6 We Do Not Sell Your Personal Information</h3>
    <p>PETS CARE USA does not sell, rent, or trade your personal information to third-party data brokers for their independent commercial use. Sharing of data with advertising platforms for retargeting purposes may constitute "sharing" under California law; see Section 7 for your opt-out rights.</p>

    <h2>SECTION 5 – DATA SECURITY</h2>
    <h3>5.1 Security Measures</h3>
    <p>We implement commercially reasonable technical, organizational, and administrative security measures designed to protect your personal information against unauthorized access, disclosure, alteration, and destruction. These measures include SSL/TLS encryption for data in transit, access controls, and Shopify's PCI-DSS compliant infrastructure.</p>
    <h3>5.2 No Absolute Security Guarantee</h3>
    <p>No method of data transmission or electronic storage is completely secure. While we take reasonable precautions to protect your data, we cannot guarantee absolute security. In the event of a data breach affecting your rights, we will notify you as required by applicable law.</p>

    <h2>SECTION 6 – DATA RETENTION</h2>
    <p>We retain personal information for as long as necessary to fulfill the purposes described in this Policy, to comply with applicable legal obligations, resolve disputes, and enforce our agreements. Order and transaction data is generally retained for a minimum of seven (7) years for tax, legal, and accounting compliance. Account data is retained for the duration of your account and for a reasonable period thereafter.</p>

    <h2>SECTION 7 – YOUR U.S. STATE PRIVACY RIGHTS</h2>
    <h3>7.1 California Residents – CCPA and CPRA</h3>
    <p>California residents have the following rights under the California Consumer Privacy Act (CCPA) and the California Privacy Rights Act (CPRA):</p>
    <ul>
      <li><strong>Right to Know:</strong> You may request that we disclose what personal information we have collected about you, the categories of sources, the business purpose, and the third parties we share it with.</li>
      <li><strong>Right to Delete:</strong> You may request deletion of personal information we have collected, subject to exceptions.</li>
      <li><strong>Right to Correct:</strong> You may request correction of inaccurate personal information we hold about you.</li>
      <li><strong>Right to Opt-Out of Sale/Sharing:</strong> You may opt out of the sale or sharing of your personal information for cross-context behavioral advertising purposes. Email support@petscareusa.com with subject "Do Not Sell or Share My Data."</li>
      <li><strong>Right to Non-Discrimination:</strong> We will not discriminate against you for exercising your privacy rights.</li>
    </ul>
    <h3>7.2 Virginia Residents – VCDPA</h3>
    <p>Virginia residents have rights under the Virginia Consumer Data Protection Act (VCDPA) including the right to access, correct, delete, obtain a copy of, and opt out of processing of personal data for targeted advertising, profiling, and sale. Contact us at support@petscareusa.com.</p>
    <h3>7.3 Colorado Residents – CPA</h3>
    <p>Colorado residents have rights under the Colorado Privacy Act (CPA) including the right to access, correct, delete, and obtain a portable copy of personal data, and to opt out of processing for targeted advertising, sale, or profiling. Contact us at support@petscareusa.com.</p>
    <h3>7.4 Connecticut Residents – CTDPA</h3>
    <p>Connecticut residents have rights under the Connecticut Data Privacy Act (CTDPA) including the right to access, correct, delete, obtain a copy, and opt out of sale and targeted advertising. Contact us at support@petscareusa.com.</p>
    <h3>7.5 Utah Residents – UCPA</h3>
    <p>Utah residents have rights under the Utah Consumer Privacy Act (UCPA) including the right to access, delete, and obtain a portable copy of personal data, and to opt out of sale and targeted advertising. Contact us at support@petscareusa.com.</p>
    <h3>7.6 Texas Residents – TDPSA</h3>
    <p>Texas residents have rights under the Texas Data Privacy and Security Act (TDPSA) including the right to access, correct, delete, and obtain a copy of personal data, and to opt out of sale and targeted advertising. Contact us at support@petscareusa.com.</p>
    <h3>7.7 Submitting Privacy Requests</h3>
    <p>To submit any privacy rights request, email support@petscareusa.com with subject "Privacy Rights Request," your full name, email address on file, state of residence, and the specific right you wish to exercise. We will respond within the timeframe required by applicable law.</p>

    <h2>SECTION 8 – EMAIL AND SMS COMMUNICATIONS</h2>
    <h3>8.1 Transactional Communications</h3>
    <p>We send transactional emails and SMS messages related to your orders, account security, and customer service. These are necessary for service delivery and cannot be opted out of without closing your account.</p>
    <h3>8.2 Marketing Communications</h3>
    <p>With your consent, we send promotional emails about products, discounts, and events. You may unsubscribe at any time by clicking the "Unsubscribe" link in any marketing email or by emailing support@petscareusa.com. SMS marketing requires express written consent; opt out by replying STOP to any marketing SMS.</p>

    <h2>SECTION 9 – CHILDREN'S PRIVACY</h2>
    <p>The Website is not directed to children under the age of thirteen (13). We do not knowingly collect personal information from children under 13. If we become aware that we have inadvertently collected information from a child under 13, we will promptly delete such information. Parents or guardians who believe we have collected information from a child should contact us immediately at support@petscareusa.com.</p>

    <h2>SECTION 10 – CHANGES TO THIS POLICY</h2>
    <p>We may update this Privacy Policy at any time. We will notify you of material changes by posting the updated Policy on the Website with a revised "Last Updated" date. Your continued use of the Website after any such changes constitutes acceptance of the updated Policy.</p>

    <h2>SECTION 11 – CONTACT</h2>
    <p>PETS CARE USA – Privacy | Email: support@petscareusa.com | Website: petscareusa.com</p>
  </div>
</div>"""

# ─── VOLUME 3: SHIPPING & RETURNS ────────────────────────────────────────────
shipping = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center;margin-bottom:40px;">SHIPPING &amp; RETURNS POLICY</h1>
  <div class="page-content policy-content">
    <p><strong>PETS CARE USA</strong> | Website: petscareusa.com | Effective Date: July 14, 2026 | Last Updated: July 14, 2026</p>
    <p>This Shipping and Returns Policy ("Policy") governs all matters related to the fulfillment, delivery, return, and refund of Products purchased through petscareusa.com. This Policy is incorporated into and forms part of our Terms of Service. Capitalized terms used herein but not defined have the meanings given in the Terms of Service.</p>

    <h2>PART I – SHIPPING POLICY</h2>
    <h3>1.1 Supplier Fulfillment Model</h3>
    <p>PETS CARE USA does not maintain physical inventory, operate warehouses, or ship Products directly. All Products listed on the Website are stored, packaged, and shipped directly by independent third-party Suppliers. By placing an Order, you acknowledge that your shipment will originate from a Supplier's facility and not from PETS CARE USA.</p>
    <h3>1.2 Order Processing Times</h3>
    <p>Order processing times are determined by the applicable Supplier and generally range from one (1) to five (5) business days from the date of order confirmation, excluding weekends and public holidays. Processing times may be extended during peak seasons, promotional events, or periods of high demand. PETS CARE USA has no control over and makes no guarantees regarding Supplier processing times.</p>
    <h3>1.3 Estimated Delivery Timeframes</h3>
    <p>Estimated delivery timeframes for domestic U.S. shipments generally range from three (3) to fifteen (15) business days following Supplier processing, depending on the Supplier's location, the selected shipping method, and the Customer's delivery address. All delivery estimates are approximate and are not guaranteed. PETS CARE USA shall not be held responsible for delivery delays.</p>
    <h3>1.4 Shipping Methods and Carriers</h3>
    <p>Shipping carriers and methods are selected by the applicable Supplier. Common carriers include USPS, UPS, FedEx, DHL, and regional courier services. PETS CARE USA does not control carrier selection and is not responsible for carrier-imposed delays, route changes, or service disruptions.</p>
    <h3>1.5 Split Shipments</h3>
    <p>If your Order includes Products from multiple Suppliers, your Order may be shipped in separate packages from different warehouse locations. Individual packages may arrive at different times. You will receive tracking information for each shipment separately.</p>
    <h3>1.6 Tracking Information</h3>
    <p>Tracking numbers are provided by Suppliers and transmitted to Customers via email when shipments are dispatched. Tracking information may not be immediately active in the carrier's system upon initial notification. PETS CARE USA provides tracking information on a best-efforts basis and is not responsible for inaccuracies in carrier tracking data.</p>
    <h3>1.7 Domestic Shipping Coverage</h3>
    <p>PETS CARE USA currently accepts orders for delivery to addresses within the contiguous United States. Availability of shipping to Alaska, Hawaii, U.S. territories (including Puerto Rico, Guam, and the U.S. Virgin Islands), APO, FPO, and DPO addresses depends on Supplier capabilities and is not universally guaranteed.</p>
    <h3>1.8 Customer Address Responsibility</h3>
    <p>Customers are solely responsible for providing a complete, accurate, and deliverable shipping address at checkout. PETS CARE USA and Suppliers are not liable for failed deliveries, returned packages, or additional shipping costs resulting from an incorrect or incomplete address provided by the Customer.</p>
    <h3>1.9 Shipping Delays</h3>
    <p>Shipping delays may occur due to Supplier processing delays, carrier disruptions, weather events, natural disasters, holidays, customs delays, labor strikes, regulatory holds, pandemic-related disruptions, or other circumstances beyond the control of PETS CARE USA or its Suppliers. PETS CARE USA shall not be liable for any loss, cost, damage, or inconvenience arising from shipping delays.</p>
    <h3>1.10 Carrier Liability</h3>
    <p>Once a Supplier delivers a package to the designated carrier, responsibility for the shipment transfers to the carrier. PETS CARE USA is not responsible for packages lost, damaged, or delayed while in carrier custody. Claims for carrier-caused damage or loss must be filed directly with the applicable shipping carrier.</p>
    <h3>1.11 Lost Packages</h3>
    <p>If your tracking information indicates that a package has been delivered but you have not received it, you must: (a) wait twenty-four (24) to forty-eight (48) hours, as carriers sometimes mark packages as delivered before physical delivery; (b) check all accessible delivery locations including porches, mailrooms, and neighbors; (c) contact the carrier directly to initiate a trace investigation; and (d) contact PETS CARE USA at support@petscareusa.com within five (5) business days of the indicated delivery date. PETS CARE USA will make commercially reasonable efforts to assist with carrier investigations but is not liable for packages confirmed as delivered by the carrier.</p>
    <h3>1.12 Stolen Packages</h3>
    <p>PETS CARE USA is not responsible for packages that are stolen after successful delivery to the confirmed address. Customers are encouraged to use a secure delivery location or request signature confirmation. If you believe a package was stolen, you should file a report with your local law enforcement agency.</p>
    <h3>1.13 Free Shipping Threshold</h3>
    <p>Free standard shipping may be available on qualifying orders meeting the minimum purchase threshold displayed on the Website. Free shipping is available on eligible Products only, excludes certain oversized or heavy items, and applies to domestic U.S. addresses only. Free shipping thresholds and eligibility are subject to change without notice.</p>

    <h2>PART II – RETURNS AND REFUNDS POLICY</h2>
    <h3>2.1 Returns Overview</h3>
    <p>Because all Products are fulfilled by independent Suppliers, returns are subject to the return policies of the applicable Supplier in addition to this Policy. PETS CARE USA coordinates return requests on behalf of Customers and Suppliers but does not operate a centralized returns warehouse.</p>
    <h3>2.2 Return Eligibility Window</h3>
    <p>Customers may submit a return request within thirty (30) days of the confirmed delivery date of their Order. Return requests submitted after this period may not be accepted. All return requests must be submitted through our customer support at support@petscareusa.com.</p>
    <h3>2.3 Eligible Return Conditions</h3>
    <p>To be eligible for a return and refund, Products must: be unused, unopened, and in their original packaging and condition; include all original accessories, tags, inserts, and documentation; not show signs of use, pet hair, damage, or alteration; and be accompanied by proof of purchase (order confirmation or order number).</p>
    <h3>2.4 Non-Returnable and Non-Refundable Items</h3>
    <p>The following categories of Products are not eligible for return or refund under any circumstances, except where required by applicable law: opened or used pet food, treats, chews, or edible products; opened dietary supplements, vitamins, probiotics, or health products; opened grooming products, shampoos, conditioners, or topical treatments; perishable or temperature-sensitive products; personalized, customized, or monogrammed products; digital products, gift cards, or promotional codes; products marked as "Final Sale" or "Non-Returnable" at time of purchase; and products that show signs of use, modification, or damage not caused by the Supplier.</p>
    <h3>2.5 Return Merchandise Authorization (RMA)</h3>
    <p>CUSTOMERS MUST OBTAIN A RETURN MERCHANDISE AUTHORIZATION ("RMA") BEFORE RETURNING ANY PRODUCT. DO NOT RETURN ANY PRODUCT TO THE SENDER ADDRESS APPEARING ON THE PACKAGE, AS THIS MAY NOT BE THE DESIGNATED RETURN ADDRESS AND PACKAGES RETURNED WITHOUT AN RMA WILL BE REJECTED AND CANNOT BE PROCESSED.</p>
    <p>To initiate a return: (1) Email support@petscareusa.com with your order number and reason for return; (2) Await confirmation and receipt of your RMA number and designated return address; (3) Ship the Product using a trackable shipping method; (4) Email your tracking number to support@petscareusa.com.</p>
    <h3>2.6 Damaged or Defective Products</h3>
    <p>If you receive a Product that is damaged in transit or is defective upon arrival, you must contact support@petscareusa.com within five (5) business days of delivery, providing your order number, a detailed written description of the damage or defect, and clear photographs or video evidence. We will work with the applicable Supplier to arrange a replacement or refund at no additional cost to you.</p>
    <h3>2.7 Wrong Item Received</h3>
    <p>If you receive an item different from what you ordered, contact support@petscareusa.com within five (5) business days of delivery with your order number and photographic evidence. We will coordinate with the Supplier to resolve the issue through a replacement or refund.</p>
    <h3>2.8 Return Shipping Responsibility</h3>
    <p>Unless the return is a result of a Supplier error, damaged item, or defective product, the Customer is responsible for all return shipping costs. PETS CARE USA and Suppliers are not responsible for return packages lost, damaged, or delayed in transit. Customers are encouraged to use a trackable shipping method and retain proof of shipment.</p>
    <h3>2.9 Refund Processing</h3>
    <p>Refunds are issued to the original payment method used for the purchase. Refund processing begins after the returned Product has been received, inspected, and approved by the applicable Supplier. Please allow two (2) to seven (7) business days for Supplier inspection upon receipt of the return, plus an additional three (3) to ten (10) business days for the refund to appear on your statement. Original shipping fees are non-refundable unless the return is due to a Supplier error or defective product.</p>
    <h3>2.10 Chargebacks</h3>
    <p>Filing a chargeback with your payment provider before contacting PETS CARE USA and allowing a reasonable resolution period is a violation of this Policy and may constitute fraud. We reserve the right to dispute any chargeback filed for a valid, delivered order and to suspend accounts that engage in chargeback abuse.</p>
    <h3>2.11 Inspection Upon Delivery</h3>
    <p>Customers are responsible for inspecting all delivered Products promptly upon receipt. Failure to report damage, defects, or incorrect items within the timeframes specified in this Policy may result in ineligibility for a return, replacement, or refund.</p>

    <h2>PART III – CONTACT</h2>
    <p>PETS CARE USA – Support | Email: support@petscareusa.com | Website: petscareusa.com</p>
  </div>
</div>"""

# ─── VOLUME 4: LEGAL PROTECTION ──────────────────────────────────────────────
legal = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center;margin-bottom:40px;">LEGAL PROTECTION POLICY</h1>
  <div class="page-content policy-content">
    <p><strong>PETS CARE USA</strong> | Website: petscareusa.com | Effective Date: July 14, 2026 | Last Updated: July 14, 2026</p>
    <p>This Legal Protection Policy ("Policy") sets forth the comprehensive legal framework governing the rights, remedies, liabilities, and protections applicable to PETS CARE USA and all persons who use the Website or purchase Products through it. This Policy supplements and is incorporated into the Terms of Service.</p>

    <h2>SECTION 1 – DISCLAIMER OF WARRANTIES</h2>
    <h3>1.1 "As Is" and "As Available" Provision</h3>
    <p>THE WEBSITE, AND ALL PRODUCTS AND SERVICES MADE AVAILABLE THROUGH THE WEBSITE, ARE PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS WITHOUT REPRESENTATION OR WARRANTY OF ANY KIND, EXPRESS, IMPLIED, OR STATUTORY. PETS CARE USA, TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, EXPRESSLY DISCLAIMS ALL WARRANTIES OF ANY KIND, INCLUDING BUT NOT LIMITED TO: the implied warranty of merchantability; the implied warranty of fitness for a particular purpose; warranties of non-infringement, title, or quiet enjoyment; warranties of accuracy, completeness, timeliness, or reliability; warranties arising from course of dealing, course of performance, or trade usage; warranties that the Website will be uninterrupted or error-free; and warranties regarding any third-party products, services, or information accessed through the Website.</p>
    <h3>1.2 No Independent Product Warranties</h3>
    <p>PETS CARE USA PROVIDES NO INDEPENDENT WARRANTY FOR ANY PRODUCT SOLD THROUGH THE WEBSITE. PRODUCTS ARE WARRANTED, IF AT ALL, SOLELY BY THEIR RESPECTIVE MANUFACTURERS. PETS CARE USA IS NOT A PARTY TO ANY MANUFACTURER WARRANTY AND ASSUMES NO OBLIGATIONS THEREUNDER.</p>

    <h2>SECTION 2 – MARKETPLACE DISCLAIMER</h2>
    <h3>2.1 Sole Role as Marketplace</h3>
    <p>PETS CARE USA ACTS SOLELY AND EXCLUSIVELY AS AN INDEPENDENT ONLINE ECOMMERCE MARKETPLACE AND SALES INTERMEDIARY. THE COMPANY DOES NOT MANUFACTURE, FORMULATE, DESIGN, DEVELOP, INSPECT, CERTIFY, INDEPENDENTLY TEST, WAREHOUSE, PACKAGE, RELABEL, MODIFY, INSTALL, REPAIR, ENDORSE, RECOMMEND, OR GUARANTEE ANY PRODUCTS SOLD THROUGH THE WEBSITE.</p>
    <h3>2.2 Exclusive Supplier Responsibility</h3>
    <p>ALL RESPONSIBILITY FOR THE FOLLOWING RESTS EXCLUSIVELY WITH THE APPLICABLE MANUFACTURER OR SUPPLIER, AND NOT WITH PETS CARE USA: manufacturing, production, and assembly; ingredient sourcing, formulation, and composition; labeling accuracy and completeness; packaging integrity and child-safety compliance; quality control, testing, and inspection; regulatory compliance including FDA, AAFCO, USDA, FTC, EPA, and CPSC standards; safety certifications and product approvals; product recalls, safety notices, and corrective actions; express and implied product warranties; instructions for safe use and adequate warnings; country of origin disclosure accuracy; nutritional completeness and accuracy of nutritional claims; and veterinary claim accuracy and substantiation.</p>

    <h2>SECTION 3 – PRODUCT LIABILITY DISCLAIMER</h2>
    <h3>3.1 No Product Liability for Marketplace</h3>
    <p>AS AN INDEPENDENT ECOMMERCE MARKETPLACE THAT DOES NOT MANUFACTURE, MODIFY, INSPECT, OR PHYSICALLY HANDLE PRODUCTS, PETS CARE USA DISCLAIMS ALL PRODUCT LIABILITY, TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, FOR CLAIMS ARISING FROM OR RELATED TO: manufacturing defects in materials or workmanship; design defects in product conception or engineering; defective warnings or labeling failures; contaminated, adulterated, or mislabeled products; undisclosed ingredient changes by Suppliers; packaging failures or seal defects; or failure to comply with applicable safety regulations by Suppliers.</p>
    <h3>3.2 Product Liability Claims Directed to Suppliers</h3>
    <p>All product liability claims arising from or related to manufacturing defects, design defects, labeling failures, or regulatory non-compliance should properly be directed to the manufacturer or Supplier of the affected Product. PETS CARE USA will, upon request, provide available information to identify the applicable Supplier to assist in directing claims appropriately.</p>

    <h2>SECTION 4 – ASSUMPTION OF RISK</h2>
    <h3>4.1 Voluntary Assumption of All Known and Unknown Risks</h3>
    <p>BY PURCHASING ANY PRODUCT THROUGH THE WEBSITE, THE CUSTOMER VOLUNTARILY ASSUMES ALL RISKS, KNOWN AND UNKNOWN, ASSOCIATED WITH: the suitability of the Product for their specific pet; potential allergic reactions, sensitivities, or adverse responses; injury, illness, or death of the animal resulting from product use; misuse, overuse, or improper administration of the Product; use of the Product contrary to manufacturer instructions or warnings; introduction of the Product without prior veterinary consultation; storage or handling of the Product in conditions not recommended by the manufacturer; and interaction of the Product with other foods, medications, supplements, or environmental factors.</p>

    <h2>SECTION 5 – VETERINARY DISCLAIMER</h2>
    <h3>5.1 No Veterinary or Medical Advice</h3>
    <p>NOTHING ON THE WEBSITE CONSTITUTES VETERINARY ADVICE, MEDICAL ADVICE, DIAGNOSIS, TREATMENT, PRESCRIPTION, BEHAVIORAL GUIDANCE, NUTRITIONAL COUNSEL, OR ANY OTHER FORM OF PROFESSIONAL CONSULTATION. ALL WEBSITE CONTENT IS PROVIDED FOR INFORMATIONAL PURPOSES ONLY AND DOES NOT SUBSTITUTE FOR PROFESSIONAL VETERINARY EXAMINATION OR GUIDANCE.</p>
    <h3>5.2 Mandatory Veterinary Consultation</h3>
    <p>CUSTOMERS ARE EXPRESSLY ADVISED TO CONSULT A LICENSED VETERINARIAN BEFORE USING ANY PRODUCT THAT MAY AFFECT THE HEALTH, DIET, BEHAVIOR, OR WELLBEING OF THEIR ANIMAL, INCLUDING BUT NOT LIMITED TO DIETARY SUPPLEMENTS, VITAMINS, PROBIOTICS, HERBAL PRODUCTS, TOPICAL TREATMENTS, CALMING PRODUCTS, JOINT SUPPORT PRODUCTS, AND ANY PRODUCT MAKING HEALTH-RELATED CLAIMS.</p>
    <h3>5.3 Emergency Situations</h3>
    <p>If your animal is experiencing a medical emergency, suspected poisoning, allergic reaction, or acute illness, immediately contact a licensed emergency veterinarian or the ASPCA Animal Poison Control Center at (888) 426-4435. Do not delay professional veterinary care in reliance on any Website content.</p>

    <h2>SECTION 6 – LIMITATION OF LIABILITY</h2>
    <h3>6.1 Exclusion of All Indirect Damages</h3>
    <p>TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, PETS CARE USA, ITS OFFICERS, DIRECTORS, EMPLOYEES, AGENTS, CONTRACTORS, AFFILIATES, SUPPLIERS, AND LICENSORS SHALL NOT BE LIABLE TO ANY PARTY FOR ANY: indirect, incidental, or consequential damages; special, punitive, or exemplary damages; loss of profits, revenue, savings, or business opportunities; loss or corruption of data or systems; business interruption of any kind; reputational harm or loss of goodwill; emotional distress, psychological suffering, or mental anguish; pet injury, illness, or death; property damage caused by Products; costs of procurement of substitute products or services; claims arising from shipping delays or lost packages; or claims arising from Supplier errors, deficiencies, or failures.</p>
    <h3>6.2 Cap on Aggregate Liability</h3>
    <p>IN ALL CASES, PETS CARE USA'S TOTAL CUMULATIVE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT, THE WEBSITE, OR ANY PRODUCT PURCHASED HEREUNDER SHALL NOT EXCEED THE LESSER OF: (A) THE TOTAL AMOUNT PAID BY THE CUSTOMER FOR THE SPECIFIC ORDER GIVING RISE TO THE CLAIM; OR (B) ONE HUNDRED DOLLARS ($100.00). THIS CAP APPLIES REGARDLESS OF THE LEGAL THEORY UNDER WHICH THE CLAIM IS ASSERTED.</p>

    <h2>SECTION 7 – INDEMNIFICATION</h2>
    <p>You shall indemnify, defend (at PETS CARE USA's election), and hold harmless PETS CARE USA and its officers, directors, employees, agents, contractors, Suppliers, affiliates, licensors, successors, and assigns from and against any and all third-party claims, demands, causes of action, suits, proceedings, judgments, liabilities, losses, damages, penalties, fines, costs, and expenses (including reasonable attorneys' fees and court costs) arising out of or relating to: your breach of any provision of this Agreement; your violation of any applicable law, regulation, or third-party right; your misuse of any Product purchased through the Website; your negligence or willful misconduct; your failure to obtain veterinary advice regarding Product suitability; any injury to person or animal caused by Products you purchased; any User Content you submit to the Website; or your infringement of any intellectual property rights.</p>

    <h2>SECTION 8 – DISPUTE RESOLUTION AND ARBITRATION</h2>
    <h3>8.1 Mandatory Informal Resolution</h3>
    <p>Before initiating any formal dispute resolution, you agree to first contact PETS CARE USA at support@petscareusa.com with a written description of your dispute, the relief you seek, and your contact information. You agree to engage in good-faith efforts to resolve the dispute informally for a period of thirty (30) days.</p>
    <h3>8.2 Mandatory Binding Arbitration</h3>
    <p>IF THE DISPUTE CANNOT BE RESOLVED INFORMALLY, ANY DISPUTE, CLAIM, OR CONTROVERSY ARISING OUT OF OR RELATING TO THIS AGREEMENT, YOUR USE OF THE WEBSITE, OR ANY PRODUCT PURCHASED THROUGH THE WEBSITE, SHALL BE RESOLVED EXCLUSIVELY THROUGH FINAL AND BINDING INDIVIDUAL ARBITRATION ADMINISTERED BY THE AMERICAN ARBITRATION ASSOCIATION ("AAA") PURSUANT TO ITS CONSUMER ARBITRATION RULES.</p>
    <h3>8.3 Class Action Waiver</h3>
    <p>YOU AND PETS CARE USA EACH AGREE THAT ALL DISPUTES SHALL BE RESOLVED IN AN INDIVIDUAL CAPACITY ONLY AND NOT AS A CLASS ACTION, COLLECTIVE ACTION, CONSOLIDATED ACTION, PRIVATE ATTORNEY GENERAL ACTION, OR REPRESENTATIVE PROCEEDING. YOU EXPRESSLY WAIVE YOUR RIGHT TO PARTICIPATE IN OR RECEIVE RELIEF FROM ANY COLLECTIVE OR CLASS ACTION PROCEEDING.</p>
    <h3>8.4 Jury Trial Waiver</h3>
    <p>TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, BOTH YOU AND PETS CARE USA KNOWINGLY, VOLUNTARILY, AND IRREVOCABLY WAIVE ANY CONSTITUTIONAL OR STATUTORY RIGHT TO A TRIAL BY JURY IN ANY ACTION, PROCEEDING, OR COUNTERCLAIM ARISING OUT OF OR RELATING TO THIS AGREEMENT OR THE USE OF THE WEBSITE OR PRODUCTS.</p>
    <h3>8.5 Limitation Period for Claims</h3>
    <p>ANY CLAIM OR CAUSE OF ACTION ARISING OUT OF OR RELATED TO THIS AGREEMENT MUST BE FILED WITHIN ONE (1) YEAR OF THE DATE ON WHICH SUCH CLAIM ACCRUED, TO THE EXTENT PERMITTED BY APPLICABLE LAW. CLAIMS NOT FILED WITHIN THIS PERIOD SHALL BE FOREVER BARRED.</p>

    <h2>SECTION 9 – GOVERNING LAW</h2>
    <p>This Agreement shall be governed by and construed in accordance with the laws of the United States and the State of Delaware, without regard to conflicts of law principles. For claims not subject to arbitration, you consent to personal jurisdiction and venue in the state and federal courts located within Delaware.</p>

    <h2>SECTION 10 – FORCE MAJEURE</h2>
    <p>PETS CARE USA shall not be liable for any failure or delay in performance of its obligations under this Agreement caused by events beyond its reasonable control, including acts of God, natural disasters, pandemics, government actions, wars, terrorism, civil unrest, cyberattacks, power failures, internet outages, Supplier failures, or carrier disruptions.</p>

    <h2>SECTION 11 – ELECTRONIC EVIDENCE</h2>
    <p>You agree that electronic records, including emails, chat logs, order records, and system logs maintained by PETS CARE USA, shall be admissible as evidence in any dispute resolution proceeding to the same extent and under the same conditions as original documents.</p>

    <h2>SECTION 12 – SURVIVAL AND WAIVER</h2>
    <p>All provisions of this Policy which by their nature should survive termination — including warranty disclaimers, product liability disclaimers, limitation of liability, indemnification, arbitration, and governing law — shall survive any termination or expiration of the Agreement. No failure or delay by PETS CARE USA in enforcing any right or provision shall constitute a waiver of that right or provision.</p>

    <h2>SECTION 13 – CONTACT</h2>
    <p>PETS CARE USA – Legal | Email: support@petscareusa.com | Website: petscareusa.com</p>
  </div>
</div>"""

# ─── VOLUME 5: COMPLIANCE ────────────────────────────────────────────────────
compliance = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center;margin-bottom:40px;">COMPLIANCE POLICY</h1>
  <div class="page-content policy-content">
    <p><strong>PETS CARE USA</strong> | Website: petscareusa.com | Effective Date: July 14, 2026 | Last Updated: July 14, 2026</p>
    <p>This Compliance Policy ("Policy") describes PETS CARE USA's practices and commitments regarding legal and regulatory compliance matters, including intellectual property, accessibility, email and SMS communications, consumer protection, and privacy. This Policy is incorporated into and made part of the Terms of Service.</p>

    <h2>SECTION 1 – DMCA COPYRIGHT POLICY</h2>
    <h3>1.1 Respect for Intellectual Property</h3>
    <p>PETS CARE USA respects the intellectual property rights of others and expects all users, Suppliers, and third parties to do the same. We comply with the Digital Millennium Copyright Act (17 U.S.C. § 512) ("DMCA") and respond to properly submitted notices of claimed copyright infringement.</p>
    <h3>1.2 Filing a DMCA Notice</h3>
    <p>If you believe that any content on the Website infringes your copyright, you must submit a written DMCA takedown notice to our designated copyright agent containing all of the following: (a) a physical or electronic signature of the copyright owner or an authorized agent; (b) identification of the copyrighted work claimed to have been infringed; (c) identification of the infringing material and its specific URL or location on the Website; (d) your name, mailing address, telephone number, and email address; (e) a statement that you have a good faith belief that the use is not authorized by the copyright owner, its agent, or the law; and (f) a statement, made under penalty of perjury, that the information is accurate and that you are the copyright owner or authorized to act on their behalf. Submit DMCA notices to: support@petscareusa.com, Subject: DMCA Takedown Notice.</p>
    <h3>1.3 Counter-Notification</h3>
    <p>If you believe your content was removed in error, you may submit a counter-notification containing: (a) your electronic signature; (b) identification of the removed content and its prior location; (c) a statement under penalty of perjury that the content was removed by mistake or misidentification; and (d) your name, address, telephone number, email, and consent to jurisdiction. Submit counter-notifications to: support@petscareusa.com.</p>
    <h3>1.4 Repeat Infringer Policy</h3>
    <p>PETS CARE USA reserves the right to terminate accounts of users who are repeat infringers of intellectual property rights.</p>

    <h2>SECTION 2 – WEBSITE ACCESSIBILITY (ADA COMPLIANCE)</h2>
    <h3>2.1 Accessibility Commitment</h3>
    <p>PETS CARE USA is committed to making the Website accessible to individuals with disabilities. We strive to align the Website with the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards published by the World Wide Web Consortium (W3C).</p>
    <h3>2.2 Reporting Accessibility Issues</h3>
    <p>If you encounter accessibility barriers on the Website or require the content in an alternative format, please contact support@petscareusa.com. We will make reasonable efforts to provide accessible alternatives in a timely manner.</p>

    <h2>SECTION 3 – COOKIES AND TRACKING</h2>
    <p>PETS CARE USA uses cookies and similar tracking technologies to operate the Website, personalize content, analyze traffic, and deliver targeted advertising. By using the Website, you consent to our use of cookies as described in our Privacy Policy. Third-party partners including Google, Meta, TikTok, and Pinterest may place their own tracking technologies on the Website. You may manage your cookie preferences through your browser settings. However, disabling certain cookies may impair Website functionality.</p>

    <h2>SECTION 4 – EMAIL MARKETING COMPLIANCE</h2>
    <h3>4.1 CAN-SPAM Act Compliance</h3>
    <p>All commercial email communications sent by PETS CARE USA comply with the Controlling the Assault of Non-Solicited Pornography And Marketing Act of 2003 (CAN-SPAM Act), 15 U.S.C. § 7701, et seq. Our commercial emails include: a valid physical postal address; a clear and honest subject line; clear identification of the message as an advertisement; and a functional and clearly visible opt-out mechanism.</p>
    <h3>4.2 Opt-Out and Unsubscribe</h3>
    <p>You may opt out of promotional email communications at any time by clicking the "Unsubscribe" link in any marketing email or by contacting support@petscareusa.com. We process all unsubscribe requests within ten (10) business days as required by the CAN-SPAM Act. Transactional and operational emails related to your Orders and account cannot be suppressed without closing your account.</p>

    <h2>SECTION 5 – SMS MARKETING COMPLIANCE</h2>
    <h3>5.1 TCPA Compliance</h3>
    <p>Our SMS marketing communications comply with the Telephone Consumer Protection Act (TCPA), 47 U.S.C. § 227. We obtain prior express written consent before sending promotional SMS messages to Customers. Consent is not a condition of purchase.</p>
    <h3>5.2 SMS Opt-Out</h3>
    <p>You may opt out of SMS marketing communications at any time by replying STOP to any marketing SMS message. You may receive a single confirmation message following your opt-out request. Standard message and data rates may apply depending on your mobile carrier plan.</p>

    <h2>SECTION 6 – PRODUCT REVIEWS POLICY</h2>
    <h3>6.1 FTC Compliance for Reviews</h3>
    <p>PETS CARE USA complies with the Federal Trade Commission (FTC) guidelines regarding endorsements and testimonials (16 C.F.R. Part 255). We do not publish fabricated reviews or artificially manipulate ratings.</p>
    <h3>6.2 Customer-Submitted Reviews</h3>
    <p>We accept and publish genuine reviews submitted by verified purchasers. Reviews are moderated to remove spam, prohibited content, personal information, or content violating our policies. We do not suppress or remove reviews solely because they contain negative feedback.</p>
    <h3>6.3 Incentivized Reviews</h3>
    <p>Where reviews are provided in exchange for free products, discounts, or other incentives, such relationships will be disclosed in accordance with FTC guidelines.</p>

    <h2>SECTION 7 – FTC COMPLIANCE</h2>
    <h3>7.1 General FTC Compliance</h3>
    <p>PETS CARE USA complies with applicable Federal Trade Commission regulations governing advertising, endorsements, disclosures, and marketing practices. All material connections between PETS CARE USA and content creators, influencers, or reviewers are disclosed as required by FTC guidelines.</p>
    <h3>7.2 Advertising Substantiation</h3>
    <p>All advertising claims made by PETS CARE USA about the Website's services are substantiated. Product-specific claims displayed on the Website originate from Suppliers and represent the Suppliers' own advertising claims, which are the sole responsibility of the applicable Supplier.</p>

    <h2>SECTION 8 – CALIFORNIA PROPOSITION 65 NOTICE</h2>
    <p>WARNING: Some products sold through petscareusa.com may contain chemicals known to the State of California to cause cancer, birth defects, or other reproductive harm. Such warnings, if applicable, are provided by the Product manufacturer and are displayed in the product listing when made available by the Supplier. PETS CARE USA does not independently evaluate or certify Proposition 65 compliance for any Product. For more information, visit www.P65Warnings.ca.gov.</p>

    <h2>SECTION 9 – STATE PRIVACY ADDENDUM</h2>
    <p>PETS CARE USA complies with state privacy laws applicable to California (CCPA/CPRA), Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), and Texas (TDPSA). For details on your state-specific privacy rights and how to exercise them, please refer to the Privacy Policy. PETS CARE USA does not sell personal information to third-party data brokers for their independent commercial use.</p>

    <h2>SECTION 10 – SECURITY DISCLOSURE</h2>
    <h3>10.1 Payment Data Security</h3>
    <p>PETS CARE USA does not store full credit card numbers. Payment data is processed through Shopify Payments and third-party payment processors that maintain PCI-DSS Level 1 compliance. SSL/TLS encryption is used for all data transmissions on the Website.</p>
    <h3>10.2 Vulnerability Disclosure</h3>
    <p>If you discover a security vulnerability on the Website, please report it responsibly to support@petscareusa.com. Do not publicly disclose vulnerabilities until we have had a reasonable opportunity to investigate and address them.</p>
    <h3>10.3 Data Breach Notification</h3>
    <p>In the event of a data breach that affects the personal information of Customers, PETS CARE USA will notify affected individuals and applicable regulatory authorities as required by applicable state and federal breach notification laws.</p>

    <h2>SECTION 11 – CONTACT</h2>
    <p>PETS CARE USA – Compliance | Email: support@petscareusa.com | Website: petscareusa.com</p>
  </div>
</div>"""

# ─── VOLUME 6: SUPPLIER TRANSPARENCY ─────────────────────────────────────────
supplier = """<div class="page-policy section container">
  <h1 class="section-title" style="text-align:center;margin-bottom:40px;">SUPPLIER TRANSPARENCY POLICY</h1>
  <div class="page-content policy-content">
    <p><strong>PETS CARE USA</strong> | Website: petscareusa.com | Effective Date: July 14, 2026 | Last Updated: July 14, 2026</p>
    <p>PETS CARE USA is committed to transparency regarding the nature of our business model, the role of independent Suppliers in our operations, and the allocation of responsibilities between PETS CARE USA and third-party manufacturers, suppliers, distributors, and fulfillment partners. This Supplier Transparency Policy ("Policy") is incorporated into the Terms of Service and should be read in conjunction with all other PETS CARE USA policies.</p>

    <h2>SECTION 1 – MARKETPLACE EXPLANATION</h2>
    <h3>1.1 How Our Marketplace Works</h3>
    <p>PETS CARE USA operates as an independent online ecommerce marketplace. We provide a digital retail platform through which independent third-party Suppliers present their products for sale to consumers in the United States. When you place an Order on our Website, that Order is transmitted electronically to the applicable Supplier, who then fulfills the Order by packaging and shipping the Product directly to you.</p>
    <h3>1.2 What PETS CARE USA Does</h3>
    <p>PETS CARE USA's responsibilities are limited to: operating and maintaining the Website as a digital retail storefront; displaying Supplier-provided product information and images; processing and transmitting customer orders to Suppliers; processing and collecting payments from Customers; providing Customer service and support for Order-related inquiries; communicating between Customers and Suppliers regarding issues; and facilitating the returns and refunds process in coordination with Suppliers.</p>
    <h3>1.3 What PETS CARE USA Does Not Do</h3>
    <p>PETS CARE USA expressly does not: manufacture, produce, formulate, or develop any Products; source, procure, or select raw ingredients or components for Products; package, label, or relabel any Products; inspect, test, or quality-control any Products; certify any Products for regulatory compliance; operate warehouses, distribution centers, or fulfillment facilities; ship or physically deliver Products to Customers; or verify the accuracy of Supplier-provided product information unless expressly stated.</p>

    <h2>SECTION 2 – SUPPLIER AND MANUFACTURER RESPONSIBILITIES</h2>
    <h3>2.1 Scope of Supplier Responsibility</h3>
    <p>Independent Suppliers and manufacturers bear sole and exclusive responsibility for all of the following:</p>
    <ul>
      <li><strong>Manufacturing:</strong> Design, production, quality of construction, and workmanship of all Products;</li>
      <li><strong>Formulation and Ingredients:</strong> Ingredient sourcing, composition, and formulation accuracy;</li>
      <li><strong>Labeling:</strong> Accuracy of all information appearing on Product labels, including ingredient lists, nutritional information, weight, country of origin, warnings, and usage instructions;</li>
      <li><strong>Packaging:</strong> Integrity of packaging, tamper-evidence, and compliance with applicable packaging regulations;</li>
      <li><strong>Quality Control:</strong> Internal testing, batch consistency, and quality assurance programs;</li>
      <li><strong>Regulatory Compliance:</strong> Compliance with all applicable federal and state regulations including FDA, AAFCO, FTC, and CPSC;</li>
      <li><strong>Certifications:</strong> Obtaining, maintaining, and accurately representing product certifications;</li>
      <li><strong>Product Safety:</strong> Ensuring Products do not present unreasonable risks to consumers or animals;</li>
      <li><strong>Recalls:</strong> Initiating, administering, and funding product recalls;</li>
      <li><strong>Warranties:</strong> Honoring any express warranties offered by the manufacturer;</li>
      <li><strong>Fulfillment:</strong> Picking, packing, and shipping Products in accordance with Order specifications.</li>
    </ul>

    <h2>SECTION 3 – FULFILLMENT PROCESS</h2>
    <h3>3.1 Order Transmission</h3>
    <p>When you complete checkout on petscareusa.com, your Order details are automatically transmitted to the applicable Supplier's system for fulfillment. This transmission occurs electronically and without manual intervention by PETS CARE USA staff in most cases.</p>
    <h3>3.2 Supplier Processing</h3>
    <p>Upon receiving your Order, the Supplier independently processes it through their own fulfillment infrastructure. This includes retrieving the Product from their warehouse, packaging it, applying shipping labels, and dispatching the package to a third-party carrier for delivery.</p>
    <h3>3.3 Carrier Handoff</h3>
    <p>Once the Supplier delivers the package to the designated carrier, custody and responsibility for the package transfer to the carrier. PETS CARE USA has no control over the carrier's handling, routing, or delivery of the package.</p>
    <h3>3.4 Multiple Suppliers</h3>
    <p>When an Order includes Products from multiple Suppliers, each Supplier independently fulfills their respective Products. Packages may be shipped from different locations at different times and may arrive separately.</p>

    <h2>SECTION 4 – QUALITY CONTROL DISCLAIMER</h2>
    <h3>4.1 No Independent Quality Control</h3>
    <p>PETS CARE USA does not conduct independent quality control, safety testing, ingredient analysis, or inspection of any Products. We rely entirely on Supplier representations regarding Product quality and safety. Customers should be aware that PETS CARE USA cannot independently validate any quality or safety claims made by Suppliers.</p>
    <h3>4.2 Supplier Quality Representations</h3>
    <p>All quality and safety certifications displayed on the Website are provided by Suppliers and represent the Supplier's own claims. These certifications have not been independently verified, confirmed, or validated by PETS CARE USA.</p>

    <h2>SECTION 5 – PRODUCT INFORMATION DISCLAIMER</h2>
    <h3>5.1 Source of Product Information</h3>
    <p>All product information displayed on the Website — including product descriptions, ingredient lists, nutritional information, images, specifications, dimensions, weight, compatibility information, care instructions, warranty information, and regulatory claims — is provided exclusively by the applicable Supplier or manufacturer. PETS CARE USA republishes this information as provided and does not author, edit, or independently verify such information.</p>
    <h3>5.2 Information Accuracy Not Guaranteed</h3>
    <p>PETS CARE USA DOES NOT WARRANT OR REPRESENT THE ACCURACY, COMPLETENESS, TIMELINESS, RELIABILITY, SAFETY, SUITABILITY, OR LEGALITY OF ANY PRODUCT INFORMATION DISPLAYED ON THE WEBSITE. Supplier-provided information may contain errors, omissions, or outdated content. Customers should not rely solely on Website information when making purchase decisions for Products intended to affect animal health.</p>

    <h2>SECTION 6 – COUNTRY OF ORIGIN</h2>
    <p>Country of origin information displayed in product listings is provided by Suppliers and is not independently verified by PETS CARE USA. Actual country of origin may differ from displayed information due to undisclosed Supplier supply chain changes. PETS CARE USA is not responsible for inaccurate country of origin representations made by Suppliers.</p>

    <h2>SECTION 7 – CERTIFICATIONS AND REGULATORY CLAIMS</h2>
    <p>All certification claims displayed on the Website — including organic, natural, veterinarian-approved, FDA-compliant, AAFCO-compliant, non-GMO, hypoallergenic, and similar designations — originate from Suppliers and are not independently verified by PETS CARE USA. PETS CARE USA does not certify Products for any regulatory standard and makes no independent regulatory compliance representations. Customers should independently verify any regulatory claim that is material to their purchasing decision.</p>

    <h2>SECTION 8 – PRODUCT TESTING</h2>
    <p>PETS CARE USA does not conduct, commission, fund, or independently review laboratory testing of any Products. All references to product testing on the Website originate from Suppliers. The existence or nature of any testing is the sole responsibility of the applicable manufacturer or Supplier. Customers should request third-party test results directly from manufacturers when safety assurances are required.</p>

    <h2>SECTION 9 – FDA DISCLAIMER</h2>
    <p>PRODUCTS SOLD THROUGH PETSCAREUSA.COM HAVE NOT BEEN EVALUATED BY THE UNITED STATES FOOD AND DRUG ADMINISTRATION (FDA) UNLESS EXPRESSLY STATED IN THE PRODUCT LISTING. PRODUCTS ARE NOT INTENDED TO DIAGNOSE, TREAT, CURE, OR PREVENT ANY DISEASE OR VETERINARY CONDITION. ALL HEALTH-RELATED CLAIMS ASSOCIATED WITH PRODUCTS ARE MADE BY THE APPLICABLE MANUFACTURER AND ARE BASED ON THE MANUFACTURER'S OWN RESEARCH, EXPERIENCE, OR CERTIFICATIONS. PETS CARE USA DOES NOT ADOPT, ENDORSE, OR INDEPENDENTLY SUBSTANTIATE SUCH CLAIMS.</p>

    <h2>SECTION 10 – VETERINARY DISCLAIMER</h2>
    <p>NOTHING ON THIS WEBSITE SHOULD BE CONSTRUED AS VETERINARY ADVICE, DIAGNOSIS, TREATMENT, PRESCRIPTION, OR PROFESSIONAL CONSULTATION OF ANY KIND. PRODUCT INFORMATION IS PROVIDED BY MANUFACTURERS AND IS FOR INFORMATIONAL PURPOSES ONLY. CUSTOMERS SHOULD CONSULT A LICENSED VETERINARIAN BEFORE USING ANY PRODUCT INTENDED TO AFFECT THE HEALTH, DIET, OR WELLBEING OF THEIR ANIMAL. IN CASE OF EMERGENCY, CONTACT THE ASPCA ANIMAL POISON CONTROL CENTER AT (888) 426-4435 OR YOUR LOCAL EMERGENCY VETERINARIAN IMMEDIATELY.</p>

    <h2>SECTION 11 – RECALL PROCEDURES</h2>
    <h3>11.1 Supplier Recall Responsibility</h3>
    <p>Product recalls are the exclusive responsibility of the applicable manufacturer or Supplier. PETS CARE USA does not administer, fund, or initiate recalls and has no independent obligation to do so. In the event a recall is announced by a Supplier or regulatory authority, PETS CARE USA will make commercially reasonable efforts to notify affected Customers who purchased the recalled Product.</p>
    <h3>11.2 Customer Action Upon Recall</h3>
    <p>If you receive notice of a product recall affecting a Product you purchased through the Website, immediately cease using the Product and follow the instructions provided by the manufacturer. Contact the manufacturer directly for recall-related remedies. You may also contact support@petscareusa.com for assistance in identifying the applicable manufacturer.</p>

    <h2>SECTION 12 – CUSTOMER RESPONSIBILITIES</h2>
    <h3>12.1 Pre-Purchase Responsibilities</h3>
    <p>Before purchasing any Product, Customers are responsible for: reading all product information, ingredient lists, and warnings; consulting a licensed veterinarian regarding suitability for their specific animal; assessing their animal's allergies, medical conditions, and medications; and independently verifying any regulatory or safety claim material to their decision.</p>
    <h3>12.2 Inspection Upon Delivery</h3>
    <p>Customers must inspect all delivered Products promptly upon receipt. You are responsible for: verifying that the correct Product was delivered; inspecting packaging for visible damage; checking expiration dates where applicable; and reporting any damage, defect, or discrepancy within five (5) business days of delivery by contacting support@petscareusa.com.</p>
    <h3>12.3 Reporting Defects and Safety Concerns</h3>
    <p>If you discover a Product defect, safety concern, or suspect contamination, you must: immediately cease use of the Product; secure the Product and retain all packaging; contact support@petscareusa.com with a detailed written description and photographs; and seek immediate veterinary care if your animal has been harmed.</p>

    <h2>SECTION 13 – POLICY REVISION LOG</h2>
    <ul>
      <li><strong>July 14, 2026:</strong> Complete restructuring and comprehensive rewrite of all PETS CARE USA legal documents to reflect marketplace-intermediary business model and enterprise-grade liability protection standards.</li>
    </ul>

    <h2>SECTION 14 – CONTACT</h2>
    <p>PETS CARE USA – Supplier Transparency | Email: support@petscareusa.com | Website: petscareusa.com</p>
  </div>
</div>"""

# Write all snippet files
files = {
    "snippets/policy-terms-of-service.liquid": tos,
    "snippets/policy-privacy-policy.liquid": privacy,
    "snippets/policy-shipping-returns.liquid": shipping,
    "snippets/policy-legal-protection.liquid": legal,
    "snippets/policy-compliance.liquid": compliance,
    "snippets/policy-supplier-transparency.liquid": supplier,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path} ({len(content):,} bytes)")

print("\nAll 6 enterprise-grade policy documents generated successfully.")
