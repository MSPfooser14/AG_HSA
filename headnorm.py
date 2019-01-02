import pandas as pd 
import numpy as np 
import csv

def normheader(line1):
	l = len(line1)
	h1n = ['' for x in range(l)]
	h2n = ['' for x in range(l)]
	for i, val in enumerate(line1):
		x = val.strip()
#Q1
		if x == 'https://i.imgur.com/dXA6s9b.jpg':
			h1n[i] = 'Q1'
			h2n[i] = 'R1'
		elif x == 'Do you wear a 2-strap mask when working in dusty environments?':
			h1n[i] = 'Q1'
			h2n[i] = 'R1'
#Q2
		elif x == 'Do you apply sunscreen lotion when exposed to the sun?':
			h1n[i] = 'Q2'
			h2n[i] = 'R1'
		elif x == 'Do you apply sunscreen when exposed to the sun?':
			h1n[i] = 'Q2'
			h2n[i] = 'R1'
#Q3			
		elif x == 'Do you wear hearing protection (hearing plugs, ear muffs) in noisy environments?':
			h1n[i] = 'Q3'
			h2n[i] = 'R1'
#Q4		
		elif x == 'Do you wear protective clothing (gloves, goggles, etc) when mixing, handling, or applying pesticides (herbicides, insecticides, fungicides, etc) to crops or livestock?':
			h1n[i] = 'Q4'
			h2n[i] = 'R1'
		elif x == 'Do you wear some type(s) of protective clothing (gloves, goggles, etc) when mixing, handling, or applying pesticides (herbicides, insecticides, fungicides, etc) to crops or livestock?':
			h1n[i] = 'Q4'
			h2n[i] = 'R1'
		
		elif x == 'Do you wear safety glasses when exposed to hazards that can damage your eyes (grinding, cutting, mowing lawn)?':
			h1n[i] = 'Q5'
			h2n[i] = 'R1'
		
		elif x == 'Have you ever rolled an ATV/Quad?':
			h1n[i] = 'Q6'
			h2n[i] = 'R1'
		
		elif x == 'Have you ever had shortness of breath, cough, fever or chills after being exposed to a dusty environment?':
			h1n[i] = 'Q7'
			h2n[i] = 'R1'
#Q8		
		elif x == 'Have you ever had ringing in your ears or decreased ability to hear after being exposed to loud noises (noisy machinery, guns, music concert)?':
			h1n[i] = 'Q8'
			h2n[i] = 'R1'
		
		elif x == 'I am concerned about the health and safety of family members or friends who are involved in agriculture?':
			h1n[i] = 'Q9'
			h2n[i] = 'R1'
		
		elif x == 'Do you allow extra riders when operating an ATV/Quad?':
			h1n[i] = 'Q10'
			h2n[i] = 'R1'
		
		elif x == 'Do you wear a helmet when operating or riding on an ATV/Quad?':
			h1n[i] = 'Q11'
			h2n[i] = 'R1'
#Q12	
		elif x == 'Do you currently or have you ever worked in a livestock confinement (livestock housing) operation?':
			h1n[i] = 'Q12'
			h2n[i] = 'R1'
		elif x == 'https://i.imgur.com/T5ieBHD.jpg':
			h1n[i] = 'Q12'
			h2n[i] = 'R1'
		elif x == 'https://i.imgur.com/T5ieBHDb.jpg':
			h1n[i] = 'Q12'
			h2n[i] = 'R1'
#Q13 
		elif x == 'Have you ever been exposed to a zoonotic disease?Â':	
			h1n[i] = 'Q13'
			h2n[i] = 'R1'
		elif x == 'Have you ever been exposed to a zoonotic disease? ( A disease that can be transmitted from animals to humans).':
			h1n[i] = 'Q13'
			h2n[i] = 'R1'
		elif x == 'Have you ever been exposed to a zoonotic disease?Â\xa0(A disease that can be transmitted from animals to humans).':
			h1n[i] = 'Q13'
			h2n[i] = 'R1'
		elif x == 'https://i.imgur.com/RwrBIiD.jpg?1':
			h1n[i] = 'Q13'
			h2n[i] = 'R1'
		
		elif x == 'Do you do welding as part of your work or home activities?':
			h1n[i] = 'Q14'
			h2n[i] = 'R1'		
#Q15		
		elif x == 'Have you ever worn a cartridge type respirator?':
			h1n[i] = 'Q15'
			h2n[i] = 'R1'
		elif x == 'https://i.imgur.com/JEadvfV.jpg':
			h1n[i] = 'Q15'
			h2n[i] = 'R1'
		elif x == 'https://i.imgur.com/JEadvfVm.jpg':
			h1n[i] = 'Q15'
			h2n[i] = 'R1'
