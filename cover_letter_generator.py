hm=input('Hiring Managers Name: ')
if hm=='NA':
	hm='Hiring Manager'
cn=input('Company Name: ')
jt=input('Job Title: ')
ja=input('Job Aggragater: ')
public=input('Public Facing? Yes|No: ')
if public=='Yes':
	public='is comfortable interfacing with and assisting your customers, '
else:
	public='is comfortable providing support to your employees, '
team=input('Team Job? Yes|No: ')
if team=='Yes':
	team='is able to work well in a team setting'
else:
	team='is able to effectively work independantly'
print()
print()
print(f'Jared Allison\n317 30th Street APT 163B\nSpringfield, Or, 97478\n(458) 201-9935\njared.allison@gmail.com\n-------------------------\n{hm}\n{cn}\n\nDear {hm},\nThank you for the opportunity to apply for the {jt} role at your company. I reviewed the job description posted on {ja}. It is clear to me that you are looking for a candidate that is technically proficient, {public} and {team}. Given those requirements, I am sure that I have the skills and traits nessecary to fill the role, and perform on the job to an exceptional level.\n\nI am an empathetic and diligent profession who has made a hapbit of using emotional intelligence and troubleshooting logic in not just my professional life, but also to resolve issies in my personal life as well. I have developed technical skills over the last year at Acuitus Inc. and am delighted to find that the main areas of study line up perfectly with the requirements listed in your job posting. I invite you to read my resume attached to this application for a detailed list of skills that I can bring to your company.\n\nAfter reviewing my resume, I hope you agree with my assertation that I am the type of candidate that you are looking for. I look forward to discussing the benefits that my skills and traits can bring to your company. Please contact me at  (458) 201-9935 or via email at jared.allison@gmail.com to arrange a convenient meeting time.\n\nThank you for your consideration. I look forward to hearing from you soon.\nSincerely,\nJared Allison')
