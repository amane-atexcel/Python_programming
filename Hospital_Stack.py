#Medication Dispensing -Last-In-First-Out (LIFO) for efficient medicine access
# Pharmacy Medication Stack
medication_stack = []

#you can create empty stack
#Stack only two operation pop and append

# Stock medications (newest on top)
medication_stack.append("Antibiotics")
medication_stack.append("Painkillers")
medication_stack.append("Insulin")
medication_stack.append("Antihistamines")
medication_stack.append("Vitamins")

print("Pharmacy Stock:", medication_stack)  
# Output: ['Antibiotics', 'Painkillers', 'Insulin']

# Dispense medications
for _ in range(2):
    dispensed = medication_stack.pop()
    print(f"Dispensed: {dispensed} → Remaining: {medication_stack}")