import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Job posting text
job_posting = """
   About Us
Dunstan's is a diversified manufacturing and engineering business with industry leading products in Agriculture, Mining, Almonds and other industries.

About the Role
We are seeking a highly motivated and technically proficient individual to join our Engineering and Production teams.
Your main responsibilities include supporting the Engineering & Production teams by resolving technical issues, leading QA processes and improving product design enabling the timely and efficient manufacturing of our products and projects.


The Role
•         Full-time, located in Kerang, Victoria.
•         Production Support – Provide engineering support to production teams.
•         Troubleshoot and resolve technical issues.
•         Coordinate with Engineering, Management and Production teams on a
           daily basis.
•         Production QA - Lead QA process through inspection, investigation and
           reporting.
•         Record issues, non-conformances, feedback and improvements.
•         Improvement Engineering – Design & revise engineering CAD models
           & drawings.
•         Maintain engineering and production related documentation, such as
           procedures, work methods and Bills of Materials.
•         Support and liaise with the management team on various
           tasks/projects.
•         Creating and updating spare parts and operator’s manuals.
•         Assist with inventory management and administration when required.


Skills & Experience
•         Bachelor’s degree in Mechanical, Manufacturing, Industrial Engineering
           or similar
•         3D CAD Experience. Experience using Solidworks preferred but not
           essential.
•         Proficient in Microsoft Systems
•         Relevant experience within the manufacturing industry

Personal Attributes
•         Self-motivated, positive and professional attitude at all times
•         Technical & mechanical aptitude.
•         Strong interpersonal and communication skills
•         Display analytical, logical thought process & attention to detail
•         Technical writing ability and strong work ethic
•         Willing to learn and work in a team
•         Able to work and perform in a fast paced environment

How to Apply
If you want to join a great business and do some fantastic work, then please submit your resume along with a cover letter detailing experience and qualifications.
"""

# Process the text with spaCy
doc = nlp(job_posting.lower())

# Extract skills and attributes using Named Entity Recognition
skills_and_attributes = [ent.text for ent in doc.ents if ent.label_ in ['skills', 'experience']]

print(skills_and_attributes)