#Q16			
		elif x == 'Has your doctor or other healthcare provider ever discussed prevention of workplace safety or health hazards with you?':
			h1n[i] = 'Q16'
			h2n[i] = 'R1'
#Q17		
		elif x == 'If youâ€™ve ever worn a cartridge type respirator, have you ever had a respirator fit test?':
			h1n[i] = 'Q17'
			h2n[i] = 'R1'
		elif x == 'https://i.imgur.com/3K7KElS.jpg':
			h1n[i] = 'Q17'
			h2n[i] = 'R1'
#Q18	
		elif x == 'Which of the following respirators should be worn when working in or around a livestock housing (confinement) building when the manure pit is being or has recently been emptied?':
			h1n[i] = 'Q18'
			h2n[i] = 'R1'
		elif x == 'Which of the following respirators should be worn when working in or around a manure channel in a large animal building when the manure channel has recently been pumped empty?':
			h1n[i] = 'Q18'
			h2n[i] = 'R1'
		elif x == 'Which of the following respirators should be worn when working in or around a manure pitÂ\xa0or confinement / housing when the pit that has recently been pumped empty?':
			h1n[i] = 'Q18'
			h2n[i] = 'R1'
		elif x == 'Which of the following respirators should be worn when working in or around a manure pit or confinement / housing when the pit that has recently been pumped empty?':
			h1n[i] = 'Q18'
			h2n[i] = 'R1'
		elif x == 'Which of the following respirators should be worn when working in or around a manure pitÂ\xa0or confinement / housing when the pit that has recently been pumped empty? (or a oxygen deficient environment)':
			h1n[i] = 'Q18'
			h2n[i] = 'R1'
#Q19		
		elif x == 'How old were you when you first started helping/working on the farm?':
			h1n[i] = 'Q19'
			h2n[i] = 'R1'
		elif x == 'How old were you when you first started helping/working on the farm or ranch?':
			h1n[i] = 'Q19'
			h2n[i] = 'R1'	
#Q20		
		elif x == 'Please check the farming activities you participated in before the age of 14':
			for r in range(18):
				h1n[i+r] = 'Q20'
				h2n[i+r] = 'R' + str(r+1)
		elif x == 'Please check the farming activities you participated in before the age of 14.':
			for r in range(18):
				h1n[i+r] = 'Q20'
				h2n[i+r] = 'R' + str(r+1)
#Q21 
		elif x == 'Please check the farming activities you participated in the past 12 months.Â':
			for r in range(18):
				h1n[i+r] = 'Q21'
				h2n[i+r] = 'R' + str(r+1)
			if h1n[i+18] == '':
				h1n[i+18] = 'Q21'
				h2n[i+18] = 'R19'
		elif x == 'Please check the farming activities you participated in the past 12 months.':
			for r in range(18):
				h1n[i+r] = 'Q21'
				h2n[i+r] = 'R' + str(r+1)
			if h1n[i+18] == '':
				h1n[i+18] = 'Q21'
				h2n[i+18] = 'R19'
			if h1n[i+19] == '':
				h1n[i+19] = 'Q21'
				h2n[i+19] = 'R20'
			if len(h1n) > (int(i) + int(20)):
				if h1n[i+20] == '':
					h1n[i+20] = 'Q21'
					h2n[i+20] = 'R21'
#Q22		
		elif x == 'I would find value in receiving personal protective equipment such as hearing protection,Â\xa0chemical gloves, coverall, respirator, and safety glasses.':
			h1n[i] = 'Q22'
			h2n[i] = 'R1'
#Q23		
		elif x == 'Do you supervise other people or workers on the farm?':
			h1n[i] = 'Q23'
			h1n[i+1] = 'Q23'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
			if h1n[i+2] == '':
				h1n[i+2] = 'Q23'
				h2n[i+2] = 'R3'
#Q24	
		elif x == 'Do you plan to work in Agriculture after you completed college?':
			h1n[i] = 'Q24'
			h2n[i] = 'R1'
		elif x == 'Do you plan to work in agriculture after you complete college?':
			h1n[i] = 'Q24'
			h1n[i+1] = 'Q24'
			h1n[i+2] = 'Q24'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
			h2n[i+2] = 'R3'
		elif x == 'Do you plan to work in agriculture after you complete you education?':
			h1n[i] = 'Q24'
			h1n[i+1] = 'Q24'
			h1n[i+2] = 'Q24'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
			h2n[i+2] = 'R3'
		elif x == 'Do you plan to work in agriculture after you complete your education?':
			h1n[i] = 'Q24'
			h1n[i+1] = 'Q24'
			h1n[i+2] = 'Q24'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
			h2n[i+2] = 'R3'
