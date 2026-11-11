/*
  PORTFOLIO CONTENT
  -----------------
  Everything a visitor reads about you and your work lives in this file.
  To add real work: put the image in assets/work/ (JPG, PNG or WebP, about
  1600px wide) and point `image` at it. Order here is the order on the page.

  category must be one of: identity, logo, cards, print
*/
window.SITE = {
  name: "Muhammad Waseem Akram",
  role: "Graphic designer",
  location: "Pakistan, working worldwide",          // TODO: your city
  email: "hello@waseemakram.com",                   // TODO: your real email
  whatsapp: "+92 300 0000000",                      // TODO: your WhatsApp number
  socials: [                                        // TODO: your real profile links
    { label: "Behance", url: "https://www.behance.net/" },
    { label: "Instagram", url: "https://www.instagram.com/" },
    { label: "LinkedIn", url: "https://www.linkedin.com/" },
    { label: "Dribbble", url: "https://dribbble.com/" }
  ]
};

window.CATEGORIES = {
  identity: "Brand identity",
  logo: "Logo design",
  cards: "Business cards",
  print: "Flyers & print"
};

// Sample projects (fictional brands) — replace with your own.
window.PROJECTS = [
  {
    id: "saffron-and-salt",
    title: "Saffron & Salt",
    client: "Restaurant",
    category: "identity",
    year: 2026,
    image: "assets/work/saffron-and-salt.svg",
    alt: "Brand board for Saffron & Salt with a rising-sun logo, green and saffron palette and type specimen",
    brief: "A family kitchen moving into a bigger space needed an identity that felt warm without looking like every other desi restaurant. The rising sun stands for the morning tandoor and works as small as a menu stamp.",
    deliverables: ["Logo and sun mark", "Colour palette", "Typography", "Menu and signage", "Brand guidelines"]
  },
  {
    id: "kora-coffee",
    title: "Kora Coffee Roasters",
    client: "Coffee roaster",
    category: "logo",
    year: 2026,
    image: "assets/work/kora-coffee.svg",
    alt: "Kora coffee bean logo in cream on dark brown, with construction circles",
    brief: "A small-batch roaster wanted a mark that could be stamped on kraft bags and still read on a phone screen. The bean is drawn on a circle grid so it holds its shape at 16 pixels.",
    deliverables: ["Primary logo", "Stamp version", "Bag label", "Social profile set"]
  },
  {
    id: "northline-cards",
    title: "Northline Architects",
    client: "Architecture studio",
    category: "cards",
    year: 2025,
    image: "assets/work/northline-cards.svg",
    alt: "Two Northline Architects business cards, a dark front with an arch mark and a light back with contact details",
    brief: "Business cards for a three-partner studio. Nested arches echo their first project, printed in two colours on 600 gsm cotton stock with the mark in copper foil.",
    deliverables: ["Business cards", "Letterhead", "Email signature"]
  },
  {
    id: "bloom-festival",
    title: "Bloom Spring Festival",
    client: "Community event",
    category: "print",
    year: 2026,
    image: "assets/work/bloom-festival.svg",
    alt: "A5 flyer for Bloom Spring Festival with a flower mark in pink and yellow",
    brief: "An A5 flyer and poster set for a one-day festival in the park. Big type carries the name from across the street, and the date sits where a passer-by looks last.",
    deliverables: ["A5 flyer", "A2 poster", "Instagram post and story"]
  },
  {
    id: "atlas-freight",
    title: "Atlas Freight",
    client: "Logistics company",
    category: "identity",
    year: 2025,
    image: "assets/work/atlas-logistics.svg",
    alt: "Atlas Freight brand board with a blue circle and teal forward arrow logo",
    brief: "A freight company rebranding to win larger contracts. The forward arrow inside a globe says movement at a glance and is simple enough to paint on a truck door.",
    deliverables: ["Logo", "Colour system", "Fleet livery", "Stationery", "Pitch deck template"]
  },
  {
    id: "noor-skincare",
    title: "Noor Skincare",
    client: "Beauty brand",
    category: "logo",
    year: 2025,
    image: "assets/work/noor-skincare.svg",
    alt: "Noor skincare logo, a plum drop with a crescent on a blush background",
    brief: "A logo for a natural skincare line. The drop and crescent nod to the name, which means light, and the soft plum keeps it calm on a crowded shelf.",
    deliverables: ["Logo", "Label design", "Packaging colours"]
  },
  {
    id: "peak-fitness",
    title: "Peak Fitness",
    client: "Gym",
    category: "print",
    year: 2026,
    image: "assets/work/peak-fitness.svg",
    alt: "Peak Fitness promotional flyer with a mountain logo and neon green circle",
    brief: "A membership offer flyer handed out around a new gym. One loud colour, one clear offer and a deadline that is easy to spot.",
    deliverables: ["Flyer", "Window poster", "Social ad set"]
  },
  {
    id: "lumen-dental",
    title: "Lumen Dental",
    client: "Dental clinic",
    category: "cards",
    year: 2025,
    image: "assets/work/lumen-dental-cards.svg",
    alt: "Lumen Dental business cards with a friendly smile mark in aqua and white",
    brief: "Appointment and business cards for a family dental clinic. The smile mark makes the clinic feel friendly to children while the layout stays clinical and clear.",
    deliverables: ["Business cards", "Appointment cards", "Clinic signage"]
  }
];
