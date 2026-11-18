"""More local guides (added Nov 18, 2026 after the AEO prompt run): item disposal and cleanout planning.
Same rules as guides_data.py: official-source facts only, no county dollar amounts, no dashes.
First-hand lines ("we donated a treadmill at Savers") are things H&M actually did."""
FX = "https://www.fairfaxcounty.gov/publicworks/recycling-trash"
HERNDON = "https://www.herndon-va.gov/residents/town-services/trash-and-recycling"
HABITAT = "https://www.habitatdcnova.org/restore/donation-information/"
HABITAT_PICKUP = "https://www.habitatdcnova.org/restore/donation-pick-up-form/"
GOODWILL_NO = "https://dcgoodwill.org/donations/donation-guidelines/donations-goodwill-cannot-accept/"

MORE = [
    {
        "slug": "how-to-get-rid-of-a-couch-northern-virginia",
        "title": "How to Get Rid of a Couch in Northern Virginia",
        "h1": "How to get rid of a couch in Northern Virginia",
        "desc": "Who takes an old couch near Herndon, Reston and Fairfax: which donation centers accept sofas, what the county and the Town of Herndon will pick up, and where to drop one off.",
        "card": "Donate it, get it picked up, or haul it: every real option for an old sofa.",
        "lede": "A couch is the single most common thing people text us about. Before you pay anyone, here is every option you have, starting with the free ones.",
        "quick": "If the couch is clean and in good shape, the Habitat ReStore in Chantilly offers free pickup in Fairfax County. If it is worn out, your choices are your trash service's bulk pickup, hauling it to a county drop-off site for a fee, or a junk removal crew.",
        "sections": [
            ("If it is still in good shape", [
                "Habitat for Humanity ReStore in Chantilly takes furniture that is clean, working and sellable, and offers free pickup for large items in Fairfax County. The couch has to be at the curb or in the garage, and pickups book 1 to 3 weeks out.",
                "The ReStore does not take upholstered furniture with stains, tears, holes or pet hair.",
                "Goodwill does not take sleeper sofas, furniture over 50 pounds, or anything damaged, stained or covered in pet hair. That rules out most full size couches.",
            ]),
            ("If you are a Fairfax County trash customer", [
                "Only about 10% of county residents are. If you are, furniture can go out as a scheduled Special Pickup.",
                "The county's limits: single items under 6 feet long and piles up to 2 cubic yards. Measure the couch first. Many are longer than 6 feet.",
                "If a private company picks up your trash, the county says to ask that hauler or call a junk removal service.",
            ]),
            ("If you live in the Town of Herndon", [
                "Couches are allowed in the Town's paid Special Collections, up to 100 pounds per item.",
                "You apply and pay ahead of time. It is not offered on Mondays, Tuesdays or weekends.",
            ]),
            ("If you can haul it yourself", [
                "Fairfax County residents can take a sofa to the I-66 Transfer Station in Fairfax or the I-95 Landfill in Lorton. It counts as a large item and has a per item fee.",
                "In Loudoun County, the landfill in Leesburg takes furniture and charges by weight.",
            ]),
        ],
        "us": "Third floor walk-up, sleeper sofa, or it just will not fit in your car? One couch is a normal job for us. Text a photo and we will send one flat price.",
        "sources": [
            ("Habitat for Humanity DC-NOVA ReStore: Donation Information", HABITAT),
            ("Habitat for Humanity DC-NOVA ReStore: Donation Pick-Up", HABITAT_PICKUP),
            ("Goodwill of Greater Washington: What Goodwill Cannot Accept", GOODWILL_NO),
            ("Fairfax County: Special Pickup", FX + "/county-collection-customers/special-pick-up"),
            ("Fairfax County: Residential Disposal Fees and Regulations", FX + "/residential-disposal-fees-and-regulations"),
            ("Town of Herndon: Trash and Recycling", HERNDON),
            ("Loudoun County: Landfill", "https://www.loudoun.gov/landfill"),
        ],
        "related": ["furniture-removal", "junk-removal", "cleanouts"],
    },
    {
        "slug": "treadmill-exercise-equipment-removal-northern-virginia",
        "title": "How to Get Rid of a Treadmill or Exercise Equipment in Northern Virginia",
        "h1": "How to get rid of a treadmill or old exercise equipment",
        "desc": "Options for an old treadmill, elliptical or weight bench near Herndon and Fairfax: donating it if it works, county Special Pickup, the Loudoun landfill, or having it hauled.",
        "card": "Donate it if it works, or get 250 pounds of steel out of the basement.",
        "lede": "Treadmills are heavy, awkward and usually in the basement. Here is what you can do with one in Fairfax and Loudoun counties.",
        "quick": "If it still works, try donating it. We dropped a working treadmill at the Savers donation center in Fair Lakes in November 2026 and they took it. If it is dead, Fairfax County trash customers can schedule it as a Special Pickup, and Loudoun's landfill accepts exercise equipment for a fee.",
        "sections": [
            ("If it still works", [
                "Call the donation center first. Rules on large items change, and nobody wants to load a treadmill twice.",
                "Savers at Fair Lakes (13067 Fair Lakes Shopping Center, Fairfax) accepted a working treadmill from us in November 2026.",
                "Goodwill does not take furniture or items over 50 pounds, which rules out most treadmills.",
            ]),
            ("If it is broken", [
                "Fairfax County trash customers: the county lists exercise equipment under metal items it will collect as a scheduled Special Pickup.",
                "If a private company picks up your trash, ask that hauler or call a junk removal service.",
                "Loudoun County: the landfill in Leesburg lists exercise equipment among the items it accepts for a fee.",
            ]),
            ("Getting it out of the house", [
                "Unplug it and remove the safety key.",
                "Most treadmill decks fold up and lock. Check the manual for the latch before you try to tip it.",
                "Measure the stairs and doorways. Taking the console arms off often makes the difference.",
                "It is a two person carry. Do not try a basement staircase alone.",
            ]),
        ],
        "us": "We carry treadmills, ellipticals and weight sets up from basements all the time, and if yours still works we will try to donate it. Text a photo for one flat price.",
        "sources": [
            ("Savers Fair Lakes Community Donation Center", "https://stores.savers.com/va/fairfax/community-donation-center-cdc1247.html"),
            ("Goodwill of Greater Washington: What Goodwill Cannot Accept", GOODWILL_NO),
            ("Fairfax County: Special Pickup", FX + "/county-collection-customers/special-pick-up"),
            ("Fairfax County: Solid Waste FAQ", FX + "/solid-waste-faq"),
            ("Loudoun County: Landfill", "https://www.loudoun.gov/landfill"),
        ],
        "related": ["junk-removal", "cleanouts", "furniture-removal"],
    },
    {
        "slug": "old-appliance-disposal-fairfax-county",
        "title": "How to Get Rid of an Old Refrigerator, Washer or Dryer in Fairfax County",
        "h1": "How to get rid of an old refrigerator, washer or dryer",
        "desc": "Where old appliances go in Fairfax County and Herndon: who takes working ones, what the county picks up, drop-off rules for refrigerators and freezers, and Loudoun's options.",
        "card": "Working or dead, with or without freon: where each appliance can go.",
        "lede": "Appliances are harder than furniture because of weight and refrigerant. Here is where each kind can go.",
        "quick": "Working appliances can be donated to the Habitat ReStore in Chantilly, which offers free pickup in Fairfax County. Dead ones can go out as a county Special Pickup if you are a county trash customer, or to the I-66 or I-95 drop-off sites, where refrigerators, freezers and air conditioners have a per item fee.",
        "sections": [
            ("If it still works", [
                "Habitat for Humanity ReStore in Chantilly takes appliances in clean, working condition and offers free pickup for large items in Fairfax County.",
                "Goodwill and The Closet in Herndon do not take large appliances.",
            ]),
            ("Fairfax County trash customers", [
                "The county collects refrigerators, freezers, dehumidifiers and air conditioners as a scheduled Special Pickup.",
                "Stoves, washers, dryers and water heaters go under its metal category.",
                "This is only for the roughly 10% of residents on county collection. Everyone else asks their private hauler.",
            ]),
            ("Dropping it off yourself", [
                "The I-66 Transfer Station and the I-95 Landfill take appliances from county residents.",
                "Refrigerators, freezers, air conditioners and dehumidifiers are charged per item.",
                "Bring proof you live in Fairfax County.",
            ]),
            ("Town of Herndon and Loudoun County", [
                "Herndon's paid Special Collections take large appliances with the doors removed, up to 100 pounds each.",
                "Loudoun County's landfill in Leesburg takes appliances for a fee, with an extra charge for anything refrigerated.",
            ]),
        ],
        "us": "We haul washers, dryers and other household appliances, up the stairs and out the door. Text a photo and tell us what floor it is on, and we will send one flat price.",
        "sources": [
            ("Habitat for Humanity DC-NOVA ReStore: Donation Information", HABITAT),
            ("Goodwill of Greater Washington: What Goodwill Cannot Accept", GOODWILL_NO),
            ("The Closet of the Greater Herndon Area: Donation List", "https://www.theclosetofgreaterherndon.org/donation-list"),
            ("Fairfax County: Special Pickup", FX + "/county-collection-customers/special-pick-up"),
            ("Fairfax County: Residential Disposal Fees and Regulations", FX + "/residential-disposal-fees-and-regulations"),
            ("Town of Herndon: Trash and Recycling", HERNDON),
            ("Loudoun County: Landfill", "https://www.loudoun.gov/landfill"),
        ],
        "related": ["furniture-removal", "junk-removal", "cleanouts"],
    },
    {
        "slug": "whole-house-estate-cleanout-northern-virginia",
        "title": "How to Clean Out a Whole House in Northern Virginia",
        "h1": "Cleaning out a whole house: a plan that works",
        "desc": "A step by step plan for an estate or whole-house cleanout in Fairfax County: what to donate and where, what the county will not take, and how long each step really takes.",
        "card": "A step by step plan for a parent's house, an estate or a full downsizing.",
        "lede": "Clearing a whole house is a different job from getting rid of one couch. Usually it is a parent's home, and there is a deadline. This is the order that keeps it manageable.",
        "quick": "Sort into keep, donate and dump before you call anyone. Book donation pickups first, because they run 1 to 3 weeks out. Take paint, chemicals and electronics to the county yourself, since haulers cannot take hazardous waste. Then bring in a truck for what is left.",
        "sections": [
            ("Step 1: sort before you haul", [
                "Walk the house with three colors of tape or sticky notes: keep, donate, dump.",
                "Pull papers, photos, jewelry and anything with an account number first. Those are the things families regret losing.",
                "Check every drawer, closet shelf, attic and crawl space. That is where the important things hide.",
            ]),
            ("Step 2: book the donations early", [
                "Habitat ReStore in Chantilly picks up large furniture and working appliances for free in Fairfax County, but pickups book 1 to 3 weeks out and items must be at the curb or in the garage.",
                "The Closet of the Greater Herndon Area takes clothing, linens and housewares on weekday mornings. It does not take furniture.",
                "Goodwill takes smaller items. It does not take mattresses, sleeper sofas or furniture over 50 pounds.",
                "Nobody takes mattresses. Plan to dump those.",
            ]),
            ("Step 3: the things a hauler cannot take", [
                "Oil based paint, stains, pesticides, pool chemicals, gasoline and fluorescent bulbs go to the county's household hazardous waste site. It is free for Fairfax County residents.",
                "TVs, computers and other electronics are also free there, up to 10 large items per visit.",
                "Latex paint can be dried out in the can and put in the regular trash.",
            ]),
            ("Step 4: why the county is not the answer for the rest", [
                "County Special Pickup is only for the roughly 10% of homes on county trash service.",
                "Even then, a pile is limited to 2 cubic yards, about 6 feet by 3 feet by 3 feet. A whole house is many times that.",
                "The Town of Herndon's paid collection tops out at 9 cubic yards.",
            ]),
        ],
        "us": "This is our cleanout work. You point at what stays, everything else goes on the truck, and we sweep out when we are done. We set the good stuff aside to donate. Text a few photos of each room for one flat price.",
        "sources": [
            ("Habitat for Humanity DC-NOVA ReStore: Donation Pick-Up", HABITAT_PICKUP),
            ("The Closet of the Greater Herndon Area: Donate", "https://www.theclosetofgreaterherndon.org/donate"),
            ("Goodwill of Greater Washington: What Goodwill Cannot Accept", GOODWILL_NO),
            ("Fairfax County: Household Hazardous Waste", FX + "/household-hazardous-waste"),
            ("Fairfax County: Electronics Recycling", FX + "/electronics"),
            ("Fairfax County: Special Pickup", FX + "/county-collection-customers/special-pick-up"),
            ("Town of Herndon: Trash and Recycling", HERNDON),
        ],
        "related": ["cleanouts", "junk-removal", "furniture-removal"],
    },
    {
        "slug": "move-out-cleanout-northern-virginia",
        "title": "Move-Out Cleanout in Northern Virginia: What to Do With What You Are Not Taking",
        "h1": "Moving out? What to do with everything you are not taking",
        "desc": "A move-out timeline for Herndon, Reston and Fairfax County: when to book donation pickups, what the trash service will not take, and what to do in the last 48 hours.",
        "card": "A timeline for the stuff that is not coming with you, from three weeks out to the last day.",
        "lede": "Every move ends the same way: the truck is full and there is still a couch, a mattress and a pile in the garage. A little planning three weeks out saves the last night.",
        "quick": "Book donation pickups three weeks before you move, because they fill up. Do not count on the curb: most trash services will not take extra bags or furniture without a scheduled, sometimes paid, pickup. Leave the last two days for a single haul of whatever is left.",
        "sections": [
            ("Three weeks out", [
                "Book a Habitat ReStore pickup for good furniture and working appliances. Pickups run 1 to 3 weeks out and items have to be at the curb or in the garage.",
                "If you are a Fairfax County trash customer, schedule a Special Pickup now. As of mid November 2026 the county posted that special pickups are running behind.",
                "In the Town of Herndon, apply and pay for a Special Collection. It is not offered on Mondays, Tuesdays or weekends, so pick your date early.",
            ]),
            ("One week out", [
                "Drop clothes, linens and housewares at a donation center. Goodwill's Herndon Donation Express is at 2525 Centreville Road.",
                "Take old paint, chemicals and electronics to the I-66 Transfer Station. They are free for county residents and no hauler can take the chemicals.",
                "Decide what is trash. Mattresses will not be accepted by any donation center.",
            ]),
            ("What will not work", [
                "Leaving it at the curb. In Herndon, only Town carts are emptied, and extra bags or cans are not collected.",
                "Leaving it at a recycling drop-off. In Loudoun County, leaving furniture or electronics at a recycling center is treated as illegal dumping.",
                "Leaving it in the unit. Landlords usually bill for the haul.",
            ]),
            ("The last 48 hours", [
                "Walk every room, closet and the garage with your phone and take photos of what is left.",
                "One haul for all of it is cheaper and faster than three trips in your own car.",
                "Sweep after the furniture is out, not before.",
            ]),
        ],
        "us": "We work around move-out dates for homeowners, renters and landlords. Text photos of what is left and your deadline, and we will send one flat price and a time.",
        "sources": [
            ("Habitat for Humanity DC-NOVA ReStore: Donation Pick-Up", HABITAT_PICKUP),
            ("Fairfax County: Special Pickup", FX + "/county-collection-customers/special-pick-up"),
            ("Town of Herndon: Trash and Recycling", HERNDON),
            ("Goodwill of Greater Washington: Donation Center Locations", "https://dcgoodwill.org/donation-center-locations/"),
            ("Goodwill of Greater Washington: What Goodwill Cannot Accept", GOODWILL_NO),
            ("Fairfax County: Household Hazardous Waste", FX + "/household-hazardous-waste"),
            ("Loudoun County: Recycling Dropoff Centers", "https://www.loudoun.gov/Facilities/Facility/Details/Loudoun-County-Recycling-Dropoff-Centers-146"),
        ],
        "related": ["cleanouts", "furniture-removal", "junk-removal"],
    },
]
