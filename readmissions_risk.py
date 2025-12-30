ages = [45, 78, 60, 30]
prior_admits = [0, 2, 1, 0]
length_of_stay = [2, 7, 4, 1]

if not (len(ages) == len(prior_admits) == len(length_of_stay)):
    print("Error: patient data lists must be the same length.")
    exit()

def calculate_risk_score(age, admits,los):
    score = 0
    if age >= 65:
        score += 1
    if admits >= 1:
        score += 1
    if admits >= 2:
        score += 2
    if los >= 5:
        score += 1
    return score

def explain_risk(age, admits):
    reasons = []
    if age >= 65:
        reasons.append("Age 65+")
    if admits >= 2:
        reasons.append("Multiple prior admissions")
    elif admits >= 1:
        reasons.append("Recent admission history")
    return reasons

high_count = 0
medium_count = 0
low_count = 0

for i in range(len(ages)):
    if ages[i] < 0 or prior_admits[i] < 0 or length_of_stay[i] < 0:
        print(f"Error: negative value found for patient {i + 1}.")
        exit()
    score = calculate_risk_score(ages[i], prior_admits[i],length_of_stay[i])
    reasons = explain_risk(ages[i], prior_admits[i])

    if score >= 3:
        risk = "High Risk"
        high_count += 1
    elif score == 2:
        risk = "Medium Risk"
        medium_count += 1
    else:
        risk = "Low Risk"
        low_count += 1

    print(f"Patient {i + 1}: {risk}")
    print("  Reasons:", ", ".join(reasons))

print("\nSummary")
print("Total patients:", len(ages))
print("High Risk:", high_count)
print("Medium Risk:", medium_count)
print("Low Risk:", low_count)