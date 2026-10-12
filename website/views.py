from django.shortcuts import render


TESTIMONIALS = [
    # Add approved client testimonials here (see the note in home() below).
]


def home(request):
    context = {
        "active": "home",
        "stats": [
            {"value": "2015", "label": "Founded"},
            {"value": "5", "label": "Branches nationwide"},
            {"value": "100%", "label": "Black female-owned"},
            {"value": "Level 1", "label": "B-BBEE contributor"},
        ],
        "what_we_do": [
            {"idx": "01", "title": "Debt Recovery Specialists",
             "body": "Outbound collections, skip tracing and legal support for outstanding accounts — "
                     "recovered ethically, in full regulatory compliance."},
            {"idx": "02", "title": "Sales Solutions",
             "body": "Vehicle tracking and car insurance solutions, helping you protect what you have."},
            {"idx": "03", "title": "Customer & Legal Support",
             "body": "Dedicated customer engagement and legal support across every account and product."},
        ],
        # Only REAL client testimonials go here, and only once the client has
        # given written permission to publish their words and name.
        # Set "approved": True once that permission is on file.
        # While this list has no approved entries, the whole testimonials
        # section (and its link in the jump menu) is hidden automatically.
        #
        # Example of one entry:
        # {
        #     "quote": "Exact words the client approved.",
        #     "name": "Thandi Mokoena",          # real person who said it
        #     "role": "Finance Manager",
        #     "organisation": "ABC College",     # or "" if they prefer not to be named
        #     "approved": True,
        # },
        "testimonials": [t for t in TESTIMONIALS if t.get("approved")],
    }
    return render(request, "home.html", context)


def about(request):
    context = {
        "active": "about",
        "who_we_work_with": [
            {"idx": "01", "title": "Education",
             "body": "Public and private schools, TVET colleges, and universities that rely on us to "
                     "strengthen their financial sustainability through improved fee recovery and "
                     "reduced outstanding balances."},
            {"idx": "02", "title": "Healthcare",
             "body": "Private hospitals and healthcare providers, for whom efficient debt management is "
                     "critical to maintaining cash flow and uninterrupted service delivery."},
            {"idx": "03", "title": "Municipalities",
             "body": "Local government bodies that partner with us to recover overdue municipal accounts, "
                     "strengthen revenue collection, and improve funding for essential service delivery."},
            {"idx": "04", "title": "Body Corporate",
             "body": "Body corporates and homeowners' associations that rely on us to recover outstanding "
                     "levies and protect the financial health of the properties they manage."},
            {"idx": "05", "title": "Private Sector",
             "body": "Retailers, financial institutions, and corporate organizations that use our recovery "
                     "strategies to reduce arrears and protect long-term customer relationships."},
        ],
        "what_sets_us_apart": [
            {"num": "01", "title": "Ethical conduct",
             "body": "Every interaction is professional, respectful, and never coercive."},
            {"num": "02", "title": "Transformation & impact",
             "body": "A B-BBEE Level 1 contributor, 100% Black female-owned, and a YES Programme partner "
                     "creating skills and jobs for unemployed youth."},
            {"num": "03", "title": "Client-centric focus",
             "body": "Strategies built around your portfolio, not a one-size template."},
            {"num": "04", "title": "Proven results",
             "body": "A track record built on measurable recovery, not promises."},
            {"num": "05", "title": "Technology-driven",
             "body": "CRM, automated dialing and analytics behind every campaign."},
            {"num": "06", "title": "Compliance first",
             "body": "NCA, POPIA and Debt Collectors Act compliant, always."},
        ],
        "values": [
            {"title": "Integrity", "body": "Honesty, transparency and fairness in every dealing."},
            {"title": "Accountability", "body": "We take full responsibility for the results we deliver."},
            {"title": "Excellence", "body": "Continuous improvement in performance and method."},
            {"title": "Respect", "body": "Every client and debtor treated with dignity."},
            {"title": "Empowerment", "body": "Inclusivity, transformation and female leadership."},
        ],
    }
    return render(request, "about.html", context)

