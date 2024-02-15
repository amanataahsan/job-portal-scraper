keyword=["sales"]
spec=""
city="jakarta"
sort_type="default"
limit=20

#seek.au
url_classification = "https://www.seek.com.au/jobs-in-{}"
category = [
    'administration-office-support',
    'accounting',
    'advertising-arts-media',
    'banking-financial-services',
    'call-centre-customer-service',
    'ceo-general-management',
    'community-services-development',
    'construction',
    'consulting-strategy',
    'design-architecture',
    'education-training',
    'engineering',
    'farming-animals-conservation',
    'government-defence',
    'healthcare-medical',
    'hospitality-tourism',
    'human-resources-recruitment',

]
contain_skill = [
    "SKILL",
    "ABILITIES",
    "ABILITY"
    "COMPETENCY",
    "COMPETENCIES"
    "PROFICIENCY"
    "PROFICIENCIES",
    "TALENT",
    "CAPABILITIES",
    "CAPABILITY"
    "EXPERTISE",
    "ABOUT YOU",
    "PERSONAL ATTRIBUTE",
    "YOUR PROFILE",
    "CANDIDATE PROFILE",
    "QUALIFICATION",
    "PERSONAL QUALITY",
    "PERSONAL QUALITIES"
    "CHARACTERISTIC",
    "REQUIREMENT",
    "QUALIFICATION",
    "PREREQUISITE",
    "CRITERIA",
    "SPECIFICATION",
    "ESSENTIAL TRAIT",
    "ESSENTIAL CRITERIA",
    "OUR IDEAL CANDIDATE",
    "OUR PERFECT CANDIDATE",
    "THE CANDIDATE WE'RE SEEKING",
    "AN IDEAL FIT FOR US",
    "THE RIGHT CANDIDATE FOR US",
    "THE IDEAL CANDIDATE FOR THIS ROLE",
    "A CANDIDATE WHO ALIGNS WITH OUR EXPECTATION",
    "A CANDIDATE THAT FITS OUR VISION",
    "THE CANDIDATE WE HAVE IN MIND",
    "PEOPLE WHO HAVE",
    "ESSENTIAL",
    "WHO YOU ARE",
    "SOMEONE WITH",
    "HAVE FOLLOWING",
    "HAVE THE FOLLOWING"
]

postgre_credential = {
    'host': 'localhost',
    'port': 5432,
    'database': 'alcazar',
    'username': 'postgres',
    'password': 'postgres'
}
postgre_table_name = 'seek'