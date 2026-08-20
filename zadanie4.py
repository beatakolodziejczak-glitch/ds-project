raw_name = "  PATIENT_age_YEARS "

step1 = raw_name.strip()
step2 = step1.lower()
step3 = step2.replace("_", " ")
clean_name = step3.title()

print(clean_name)