def services(request):
    context = {
        "active": "services",
        "core_services": [
            {"idx": "01", "title": "Debt Collection & Recovery",
             "body": "Outbound calls, SMS, WhatsApp and email campaigns across early-stage, soft and "
                     "late-stage collections, with skip tracing for unreachable customers and "
                     "settlement negotiation throughout."},
            {"idx": "02", "title": "Revenue Enhancement & Credit Control",
             "body": "A review of your collection strategy, debit order success rates and arrear "
                     "management policies — with concrete recommendations to reduce future defaults."},
            {"idx": "03", "title": "Call Centre & Customer Engagement",
             "body": "A dedicated, supervised team running multi-channel contact campaigns with "
                     "quality assurance and daily productivity monitoring."},
            {"idx": "04", "title": "Legal Support Services",
             "body": "Letter of demand distribution and escalation support for accounts that need a "
                     "firmer hand, still within full regulatory compliance."},
            {"idx": "05", "title": "Consulting & Advisory Services",
             "body": "Portfolio assessment, risk segmentation and workflow review for institutions "
                     "building or improving their own in-house recovery function."},
        ],
        "recovery_process_steps": [
            {"tag": "1", "title": "Portfolio assessment",
             "body": "Review debtor books, segment by risk and delinquency stage, and prioritise "
                     "recoverable accounts."},
            {"tag": "2", "title": "Collection & recovery",
             "body": "Multi-channel outbound contact, skip tracing and settlement negotiation on "
                     "prioritised accounts."},
            {"tag": "3", "title": "Revenue enhancement",
             "body": "Ongoing review of collection strategy and workflows to lift recovery rates "
                     "over time."},
            {"tag": "4", "title": "Customer rehabilitation",
             "body": "Affordable repayment plans and counselling referrals that protect the "
                     "relationship long-term."},
        ],
        "sales_process_steps": [
            {"tag": "1", "title": "Enquiry & needs assessment",
             "body": "Understand what you're looking to protect — your vehicle, yourself, or both — "
                     "and match it to the right solution."},
            {"tag": "2", "title": "Quote & recommendation",
             "body": "A clear, no-obligation quote and recommendation based on your needs and budget."},
        ],
        "tech_tags": [
            "Automated dialing", "CRM management", "SMS integration", "WhatsApp",
            "Email automation", "Collection dashboards", "Performance analytics",
            "Voice recording & call monitoring", "Secure data management",
        ],
        "compliance_items": [
            "National Credit Act (NCA)",
            "Protection of Personal Information Act (POPIA)",
            "Debt Collectors Act",
            "Consumer Protection Act",
            "Financial Intelligence Centre Act, where applicable",
            "Financial Advisory and Intermediary Services Act (FAIS)",
            "Short-term Insurance Act",
            "Industry Codes of Conduct",
        ],
    }
    return render(request, "services.html", context)


