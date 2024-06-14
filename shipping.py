weight = 8.4

#"Ground shipping"

if weight <= 2:
    cost = 1.50
elif weight > 2 and weight <= 6:
    cost = 3.00
elif weight > 6 and weight <= 10:
    cost = 4.00
else:
    cost = 4.75

cost_ground_shipping = 20.00

print("Ground shipping is $", weight * cost + cost_ground_shipping)

#"Ground Shipping Premium"

cost_ground_premium = 125.00

#Drone Shipping

weight =  1.5

if weight <= 2:
    cost = 4.50
elif weight > 2 and weight <= 6:
    cost = 9.00
elif weight > 6 and weight <= 10:
    cost = 12.00
else:
    cost = 14.25

print("Shipping by drone $", weight * cost)