#Q25		
		elif x == 'What type of agriculture-related work do you plan to do after graduating?':
			for r in range(9):
				h1n[i+r] = 'Q25'
				h2n[i+r] = 'R' + str(r+1)			
		elif x == 'What type of agriculture-related work do you plan to do?':
			for r in range(9):
				h1n[i+r] = 'Q25'
				h2n[i+r] = 'R' + str(r+1)
		elif x == 'What are you studying?':
			h1n[i] = 'Q26'
			h2n[i] = 'R1'
#Q27  
		elif x == 'Where do you currently go to get Ag or workplace information and resources. (for example: best practices, trainings, resources, personal protective equipment) ':
			h1n[i] = 'Q27'
			h2n[i] = 'R1'
		elif x == 'Where do you currently go to get Ag or workplace information and resources. (for example: best practices, trainings, resources, personal protective equipment)Â':
			h1n[i] = 'Q27'
			h2n[i] = 'R1'
#Q28		     
		elif x == 'Do you currently use social media to get Ag Health and Safety information. If yes; check all that apply.':
			for r in range(5):
				h1n[i+r] = 'Q28'
				h2n[i+r] = 'R' + str(r+1)
		elif x == 'Do you currently use social media to get Ag Health and Safety information. If yes; check all the apply':
			for r in range(5):
				h1n[i+r] = 'Q28'
				h2n[i+r] = 'R' + str(r+1)	
		elif x == 'Do you currently use social media to get Ag health and safety information. If yes; check all that apply.':
			for r in range(5):
				h1n[i+r] = 'Q28'
				h2n[i+r] = 'R' + str(r+1)	
#Q29				
		elif x == 'What type of Agriculture do you plan to work in?':
			h1n[i] = 'Q29'
			h2n[i] = 'R1'
		elif x == 'What type of Agriculture do you plan to work in?Â':
			h1n[i] = 'Q29'
			h2n[i] = 'R1'
#Q31
		elif x == 'Have you ever been in a crash involving farm equipment on the road?':
			h1n[i] = 'Q31'
			h1n[i+1] = 'Q31'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
		elif x == 'Have you ever been in a near-miss incident while operating farm equipment on the road?':
			h1n[i] = 'Q32'
			h1n[i+1] = 'Q32'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
#Q33	
		elif x == 'Where are you in your studies':
			h1n[i] = 'Q33'
			h2n[i] = 'R1'
			for r in range(4):
				if h1n[i+r+1] == '':
					h1n[i+r+1] = 'Q33'
					h2n[i+r+1] = 'R' + str(r+1)
#Q34
		elif x == 'Did you take the diploma farm safety course':
			h1n[i] = 'Q34'
			h2n[i] = 'R1'
#Q35
		elif x == 'Are you a University of Manitoba Staff Member?Â\xa0 If yes please check.Â':
			h1n[i] = 'Q35'
			h2n[i] = 'R1'
			if h1n[i+1] == '':
				h1n[i+1] = 'Q35'
				h2n[i+1] = 'R2'
#Q36
		elif x == 'Are you an industry representative? If yes, please check which applies to you.Â':
			h1n[i] = 'Q36'
			h2n[i] = 'R1'
			for r in range(4):
				if h1n[i+r+1] == '':
					h1n[i+r+1] = 'Q36'
					h2n[i+r+1] = 'R' + str(r+1)		
#Q37
		elif x == 'Have you worked on a farm':
			h1n[i] = 'Q37'
			h2n[i] = 'R1'
#Q38
		elif x == 'If you have worked on a farmÂ\xa0have you received safety training':
			h1n[i] = 'Q38'
			h2n[i] = 'R1'
#Q39
		elif x == 'Have youÂ\xa0received safety training from somewhere else?Â\xa0 If yes, please tell us where you received the training.':
			h1n[i] = 'Q39'
			h1n[i+1] = 'Q39'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
#Q40
		elif x == 'Please provide your name':
			h1n[i] = 'Q40'
			h1n[i+1] = 'Q40'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'
		elif x == 'Please provide your name.Â':
			h1n[i] = 'Q40'
			h1n[i+1] = 'Q40'
			h2n[i] = 'R1'
			h2n[i+1] = 'R2'

	return(h1n, h2n)