def contact(request):
    submitted = False
    error = None
    if request.method == "POST":
        # POPIA: we only process the enquiry if the person has ticked the
        # consent box agreeing to the Privacy Policy.
        if request.POST.get("consent") != "yes":
            error = "Please tick the consent box so we can respond to your enquiry."
        else:
            full_name = request.POST.get("full_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            company = request.POST.get("company")
            message = request.POST.get("message")
            # NOTE: this only accepts the submission for now — wire this up to
            # an email service (e.g. django-anymail, SendGrid) to actually
            # deliver messages.
            print(f"New inquiry from {full_name} <{email}> ({phone}, {company}): {message} [POPIA consent: yes]")
            submitted = True
    return render(request, "contact.html", {
        "active": "contact", "submitted": submitted, "error": error,
    })


def partners(request):
    # IMPORTANT: only list organisations that have agreed (ideally in writing)
    # to have their name and logo shown on this site. To remove one, delete
    # its line; to add one, put the logo in static/img/logos/ and add a line.
    context = {
        "active": "partners",
        "clients": [
            {"name": "Dalpark Learning Academy", "logo": "dalpark-learning-academy.png",
             "sector": "Education · The King's Academies"},
            {"name": "St. Raphael's Learning Academy", "logo": "st-raphaels-learning-academy.png",
             "sector": "Education · The King's Academies"},
            {"name": "Lee Rand High", "logo": "lee-rand-high.png",
             "sector": "Education · The King's Academies"},
            {"name": "Denver Technical College", "logo": "denver-technical-college.png",
             "sector": "Education · Technical college"},
            {"name": "College on Hills", "logo": "college-on-hills.png",
             "sector": "Education · Independent college"},
            {"name": "SA Academy of Applied Competence", "logo": "saaac.png",
             "sector": "Education · Skills training"},
        ],
        "partners": [
            {"name": "King Price Insurance", "logo": "king-price-insurance.png",
             "sector": "Car insurance"},
            {"name": "Pineapple", "logo": "pineapple.png",
             "sector": "Car insurance"},
            {"name": "Hippo", "logo": "hippo.png",
             "sector": "Insurance comparison"},
            {"name": "Tracker", "logo": "tracker.png",
             "sector": "Vehicle tracking"},
            {"name": "Cartrack", "logo": "cartrack.png",
             "sector": "Vehicle tracking"},
        ],
    }
    return render(request, "partners.html", context)


def privacy(request):
    # Fill these in with the client's real details before going live.
    context = {
        "active": "privacy",
        "information_officer": {
            "name": "[Information Officer full name]",
            "email": "privacy@nokamabovu.co.za",
            "phone": "010 018 3411",
        },
        "last_updated": "October 2026",
    }
    return render(request, "privacy.html", context)


def careers(request):
    # Sample vacancies: replace with the real roles (or move them to a model/admin later).
    vacancies = [
        {"id": "debt-agent", "title": "Debt Recovery Agent", "dept": "Debt recovery",
         "location": "Johannesburg (HQ)", "type": "Full-time", "closes": "16 Oct 2026", "tag": "Closing soon",
         "resp": ["Contact customers by phone to agree affordable repayment arrangements",
                  "Record every conversation accurately on our system",
                  "Treat every customer with respect and follow our compliance standards"],
         "reqs": ["Matric certificate",
                  "Clear, confident phone manner in English and one other local language",
                  "Comfortable working to daily targets"]},
        {"id": "insurance-consultant", "title": "Car Insurance Sales Consultant", "dept": "Car insurance",
         "location": "Johannesburg (HQ)", "type": "Full-time", "closes": "30 Oct 2026", "tag": "New",
         "resp": ["Speak to customers about our car insurance solutions and answer their questions",
                  "Prepare clear, no-obligation quotes and follow up on enquiries",
                  "Meet monthly sales targets"],
         "reqs": ["Matric certificate; sales experience is an advantage",
                  "Strong listening and communication skills",
                  "Willing to complete the required product training"]},
        {"id": "team-leader", "title": "Call Centre Team Leader", "dept": "Debt recovery",
         "location": "Durban", "type": "Full-time", "closes": "13 Nov 2026", "tag": "",
         "resp": ["Coach and support a team of agents day to day",
                  "Track team performance and report on results",
                  "Handle escalated customer queries"],
         "reqs": ["Previous call centre or collections experience",
                  "Experience leading or mentoring others",
                  "Good reporting and organising skills"]},
        {"id": "support-admin", "title": "Customer & Legal Support Administrator", "dept": "Support",
         "location": "Bloemfontein", "type": "Contract", "closes": "20 Nov 2026", "tag": "",
         "resp": ["Support customers and the sales and collections teams with daily queries",
                  "Prepare and file customer and legal documents",
                  "Keep account information accurate and up to date"],
         "reqs": ["Matric certificate",
                  "Accurate data capture and attention to detail",
                  "Working knowledge of Microsoft Office"]},
    ]
    for r in vacancies:
        r["subject"] = "Application: " + r["title"]
    context = {
        "active": "careers",
        "vacancies": vacancies,
        "categories": ["Debt recovery", "Car insurance", "Support"],
        "benefits": [
            {"icon": "cap", "title": "Paid training and onboarding", "body": "Learn our systems, processes and compliance basics before you take your first call."},
            {"icon": "growth", "title": "Room to grow", "body": "We prefer promoting from within, so strong performers move up into senior and leadership roles."},
            {"icon": "screen", "title": "Modern tools", "body": "CRM, automated dialing and analytics sit behind every campaign, so you spend your time on the conversation."},
            {"icon": "clock", "title": "Predictable hours", "body": "Stable weekday schedules so you can plan your week, your studies and your family time."},
            {"icon": "team", "title": "A supportive, female-led team", "body": "Founded and led by a 100% Black female-owned team since 2015, with leaders who coach you from day one."},
            {"icon": "award", "title": "Skills and jobs for young people", "body": "As a B-BBEE Level 1 contributor and YES Programme partner, we create skills and job opportunities for unemployed youth."},
        ],
        "hire_steps": [
            {"title": "Apply", "body": "Send your CV via email."},
            {"title": "Get feedback", "body": "You will get a reply within 7 business days by email or call, along with an interview request."},
            {"title": "Interview", "body": "Meet our HR team and receive an offer."},
            {"title": "Begin training", "body": "Meet your team and your team leader."},
        ],
        "faqs": [
            {"q": "Do I need experience?", "a": "Not always. Many roles include paid training, and as a YES Programme partner we also create skills and job opportunities for unemployed youth."},
            {"q": "How long until I hear back?", "a": "We aim to respond to every application within 7 business days of receiving it."},
            {"q": "What should I include?", "a": "Your CV, the role you're applying for, your contact number and the city you'd like to work in."},
            {"q": "Can I apply for more than one role?", "a": "Yes. Mention each role in your email and we'll consider you for all of them."},
        ],
        "values": [
            {"title": "Integrity", "body": "Honesty, transparency and fairness in every dealing."},
            {"title": "Accountability", "body": "We take full responsibility for the results we deliver."},
            {"title": "Excellence", "body": "Continuous improvement in performance and method."},
            {"title": "Respect", "body": "Every client and debtor treated with dignity."},
            {"title": "Empowerment", "body": "Inclusivity, transformation and female leadership."},
        ],
    }
    return render(request, "careers.html", context)
