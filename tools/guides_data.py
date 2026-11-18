"""Local guides for hmjunkland.org. Facts checked against official county/town/org pages on CHECKED.
Rules: only what the source says, no county dollar amounts (they change: link to the fee page), no dashes."""
CHECKED = "November 18, 2026"

FX = "https://www.fairfaxcounty.gov/publicworks/recycling-trash"
GUIDES = [
    {
        "slug": "fairfax-county-bulk-pickup",
        "title": "Fairfax County Bulk Pickup: Who Gets It and What They Take",
        "h1": "Fairfax County bulk pickup: who gets it and what they take",
        "desc": "Only about 1 in 10 Fairfax County homes get county special pickup. Here is who qualifies, what it takes, the size limits, and what to do if you have a private hauler.",
        "card": "Who qualifies for county special pickup, what it takes, and the size limits.",
        "lede": "Most people in Fairfax County assume the county will pick up a couch at the curb. For about 9 out of 10 homes, it won't. Here is how it really works.",
        "quick": "Fairfax County only does special pickups for its own trash customers, which is about 10% of residents. Everyone else has a private hauler and has to ask that hauler, or use a junk removal company.",
        "sections": [
            ("First, check who picks up your trash", [
                "The county only collects from homes in its own collection districts. The county says that is about 10% of residents.",
                "Use the county's \"Does Fairfax County Pick Up My Trash?\" lookup, or call 703-802-3322.",
                "If a private company picks up your trash (most HOAs and neighborhoods), the county says to contact your hauler or a junk removal service.",
            ]),
            ("If you are a county customer", [
                "Special pickups have to be scheduled ahead of time, online or at 703-802-3322, Monday to Friday, 7:30 a.m. to 4:30 p.m.",
                "County customers get a set number of free special collections each fiscal year (July 1 to June 30). Check the county page for the current count.",
                "A pile can be up to 2 cubic yards, about 6 feet by 3 feet by 3 feet. Bigger piles are charged.",
                "Single items have to be under 6 feet long, and piles should be separated by type.",
                "Put it at the curb by 6 a.m., clear of wires and branches.",
            ]),
            ("What county special pickup takes", [
                "Bulk: furniture, lumber, doors, mattresses and box springs, carpet rolls 6 feet or shorter, wood pallets.",
                "Metal: stoves, washers and dryers, bed frames, grills without the propane tank, exercise equipment, water heaters.",
                "Freon appliances: refrigerators, freezers, dehumidifiers, air conditioners.",
                "Electronics: TVs, computers, phones, audio and video gear.",
                "Brush and limbs under 6 inches thick and under 6 feet long.",
            ]),
            ("What it will not take", [
                "Construction debris, cardboard, plastic bags, and anything not on the county's accepted list.",
                "As of mid November 2026 the county posted a notice that special pickups are running behind, and asks people to leave items at the curb until they are collected.",
            ]),
        ],
        "us": "If you have a private hauler, more than a 2 cubic yard pile, stuff that is still inside the house, or you just need it gone this week, that is the kind of job we do. Text us a photo and we will send one flat price.",
        "sources": [
            ("Fairfax County: Special Pickup", FX + "/county-collection-customers/special-pick-up"),
            ("Fairfax County: County Collection Customers", FX + "/county-collection-customers"),
            ("Fairfax County: Solid Waste FAQ", FX + "/solid-waste-faq"),
        ],
        "related": ["junk-removal", "furniture-removal", "cleanouts"],
    },
    {
        "slug": "i-66-transfer-station-and-i-95-landfill",
        "title": "I-66 Transfer Station and I-95 Landfill: What Residents Can Drop Off",
        "h1": "Taking junk to the I-66 Transfer Station or the I-95 Landfill",
        "desc": "Addresses, hours, what is free, what has a fee, and what to bring to Fairfax County's two drop-off sites on West Ox Road and in Lorton.",
        "card": "Addresses, hours, what is free and what has a fee at the two county drop-off sites.",
        "lede": "If you have a truck and a free Saturday, Fairfax County's two drop-off sites are the cheapest way to get rid of most junk. Here is what to know before you load up.",
        "quick": "Fairfax County residents can haul their own junk to the I-66 Transfer Station in Fairfax or the I-95 Landfill Complex in Lorton. Recycling, electronics and household hazardous waste are free. Furniture, mattresses, appliances, trash and yard waste have a fee.",
        "sections": [
            ("Where they are and when they are open", [
                "I-66 Transfer Station: 4618 West Ox Road, Fairfax, VA 22030. Phone 703-631-1179.",
                "I-95 Landfill Complex: 9850 Furnace Road, Lorton, VA 22079. Phone 703-690-1703.",
                "Trash and recycling hours at both: Monday to Friday 7 a.m. to 5 p.m., Saturday and Sunday 7 a.m. to 4 p.m.",
                "Closed on Independence Day, Thanksgiving, Christmas, New Year's Day and Easter Sunday. Early close on Christmas Eve and New Year's Eve.",
                "Fairfax County residents only. Bring a driver's license, state ID, or a tax or utility bill.",
            ]),
            ("What is free", [
                "Most recyclables: cans, bottles, paper, cardboard and metal.",
                "Motor oil, antifreeze, car batteries and cooking oil.",
                "Electronics and household hazardous waste, during the hazardous waste hours.",
                "Bicycles. The county also gives away free mulch.",
            ]),
            ("What has a fee", [
                "Large items like a sofa, dresser, desk, recliner, dining table, carpet, or a mattress and box spring are charged per item.",
                "Refrigerators, freezers, air conditioners and dehumidifiers are charged per item.",
                "Bagged trash, bulk trash, brush and yard waste are charged by the bag, the truckload or the ton.",
                "Brick, concrete, dirt and rock are charged by the ton, with a 2 cubic yard per day limit.",
                "The county updates its fees every July. Use the fee page in the sources below for today's numbers.",
            ]),
            ("Hazardous waste and electronics have their own hours", [
                "I-66: Monday and Friday 7 a.m. to 5 p.m., Tuesday and Thursday noon to 5 p.m., Saturday and Sunday 7 a.m. to 4 p.m. Closed Wednesday.",
                "I-95: Wednesday 7 a.m. to 5 p.m. and Saturday 7 a.m. to 4 p.m. only.",
                "No yard waste in plastic bags. It gets turned away at both sites.",
            ]),
        ],
        "us": "No truck, no time, or the couch will not fit in your SUV? We load it, haul it and sweep up. Text us a photo for one flat price.",
        "sources": [
            ("Fairfax County: Locations and Hours", FX + "/locations-hours"),
            ("Fairfax County: I-66 Transfer Station", FX + "/i-66-transfer-station"),
            ("Fairfax County: Residential Disposal Fees and Regulations", FX + "/residential-disposal-fees-and-regulations"),
        ],
        "related": ["junk-removal", "cleanouts", "furniture-removal"],
    },
    {
        "slug": "herndon-bulk-trash-and-leaf-collection",
        "title": "Town of Herndon Bulk Trash and Leaf Collection: How It Works",
        "h1": "Town of Herndon bulk trash and leaf collection, explained",
        "desc": "How Herndon's paid Special Collections work, what the Town takes, yard waste rules, and the 2026 vacuum leaf collection weeks north and south of the W&OD Trail.",
        "card": "Herndon's paid special collections, yard waste rules and the 2026 leaf vacuum weeks.",
        "lede": "Herndon is our home base, and the Town runs its own trash service, separate from Fairfax County. Here is how bulk pickup and leaf season work inside town limits.",
        "quick": "The Town of Herndon picks up bulk items only as a paid Special Collection that you apply and pay for ahead of time. Leaves are vacuumed from the curb on set weeks from October 12 to December 11, 2026.",
        "sections": [
            ("Regular weekly service", [
                "Town crews pick up trash, recycling and yard waste once a week.",
                "Carts go out by 6 a.m., and no earlier than 24 hours before.",
                "Only Town carts are emptied. Extra bags or cans next to the cart are not collected.",
            ]),
            ("Bulk items: Special Collections", [
                "It is optional and paid. Fill out the Town's Special Collections Application and pay. The receipt is your confirmation.",
                "Priced per 3 cubic yards, up to 9 cubic yards. Larger loads are up to the Town.",
                "Furniture like couches, chairs, tables and mattresses is allowed, up to 100 pounds per item.",
                "Large appliances with the doors removed, small scrap metal, and some construction debris like cabinets, sinks, fencing, lumber and carpet are allowed.",
                "Not offered on Mondays, Tuesdays or weekends, or during the weeks of Memorial Day, Thanksgiving, Christmas and New Year.",
                "The Town's Spring Clean-up was cut from this year's budget and is not being offered.",
                "Questions go to Public Works at 703-435-6856.",
            ]),
            ("Yard waste and brush", [
                "Collected on your trash day in a reusable container marked Yard Waste (50 gallons or 50 pounds max) or in 30 gallon paper yard bags.",
                "Tie brush in bundles no longer than 4 feet and no heavier than 50 pounds. Limbs can be up to 3 inches thick.",
                "The Town does not take trees or stumps cut by a tree company or contractor.",
            ]),
            ("2026 vacuum leaf collection", [
                "The season runs October 12 to December 11, alternating north and south of the W&OD Trail.",
                "North of the trail: October 12 to 16, October 26 to 30, November 9 to 13, November 30 to December 4.",
                "South of the trail: October 19 to 23, November 2 to 6, November 16 to 20, December 7 to 11.",
                "No collection the week of Thanksgiving, November 23 to 27.",
                "Rake leaves to the curb before your week starts. Leaves only, no sticks, and keep drains, hydrants and sidewalks clear.",
            ]),
            ("What the Town does not collect", [
                "Hazardous waste and electronics. The Town sends residents to Fairfax County's I-66 Transfer Station for those.",
            ]),
        ],
        "us": "Missed your leaf week, have more than the Town will take, or need the whole yard cleaned up in one visit? We are in Herndon. Text us a photo for a free quote.",
        "sources": [
            ("Town of Herndon: Trash and Recycling", "https://www.herndon-va.gov/residents/town-services/trash-and-recycling"),
            ("Town of Herndon: Yard Waste and Brush", "https://www.herndon-va.gov/residents/town-services/trash-and-recycling/yard-waste-and-brush"),
            ("Town of Herndon: Fall Collections", "https://www.herndon-va.gov/departments/public-works/fall-collections"),
        ],
        "related": ["yard-cleanup", "junk-removal", "furniture-removal"],
    },
    {
        "slug": "where-to-donate-furniture-herndon-reston",
        "title": "Where to Donate Furniture Near Herndon, Reston and Chantilly",
        "h1": "Where to donate furniture near Herndon, Reston and Chantilly",
        "desc": "Which donation centers near Herndon take furniture, which ones do not, who offers pickup, and what nobody will accept. Addresses and hours included.",
        "card": "Who takes furniture, who does not, and who will come pick it up.",
        "lede": "If it is clean and still works, donating it beats paying to dump it. We do this ourselves on jobs. Here is who takes what near Herndon.",
        "quick": "For furniture, start with the Habitat ReStore in Chantilly, which offers free pickup for large items in Fairfax County. Goodwill takes smaller furniture under 50 pounds. Almost nobody takes mattresses.",
        "sections": [
            ("Habitat for Humanity ReStore, Chantilly", [
                "4311 Walney Road, Chantilly, VA 20151. Phone 703-953-3747. Drop-off Monday to Saturday, 10 a.m. to 4 p.m.",
                "Takes furniture, appliances, building materials, lighting and flooring that is clean, working and sellable.",
                "Free pickup for large items in Fairfax and Arlington counties and limited parts of Loudoun. Items have to be at the curb or in the garage, and pickups book 1 to 3 weeks out.",
                "Does not take mattresses or bedding, upholstered furniture with stains, tears or pet hair, tube TVs, paint or baby items.",
            ]),
            ("Goodwill", [
                "Herndon Donation Express: 2525 Centreville Road, Suite 61, Herndon, VA 20171.",
                "Sterling: 22405 Enterprise Street. Dulles: 45380 Manifest Boulevard, Sterling. Centreville: 5077 Westfields Boulevard.",
                "Donation hours are Monday to Saturday 10 a.m. to 7 p.m. and Sunday 10 a.m. to 5 p.m.",
                "Does not take mattresses, box springs, sleeper sofas, furniture over 50 pounds, damaged or stained furniture, large appliances or building materials.",
                "Pickup is a paid service through a third party.",
            ]),
            ("Savers, Fair Lakes", [
                "13067 Fair Lakes Shopping Center, Fairfax, VA 22033. Donations Monday to Saturday 9 a.m. to 9 p.m., Sunday 10 a.m. to 7 p.m.",
                "Takes clothing, housewares, electronics, small appliances and small furniture. Call ahead for anything big.",
            ]),
            ("The Closet of the Greater Herndon Area", [
                "845 Station Street, Herndon, VA 20170. Donations 8 a.m. to noon on Monday, Tuesday, Wednesday, Friday and Saturday.",
                "Great for clothing, linens, housewares, small appliances and flat screen TVs.",
                "Does not take furniture, mattresses or large appliances, and does not do pickups.",
            ]),
            ("What nobody wants", [
                "Mattresses and box springs. Habitat, Goodwill and The Closet all refuse them.",
                "Anything stained, torn, broken or covered in pet hair.",
                "Old tube TVs, paint, cribs and car seats.",
            ]),
        ],
        "us": "When we clear out a house, we pull the good stuff aside and donate what we can. If your pile is a mix of donate and dump, text us a photo and we will handle both in one trip.",
        "sources": [
            ("Habitat for Humanity DC-NOVA ReStore: Donation Information", "https://www.habitatdcnova.org/restore/donation-information/"),
            ("Habitat for Humanity DC-NOVA ReStore: Locations", "https://www.habitatdcnova.org/restore/locations/"),
            ("Goodwill of Greater Washington: What Goodwill Cannot Accept", "https://dcgoodwill.org/donations/donation-guidelines/donations-goodwill-cannot-accept/"),
            ("Goodwill of Greater Washington: Donation Center Locations", "https://dcgoodwill.org/donation-center-locations/"),
            ("Savers Fair Lakes Community Donation Center", "https://stores.savers.com/va/fairfax/community-donation-center-cdc1247.html"),
            ("The Closet of the Greater Herndon Area: Donate", "https://www.theclosetofgreaterherndon.org/donate"),
        ],
        "related": ["furniture-removal", "cleanouts", "junk-removal"],
    },
    {
        "slug": "mattress-tv-paint-disposal-fairfax-county",
        "title": "How to Get Rid of a Mattress, TV or Old Paint in Fairfax County",
        "h1": "How to get rid of a mattress, a TV or old paint in Fairfax County",
        "desc": "The three things donation centers will not take. Where Fairfax County residents can bring mattresses, TVs, electronics, paint and household chemicals, and what is free.",
        "card": "The three things donation centers refuse, and where they actually go.",
        "lede": "These are the three things people get stuck with, because the donation centers say no and the trash truck leaves them at the curb.",
        "quick": "In Fairfax County, mattresses go to the I-66 or I-95 drop-off sites for a per item fee. TVs and electronics are free there during hazardous waste hours. Dried latex paint can go in your regular trash, and oil based paint goes to the hazardous waste site for free.",
        "sections": [
            ("Mattresses and box springs", [
                "Habitat ReStore, Goodwill and The Closet in Herndon all refuse mattresses.",
                "Residents can bring them to the I-66 Transfer Station or the I-95 Landfill. They count as a large item and have a per item fee. Bring proof you live in the county.",
                "County trash customers can put a mattress out as a scheduled Special Pickup.",
                "In the Town of Herndon, mattresses are allowed in a paid Special Collection.",
                "If you have a private hauler, the county says to ask the hauler or call a junk removal service.",
            ]),
            ("TVs and electronics", [
                "Free for Fairfax County residents at the I-66 and I-95 hazardous waste and electronics areas.",
                "They take TVs, monitors, computers, laptops, phones, printers, cables and even strands of Christmas lights.",
                "Limit of 10 large items per visit, and only during the posted hours. There is no after hours drop-off.",
                "The Town of Herndon does not collect electronics.",
            ]),
            ("Paint and household chemicals", [
                "Latex paint: let it air dry in the can, then put it in your regular trash. If it will not dry, there is a latex only drop-off at the I-95 site.",
                "Oil based paint, stains, thinners, pesticides, pool chemicals, gasoline, batteries and fluorescent bulbs go to the hazardous waste site. It is free for residents.",
                "Small propane tanks up to 20 pounds are accepted for a fee.",
                "Not accepted: ammunition, large propane tanks, compressed gas cylinders and medications.",
            ]),
            ("When the hazardous waste areas are open", [
                "I-66 (4618 West Ox Road, Fairfax): Monday and Friday 7 a.m. to 5 p.m., Tuesday and Thursday noon to 5 p.m., weekends 7 a.m. to 4 p.m. Closed Wednesday.",
                "I-95 (9850 Furnace Road, Lorton): Wednesday 7 a.m. to 5 p.m. and Saturday 7 a.m. to 4 p.m.",
            ]),
        ],
        "us": "We haul mattresses, old TVs and the rest of the pile in one trip. We cannot take paint or chemicals, so use the county site for those. Text us a photo for a free quote.",
        "sources": [
            ("Fairfax County: Electronics Recycling", FX + "/electronics"),
            ("Fairfax County: Household Hazardous Waste", FX + "/household-hazardous-waste"),
            ("Fairfax County: Residential Disposal Fees and Regulations", FX + "/residential-disposal-fees-and-regulations"),
            ("Fairfax County: Locations and Hours", FX + "/locations-hours"),
        ],
        "related": ["junk-removal", "furniture-removal", "cleanouts"],
    },
    {
        "slug": "loudoun-county-junk-disposal-sterling-ashburn",
        "title": "Junk and Bulk Trash in Sterling and Ashburn: Loudoun County Options",
        "h1": "Getting rid of junk in Sterling and Ashburn",
        "desc": "Loudoun County has no county bulk pickup. Here is what the Leesburg landfill takes, what the recycling centers will not, and how electronics and hazardous waste events work.",
        "card": "No county bulk pickup in Loudoun. Here is what the landfill and drop-off centers take.",
        "lede": "Loudoun works differently from Fairfax. There is no county bulk pickup at all, so it comes down to your HOA, your hauler, the landfill or a junk removal crew.",
        "quick": "Loudoun County does not run a bulk pickup program. Curbside service comes from your town, HOA or private hauler. The county landfill in Leesburg takes furniture, mattresses, appliances and electronics for a fee.",
        "sections": [
            ("Loudoun County landfill", [
                "Loudoun County Solid Waste Management Facility, 21101 Evergreen Mills Road, Leesburg, VA 20175. Phone 703-771-5500.",
                "Open Monday to Saturday, 8 a.m. to 4 p.m. Closed Sunday. The gate closes at 4:00.",
                "Only takes material that came from Loudoun County.",
                "Takes furniture, mattresses and box springs, appliances, carpet, electronics, exercise equipment, scrap metal and construction debris, charged by weight with a small minimum.",
                "Refrigerators, propane tanks and tires have an extra charge.",
                "Free at the landfill recycling center: motor oil, antifreeze, oil filters and car batteries.",
            ]),
            ("Recycling drop-off centers are for recycling only", [
                "The Sterling Recycling Center is at 46279 West Juniper Avenue, Sterling, VA 20164.",
                "The drop-off centers take bottles, cans, jugs, jars, paper and cardboard.",
                "They do not take furniture, electronics, yard waste or scrap metal. The county treats leaving those there as illegal dumping.",
            ]),
            ("Electronics and hazardous waste are event based", [
                "Loudoun collects household hazardous waste and electronics at scheduled events, not every day.",
                "The 2026 events are finished. The county has said 2027 electronics events are planned for May, June, September and October.",
                "TVs and monitors have a fee at the events. Electronics can also go to the landfill for a fee.",
            ]),
            ("Donating instead", [
                "Goodwill has donation centers at 22405 Enterprise Street in Sterling and 45380 Manifest Boulevard near Dulles.",
                "The Chantilly Habitat ReStore offers pickup in limited parts of Loudoun.",
            ]),
        ],
        "us": "Leesburg is a long drive from Sterling with a couch in the back. We cover Sterling and Ashburn from our Herndon base. Text us a photo for one flat price.",
        "sources": [
            ("Loudoun County: Landfill", "https://www.loudoun.gov/landfill"),
            ("Loudoun County: Residential Recycling", "https://www.loudoun.gov/5807/Residential-Recycling"),
            ("Loudoun County: Recycling Dropoff Centers", "https://www.loudoun.gov/Facilities/Facility/Details/Loudoun-County-Recycling-Dropoff-Centers-146"),
            ("Loudoun County: Household Hazardous Waste", "https://www.loudoun.gov/hhw"),
            ("Loudoun County: Electronics Recycling", "https://www.loudoun.gov/electronics"),
        ],
        "related": ["junk-removal", "furniture-removal", "yard-cleanup"],
    },
]

from guides_more import MORE  # noqa: E402

GUIDES += MORE
